# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created: Sat Aug  2 22:02:19 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.dockWidget_7 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_7.setMinimumSize(QtCore.QSize(360, 540))
        self.dockWidget_7.setMaximumSize(QtCore.QSize(32768, 32768))
        self.dockWidget_7.setFloating(False)
        self.dockWidget_7.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_7.setObjectName("dockWidget_7")
        self.dockWidgetContents_9 = QtWidgets.QWidget()
        self.dockWidgetContents_9.setObjectName("dockWidgetContents_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.dockWidgetContents_9)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox_9 = QtWidgets.QGroupBox(self.dockWidgetContents_9)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 64))
        self.groupBox_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_58 = QtWidgets.QLabel(self.groupBox_9)
        self.label_58.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 6, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.groupBox_9)
        self.label_55.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 2, 0, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.groupBox_9)
        self.label_57.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 5, 0, 1, 1)
        self.ptBlacklevel = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.ptBlacklevel.setMaximum(1.0)
        self.ptBlacklevel.setSingleStep(0.05)
        self.ptBlacklevel.setProperty("value", 0.5)
        self.ptBlacklevel.setObjectName("ptBlacklevel")
        self.gridLayout.addWidget(self.ptBlacklevel, 8, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.groupBox_9)
        self.label_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 11, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_9)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 8, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.groupBox_9)
        self.label_54.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.gridLayout.addWidget(self.label_54, 1, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.groupBox_9)
        self.label_60.setObjectName("label_60")
        self.gridLayout.addWidget(self.label_60, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_9)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.groupBox_9)
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 3, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.groupBox_9)
        self.label_61.setObjectName("label_61")
        self.gridLayout.addWidget(self.label_61, 10, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_9)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 1, 1, 1)
        self.ptOpttolerance = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.ptOpttolerance.setDecimals(2)
        self.ptOpttolerance.setMaximum(99.0)
        self.ptOpttolerance.setSingleStep(0.1)
        self.ptOpttolerance.setProperty("value", 0.2)
        self.ptOpttolerance.setObjectName("ptOpttolerance")
        self.gridLayout.addWidget(self.ptOpttolerance, 5, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox_9)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 10, 1, 1, 1)
        self.ptInvert = QtWidgets.QCheckBox(self.groupBox_9)
        self.ptInvert.setObjectName("ptInvert")
        self.gridLayout.addWidget(self.ptInvert, 9, 1, 1, 1)
        self.ptTurdsize = QtWidgets.QSpinBox(self.groupBox_9)
        self.ptTurdsize.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ptTurdsize.setObjectName("ptTurdsize")
        self.gridLayout.addWidget(self.ptTurdsize, 2, 1, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.groupBox_9)
        self.label_59.setObjectName("label_59")
        self.gridLayout.addWidget(self.label_59, 7, 0, 1, 1)
        self.ptUnit = QtWidgets.QSpinBox(self.groupBox_9)
        self.ptUnit.setMinimum(1)
        self.ptUnit.setMaximum(1200)
        self.ptUnit.setProperty("value", 10)
        self.ptUnit.setObjectName("ptUnit")
        self.gridLayout.addWidget(self.ptUnit, 6, 1, 1, 1)
        self.ptTurnpolicy = QtWidgets.QComboBox(self.groupBox_9)
        self.ptTurnpolicy.setObjectName("ptTurnpolicy")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.ptTurnpolicy.addItem("")
        self.gridLayout.addWidget(self.ptTurnpolicy, 1, 1, 1, 1)
        self.ptPagesize = QtWidgets.QComboBox(self.groupBox_9)
        self.ptPagesize.setObjectName("ptPagesize")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.ptPagesize.addItem("")
        self.gridLayout.addWidget(self.ptPagesize, 11, 1, 1, 1)
        self.ptLongcurve = QtWidgets.QCheckBox(self.groupBox_9)
        self.ptLongcurve.setObjectName("ptLongcurve")
        self.gridLayout.addWidget(self.ptLongcurve, 4, 1, 1, 1)
        self.ptAlphamax = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.ptAlphamax.setMaximum(99.0)
        self.ptAlphamax.setSingleStep(0.1)
        self.ptAlphamax.setProperty("value", 1.0)
        self.ptAlphamax.setObjectName("ptAlphamax")
        self.gridLayout.addWidget(self.ptAlphamax, 3, 1, 1, 1)
        self.ptTight = QtWidgets.QCheckBox(self.groupBox_9)
        self.ptTight.setObjectName("ptTight")
        self.gridLayout.addWidget(self.ptTight, 12, 1, 1, 1)
        self.verticalLayout_18.addWidget(self.groupBox_9)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_9)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.ptBackend = QtWidgets.QComboBox(self.dockWidgetContents_9)
        self.ptBackend.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ptBackend.setObjectName("ptBackend")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.ptBackend.addItem("")
        self.gridLayout_2.addWidget(self.ptBackend, 0, 1, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_2)
        self.btnSaveAs = QtWidgets.QPushButton(self.dockWidgetContents_9)
        self.btnSaveAs.setMinimumSize(QtCore.QSize(0, 48))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICONS/res/picture_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveAs.setIcon(icon)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.verticalLayout_18.addWidget(self.btnSaveAs)
        self.dockWidget_7.setWidget(self.dockWidgetContents_9)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_7)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionFileClose = QtWidgets.QAction(MainWindow)
        self.actionFileClose.setObjectName("actionFileClose")
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ICONS/res/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileOpen.setIcon(icon1)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.actionViewZoomIn = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ICONS/res/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewZoomIn.setIcon(icon2)
        self.actionViewZoomIn.setObjectName("actionViewZoomIn")
        self.actionViewZoomOut = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ICONS/res/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewZoomOut.setIcon(icon3)
        self.actionViewZoomOut.setObjectName("actionViewZoomOut")
        self.actionViewZoomReset = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ICONS/res/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewZoomReset.setIcon(icon4)
        self.actionViewZoomReset.setObjectName("actionViewZoomReset")
        self.actionFileSave = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ICONS/res/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSave.setIcon(icon5)
        self.actionFileSave.setObjectName("actionFileSave")
        self.actionFileSaveAs = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ICONS/res/disk_multiple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSaveAs.setIcon(icon6)
        self.actionFileSaveAs.setObjectName("actionFileSaveAs")
        self.actionHelpAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ICONS/res/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelpAbout.setIcon(icon7)
        self.actionHelpAbout.setObjectName("actionHelpAbout")
        self.menu_F.addAction(self.actionFileOpen)
        self.menu_F.addAction(self.actionFileSaveAs)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.actionFileClose)
        self.menu_Help.addAction(self.actionHelpAbout)
        self.menu_View.addAction(self.actionViewZoomIn)
        self.menu_View.addAction(self.actionViewZoomOut)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionViewZoomReset)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionFileOpen)
        self.toolBar.addAction(self.actionFileSaveAs)
        self.toolBar_2.addAction(self.actionViewZoomIn)
        self.toolBar_2.addAction(self.actionViewZoomOut)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionViewZoomReset)
        self.toolBar_3.addAction(self.actionHelpAbout)

        self.retranslateUi(MainWindow)
        self.ptTurnpolicy.setCurrentIndex(4)
        self.btnSaveAs.clicked.connect(self.actionFileSaveAs.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ptTurnpolicy, self.ptTurdsize)
        MainWindow.setTabOrder(self.ptTurdsize, self.ptAlphamax)
        MainWindow.setTabOrder(self.ptAlphamax, self.ptLongcurve)
        MainWindow.setTabOrder(self.ptLongcurve, self.ptOpttolerance)
        MainWindow.setTabOrder(self.ptOpttolerance, self.ptUnit)
        MainWindow.setTabOrder(self.ptUnit, self.ptBlacklevel)
        MainWindow.setTabOrder(self.ptBlacklevel, self.ptInvert)
        MainWindow.setTabOrder(self.ptInvert, self.ptPagesize)
        MainWindow.setTabOrder(self.ptPagesize, self.ptTight)
        MainWindow.setTabOrder(self.ptTight, self.btnSaveAs)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "potrace GUI"))
        self.menu_F.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Options:"))
        self.label_58.setText(_translate("MainWindow", "-u, --unit"))
        self.label_55.setText(_translate("MainWindow", "-t, --turdsize"))
        self.label_57.setText(_translate("MainWindow", "-O, --opttolerance"))
        self.label_47.setText(_translate("MainWindow", "-P, --pagesize"))
        self.label_32.setText(_translate("MainWindow", "-k, --blacklevel"))
        self.label_54.setText(_translate("MainWindow", "-z, --turnpolicy"))
        self.label_60.setText(_translate("MainWindow", "> Advanced"))
        self.label_56.setText(_translate("MainWindow", "-a, --alphamax"))
        self.label_61.setText(_translate("MainWindow", "> Scaling and Placement"))
        self.ptInvert.setText(_translate("MainWindow", "-i, --invert"))
        self.label_59.setText(_translate("MainWindow", "> Backend"))
        self.ptTurnpolicy.setItemText(0, _translate("MainWindow", "black"))
        self.ptTurnpolicy.setItemText(1, _translate("MainWindow", "white"))
        self.ptTurnpolicy.setItemText(2, _translate("MainWindow", "right"))
        self.ptTurnpolicy.setItemText(3, _translate("MainWindow", "left"))
        self.ptTurnpolicy.setItemText(4, _translate("MainWindow", "minority"))
        self.ptTurnpolicy.setItemText(5, _translate("MainWindow", "majority"))
        self.ptTurnpolicy.setItemText(6, _translate("MainWindow", "random"))
        self.ptPagesize.setItemText(0, _translate("MainWindow", "A4"))
        self.ptPagesize.setItemText(1, _translate("MainWindow", "A3"))
        self.ptPagesize.setItemText(2, _translate("MainWindow", "A5"))
        self.ptPagesize.setItemText(3, _translate("MainWindow", "B5"))
        self.ptPagesize.setItemText(4, _translate("MainWindow", "Letter"))
        self.ptPagesize.setItemText(5, _translate("MainWindow", "Legal"))
        self.ptPagesize.setItemText(6, _translate("MainWindow", "Tabloid"))
        self.ptPagesize.setItemText(7, _translate("MainWindow", "Statement"))
        self.ptPagesize.setItemText(8, _translate("MainWindow", "Executive"))
        self.ptPagesize.setItemText(9, _translate("MainWindow", "Folio"))
        self.ptPagesize.setItemText(10, _translate("MainWindow", "Quarto"))
        self.ptPagesize.setItemText(11, _translate("MainWindow", "10x14"))
        self.ptLongcurve.setText(_translate("MainWindow", "-n, --longcurve"))
        self.ptTight.setText(_translate("MainWindow", "--tight"))
        self.label.setText(_translate("MainWindow", "BACKEND TYPES"))
        self.ptBackend.setItemText(0, _translate("MainWindow", "eps"))
        self.ptBackend.setItemText(1, _translate("MainWindow", "ps"))
        self.ptBackend.setItemText(2, _translate("MainWindow", "pdf"))
        self.ptBackend.setItemText(3, _translate("MainWindow", "svg"))
        self.ptBackend.setItemText(4, _translate("MainWindow", "dxf"))
        self.ptBackend.setItemText(5, _translate("MainWindow", "geojson"))
        self.ptBackend.setItemText(6, _translate("MainWindow", "pgm"))
        self.ptBackend.setItemText(7, _translate("MainWindow", "gimppath"))
        self.ptBackend.setItemText(8, _translate("MainWindow", "xfig"))
        self.btnSaveAs.setText(_translate("MainWindow", "SaveAs..."))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionFileClose.setText(_translate("MainWindow", "Close"))
        self.actionFileClose.setToolTip(_translate("MainWindow", "Close"))
        self.actionFileOpen.setText(_translate("MainWindow", "Open"))
        self.actionFileOpen.setToolTip(_translate("MainWindow", "Open"))
        self.actionViewZoomIn.setText(_translate("MainWindow", "ZoomIn"))
        self.actionViewZoomIn.setToolTip(_translate("MainWindow", "ZoomIn"))
        self.actionViewZoomOut.setText(_translate("MainWindow", "ZoomOut"))
        self.actionViewZoomReset.setText(_translate("MainWindow", "ZoomReset"))
        self.actionFileSave.setText(_translate("MainWindow", "Save"))
        self.actionFileSaveAs.setText(_translate("MainWindow", "SaveAs..."))
        self.actionHelpAbout.setText(_translate("MainWindow", "About..."))

import resource_rc
