#!/usr/bin/env python3

import rospy
import os
import rospy
import rospkg
import subprocess
import roslaunch
import time
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Ocular', anonymous=True)

    rospy.Subscriber('chatter', String, callback)
    try_catch_launch()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def try_catch_launch():
    """
    Does work as well from service/topic callbacks using launch files
    """
    package = 'simulation_gazebo'
    launch_file = 'main.launch'

    command = "roslaunch {0} {1}".format(package, launch_file)

    p = subprocess.Popen(command, shell=True)

    state = p.poll()
    while True:
        if rospy.is_shutdown():
            break
        state = p.poll()
        if state is None:
            state == None
            #harmless, meant so we can read elif
        elif state < 0:
            rospy.loginfo("Process terminated with error")
            command = "roslaunch {0} {1}".format(package, launch_file)
        elif state > 0:
            rospy.loginfo("Process terminated without error")
            break
        time.sleep(3000)
    rospy.loginfo("Process terminated without error, shifting to spin() for container EOL")


if __name__ == '__main__':
    listener()
