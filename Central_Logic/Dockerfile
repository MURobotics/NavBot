FROM ros:melodic-ros-base

# install build tools
RUN apt-get update && apt-get install -y \
      python-catkin-tools \
    && rm -rf /var/lib/apt/lists/*

# clone ros package repo
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS
RUN git -C src clone \
      -b $ROS_DISTRO-devel \
      https://github.com/ros/ros_tutorials.git

# install ros package dependencies
RUN apt-get update && \
  rosdep update && \
  rosdep install -y \
    --from-paths \
      src/ros_tutorials/rospy_tutorials \
    --ignore-src && \
  rm -rf /var/lib/apt/lists/*

# build ros package source
RUN catkin config \
    --extend /opt/ros/$ROS_DISTRO && \
  catkin build \
    rospy_tutorials

# source ros package from entrypoint
RUN echo 'export ROS_MASTER_URI=http://master_node:11311' >> $ROS_WS/devel/setup.bash && \
    sed --in-place --expression \
    '$isource "$ROS_WS/devel/setup.bash"' \
    /ros_entrypoint.sh

CMD ["rosrun","rospy_tutorials","talker.py"]

#https://answers.ros.org/question/312577/catkin_make-command-not-found-executing-by-a-dockerfile/ ruffsl is a saint
