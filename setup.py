# -*- coding: utf-8 -*-
import sys

from cx_Freeze import setup, Executable

application_title = "potraceGUI"
main_python_file = "potrace_gui.py"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "packages": ["os", "subprocess"],
    "excludes": ["tkinter"],
    "include_files": []
}

setup(
        name = application_title,
        version = "0.0",
        description = "potrace GUI(PyQt5)",
        author="@MizunagiKB",
        url="https://github.com/MizunagiKB/potrace_gui",
        options = {
            "build_exe" : build_exe_options
        },
        executables = [Executable(main_python_file, base = base)])
