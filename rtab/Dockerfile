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

# Install rtab and rtab-ros wrapper
RUN git clone --depth 1 --branch 0.20.22-humble https://github.com/introlab/rtabmap.git src/rtabmap && \
  git clone --depth 1 --branch 0.20.22-humble https://github.com/introlab/rtabmap_ros.git src/rtabmap_ros

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/rtabmap \
        src/rtabmap_ros \
      --ignore-src -y \
    && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --symlink-install \
      --cmake-args \
      -DRTABMAP_SYNC_MULTI_RGBD=ON \
      -DRTABMAP_SYNC_USER_DATA=ON \
      -DCMAKE_BUILD_TYPE=Release \
      --packages-select \
        rtabmap \
        rtabmap_ros \
      --mixin $OVERLAY_MIXINS 
      
# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

FROM prebuild AS builder

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
COPY src/rtab_launch rtab_launch

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/rtab_launch \
      --ignore-src \
      --skip-keys=librealsense2 \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --packages-select \
        rtab_launch \
      --mixin $OVERLAY_MIXINS

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

COPY ./ ./

# run launch file
CMD ["ros2", "launch", "rtab_launch", "rtab.launch.py"]