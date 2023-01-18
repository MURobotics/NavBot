ARG FROM_IMAGE=ros:galactic
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for caching
FROM $FROM_IMAGE AS prebuilder

# Install librealsense2-ros wrapper
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
RUN git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-development realsense-ros

# add RealSense ROS2 Wrapper
# required to use add-apt-repository
RUN apt-get update && \ 
  apt-get install -y \
  software-properties-common \
  python3-rosdep \
  git-all \
  ros-galactic-rmw-fastrtps-cpp \
  ros-galactic-imu-tools

# Install librealsense2
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE && \
  add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u && \
  apt-get update && \
  apt-get install --allow-unauthenticated -y \
  librealsense2-dkms \
  librealsense2-utils \
  librealsense2-dev
  
# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/realsense-ros \
      --ignore-src \
      --skip-keys=librealsense2 \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --packages-select \
        realsense2_camera_msgs \
        realsense2_camera  \
      --mixin $OVERLAY_MIXINS

# multi-stage for building
FROM prebuilder AS builder

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
COPY src/realsense_launch realsense_launch

# install overlay dependencies
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/realsense_launch \
      --ignore-src \
      --skip-keys=librealsense2 \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --packages-select \
        realsense_launch \
      --mixin $OVERLAY_MIXINS

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

COPY ./ ./

# run launch file
CMD ["ros2", "launch", "realsense_launch", "realsense.launch.py"]