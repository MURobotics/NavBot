import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes


class RealSense(Node):
  def __init__(self):
    super().__init__('real_sense')
    



  


def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  real_sense = RealSense()
  
  # Spin the node so the callback function is called.
  rclpy.spin(real_sense)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  real_sense.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()