ARG FROM_IMAGE=ros:galactic
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for building
FROM $FROM_IMAGE AS builder

ENV DEBIAN_FRONTEND=noninteractive

# required to use add-apt-repository
RUN apt-get update && \ 
  apt-get install -y \
  software-properties-common \
  python3-rosdep \
  git-all \
  ros-galactic-rmw-fastrtps-cpp \
  ros-galactic-xacro

ENV MAKEFLAGS="-j1"

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS

COPY src/handheld_description src/handheld_description
COPY src/state_publisher_launch src/state_publisher_launch

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/state_publisher_launch \
        src/handheld_description \
      --ignore-src -y \
    && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --symlink-install \
      --cmake-args \
      -DCMAKE_BUILD_TYPE=Release \
      --packages-select \
        state_publisher_launch \
        handheld_description \
      --mixin $OVERLAY_MIXINS 
      
# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

COPY ./ ./

# run launch file
CMD ["ros2", "launch", "state_publisher_launch", "state_publisher.launch.py"]