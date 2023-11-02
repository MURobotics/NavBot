ARG FROM_IMAGE=ros:galactic
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for building
FROM $FROM_IMAGE AS prebuild

ENV DEBIAN_FRONTEND=noninteractive

# required to use add-apt-repository
RUN apt-get update && \ 
  apt-get install -y \
  software-properties-common \
  python3-rosdep \
  git-all \
  ros-galactic-rmw-fastrtps-cpp

ENV MAKEFLAGS="-j1"

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS

# Install nav2
RUN apt-get update && \ 
  apt-get install -y \
  ros-galactic-navigation2 \
  ros-galactic-nav2-bringup

FROM prebuild AS builder

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
COPY src/nav_launch nav_launch

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/nav_launch \
      --ignore-src \
      --skip-keys=librealsense2 \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --packages-select \
        nav_launch \
      --mixin $OVERLAY_MIXINS

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

COPY ./ ./

# run launch file
CMD ["ros2", "launch", "nav_launch", "nav.launch.py"]