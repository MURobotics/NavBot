source ./catkin_ws/devel/setup.bash


roslaunch webots_ros webots.launch mode:="run" no-gui:="true" world:="$PWD/webots_sim/worlds/navbot-with-ros-controller.wbt"

