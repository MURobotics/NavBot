cmake_minimum_required(VERSION 3.0.2)
project(move_navrobot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  webots_ros
  sensor_msgs message_generation tf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES move_navrobot
#  CATKIN_DEPENDS roscpp rospy std_msgs webots_ros
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(robot_information_parser src/robot_information_parser.cpp)
add_executable(robot_navbot_controller src/robot_navbot_controller.cpp)

add_dependencies(robot_information_parser ${catkin_EXPORTED_TARGETS})
add_dependencies(robot_navbot_controller ${catkin_EXPORTED_TARGETS})

target_link_libraries(robot_information_parser
	${catkin_LIBRARIES}
)


target_link_libraries(robot_navbot_controller
	${catkin_LIBRARIES}
)
