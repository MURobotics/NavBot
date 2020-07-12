#!/usr/bin/env python3.6

from geometry_util import *



class RobotModel():

    def __init__(self, init_pos = None, init_angle = None):

        if (init_angle == None):
            self.angle = 0
        else:
            self.angle = init_angle

        if (init_pos == None):
            self.pos = Point.create(0,0)
        else:
            self.pos = init_pos

    def getPosition(self):
        return self.pos

    def setPosition(self, new_position):
        self.pos = new_position

    def getAngle(self):
        return self.angle

    def setAngle(self, new_angle):
        self.angle = new_angle

    def render(self, ui_system):

        polygon_points = [
            Point.create(-2,0),
            Point.create(1,2),
            Point.create(1, -2)
        ]
        robot_scale = 10
        robot_color = 0xFF0000

        robot_polygon = Polygon(polygon_points)

        robot_polygon.rotate(self.angle)
        robot_polygon.scale(robot_scale)
        robot_polygon.move(self.pos)

        ui_system.drawPolygon(robot_polygon, robot_color)
