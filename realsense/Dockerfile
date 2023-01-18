ARG FROM_IMAGE=ros:galactic
ARG OVERLAY_WS=/opt/ros/overlay_ws

# multi-stage for caching
FROM $FROM_IMAGE AS cacher

# clone overlay source
ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src
COPY src/realsense realsense

# Install librealsense2-ros wrapper
WORKDIR $OVERLAY_WS/src
RUN git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-development

# copy manifests for caching
WORKDIR /opt
RUN mkdir -p /tmp/opt && \
    find ./ -name "package.xml" | \
      xargs cp --parents -t /tmp/opt && \
    find ./ -name "COLCON_IGNORE" | \
      xargs cp --parents -t /tmp/opt || true

# multi-stage for building
FROM $FROM_IMAGE AS builder

# add RealSense ROS2 Wrapper
# required to use add-apt-repository
RUN apt-get update && \ 
  apt-get install -y \
  software-properties-common \
  python3-rosdep \
  git-all \
  ros-galactic-rmw-fastrtps-cpp

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
COPY --from=cacher /tmp/$OVERLAY_WS/src ./src
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && rosdep install -y \
      --from-paths \
        src/realsense-ros \
        src/realsense \
      --ignore-src \
      --skip-keys=librealsense2 \
    && rm -rf /var/lib/apt/lists/*

# build overlay source
COPY --from=cacher $OVERLAY_WS/src ./src
ARG OVERLAY_MIXINS="release"
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build \
      --packages-select \
        realsense2_camera_msgs \
        realsense2_camera  \
        realsense \
      --mixin $OVERLAY_MIXINS

# source entrypoint setup
ENV OVERLAY_WS $OVERLAY_WS
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

COPY ./ ./

# run launch file
CMD ["ros2", "launch", "realsense2_camera", "rs_launch.py"]