"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ["data"]
OPTIONS = {
    "iconfile": "Rak.icns",
    "argv_emulation": True,
    "packages": ["pygame", "tcod", "numpy", "cffi"]

}

setup(
    app=APP,
    data_files=DATA_FILES,
    name="Tower of Rak",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
