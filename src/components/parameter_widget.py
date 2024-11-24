import logging
import re
from ast import Dict
from operator import methodcaller
from sys import flags
from tabnanny import check
from typing import Any

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
    Signal,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QHBoxLayout,
    QKeySequenceEdit,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("setting_container")
        Form.resize(856, 38)
        Form.setMinimumSize(QSize(0, 38))
        Form.setMaximumSize(QSize(16777215, 38))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(Form)
        self.container.setObjectName("setting_container")
        self.container.setMinimumSize(QSize(0, 38))
        self.container.setMaximumSize(QSize(16777215, 38))
        self.container.setFrameShape(QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.name_label = QLabel(self.container)
        self.name_label.setObjectName("name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.horizontalSpacer = QSpacerItem(
            379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # type:ignore
        line.setFrameShadow(QFrame.Sunken)  # type:ignore
        line.setFixedWidth(1)
        line.setFixedHeight(38)
        line.setStyleSheet("background-color: #383838;")  # Set the background color
        self.horizontalLayout.addWidget(line)

        QMetaObject.connectSlotsByName(Form)


class ParameterWidget(QWidget):
    function_map = {}
    update_value = Signal(object)

    def __init__(
        self,
        current_value,
    ):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.log = logging.getLogger(f"config")

        self.current_value = current_value
        _type = type(self.current_value).__name__
        setup_function = self.function_map.get(_type, None)

        self.function_map = {
            "bool": self._setup_bool,
            "dict": self._setup_list,
            "int": self._setup_int,
            "float": self._setup_float,
        }
        setup_function = self.function_map.get(_type, None)

        if not setup_function:
            print(f"Type Not Valid '{_type}' in {self.ui.name_label.text()}")
            return

        self.is_dict = False
        self.dict_instance = None

        setup_function()

    def _update_data(self):
        # Identify the sender widget
        sender = self.sender()
        new_value = None  # Initialize new_value

        # Check custom flag status and toggle visibility

        # Retrieve and validate new_value based on widget type
        if isinstance(sender, QLineEdit):
            new_value = sender.text()
            self.log.debug(f"QLineEdit value: '{new_value}'")

        elif isinstance(sender, QCheckBox):
            new_value = sender.isChecked()
            self.log.debug(f"QCheckBox value: '{new_value}'")

        elif isinstance(sender, QComboBox):
            new_value = sender.currentText()
            new_value = self.current_value[new_value]
            self.log.debug(f"QComboBox value: '{new_value}'")

        elif isinstance(sender, (QSpinBox, QDoubleSpinBox)):
            new_value = sender.value()
            self.log.debug(f"QSpinBox/QDoubleSpinBox value: '{new_value}'")

        else:
            self.log.warning(f"Unknown widget type: '{sender}'")
            return

        # Set the new configuration if new_value is valid
        self.update_value.emit(new_value)

    def check_if_it_is_dict(self):
        if self.is_dict:
            if self.dict_instance:
                new_value = self.current_value[self.dict_instance.currentText()]
                self.update_value.emit(new_value)

    def _setup_bool(self):
        checkbox = QCheckBox(self.ui.container)
        checkbox.setObjectName("checkbox")
        checkbox.setCursor(QCursor(Qt.PointingHandCursor))  # type: ignore

        # checkbox.setChecked(self.initial_value)

        checkbox.setFixedHeight(30)
        checkbox.setFixedWidth(30)
        checkbox.setFocusPolicy(Qt.ClickFocus)  # type: ignore
        checkbox.stateChanged.connect(self._update_data)

        self.ui.horizontalLayout.addWidget(checkbox)
        self.ui.verticalLayout.addWidget(self.ui.container)

    def _setup_list(self):
        combo_box = QComboBox(self.ui.container)
        combo_box.setObjectName("combo_box")

        combo_box.setFixedHeight(30)
        combo_box.setFixedWidth(200)
        combo_box.setFocusPolicy(Qt.ClickFocus)  # type: ignore
        combo_box.currentIndexChanged.connect(self._update_data)

        combo_box.addItems(self.current_value.keys())

        self.ui.horizontalLayout.addWidget(combo_box)
        self.ui.verticalLayout.addWidget(self.ui.container)

        self.is_dict = True
        self.dict_instance = combo_box

    def _setup_int(self):
        spinbox = QSpinBox(self.ui.container)
        spinbox.setObjectName("spinbox")
        spinbox.setCursor(QCursor(Qt.PointingHandCursor))  # type: ignore

        spinbox.setValue(self.current_value)

        spinbox.setFixedHeight(30)
        spinbox.setFixedWidth(200)
        spinbox.setFocusPolicy(Qt.ClickFocus)  # type: ignore
        spinbox.valueChanged.connect(self._update_data)

        spinbox.setMaximum(100000000)
        spinbox.setMinimum(-100000000)

        self.ui.horizontalLayout.addWidget(spinbox)
        self.ui.verticalLayout.addWidget(self.ui.container)

    def _setup_float(self):
        spinbox = QDoubleSpinBox(self.ui.container)
        spinbox.setObjectName("doublespinbox")
        spinbox.setCursor(QCursor(Qt.PointingHandCursor))  # type: ignore

        spinbox.setValue(self.current_value)

        spinbox.setFixedHeight(30)
        spinbox.setFixedWidth(200)
        spinbox.setFocusPolicy(Qt.ClickFocus)  # type: ignore
        spinbox.valueChanged.connect(self._update_data)

        spinbox.setMaximum(100000000)
        spinbox.setMinimum(-100000000)
        spinbox.setDecimals(6)

        self.ui.horizontalLayout.addWidget(spinbox)
        self.ui.verticalLayout.addWidget(self.ui.container)
