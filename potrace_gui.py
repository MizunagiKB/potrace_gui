#!/usr/bin/env python3
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

# ------------------------------------------------------------------- param(s)
POTRACE_PATH = None
VIEW_MODE_SRC = 0
VIEW_MODE_DST = 1

# ------------------------------------------------------------------ global(s)
APP_INSTANCE = None

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
class CViewSVG(PyQt5.QtWidgets.QGraphicsView):

    m_listArgv = []
    CurrentSVGFile = ""
    CurrentSVGData = ""

    VIEW_MODE = None
    src_path = None
    svg_data = None
    bmp_data = None

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

    def set_view_mode(self, VIEW_MODE):
        self.VIEW_MODE = VIEW_MODE

    # -----------------------------------------------------------------------
    def save(self, strPathname, strBackend):

        listSave = [
            "--backend=" + strBackend,
            "-",
            "--output=" + strPathname
        ]

        listArgv = [POTRACE_PATH] + self.m_listArgv + listSave

        o_process = subprocess.Popen(
            listArgv,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False
        )

        o_process.communicate(input=self.bmp_data)

    # -----------------------------------------------------------------------
    def open(self, src_pathname):

        self.resetTransform()
        self.scene().clear()

        self.setScene(PyQt5.QtWidgets.QGraphicsScene(self))

        h_file = io.BytesIO()
        o_image = PIL.Image.open(src_pathname)
        o_image.save(h_file, "bmp")

        h_file.seek(0)
        self.bmp_data = h_file.read()

        o_pixmap = PyQt5.Qt.QPixmap()
        o_pixmap.loadFromData(self.bmp_data)

        o_item_src = PyQt5.Qt.QGraphicsPixmapItem()
        o_item_src.setPixmap(o_pixmap)

        self.o_item_src = o_item_src

        self.src_path = src_pathname

        self.reload()
        self.update()


    def set_argv(self, listArgv):

        self.m_listArgv = listArgv

    def reload(self):

        if self.bmp_data is not None:

            list_argv = [POTRACE_PATH] + self.m_listArgv + ["-s", "-", "-o-"]

            o_proc = subprocess.Popen(
                list_argv,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False
            )

            self.svg_data, byteStderr = o_proc.communicate(input=self.bmp_data)

            o_svg_renderer = PyQt5.QtSvg.QSvgRenderer(self.svg_data)

            o_item_dst = PyQt5.QtSvg.QGraphicsSvgItem()
            o_item_dst.setSharedRenderer(o_svg_renderer)
            o_item_dst.setFlags(PyQt5.QtWidgets.QGraphicsItem.ItemClipsToShape)
            o_item_dst.setCacheMode(PyQt5.QtWidgets.QGraphicsItem.NoCache)
            o_item_dst.setZValue(0)

            self.o_item_dst = o_item_dst

    def update(self):

        for o in self.scene().items():
            self.scene().removeItem(o)

        if self.VIEW_MODE == VIEW_MODE_SRC:
            self.scene().addItem(self.o_item_src)
        else:
            self.scene().addItem(self.o_item_dst)

    def wheelEvent(self, oCQWheelEvent):
        fValue = 0
        fValue += oCQWheelEvent.angleDelta().x()
        fValue += oCQWheelEvent.angleDelta().y()
        fFactor = pow(1.2, fValue / 240.0)

        APP_INSTANCE.m_view_dst.scale(fFactor, fFactor)


# ---------------------------------------------------------------------------
class CDropWidget(PyQt5.QtWidgets.QGroupBox):

    def attach(self, o_parent):
        self.m_o_parent = o_parent

    def detach(self):
        o_parent = self.m_o_parent
        self.m_o_parent = None

        return o_parent

    def dragEnterEvent(self, oCQDragEnterEvent):
        if oCQDragEnterEvent.mimeData().hasUrls() is True:
            oCQDragEnterEvent.acceptProposedAction()

    def dropEvent(self, oCQDropEvent):
        for s in oCQDropEvent.mimeData().urls():

            if sys.platform == "win32":
                pathname = s.path()[1:]
            else:
                pathname = s.path()

            self.m_o_parent.actionFileOpen(pathname)

            str_backend = self.m_o_parent.ui.ptBackend.currentText()

            self.m_o_parent.m_oCViewSVG.save(
                pathname + "." + str_backend,
                str_backend
            )
        oCQDropEvent.acceptProposedAction()


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

        global POTRACE_PATH

        # check potrace binary
        try:
            base_pathname = os.path.split(sys.argv[0])[0]
            POTRACE_PATH = potrace_exists(base_pathname)
        except CExcPotrace as exc_message:
            POTRACE_PATH = None
            PyQt5.QtWidgets.QMessageBox.critical(
                self,
                "Potrace exists check.",
                str(exc_message)
            )

        self.ui = ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.m_oCViewSVG = CViewSVG()
        self.m_oCViewSVG.set_view_mode(VIEW_MODE_DST)
        self.setCentralWidget(self.m_oCViewSVG)

        APP_INSTANCE.m_view_src = None
        APP_INSTANCE.m_view_dst = self.m_oCViewSVG



        self.setAcceptDrops(True)

        o_drop_region = CDropWidget(self)
        o_drop_region.setAcceptDrops(True)
        self.ui.verticalLayout.addWidget(o_drop_region)
        o_drop_region.attach(self)

        #
        self.m_refresh_timer = PyQt5.Qt.QTimer(self)

        # Event Connect

        self.ui.actionFileOpen.triggered.connect(self.actionFileOpen)
        self.ui.actionFileSaveAs.triggered.connect(self.actionFileSaveAs)
        self.ui.actionViewZoomIn.triggered.connect(self.actionViewZoomIn)
        self.ui.actionViewZoomOut.triggered.connect(self.actionViewZoomOut)
        self.ui.actionViewZoomReset.triggered.connect(self.actionViewZoomReset)
        self.ui.actionViewRefresh.triggered.connect(self.actionViewRefresh)
        self.ui.actionViewAutoRefresh.triggered.connect(self.actionViewAutoRefresh)
        self.ui.actionViewPreview.triggered.connect(self.actionViewPreview)
        self.ui.actionHelpAbout.triggered.connect(self.actionHelpAbout)

        self.ui.ptTurnpolicy.currentIndexChanged.connect(self.currentIndexChanged)
        self.ui.ptTurdsize.valueChanged.connect(self.valueChanged)
        self.ui.ptAlphamax.valueChanged.connect(self.valueChanged)
        self.ui.ptLongcurve.stateChanged.connect(self.stateChanged)
        self.ui.ptOpttolerance.valueChanged.connect(self.valueChanged)
        self.ui.ptUnit.valueChanged.connect(self.valueChanged)

        self.ui.ptOpaque.stateChanged.connect(self.stateChanged)

        self.ui.ptBlacklevel.valueChanged.connect(self.valueChanged)
        self.ui.ptInvert.stateChanged.connect(self.stateChanged)

        self.ui.ptPagesize.currentIndexChanged.connect(self.currentIndexChanged)
        self.ui.ptTight.stateChanged.connect(self.stateChanged)

        self.m_refresh_timer.timeout.connect(self.singleShot)

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

        listArgv.append("--pagesize=" + self.ui.ptPagesize.currentText())
        if(self.ui.ptTight.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--tight")

        if(self.ui.ptOpaque.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--opaque")

        listArgv.append("--blacklevel=" + str(self.ui.ptBlacklevel.value()))
        if(self.ui.ptInvert.checkState() == PyQt5.QtCore.Qt.Checked):
            listArgv.append("--invert")

        self.m_oCViewSVG.set_argv(listArgv)

        if self.ui.actionViewAutoRefresh.isChecked() is True:
            self.m_refresh_timer.setSingleShot(True)
            self.m_refresh_timer.start(1000)

    def singleShot(self):
        self.m_oCViewSVG.reload()
        self.m_oCViewSVG.update()

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
                "Potrace Supported File",
                "Image files (*.bmp *.gif *.jpg *.jpeg *.pcx *.png *.tga *.tif *.tiff)"
                ";;Bitmap file (*.bmp)"
                ";;GIF file (*.gif)"
                ";;JPEG file (*.jpg *.jpeg)"
                ";;PCX file (*.pcx)"
                ";;PNG file (*.png)"
                ";;TGA file (*.tga)"
                ";;TIFF file (*.tif *.tiff)"
            )

        if path:

            svg_file = PyQt5.QtCore.QFile(path)

            if svg_file.exists() is True:
                self.__build_potrace_argv()
                self.m_oCViewSVG.open(svg_file.fileName())
            else:
                PyQt5.QtWidgets.QMessageBox.critical(
                    self,
                    "Open SVG File",
                    "Could not open file '%s'." % (path,)
                )

    def actionFileSaveAs(self):

        strBackend = self.ui.ptBackend.currentText()

        strPath, strExt = os.path.splitext(self.m_oCViewSVG.src_path)

        if strPath != "":

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
        self.m_oCViewSVG.update()

    def actionViewAutoRefresh(self, b_checked):
        self.m_oCViewSVG.reload()
        self.m_oCViewSVG.update()


    def actionViewPreview(self, b_checked):
        if b_checked is True:
            self.m_oCViewSVG.set_view_mode(VIEW_MODE_DST)
        else:
            self.m_oCViewSVG.set_view_mode(VIEW_MODE_SRC)
        self.m_oCViewSVG.update()

    def actionHelpAbout(self):
        oCAbout = CAbout()
        oCAbout.exec()

    def dragEnterEvent(self, oCQDragEnterEvent):
        if oCQDragEnterEvent.mimeData().hasUrls() is True:
            oCQDragEnterEvent.acceptProposedAction()

    def dropEvent(self, oCQDropEvent):
        for s in oCQDropEvent.mimeData().urls():

            if sys.platform == "win32":
                pathname = s.path()[1:]
            else:
                pathname = s.path()

            self.actionFileOpen(pathname)
            break

        oCQDropEvent.acceptProposedAction()


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
    global APP_INSTANCE

    APP_INSTANCE = PyQt5.QtWidgets.QApplication(sys.argv)

    if APP_INSTANCE is not None:
        o_main = CMainWindow()
        o_main.show()

        APP_INSTANCE.exec_()


if __name__ == "__main__":
    main()



# --------------------------------------------------------------------- [EOF]
