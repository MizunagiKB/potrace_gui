#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------- import(s)
import sys
import os
import subprocess

import PyQt5
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtSvg
import PyQt5.QtWidgets

import ui_MainWindow
import ui_About

POTRACE_BIN = "bin/potrace"
DEFAULT_ARGV = [
    "-s",
    "-o-"
]

class CViewSVG(PyQt5.QtWidgets.QGraphicsView):

    m_listArgv = []
    CurrentSVGFile = ""
    CurrentSVGData = ""
    PotraceAbsPath = ""

    def __init__(self):
        super(CViewSVG, self).__init__()

        self.svgItem = None

        self.setScene(PyQt5.QtWidgets.QGraphicsScene(self))
        self.setTransformationAnchor(PyQt5.QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setDragMode(PyQt5.QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setViewportUpdateMode(PyQt5.QtWidgets.QGraphicsView.FullViewportUpdate)

        # Prepare background check-board pattern.
        tilePixmap = PyQt5.QtGui.QPixmap(64, 64)
        tilePixmap.fill(PyQt5.QtCore.Qt.white)
        tilePainter = PyQt5.QtGui.QPainter(tilePixmap)
        color = PyQt5.QtGui.QColor(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        self.setBackgroundBrush(PyQt5.QtGui.QBrush(tilePixmap))

    def set_potrace_path(self, strPath):

        self.PotraceAbsPath = strPath

    def save(self, strPathname, strBackend):

        listSave = [
            "--backend=" + strBackend,
            "--output=" + strPathname
        ]

        listArgv = [
            self.PotraceAbsPath, self.CurrentSVGFile
        ] + self.m_listArgv + listSave

        subprocess.check_output(listArgv)

    def open(self, strPathname):

        if(strPathname != self.CurrentSVGFile):
            bResetTransform = True
        else:
            bResetTransform = False

        listArgv = [
            self.PotraceAbsPath, strPathname
        ] + self.m_listArgv + DEFAULT_ARGV

        oCSVGData = subprocess.check_output(listArgv)

        self.CurrentSVGFile = strPathname
        self.CurrentSVGData = oCSVGData

        self.update(bResetTransform)

    def set_argv(self, listArgv):
        self.m_listArgv = listArgv

    def reload(self):

        if(os.path.exists(self.CurrentSVGFile) is True):
            self.open(self.CurrentSVGFile)

    def update(self, bResetTransform):

        if(self.CurrentSVGData != ""):
            if(bResetTransform is True):
                self.setScene(PyQt5.QtWidgets.QGraphicsScene(self))
                self.resetTransform()

            s = self.scene()
            s.clear()

            oCQSvgRenderer = PyQt5.QtSvg.QSvgRenderer(self.CurrentSVGData)

            oCQSvgItem = PyQt5.QtSvg.QGraphicsSvgItem()
            oCQSvgItem.setSharedRenderer(oCQSvgRenderer)

            self.svgItem = oCQSvgItem
            self.svgItem.setFlags(PyQt5.QtWidgets.QGraphicsItem.ItemClipsToShape)
            self.svgItem.setCacheMode(PyQt5.QtWidgets.QGraphicsItem.NoCache)
            self.svgItem.setZValue(0)

            s.addItem(self.svgItem)

    def wheelEvent(self, oCQWheelEvent):
        fValue = oCQWheelEvent.angleDelta().x() + oCQWheelEvent.angleDelta().y()
        fFactor = pow(1.2, fValue / 240.0)
        self.scale(fFactor, fFactor)


class CMainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self):
        super(CMainWindow, self).__init__()

        self.ui = ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.m_oCViewSVG = CViewSVG()

        self.setCentralWidget(self.m_oCViewSVG)

        ## Event Connect

        self.ui.actionFileOpen.triggered.connect(self.actionFileOpen)
        self.ui.actionFileSaveAs.triggered.connect(self.actionFileSaveAs)
        self.ui.actionViewZoomIn.triggered.connect(self.actionViewZoomIn)
        self.ui.actionViewZoomOut.triggered.connect(self.actionViewZoomOut)
        self.ui.actionViewZoomReset.triggered.connect(self.actionViewZoomReset)
        self.ui.actionHelpAbout.triggered.connect(self.actionHelpAbout)

        self.ui.ptTurnpolicy.currentIndexChanged.connect(self.currentIndexChanged)
        self.ui.ptTurdsize.valueChanged.connect(self.valueChanged)
        self.ui.ptAlphamax.valueChanged.connect(self.valueChanged)
        self.ui.ptLongcurve.stateChanged.connect(self.stateChanged)
        self.ui.ptOpttolerance.valueChanged.connect(self.valueChanged)
        self.ui.ptUnit.valueChanged.connect(self.valueChanged)

        self.ui.ptBlacklevel.valueChanged.connect(self.valueChanged)
        self.ui.ptInvert.stateChanged.connect(self.stateChanged)

        self.ui.ptPagesize.currentIndexChanged.connect(self.currentIndexChanged)
        self.ui.ptTight.stateChanged.connect(self.stateChanged)

    def __build_potrace_argv(self):

        listArgv = []

        listArgv.append("--turnpolicy=" + self.ui.ptTurnpolicy.currentText())
        listArgv.append("--turdsize=" + str(self.ui.ptTurdsize.value()))
        listArgv.append("--alphamax=" + str(self.ui.ptAlphamax.value()))

        if(self.ui.ptLongcurve.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--longcurve")

        listArgv.append("--opttolerance=" + str(self.ui.ptOpttolerance.value()))
        listArgv.append("--unit=" + str(self.ui.ptUnit.value()))

        listArgv.append("--blacklevel=" + str(self.ui.ptBlacklevel.value()))
        if(self.ui.ptInvert.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--invert")

        listArgv.append("--pagesize=" + self.ui.ptPagesize.currentText())
        if(self.ui.ptTight.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--tight")

        self.m_oCViewSVG.set_argv(listArgv)
        self.m_oCViewSVG.reload()

    def set_potrace_path(self, strPath):
        self.m_oCViewSVG.set_potrace_path(strPath)

    def currentIndexChanged(self, nIndex):
        self.__build_potrace_argv()

    def valueChanged(self, nValue):
        self.__build_potrace_argv()

    def stateChanged(self, nState):
        self.__build_potrace_argv()

    def actionFileOpen(self, path=None):

        if not path:
            path, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName(
                self,
                "Open Bitmap File",
                "Potrace Supported File", "Bitmap files (*.pbm *.pgm *.ppm *.bmp)")

        if path:
            svg_file = PyQt5.QtCore.QFile(path)
            if not svg_file.exists():
                QMessageBox.critical(self, "Open SVG File",
                        "Could not open file '%s'." % path)

                self.outlineAction.setEnabled(False)
                self.backgroundAction.setEnabled(False)
                return

            self.m_oCViewSVG.open(svg_file.fileName())

    def actionFileSaveAs(self):

        strBackend = self.ui.ptBackend.currentText()

        strPath, strExt = os.path.splitext(self.m_oCViewSVG.CurrentSVGFile)

        if(strPath != ""):

            strSavePathname = strPath + ".%s" % (strBackend,)
            strMask = "Vector files (*.%s)" % (strBackend,)

            path, _ = PyQt5.QtWidgets.QFileDialog.getSaveFileName(
                self,
                "Save Vector File",
                strSavePathname,
                strMask
            )

            if path:
                self.m_oCViewSVG.save(
                    path,
                    strBackend
                )

    def actionViewZoomIn(self):
        self.m_oCViewSVG.scale(2.0, 2.0)

    def actionViewZoomOut(self):
        self.m_oCViewSVG.scale(0.5, 0.5)

    def actionViewZoomReset(self):
        self.m_oCViewSVG.resetTransform()

    def actionHelpAbout(self):
        oCAbout = CAbout()
        oCAbout.exec()


class CAbout(PyQt5.QtWidgets.QDialog):

    def __init__(self):
        super(CAbout, self).__init__()

        self.ui = ui_About.Ui_Dialog()
        self.ui.setupUi(self)


# ===========================================================================
##
#
def main():

    if(os.path.exists(POTRACE_BIN) is True):

        oCApp = PyQt5.QtWidgets.QApplication(sys.argv)

        oCMain = CMainWindow()
        oCMain.set_potrace_path(os.path.abspath(POTRACE_BIN))
        oCMain.show()

        return(oCApp.exec_())

    else:

        return(-1)

if(__name__ == '__main__'):
    sys.exit(main())



# ---------------------------------------------------------------------- [EOF]
