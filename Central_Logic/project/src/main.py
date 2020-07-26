#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

chatterRoute = rospy.Publisher('chatter', String, queue_size=10)

def receivingInfo(data):
    rospy.loginfo(rospy.get_caller_id() + ' received %s', data.data)
    if not rospy.is_shutdown():
        print(chatterRoute)
        chatterRoute.publish("chatter")

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' received %s', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Central_Logic', anonymous=True)

    rospy.Subscriber('GuiToCen', String, receivingInfo)
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()



if __name__ == '__main__':
    listener()
