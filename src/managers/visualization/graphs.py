# type: ignore
import numpy as np
import pyqtgraph as pg
from PySide6.QtGui import QFont

FONT = QFont("Aux Mono", 9)
TICKOFFSET = 5
Y_PADDING = 0.2


class MonoAxePlotWidget(pg.PlotItem):
    """_summary_

    Args:
        color (str): the color of the graph line.
        title (str): the title of the graph.
        name (str): the name of the value, in this case the same as title is ok.
        pen_width (float): thw thickness of the line.
        datapoints (int): the amount of data points shown.
    """

    # TODO: fix bug when Y axis changes range a margin appears
    def __init__(
        self,
        color: str,
        title: str,
        name: str,
        pen_width: float,
        datapoints: int,
        antialias: bool,
    ):
        super().__init__(title=title, enableMenu=True)

        self.color = f"#{color.lstrip('#')}"
        self.initGraph(name, pen_width, datapoints, antialias)

    def initGraph(self, name, pen_width, datapoints, antialias_enabled):
        self.x_vals = np.linspace(0, 1, datapoints)
        self.y_vals = np.zeros(datapoints)

        self.graph_plot = self.plot(
            x=self.x_vals,
            y=self.y_vals,
            name=name,
            pen=pg.mkPen(self.color, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.setupAxes()
        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left", "top", "right"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)
            if side == "left":
                axis.setStyle(tickTextOffset=TICKOFFSET)
        self.titleLabel.item.setFont(FONT)

        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, value: float):
        self.y_vals = np.roll(self.y_vals, -1)
        self.y_vals[-1] = value

        self.graph_plot.setData(x=self.x_vals, y=self.y_vals)

        # Calculate new Y range with padding
        y_max = np.max(self.y_vals)
        y_min = np.min(self.y_vals)

        # Apply the new Y range
        self.setYRange(y_min, y_max, padding=Y_PADDING)

        # Reapply margin settings after setData
        self.setXRange(self.x_vals[0], self.x_vals[-1], padding=0.0, update=True)

    def clear(self):
        self.y_vals.fill(0)
        self.graph_plot.clear()
        self.update(0.0)


class DualAxePlotWidget(pg.PlotItem):
    def __init__(
        self,
        color1: str,
        color2: str,
        title: str,
        name1: str,
        name2: str,
        pen_width: float,
        datapoints: int,
        antialias: bool,
    ):
        super().__init__(title=title, enableMenu=True)

        self.color1 = f"#{color1.lstrip('#')}"
        self.color2 = f"#{color2.lstrip('#')}"

        self.addLegend()
        self.initGraph(name1, name2, pen_width, datapoints, antialias)

    def initGraph(self, name1, name2, pen_width, datapoints, antialias_enabled):
        self.x_vals = np.linspace(0, 1, datapoints)
        self.y_vals1 = np.zeros(datapoints)
        self.y_vals2 = np.zeros(datapoints)

        self.graph_plot1 = self.plot(
            x=self.x_vals,
            y=self.y_vals1,
            name=name1,
            pen=pg.mkPen(self.color1, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.graph_plot2 = self.plot(
            x=self.x_vals,
            y=self.y_vals2,
            name=name2,
            pen=pg.mkPen(self.color2, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.setupAxes()
        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left", "top", "right"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)
            if side == "left":
                axis.setStyle(tickTextOffset=TICKOFFSET)
        self.titleLabel.item.setFont(FONT)

        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, value1: float, value2: float):
        self.y_vals1 = np.roll(self.y_vals1, -1)
        self.y_vals1[-1] = value1
        self.graph_plot1.setData(x=self.x_vals, y=self.y_vals1)

        self.y_vals2 = np.roll(self.y_vals2, -1)
        self.y_vals2[-1] = value2
        self.graph_plot2.setData(x=self.x_vals, y=self.y_vals2)

        y_min = min(np.min(self.y_vals1), np.min(self.y_vals2))
        y_max = max(np.max(self.y_vals1), np.max(self.y_vals2))

        self.setYRange(y_min, y_max, padding=Y_PADDING)

        # Reapply margin settings after setData
        self.setXRange(self.x_vals[0], self.x_vals[-1], padding=0.0, update=True)

    def clear(self):
        self.y_vals1.fill(0)
        self.y_vals2.fill(0)
        self.graph_plot1.clear()
        self.graph_plot2.clear()
        self.update(0.0, 0.0)


class TripleAxePlotWidget(pg.PlotItem):
    def __init__(
        self,
        color1: str,
        color2: str,
        color3: str,
        title: str,
        name1: str,
        name2: str,
        name3: str,
        pen_width: float,
        datapoints: int,
        antialias: bool,
    ):
        super().__init__(title=title, enableMenu=True)

        self.color1 = f"#{color1.lstrip('#')}"
        self.color2 = f"#{color2.lstrip('#')}"
        self.color3 = f"#{color3.lstrip('#')}"

        self.addLegend()
        self.initGraph(name1, name2, name3, pen_width, datapoints, antialias)

    def initGraph(self, name1, name2, name3, pen_width, datapoints, antialias_enabled):
        self.x_vals = np.linspace(0, 1, datapoints)
        self.y_vals1 = np.zeros(datapoints)
        self.y_vals2 = np.zeros(datapoints)
        self.y_vals3 = np.zeros(datapoints)

        self.graph_plot1 = self.plot(
            x=self.x_vals,
            y=self.y_vals1,
            name=name1,
            pen=pg.mkPen(self.color1, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.graph_plot2 = self.plot(
            x=self.x_vals,
            y=self.y_vals2,
            name=name2,
            pen=pg.mkPen(self.color2, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.graph_plot3 = self.plot(
            x=self.x_vals,
            y=self.y_vals3,
            name=name3,
            pen=pg.mkPen(self.color3, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.setupAxes()
        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left", "top", "right"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)
            if side == "left":
                axis.setStyle(tickTextOffset=TICKOFFSET)
        self.titleLabel.item.setFont(FONT)

        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, value1: float, value2: float, value3: float):

        self.y_vals1 = np.roll(self.y_vals1, -1)
        self.y_vals1[-1] = value1
        self.graph_plot1.setData(x=self.x_vals, y=self.y_vals1)

        self.y_vals2 = np.roll(self.y_vals2, -1)
        self.y_vals2[-1] = value2
        self.graph_plot2.setData(x=self.x_vals, y=self.y_vals2)

        self.y_vals3 = np.roll(self.y_vals3, -1)
        self.y_vals3[-1] = value3
        self.graph_plot3.setData(x=self.x_vals, y=self.y_vals3)

        y_min = min(np.min(self.y_vals1), np.min(self.y_vals2), np.min(self.y_vals3))
        y_max = max(np.max(self.y_vals1), np.max(self.y_vals2), np.max(self.y_vals3))

        self.setYRange(y_min, y_max, padding=Y_PADDING)

        # Reapply margin settings after setData
        self.setXRange(self.x_vals[0], self.x_vals[-1], padding=0.0, update=True)

    def clear(self):
        self.y_vals1.fill(0)
        self.y_vals2.fill(0)
        self.y_vals3.fill(0)
        self.graph_plot1.clear()
        self.graph_plot2.clear()
        self.graph_plot3.clear()
        self.update(0.0, 0.0, 0.0)


class GpsPlotWidget(pg.PlotItem):
    def __init__(
        self, color: str, title: str, pen_width: float, datapoints: int, antialias: bool
    ):
        super().__init__(title=title, enableMenu=True)
        self.color = f"#{color.lstrip('#')}"
        self.max_datapoints = datapoints
        self.initGraph(pen_width, antialias)
        self.setupAxes()

    def initGraph(self, pen_width, antialias_enabled):
        # Initialize empty lists to store points
        self.x_vals = []
        self.y_vals = []

        # Initialize the graph plot
        self.graph_plot = self.plot(
            pen=pg.mkPen(self.color, width=pen_width),
            antialias=antialias_enabled,
            connect="finite",
        )

        # Scatter plot for the current point
        self.scatter_plot = pg.ScatterPlotItem(
            symbol="t1", size=6, brush=pg.mkBrush(self.color)
        )
        self.addItem(self.scatter_plot)

        # Fixed scatter point
        self.scatter_plot_2 = pg.ScatterPlotItem(
            symbol="o", size=10, brush=pg.mkBrush("#d35400")
        )
        self.scatter_plot_2.setData(x=[-4.89459], y=[-4272.96042])
        self.addItem(self.scatter_plot_2)

        # Configure view
        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)

        self.titleLabel.item.setFont(FONT)
        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, longitude: float, latitude: float):
        # Add the new point
        self.x_vals.append(longitude)
        self.y_vals.append(latitude)

        # Ensure the number of points doesn't exceed the limit
        if len(self.x_vals) > self.max_datapoints:
            self.x_vals.pop(0)
            self.y_vals.pop(0)

        # Update the plot and scatter
        self.graph_plot.setData(x=self.x_vals, y=self.y_vals)
        self.scatter_plot.setData(x=[longitude], y=[latitude], symbol="t1")

        # Adjust the view range only if there are points
        if len(self.x_vals) > 0 and len(self.y_vals) > 0:
            x_range = (min(self.x_vals), max(self.x_vals))
            y_range = (min(self.y_vals), max(self.y_vals))
            # Avoid calling setRange with invalid (nan) values
            if not (
                np.isnan(x_range[0])
                or np.isnan(x_range[1])
                or np.isnan(y_range[0])
                or np.isnan(y_range[1])
            ):
                self.setRange(xRange=x_range, yRange=y_range, padding=1.0)

    def clear(self):
        # Clear the data and plots
        self.x_vals.clear()
        self.y_vals.clear()
        self.graph_plot.clear()
        self.scatter_plot.clear()


class GpsPlotWidget2(pg.PlotItem):
    def __init__(
        self, color: str, title: str, pen_width: float, datapoints: int, antialias: bool
    ):
        super().__init__(title=title, enableMenu=True)

        self.color = f"#{color.lstrip('#')}"
        self.initGraph(pen_width, datapoints, antialias)
        self.setupAxes()

    def initGraph(self, pen_width, datapoints, antialias_enabled):
        self.x_vals = np.zeros(datapoints)
        self.y_vals = np.zeros(datapoints)

        self.graph_plot = self.plot(
            x=self.x_vals,
            y=self.y_vals,
            pen=pg.mkPen(f"{self.color}", width=pen_width),
            antialias=antialias_enabled,
            connect="finite",
        )

        self.scatter_plot = pg.ScatterPlotItem(
            symbol="t1", size=6, brush=pg.mkBrush(self.color)
        )
        self.addItem(self.scatter_plot)

        # Set scatter point size to 4 pixels
        self.scatter_plot_2 = pg.ScatterPlotItem(
            symbol="o", size=10, brush=pg.mkBrush("#d35400")
        )
        self.scatter_plot_2.setData(x=[-4.89459], y=[-4272.96042])
        self.addItem(self.scatter_plot_2)

        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.counter = 0

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)
            # axis.setStyle(tickTextOffset=TICKOFFSET)

        self.titleLabel.item.setFont(FONT)
        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, longitude: float, latitude: float):

        self.x_vals = np.roll(self.x_vals, -1)
        self.y_vals = np.roll(self.y_vals, -1)

        self.x_vals[-1] = longitude
        self.y_vals[-1] = latitude

        self.graph_plot.setData(x=self.x_vals, y=self.y_vals)
        self.scatter_plot.setData(x=[longitude], y=[latitude], symbol="t1")

        # Adjust the view range
        x_range = (min(self.x_vals), max(self.x_vals))
        y_range = (min(self.y_vals), max(self.y_vals))
        self.setRange(xRange=x_range, yRange=y_range, padding=1.0)

    def clear(self):
        self.x_vals.fill(0)
        self.y_vals.fill(0)
        self.graph_plot.clear()
        self.scatter_plot.clear()
        self.update(0.0, 0.0)
