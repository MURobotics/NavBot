#!/usr/bin/env python3.6

from controller import Supervisor
import math

from geometry_util import *

class UISystem():

    def __init__(self, display):
        self.display = display

    def getDisplay(self):
        return self.display

    def resetScreen(self, color):
        self.display.setColor(color)
        self.display.fillRectangle(0,0,self.display.getWidth(), self.display.getHeight())

    def log_point(self, point, color):
        self.display.setColor(color)
        self.display.fillRectangle(point["x"], point["y"], 10,10)

    def log_points(self, points, color = 0x000000):
        for point in points:
            self.log_point(point, color)

    def drawPolygon(self, polygon, color):
        self.display.setColor(color)

        x_pos = []
        y_pos = []

        for point in polygon.getPoints():

            x_pos.append(point["x"])
            y_pos.append(point["y"])

        self.display.fillPolygon(x_pos, y_pos)
