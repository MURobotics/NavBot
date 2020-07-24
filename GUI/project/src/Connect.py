#file for connection/api classes and
import rospy
from std_msgs.msg import String

def getLocation():
    return 0,0

print("top")

class RosNode():
    rospy.init_node('Gui')
    toggleRoute = rospy.Publisher('GuiToCen', String, queue_size=10)

    def __init__(self, **kwargs):
        pass

    def toggle(self):
        if not rospy.is_shutdown():
            print(self.toggleRoute)
            r = rospy.Rate(10) # 10hz
            self.toggleRoute.publish("switch")
        else:
            print('rospy down')
