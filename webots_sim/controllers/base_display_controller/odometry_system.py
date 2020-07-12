#!/usr/bin/env python3.6

'''
TwoWheelOdometry

Wheel vel is in Radians/Sec
'''

from geometry_util import *

def computeLinearVelocity(angular_velocity, radius):
    return angular_velocity * radius

def computeChangeInPosition(linear_velocity, delta_time):
    return linear_velocity * delta_time

def computeAngularVelocity(tangential_velocity, radius):
    return tangential_velocity / radius

def computeChangeInAngle(angular_velocity, delta_time):
    return angular_velocity * delta_time


class TwoWheelOdometry():

    def __init__(self, wheel_radius, chassis_distance):
        self.wheel_radius = wheel_radius
        self.chassis_distance = chassis_distance

        self.left_wheel_angular_vel = 0
        self.right_wheel_angular_vel = 0

    def updateWheelAngularVelocity(self, left_wheel_angular_vel, right_wheel_angular_vel):
        self.left_wheel_angular_vel = left_wheel_angular_vel
        self.right_wheel_angular_vel = right_wheel_angular_vel

    def performOdometry(self, timestep):

        #initialize variables
        pos_offset = 0
        delta_angle = 0
        # Perform Logic Here

        # If Both Wheels spinning at same velocity
        # Case One: Translation
        if (self.left_wheel_angular_vel == self.right_wheel_angular_vel):
            pos_offset = self.get_position_change(timestep)

        # Or If Both Wheels spinning at same speed but flipped velocity
        # Case Two: Rotation
        elif (self.left_wheel_angular_vel == -self.right_wheel_angular_vel):
            delta_angle = self.get_angle_change(timestep)

        # OR If Both Wheels spinning at DIFFERENT speed
        # Case Three

        # Return result
        return {
            "position_offset": pos_offset,
            "angle_offset": delta_angle
        }

    def get_position_change(self, timestep):
        # angular velocity = rad/s
        # velocity = w * radius


        w = self.left_wheel_angular_vel

        overall_vel = computeLinearVelocity(w, self.wheel_radius)
        delta_time = (timestep/1000.0) #magic number
        position_change = computeChangeInPosition(overall_vel, delta_time)

        return position_change

    def get_angle_change(self, timestep):

        wheel_angular_velocity = self.left_wheel_angular_vel
        wheel_linear_velocity = computeLinearVelocity(wheel_angular_velocity, self.wheel_radius)

        chassis_angular_velocity = computeAngularVelocity(wheel_linear_velocity, self.chassis_distance)

        delta_time = (timestep / 1000.0) #magic number

        delta_angle = computeChangeInAngle(chassis_angular_velocity, delta_time)
        return delta_angle


    def PositionOffsetInDirection(angle, position_delta):

        orientation_vec = Point.angleVector(angle)
        position_delta_in_direction = Point.create(
            x = position_delta * orientation_vec["x"],
            y = position_delta * orientation_vec["y"]
        )

        return position_delta_in_direction
