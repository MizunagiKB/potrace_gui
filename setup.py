# -*- coding: utf-8 -*-
# ----------------------------------------------------------------- import(s)
import sys
from cx_Freeze import setup, Executable

base = None
if(sys.platform == "win32"):
    base = None

build_exe_options = {
    "packages": ["os", "codecs", "encodings", "subprocess"],
    "excludes": ["tkinter"],
    "include_files": [
        "bin"
    ]
}

setup(
    name="potraceGUI",
    version="0.1.2",
    description="potrace GUI(PyQt5)",
    author="@MizunagiKB",
    url="https://github.com/MizunagiKB/potrace_gui",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable("potrace_gui.py", base=base)]
)
