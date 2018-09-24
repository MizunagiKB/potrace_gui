#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------- import(s)
import sys
import os
import io
import subprocess
import traceback

import PIL.Image

import PyQt5
import PyQt5.Qt
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtSvg
import PyQt5.QtWidgets

import ui_MainWindow
import ui_About

DEFAULT_ARGV = [
    "-s",
    "-",
    "-o-"
]


# --------------------------------------------------------------- exception(s)
class CExc(Exception):
    pass

class CExcPotrace(Exception):
    pass

class CExcPotraceNotFound(CExcPotrace):
    pass

class CExcPotraceNotExecutable(CExcPotrace):
    pass

class CExcPotracePermissionError(CExcPotrace):
    pass

# ------------------------------------------------------------------- class(s)
# ----------------------------------------------------------------------------
##
#
class CViewSVG(PyQt5.QtWidgets.QGraphicsView):

    m_listArgv = []
    CurrentSVGFile = ""
    CurrentSVGData = ""
    PotraceAbsPath = ""

    raw_bitmap_buffer = None

    # -----------------------------------------------------------------------
    ##
    #
    def __init__(self):
        super(CViewSVG, self).__init__()

        self.setScene(
            PyQt5.QtWidgets.QGraphicsScene(self)
        )
        self.setTransformationAnchor(
            PyQt5.QtWidgets.QGraphicsView.AnchorUnderMouse
        )
        self.setDragMode(
            PyQt5.QtWidgets.QGraphicsView.ScrollHandDrag
        )
        self.setViewportUpdateMode(
            PyQt5.QtWidgets.QGraphicsView.FullViewportUpdate
        )

        # Prepare background check-board pattern.

        tilePixmap = PyQt5.QtGui.QPixmap(64, 64)
        tilePixmap.fill(PyQt5.QtCore.Qt.white)
        tilePainter = PyQt5.QtGui.QPainter(tilePixmap)
        color = PyQt5.QtGui.QColor(220, 220, 220)
        tilePainter.fillRect(0, 0, 32, 32, color)
        tilePainter.fillRect(32, 32, 32, 32, color)
        tilePainter.end()

        self.setBackgroundBrush(PyQt5.QtGui.QBrush(tilePixmap))

    def set_potrace_exec_pathname(self, strPath):

        self.PotraceAbsPath = os.path.abspath(strPath)

    # -----------------------------------------------------------------------
    ##
    #
    def save(self, strPathname, strBackend):

        listSave = [
            "--backend=" + strBackend,
            "--output=" + strPathname
        ]

        listArgv = [
            self.PotraceAbsPath, self.CurrentSVGFile
        ] + self.m_listArgv + listSave

        subprocess.check_output(listArgv)

    # -----------------------------------------------------------------------
    def open(self, image_pathname):

        h_file = io.BytesIO()
        o_image = PIL.Image.open(image_pathname)
        o_image.save(h_file, "bmp")

        h_file.seek(0)
        self.raw_bitmap_buffer = h_file.read()

        self.CurrentSVGFile = image_pathname

        self.reload()
        self.update(True)


    def set_argv(self, listArgv):
        self.m_listArgv = listArgv

    def reload(self):

        if self.raw_bitmap_buffer is not None:

            listArgv = [
                self.PotraceAbsPath
            ] + self.m_listArgv + DEFAULT_ARGV

            oCProcess = subprocess.Popen(
                listArgv,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False
            )

            byteStdout, byteStderr = oCProcess.communicate(input=self.raw_bitmap_buffer)

            self.CurrentSVGData = byteStdout

            self.update(False)

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
            oCQSvgItem.setFlags(
                PyQt5.QtWidgets.QGraphicsItem.ItemClipsToShape
            )
            oCQSvgItem.setCacheMode(
                PyQt5.QtWidgets.QGraphicsItem.NoCache
            )
            oCQSvgItem.setZValue(0)

            s.addItem(oCQSvgItem)

    def wheelEvent(self, oCQWheelEvent):
        fValue = 0
        fValue += oCQWheelEvent.angleDelta().x()
        fValue += oCQWheelEvent.angleDelta().y()
        fFactor = pow(1.2, fValue / 240.0)
        self.scale(fFactor, fFactor)


# ---------------------------------------------------------------------------
class CMainWindow(PyQt5.QtWidgets.QMainWindow):
    """
    MainFrame
    """

    # -----------------------------------------------------------------------
    def __init__(self):
        """
        Constructer
        """

        super(CMainWindow, self).__init__()

        # check potrace binary
        try:
            base_pathname = os.path.split(sys.argv[0])[0]
            self.potrace_exec_pathname = potrace_exists(base_pathname)
        except CExcPotrace as exc_message:
            self.potrace_exec_pathname = "None"
            print(exc_message)
            PyQt5.QtWidgets.QMessageBox.critical(
                self,
                "Potrace exists check.",
                str(exc_message)
            )

        self.ui = ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.m_oCViewSVG = CViewSVG()
        self.m_oCViewSVG.set_potrace_exec_pathname(self.potrace_exec_pathname)

        self.setCentralWidget(self.m_oCViewSVG)

        self.setAcceptDrops(True)

        # Event Connect

        self.ui.actionFileOpen.triggered.connect(self.actionFileOpen)
        self.ui.actionFileSaveAs.triggered.connect(self.actionFileSaveAs)
        self.ui.actionViewZoomIn.triggered.connect(self.actionViewZoomIn)
        self.ui.actionViewZoomOut.triggered.connect(self.actionViewZoomOut)
        self.ui.actionViewZoomReset.triggered.connect(self.actionViewZoomReset)
        self.ui.actionViewRefresh.triggered.connect(self.actionViewRefresh)
        self.ui.actionViewAutoRefresh.triggered.connect(self.actionViewAutoRefresh)
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

    # -----------------------------------------------------------------------
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

        if(self.ui.actionViewAutoRefresh.isChecked() is True):
            self.m_oCViewSVG.reload()

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
                "Potrace Supported File", "Bitmap files (*.bmp *.jpg *.jpeg *.png)")

        if path:
            svg_file = PyQt5.QtCore.QFile(path)
            if not svg_file.exists():
                PyQt5.QtWidgets.QMessageBox.critical(
                    self,
                    "Open SVG File",
                    "Could not open file '%s'." % (path,)
                )

                #self.outlineAction.setEnabled(False)
                #self.backgroundAction.setEnabled(False)
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

    def actionViewRefresh(self):
        self.m_oCViewSVG.reload()

    def actionViewAutoRefresh(self, bChecked):
        if(bChecked is True):
            self.m_oCViewSVG.reload()

    def actionHelpAbout(self):
        oCAbout = CAbout()
        oCAbout.exec()

    def dragEnterEvent(self, oCQDragEnterEvent):
        if(oCQDragEnterEvent.mimeData().hasFormat("text/uri-list") is True):
            oCQDragEnterEvent.acceptProposedAction()

    def dropEvent(self, oCQDropEvent):
        strPath = oCQDropEvent.mimeData().text()
        if sys.platform in ("win32",):
            prefix_path = "file:///"
        else:
            prefix_path = "file://"

        prefix_path_len = len(prefix_path)
        if strPath.find(prefix_path) == 0:
            self.actionFileOpen(strPath[prefix_path_len:])


class CAbout(PyQt5.QtWidgets.QDialog):

    def __init__(self):
        super(CAbout, self).__init__()

        self.ui = ui_About.Ui_Dialog()
        self.ui.setupUi(self)


# ---------------------------------------------------------------- function(s)
def potrace_exists(base_pathname):
    """
    potraceが呼び出せるか確認を行います。
    """

    list_potrace_pathname = [
        "potrace",
        os.path.join(base_pathname, "bin", "potrace")
    ]

    for rel_path in list_potrace_pathname:
        if sys.platform in ("win32",):
            rel_path += ".exe"
        abs_path = os.path.abspath(rel_path)
        if os.path.exists(abs_path) is True:
            stdout_captured = io.TextIOBase()
            try:
                o_result = subprocess.run([abs_path, "-v"], check=True, stdout=subprocess.PIPE)
                if o_result.returncode == 0:
                    return abs_path
                else:
                    raise CExcPotraceNotExecutable("'{}' can not be executed.".format(abs_path))
            except PermissionError:
                raise CExcPotraceNotExecutable("'{}' can not be executed.".format(abs_path))

    raise CExcPotraceNotFound("Potrace is not found.")


# ===========================================================================
##
#
def main():

    oCApp = PyQt5.QtWidgets.QApplication(sys.argv)

    oCMain = CMainWindow()
    oCMain.show()

    return(oCApp.exec_())


if __name__ == "__main__":
    main()



# --------------------------------------------------------------------- [EOF]
