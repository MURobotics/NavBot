#!/usr/bin/env python3
import platform
print(platform.python_version())

import KioskUI as ui

from kivy.core.window import Window
Window.fullscreen = 'auto'

def main():
    ui.Menu().run()

if __name__ == "__main__":
    main()
