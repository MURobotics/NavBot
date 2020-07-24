#!/usr/bin/env python3
import platform
print(platform.python_version())

import KioskUI as ui

def main():
    ui.Menu().run()

if __name__ == "__main__":
    main()
