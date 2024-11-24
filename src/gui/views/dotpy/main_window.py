# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)
from src.gui.assets import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(1000, 650))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 400))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 32, 0, 0)
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.Shape.NoFrame)
        self.centralframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.centralframe)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 1))
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.centralStackedWidget = QStackedWidget(self.centralframe)
        self.centralStackedWidget.setObjectName(u"centralStackedWidget")
        self.dashPage = QWidget()
        self.dashPage.setObjectName(u"dashPage")
        self.verticalLayout_3 = QVBoxLayout(self.dashPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashPageFrame = QFrame(self.dashPage)
        self.dashPageFrame.setObjectName(u"dashPageFrame")
        self.dashPageFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.dashPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.dashPageFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.dashContainer = QFrame(self.dashPageFrame)
        self.dashContainer.setObjectName(u"dashContainer")
        self.dashContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.dashContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.dashContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.dashContainer)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(250, 16777215))
        self.sidebar.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.sidebar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.sidebar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.msn_indicator_dash = QLabel(self.frame_3)
        self.msn_indicator_dash.setObjectName(u"msn_indicator_dash")
        self.msn_indicator_dash.setMinimumSize(QSize(0, 25))
        self.msn_indicator_dash.setMaximumSize(QSize(16777215, 25))
        self.msn_indicator_dash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.msn_indicator_dash)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.line9 = QFrame(self.sidebar)
        self.line9.setObjectName(u"line9")
        self.line9.setMinimumSize(QSize(0, 1))
        self.line9.setMaximumSize(QSize(16777215, 1))
        self.line9.setFrameShape(QFrame.Shape.HLine)
        self.line9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line9)

        self.frame_2 = QFrame(self.sidebar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.record_btn = QPushButton(self.frame_2)
        self.record_btn.setObjectName(u"record_btn")
        self.record_btn.setMinimumSize(QSize(0, 32))
        self.record_btn.setMaximumSize(QSize(16777215, 32))
        self.record_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.record_btn.setCheckable(True)
        self.record_btn.setChecked(False)

        self.horizontalLayout_3.addWidget(self.record_btn)

        self.line_11 = QFrame(self.frame_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(1, 0))
        self.line_11.setMaximumSize(QSize(1, 16777215))
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_11)

        self.msn_exit_btn = QPushButton(self.frame_2)
        self.msn_exit_btn.setObjectName(u"msn_exit_btn")
        self.msn_exit_btn.setMinimumSize(QSize(0, 32))
        self.msn_exit_btn.setMaximumSize(QSize(16777215, 32))
        self.msn_exit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.msn_exit_btn)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.line6 = QFrame(self.sidebar)
        self.line6.setObjectName(u"line6")
        self.line6.setMinimumSize(QSize(0, 1))
        self.line6.setMaximumSize(QSize(16777215, 1))
        self.line6.setFrameShape(QFrame.Shape.HLine)
        self.line6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line6)

        self.state_label = QLabel(self.sidebar)
        self.state_label.setObjectName(u"state_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())
        self.state_label.setSizePolicy(sizePolicy)
        self.state_label.setMinimumSize(QSize(0, 39))
        self.state_label.setMaximumSize(QSize(16777215, 39))
        self.state_label.setLineWidth(0)
        self.state_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.state_label)

        self.line4 = QFrame(self.sidebar)
        self.line4.setObjectName(u"line4")
        self.line4.setMinimumSize(QSize(0, 1))
        self.line4.setMaximumSize(QSize(16777215, 1))
        self.line4.setFrameShadow(QFrame.Shadow.Plain)
        self.line4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_6.addWidget(self.line4)

        self.primaryLabelsFrame = QFrame(self.sidebar)
        self.primaryLabelsFrame.setObjectName(u"primaryLabelsFrame")
        self.primaryLabelsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.primaryLabelsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.primaryLabelsFrame)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.primaryLabelsLayout = QGridLayout()
        self.primaryLabelsLayout.setSpacing(0)
        self.primaryLabelsLayout.setObjectName(u"primaryLabelsLayout")
        self.primaryLabelsLayout.setContentsMargins(-1, 1, -1, 1)

        self.verticalLayout_11.addLayout(self.primaryLabelsLayout)


        self.verticalLayout_6.addWidget(self.primaryLabelsFrame)

        self.line7 = QFrame(self.sidebar)
        self.line7.setObjectName(u"line7")
        self.line7.setMinimumSize(QSize(0, 1))
        self.line7.setMaximumSize(QSize(16777215, 1))
        self.line7.setFrameShape(QFrame.Shape.HLine)
        self.line7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line7)

        self.secondaryLabelsFrame = QFrame(self.sidebar)
        self.secondaryLabelsFrame.setObjectName(u"secondaryLabelsFrame")
        self.secondaryLabelsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.secondaryLabelsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.secondaryLabelsFrame)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.secondaryLabelsLayout = QGridLayout()
        self.secondaryLabelsLayout.setSpacing(0)
        self.secondaryLabelsLayout.setObjectName(u"secondaryLabelsLayout")

        self.verticalLayout_13.addLayout(self.secondaryLabelsLayout)


        self.verticalLayout_6.addWidget(self.secondaryLabelsFrame)

        self.line8 = QFrame(self.sidebar)
        self.line8.setObjectName(u"line8")
        self.line8.setMinimumSize(QSize(0, 1))
        self.line8.setMaximumSize(QSize(16777215, 1))
        self.line8.setFrameShape(QFrame.Shape.HLine)
        self.line8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.frame_5 = QFrame(self.sidebar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.line_15 = QFrame(self.frame_5)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setMinimumSize(QSize(0, 1))
        self.line_15.setMaximumSize(QSize(16777215, 1))
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_15)

        self.kp = QDoubleSpinBox(self.frame_5)
        self.kp.setObjectName(u"kp")
        self.kp.setWrapping(True)
        self.kp.setDecimals(15)
        self.kp.setMaximum(1199.990000000000009)
        self.kp.setSingleStep(0.100000000000000)

        self.verticalLayout_16.addWidget(self.kp)

        self.kd = QDoubleSpinBox(self.frame_5)
        self.kd.setObjectName(u"kd")
        self.kd.setDecimals(15)
        self.kd.setMaximum(1199.990000000000009)
        self.kd.setSingleStep(0.100000000000000)

        self.verticalLayout_16.addWidget(self.kd)

        self.ki = QDoubleSpinBox(self.frame_5)
        self.ki.setObjectName(u"ki")
        self.ki.setDecimals(15)
        self.ki.setMaximum(1189.990000000000009)
        self.ki.setSingleStep(0.100000000000000)

        self.verticalLayout_16.addWidget(self.ki)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.sidebar)

        self.line = QFrame(self.dashContainer)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_2.addWidget(self.line)

        self.dashContainer_2 = QFrame(self.dashContainer)
        self.dashContainer_2.setObjectName(u"dashContainer_2")
        self.dashContainer_2.setFrameShape(QFrame.Shape.NoFrame)
        self.dashContainer_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.dashContainer_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dashSplitter = QSplitter(self.dashContainer_2)
        self.dashSplitter.setObjectName(u"dashSplitter")
        self.dashSplitter.setOrientation(Qt.Orientation.Vertical)
        self.dashSplitter.setOpaqueResize(False)
        self.dashSplitter.setHandleWidth(0)
        self.verticalLayoutWidget = QWidget(self.dashSplitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.dashTop = QVBoxLayout(self.verticalLayoutWidget)
        self.dashTop.setSpacing(0)
        self.dashTop.setObjectName(u"dashTop")
        self.dashTop.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.verticalLayoutWidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMinimumSize(QSize(0, 400))
        self.topFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.topFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.graph_container = QVBoxLayout()
        self.graph_container.setObjectName(u"graph_container")

        self.verticalLayout_10.addLayout(self.graph_container)


        self.dashTop.addWidget(self.topFrame)

        self.dashSplitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.dashSplitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.dashBottom = QVBoxLayout(self.verticalLayoutWidget_2)
        self.dashBottom.setSpacing(0)
        self.dashBottom.setObjectName(u"dashBottom")
        self.dashBottom.setContentsMargins(0, 0, 0, 0)
        self.line3 = QFrame(self.verticalLayoutWidget_2)
        self.line3.setObjectName(u"line3")
        self.line3.setMinimumSize(QSize(0, 1))
        self.line3.setMaximumSize(QSize(16777215, 1))
        self.line3.setFrameShape(QFrame.Shape.HLine)
        self.line3.setFrameShadow(QFrame.Shadow.Sunken)

        self.dashBottom.addWidget(self.line3)

        self.terminal = QTextBrowser(self.verticalLayoutWidget_2)
        self.terminal.setObjectName(u"terminal")

        self.dashBottom.addWidget(self.terminal)

        self.dashSplitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_8.addWidget(self.dashSplitter)


        self.horizontalLayout_2.addWidget(self.dashContainer_2)


        self.verticalLayout_4.addWidget(self.dashContainer)


        self.verticalLayout_3.addWidget(self.dashPageFrame)

        self.centralStackedWidget.addWidget(self.dashPage)
        self.msnSelectPage = QWidget()
        self.msnSelectPage.setObjectName(u"msnSelectPage")
        self.verticalLayout_5 = QVBoxLayout(self.msnSelectPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centeringFrame = QFrame(self.msnSelectPage)
        self.centeringFrame.setObjectName(u"centeringFrame")
        self.centeringFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.centeringFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.centeringFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mission_selector_frame = QFrame(self.centeringFrame)
        self.mission_selector_frame.setObjectName(u"mission_selector_frame")
        self.mission_selector_frame.setMinimumSize(QSize(250, 0))
        self.mission_selector_frame.setMaximumSize(QSize(250, 16777215))
        self.mission_selector_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.mission_selector_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.mission_selector_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.folder_combobox_container = QFrame(self.mission_selector_frame)
        self.folder_combobox_container.setObjectName(u"folder_combobox_container")
        self.folder_combobox_container.setMinimumSize(QSize(0, 38))
        self.folder_combobox_container.setMaximumSize(QSize(16777215, 16777215))
        self.folder_combobox_container.setFrameShape(QFrame.Shape.NoFrame)
        self.folder_combobox_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.folder_combobox_container)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 0, 0, 0)
        self.label_2 = QLabel(self.folder_combobox_container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.line_7 = QFrame(self.folder_combobox_container)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(1, 16777215))
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.msn_folder_comboBox = QComboBox(self.folder_combobox_container)
        self.msn_folder_comboBox.setObjectName(u"msn_folder_comboBox")
        self.msn_folder_comboBox.setMinimumSize(QSize(0, 38))
        self.msn_folder_comboBox.setMaximumSize(QSize(16777215, 38))
        self.msn_folder_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.msn_folder_comboBox)


        self.verticalLayout_12.addWidget(self.folder_combobox_container)

        self.line_5 = QFrame(self.mission_selector_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 1))
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_5)

        self.msn_combobox_container = QFrame(self.mission_selector_frame)
        self.msn_combobox_container.setObjectName(u"msn_combobox_container")
        self.msn_combobox_container.setMinimumSize(QSize(0, 38))
        self.msn_combobox_container.setMaximumSize(QSize(16777215, 16777215))
        self.msn_combobox_container.setFrameShape(QFrame.Shape.NoFrame)
        self.msn_combobox_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.msn_combobox_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 0, 0, 0)
        self.label_3 = QLabel(self.msn_combobox_container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.line_6 = QFrame(self.msn_combobox_container)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(1, 0))
        self.line_6.setMaximumSize(QSize(1, 16777215))
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.msn_combobox = QComboBox(self.msn_combobox_container)
        self.msn_combobox.setObjectName(u"msn_combobox")
        self.msn_combobox.setMinimumSize(QSize(0, 38))
        self.msn_combobox.setMaximumSize(QSize(16777215, 38))
        self.msn_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.msn_combobox)


        self.verticalLayout_12.addWidget(self.msn_combobox_container)

        self.line_4 = QFrame(self.mission_selector_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 1))
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_4)

        self.execute_btn = QPushButton(self.mission_selector_frame)
        self.execute_btn.setObjectName(u"execute_btn")
        self.execute_btn.setMinimumSize(QSize(0, 38))
        self.execute_btn.setMaximumSize(QSize(16777215, 38))
        self.execute_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.execute_btn)

        self.line_8 = QFrame(self.mission_selector_frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 1))
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.line_14 = QFrame(self.mission_selector_frame)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMinimumSize(QSize(0, 1))
        self.line_14.setMaximumSize(QSize(16777215, 1))
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_14)

        self.edit_btn = QPushButton(self.mission_selector_frame)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(0, 38))
        self.edit_btn.setMaximumSize(QSize(16777215, 38))
        self.edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.edit_btn)

        self.line_12 = QFrame(self.mission_selector_frame)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMinimumSize(QSize(0, 1))
        self.line_12.setMaximumSize(QSize(16777215, 1))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_12)

        self.logs_btn = QPushButton(self.mission_selector_frame)
        self.logs_btn.setObjectName(u"logs_btn")
        self.logs_btn.setMinimumSize(QSize(0, 38))
        self.logs_btn.setMaximumSize(QSize(16777215, 38))
        self.logs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.logs_btn)

        self.line_9 = QFrame(self.mission_selector_frame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(0, 1))
        self.line_9.setMaximumSize(QSize(16777215, 1))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_9)

        self.pushButton = QPushButton(self.mission_selector_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 38))
        self.pushButton.setMaximumSize(QSize(16777215, 38))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.mission_selector_frame)

        self.line_2 = QFrame(self.centeringFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(1, 0))
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.frame_4 = QFrame(self.centeringFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.msn_title_label = QLabel(self.frame)
        self.msn_title_label.setObjectName(u"msn_title_label")
        self.msn_title_label.setMinimumSize(QSize(0, 38))
        self.msn_title_label.setMaximumSize(QSize(16777215, 38))

        self.verticalLayout_15.addWidget(self.msn_title_label)

        self.line_10 = QFrame(self.frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(0, 1))
        self.line_10.setMaximumSize(QSize(16777215, 1))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_10)

        self.msn_description_label = QLabel(self.frame)
        self.msn_description_label.setObjectName(u"msn_description_label")
        self.msn_description_label.setMinimumSize(QSize(0, 38))
        self.msn_description_label.setMaximumSize(QSize(16777215, 38))

        self.verticalLayout_15.addWidget(self.msn_description_label)


        self.verticalLayout_14.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.line_13 = QFrame(self.scrollAreaWidgetContents)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setMinimumSize(QSize(0, 1))
        self.line_13.setMaximumSize(QSize(16777215, 1))
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line_13)

        self.mission_parameters_layout = QVBoxLayout()
        self.mission_parameters_layout.setObjectName(u"mission_parameters_layout")

        self.verticalLayout_18.addLayout(self.mission_parameters_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 573, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.msn_parameter_frame = QFrame(self.frame_4)
        self.msn_parameter_frame.setObjectName(u"msn_parameter_frame")
        self.msn_parameter_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.msn_parameter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.msn_parameter_frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.msn_parameter_frame)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.centeringFrame)

        self.centralStackedWidget.addWidget(self.msnSelectPage)

        self.verticalLayout_2.addWidget(self.centralStackedWidget)


        self.verticalLayout.addWidget(self.centralframe)

        self.statusBarFrame = QFrame(self.centralwidget)
        self.statusBarFrame.setObjectName(u"statusBarFrame")
        self.statusBarFrame.setMinimumSize(QSize(0, 17))
        self.statusBarFrame.setMaximumSize(QSize(16777215, 17))
        self.statusBarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.statusBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.statusBarFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.line2 = QFrame(self.statusBarFrame)
        self.line2.setObjectName(u"line2")
        self.line2.setMinimumSize(QSize(0, 1))
        self.line2.setMaximumSize(QSize(16777215, 1))
        self.line2.setFrameShape(QFrame.Shape.HLine)
        self.line2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line2)

        self.statusbarcontainer = QFrame(self.statusBarFrame)
        self.statusbarcontainer.setObjectName(u"statusbarcontainer")
        self.statusbarcontainer.setFrameShape(QFrame.Shape.NoFrame)
        self.statusbarcontainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.statusbarcontainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.status_label = QLabel(self.statusbarcontainer)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout.addWidget(self.status_label)

        self.spacer_statusbar = QSpacerItem(989, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer_statusbar)

        self.version_label = QLabel(self.statusbarcontainer)
        self.version_label.setObjectName(u"version_label")

        self.horizontalLayout.addWidget(self.version_label)


        self.verticalLayout_7.addWidget(self.statusbarcontainer)


        self.verticalLayout.addWidget(self.statusBarFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centralStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.msn_indicator_dash.setText(QCoreApplication.translate("MainWindow", u"demo/hop_test", None))
        self.record_btn.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.msn_exit_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.state_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.kp.setPrefix(QCoreApplication.translate("MainWindow", u"Kp ", None))
        self.kd.setPrefix(QCoreApplication.translate("MainWindow", u"Ki ", None))
        self.ki.setPrefix(QCoreApplication.translate("MainWindow", u"Kd ", None))
        self.terminal.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Aux Mono';\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Folder:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mission:", None))
#if QT_CONFIG(tooltip)
        self.execute_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Execute current selected mission", None))
#endif // QT_CONFIG(tooltip)
        self.execute_btn.setText(QCoreApplication.translate("MainWindow", u"EXECUTE", None))
#if QT_CONFIG(tooltip)
        self.edit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Open mission json file", None))
#endif // QT_CONFIG(tooltip)
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
#if QT_CONFIG(tooltip)
        self.logs_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Open mission realted logs folder", None))
#endif // QT_CONFIG(tooltip)
        self.logs_btn.setText(QCoreApplication.translate("MainWindow", u"LOGS", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Set current parameters as default for the mission", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.msn_title_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.msn_description_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.status_label.setText("")
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"v0.1.0", None))
    # retranslateUi

