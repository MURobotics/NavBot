#!/usr/bin/env python3.6
import math

class Point():

    def create(x, y):
        return {
            "x": x,
            "y": y
        }

    def roundCoordinatesToInt(point):
        return Point.create(
            x = int(point["x"]),
            y = int(point["y"])
        )

    def move(point, offset_point):
        return Point.create(
            x = point["x"] + offset_point["x"],
            y = point["y"] + offset_point["y"]
        )

    def copy(point):
        return Point.create(
            x = point["x"],
            y = point["y"]
        )

    def scale(point, scale):
        return Point.create(
            x = point["x"] * scale,
            y = point["y"] * scale
        )

    #angle in radians
    # point from createPoint
    def rotate(point, angle):

        cos = math.cos(angle)
        sin = math.sin(angle)

        x = point["x"]
        y = point["y"]

        new_point_x = x * cos - y * sin
        new_point_y = x * sin + y * cos

        return Point.create(new_point_x, new_point_y)

    def angleVector(angle):
        return Point.create(math.cos(angle), math.sin(angle))

class Polygon():
    def __init__(self, points):
        self.points = points

    def getPoints(self):
        return self.points

    def scale(self, scale):
        for i in range(len(self.points)):
            curr_point = self.points[i]
            scaled_point = Point.scale(curr_point, scale)
            self.points[i] = scaled_point

    def move(self, offset_pos):
        for i in range(len(self.points)):
            curr_point = self.points[i]
            moved_point = Point.move(curr_point, offset_pos)
            self.points[i] = moved_point

    def rotate(self, angle):
        for i in range(len(self.points)):
            curr_point = self.points[i]
            rotated_point = Point.rotate(curr_point, angle)
            self.points[i] = rotated_point
