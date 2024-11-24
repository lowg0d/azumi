import json
import logging
import os
import random
from turtle import color

import pyqtgraph as pg
from PySide6.QtCore import QObject, Qt, QThread, QTimer, Signal
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from src.managers.visualization import graphs

from .graphs import (
    DualAxePlotWidget,
    GpsPlotWidget,
    MonoAxePlotWidget,
    TripleAxePlotWidget,
)

MAX_LABEL_CHARS = 10


class VisualizationUpdaterThread(QThread):
    def __init__(self, update_callable) -> None:
        super().__init__()
        self.update_callable = update_callable

    def run(self):
        while True:
            self.update_callable()


class VisualizationModel(QObject):
    update_dashboard = Signal(dict)

    def __init__(
        self,
        mission_control,
        graph_container_layout,
        main_label_layout,
        secondary_label_layout,
    ) -> None:
        super().__init__()
        self.log = logging.getLogger(f"azumi.visualization")

        self.mission_control = mission_control
        self.main_label_layout = main_label_layout
        self.secondary_label_layout = secondary_label_layout

        pg.setConfigOptions(
            background="transparent",
            segmentedLineMode="off",
            exitCleanup=True,
            antialias=False,
            useOpenGL=False,
            useCupy=True,
            useNumba=True,
        )

        self.graph_container_layout = graph_container_layout
        self.graphics_widget = pg.GraphicsLayoutWidget()
        graph_container_layout.addWidget(self.graphics_widget)

        self.update_dashboard.connect(self.setup_dashborad)

        self.MAX_AXIS = 3
        self.PEN_WIDTH = 2
        self.ANTIALIAS = True
        self.DECIMALS = 5

        self.mono_axis_graphs_map = {}
        self.dual_axis_graphs_map = {}
        self.triple_axis_graphs_map = {}
        self.labels_map = {}

        self.choose_add_function = {
            1: self.setup_mono_axis_graphs,
            2: self.setup_dual_axis_graphs,
            3: self.setup_triple_axis_graphs,
        }

        self.update_thread = VisualizationUpdaterThread(self.update_graphs)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_graphs)

    def clear(self):
        self.clear_layout(self.main_label_layout)
        self.clear_layout(self.secondary_label_layout)
        self.graphics_widget.ci.clear()
        self.graphics_widget.repaint()

        self.mono_axis_graphs_map = {}
        self.dual_axis_graphs_map = {}
        self.triple_axis_graphs_map = {}
        self.labels_map = {}

    def setup_dashborad(self, data):
        graph_data = data.get("graphs")
        self.setup_graphs(graph_data)

        label_data = data.get("labels")
        self.setup_labels(label_data)

        return

    def _calculate_rows(self, amount: int, max_cols: int) -> int:
        try:
            max_per_column = int(round(amount / 3.5))
            num_columns = min((amount + max_per_column - 1) // max_per_column, max_cols)
            num_rows = (amount + num_columns - 1) // num_columns
            return num_rows

        except:
            return 1

    def setup_labels(self, data):

        len_list = [i for i in data if not i.get("primary")]
        rows = self._calculate_rows(len(len_list), 2)
        row, col = 0, 0

        primary_row = 0
        for label in data:
            widget = self._gen_label(label)

            if not label.get("primary"):
                self.secondary_label_layout.addLayout(widget, row, col)
                row += 1
                if row == rows:
                    row = 0
                    col += 1
                continue

            self.main_label_layout.addLayout(widget, primary_row, 0)
            primary_row += 1

    def _gen_label(self, data: dict) -> QHBoxLayout:
        name = (
            data["name"][:MAX_LABEL_CHARS] + "..."
            if len(data["name"]) > MAX_LABEL_CHARS
            else data["name"]
        )

        unit = data["unit"]
        show_unit = True

        ## Set the default value and unit based on unit type.
        default_value = "N/A"

        name_label = QLabel(f"""{name}: """)

        ## Create the unit and telemetry labels.
        unit_label = QLabel(f"{unit}")
        tlm_label = QLabel(f"""<b>{default_value}</b>""")

        ## Create the layout and add the labels.
        group_layout = QHBoxLayout()
        group_layout.addWidget(name_label, alignment=Qt.AlignmentFlag.AlignLeft)
        group_layout.addStretch(1)
        group_layout.addWidget(tlm_label, alignment=Qt.AlignmentFlag.AlignRight)

        ## Add the unit label if it should be shown.
        if show_unit:
            group_layout.addWidget(unit_label, alignment=Qt.AlignmentFlag.AlignRight)

        group_layout.addSpacing(10)

        self.labels_map[tlm_label] = (data["value"], data.get("decimals", 2))

        return group_layout

    def setup_graphs(self, data):
        for graph in data:
            values = graph.get("values")
            value_amount = len(values)

            gps = graph.get("gps")
            if not gps:
                if value_amount > self.MAX_AXIS:
                    title = graph.get("title")
                    self.log.warning(
                        f"'{title}' has too many values to plot in a single graph, the maximum axis allowed is '{self.MAX_AXIS}' yours: '{value_amount}'"
                    )

                function_ = self.choose_add_function[value_amount]
                function_(graph)

            else:
                if value_amount > 2:
                    title = graph.get("title")
                    self.log.warning(
                        f"'{title}' has too many values to plot in a single graph, the maximum axis allowed for GPS is '2' yours: '{value_amount}'"
                    )

                self.setup_gps_graphs(graph)

        graphs = self.mono_axis_graphs_map.copy()
        graphs.update(self.dual_axis_graphs_map)
        graphs.update(self.triple_axis_graphs_map)

        self.added_graphs = graphs

        graph_len = len(graphs)

        max_rows = 2
        if graph_len > 4:
            max_rows = 4

        rows = max_rows
        row, col = 0, 0

        for graph in graphs:
            self.graphics_widget.ci.addItem(graph, col, row)

            row += 1
            if row >= rows:
                row = 0
                col += 1

    def update_graphs(self):
        for graph in self.mono_axis_graphs_map:
            value = self.mission_control.get_tlm(self.mono_axis_graphs_map[graph])
            graph.update(value)

        for graph in self.dual_axis_graphs_map:
            value_1, value_2 = self.dual_axis_graphs_map[graph]
            value_1 = self.mission_control.get_tlm(value_1)
            value_2 = self.mission_control.get_tlm(value_2)

            graph.update(value_1, value_2)

        for graph in self.triple_axis_graphs_map:
            value_1, value_2, value_3 = self.triple_axis_graphs_map[graph]

            value_1 = self.mission_control.get_tlm(value_1)
            value_2 = self.mission_control.get_tlm(value_2)
            value_3 = self.mission_control.get_tlm(value_3)

            graph.update(value_1, value_2, value_3)

        for label in self.labels_map:
            value, decimals = self.labels_map[label]
            try:
                value = self.mission_control.get_tlm(value)
            except:
                self.log.error(
                    f"'{value}' was not found make sure to register it in the prelaunch..."
                )

            label.setText(f"<b>{round(value, decimals)}</b>")

    def setup_mono_axis_graphs(self, data):

        title = data.get("title", "N/A")
        unit = data.get("unit", "N/A")
        title = f"{title} ({unit})"
        values = data.get("values")
        value_1 = values[0]

        color = data.get("color_1", None)
        datapoints = data.get("datapoints", 500)

        if color == None:
            r = random.randint(100, 200)
            g = random.randint(100, 200)
            b = random.randint(100, 200)

            # Format the RGB values as a hex color string
            color = f"#{r:02x}{g:02x}{b:02x}"

        plot_widget = MonoAxePlotWidget(
            color, title, value_1, self.PEN_WIDTH, datapoints, self.ANTIALIAS
        )
        plot_widget.update(0.0)

        self.mono_axis_graphs_map[plot_widget] = value_1
        self.log.debug(f"single axis graph '{title}' added !")

    def gen_color(self, color_1):
        if color_1:
            return color_1

        r = random.randint(100, 200)
        g = random.randint(100, 200)
        b = random.randint(100, 200)

        return f"#{r:02x}{g:02x}{b:02x}"

    def setup_dual_axis_graphs(self, data):

        title = data.get("title", "N/A")
        unit = data.get("unit", "N/A")
        title = f"{title} ({unit})"
        values = data.get("values")
        value_1 = values[0]
        value_2 = values[1]

        color_1 = data.get("color_1", None)
        color_2 = data.get("color_2", None)
        datapoints = data.get("datapoints", 500)

        color_1 = self.gen_color(color_1)
        color_2 = self.gen_color(color_2)

        plot_widget = DualAxePlotWidget(
            color_1,
            color_2,
            title,
            value_1,
            value_2,
            self.PEN_WIDTH,
            datapoints,
            self.ANTIALIAS,
        )

        self.dual_axis_graphs_map[plot_widget] = (value_1, value_2)
        self.log.debug(f"dual axis graph '{title}' added !")

    def setup_triple_axis_graphs(self, data):

        title = data.get("title", "N/A")
        unit = data.get("unit", "N/A")
        title = f"{title} ({unit})"
        values = data.get("values")
        value_1 = values[0]
        value_2 = values[1]
        value_3 = values[2]

        color_1 = data.get("color_1", None)
        color_2 = data.get("color_2", None)
        color_3 = data.get("color_3", None)
        datapoints = data.get("datapoints", 500)

        color_1 = self.gen_color(color_1)
        color_2 = self.gen_color(color_2)
        color_3 = self.gen_color(color_3)

        plot_widget = TripleAxePlotWidget(
            color_1,
            color_2,
            color_3,
            title,
            value_1,
            value_2,
            value_3,
            self.PEN_WIDTH,
            datapoints,
            self.ANTIALIAS,
        )

        self.triple_axis_graphs_map[plot_widget] = (value_1, value_2, value_3)
        self.log.debug(f"triple axis graph '{title}' added !")

    def setup_gps_graphs(self, data):

        title = data.get("title", "N/A")
        unit = data.get("unit", "N/A")
        title = f"{title} ({unit})"
        values = data.get("values")
        value_1 = values[0]
        value_2 = values[1]

        color_1 = data.get("color_1", None)
        datapoints = data.get("datapoints", 500)

        color_1 = self.gen_color(color_1)

        plot_widget = GpsPlotWidget(
            color_1, title, self.PEN_WIDTH, datapoints, self.ANTIALIAS
        )

        self.graphics_widget.addItem(plot_widget, 1, 0)

        self.dual_axis_graphs_map[plot_widget] = (value_1, value_2)
        self.log.debug(f"gps axis graph '{title}' added !")

    def clear_layout(self, layout) -> None:
        if isinstance(layout, QGridLayout):
            # Clear the layout's columns and rows
            for i in reversed(range(layout.columnCount())):
                layout.setColumnMinimumWidth(i, 0)
                layout.setColumnStretch(i, 0)

            for i in reversed(range(layout.rowCount())):
                layout.setRowMinimumHeight(i, 0)
                layout.setRowStretch(i, 0)

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.clear_layout(sub_layout)
