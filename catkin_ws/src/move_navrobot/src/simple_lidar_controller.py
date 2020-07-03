#!/usr/bin/env python3

from __future__ import print_function

import rospy
import math
from webots_ros.srv import *

from robot_util import RobotModel

time_step = 32
robot_name = "navbot"

def robot_init():
    rospy.init_node('navrobot')
    print("Node running...")

    Navbot = RobotModel("navbot", wheels = ["wheel1", "wheel2", "wheel3", "wheel4"], lidar_name="navbot_lidar")
    Navbot.Lidar.enable_lidar(time_step)
    Navbot.Lidar.enable_point_cloud()

    rate = rospy.Rate(30)
    while not rospy.is_shutdown():

        if not Navbot.timestep(time_step):
            break

        Navbot.move_robot(10.0)
        rate.sleep()

    print("Disconnected from Robot!")
    rospy.spin()

if __name__ == "__main__":
    robot_init()
