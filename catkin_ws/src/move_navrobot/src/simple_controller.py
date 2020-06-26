#!/usr/bin/env python3

from __future__ import print_function

import rospy
import math
from webots_ros.srv import *

time_step = 32

def move_robot():

    wheels = ["wheel1", "wheel2", "wheel3", "wheel4"]

    for wheel in wheels:
        base_endpoint = "/navbot/" + wheel

        position_service_name = base_endpoint + "/set_position"
        velocity_service_name = base_endpoint + "/set_velocity"

        set_position = rospy.ServiceProxy(position_service_name, set_float)
        set_velocity = rospy.ServiceProxy(velocity_service_name, set_float)

        try:
            position = set_position(math.inf)
            velocity = set_velocity(1.0)
            
        except rospy.ServiceException as exc:
            print("Service did not process request: " + str(exc))

def apply_timestep(time_step):
    timestep_service_endpoint = "/navbot/robot/time_step"
    timestep = rospy.ServiceProxy(timestep_service_endpoint, set_int)

    try:
        res = timestep(time_step)
        return res
    except rospy.ServiceException as exc:
        print("Fail")
        return False

def robot_init():
    rospy.init_node('navrobot')
    print("Node running...")

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():

        if not apply_timestep(time_step):
            break

        move_robot()
        rate.sleep()

    print("Disconnected from Robot!")
    rospy.spin()

if __name__ == "__main__":
    robot_init()
