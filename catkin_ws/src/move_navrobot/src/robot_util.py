#!/usr/bin/env python3

from __future__ import print_function

import rospy
import math
from webots_ros.srv import *

class LidarModel:

    def __init__(self, robot_model, lidar_name=""):
        self.robot_model = robot_model
        self.lidar_endpoint = self.robot_model.base_robot_url + "/" + lidar_name

    def enable_lidar(self, sampling_period):
        enable_endpoint = self.lidar_endpoint + "/" + "enable"
        enable_lidar = rospy.ServiceProxy(enable_endpoint, set_int)

        try:
            result = enable_lidar(sampling_period)
            return result
        except rospy.ServiceException as exc:
            print("Failed to enable lidar")
            return False

    def enable_point_cloud(self):
        enable_endpoint = self.lidar_endpoint + "/" + "enable_point_cloud"
        enable_point_cloud = rospy.ServiceProxy(enable_endpoint, set_bool)

        try:
            result = enable_point_cloud(True)
            return result
        except rospy.ServiceException as exc:
            print("Failed to enable lidar")
            return False

    def grab_lidar_data(self):
        return []

class RobotModel:

    def __init__(self, robot_name, wheels = [], lidar_name = ""):
        self.base_robot_url = "/" + robot_name
        self.Lidar = LidarModel(self, lidar_name = lidar_name)
        self.wheels = wheels

    def move_robot(self, vel):
        for wheel in self.wheels:
            base_endpoint = self.base_robot_url + "/" + wheel

            position_service_name = base_endpoint + "/set_position"
            velocity_service_name = base_endpoint + "/set_velocity"

            set_position = rospy.ServiceProxy(position_service_name, set_float)
            set_velocity = rospy.ServiceProxy(velocity_service_name, set_float)

            try:
                set_position(math.inf)
                set_velocity(vel)
            except rospy.ServiceException as exc:
                print("Service did not process request: " + str(exc))

    def timestep(self, time_step):
        timestep_service_endpoint = self.base_robot_url + "/robot/time_step"
        timestep = rospy.ServiceProxy(timestep_service_endpoint, set_int)

        try:
            res = timestep(time_step)
            return res
        except rospy.ServiceException as exc:
            print("Fail")
            return False
