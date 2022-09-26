FROM ros:melodic-ros-base

# install build tools
RUN apt-get update && apt-get install -y \
      python-catkin-tools \
    && rm -rf /var/lib/apt/lists/*

# clone ros package repo
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/project

WORKDIR $ROS_WS
COPY project $ROS_WS/src/project

RUN chmod +x /opt/ros_ws/src/project/src/main.py

# install ros package dependencies
RUN apt-get update && \
  rosdep update && \
  rosdep install -y \
    --from-paths \
      src/project \
    --ignore-src && \
  rm -rf /var/lib/apt/lists/*

# install python3 ROS deps
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-yaml && \
    export ROS_PYTHON_VERSION=3 && \
    python3 -m pip install rospkg catkin_pkg

# build ros package source
RUN catkin config \
    --extend /opt/ros/$ROS_DISTRO && \
  catkin build \
    project

# source ros package from entrypoint
RUN echo 'export ROS_MASTER_URI=http://master_node:11311' >> $ROS_WS/devel/setup.bash && \
    sed --in-place --expression \
    '$isource "$ROS_WS/devel/setup.bash"' \
    /ros_entrypoint.sh

CMD ["rosrun","project","main.py"]

#https://answers.ros.org/question/312577/catkin_make-command-not-found-executing-by-a-dockerfile/ ruffsl is a saint
