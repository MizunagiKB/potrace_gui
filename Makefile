#
#	Makefile for PyQt5
#		Author @MizunagiKB
#
PYTHON3 = python3
PYUIC = pyuic5
PYRCC = pyrcc5

.PHONY: all
all: PYUIC PYRCC

PYUIC: ui_About.py ui_MainWindow.py
PYRCC: resource_rc.py

ui_About.py: ui/About.ui
	$(PYUIC) $< -o $@

ui_MainWindow.py: ui/MainWindow.ui
	$(PYUIC) $< -o $@

resource_rc.py: resource.qrc
	$(PYRCC) $< -o $@

.PHONY: run
run: PYUIC PYRCC
	$(PYTHON3) potrace_gui.py
