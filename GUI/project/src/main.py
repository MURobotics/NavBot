#!/usr/bin/env python3
import platform
print(platform.python_version())

import rospy
from std_msgs.msg import String

import os

import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy import Config
Config.set('graphics', 'multisamples', '0')
import KioskUI as ui

def main():
    ui.Menu().run()

if __name__ == "__main__":
    main()
