FROM ros:melodic-ros-base

# install build tools
RUN apt-get update && apt-get install -y \
      python-catkin-tools \
    && rm -rf /var/lib/apt/lists/*

# install python3 ROS deps
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-yaml && \
    export ROS_PYTHON_VERSION=3 && \
    python3 -m pip install rospkg catkin_pkg

# clone ros package repo
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/project

WORKDIR $ROS_WS
COPY project $ROS_WS/src/project

# allow main to be executed
RUN chmod +x /opt/ros_ws/src/project/src/main.py

# install ros package dependencies
RUN apt-get update && \
  rosdep update && \
  rosdep install -y \
    --from-paths \
      src/project \
    --ignore-src && \
  rm -rf /var/lib/apt/lists/*

# build ros package source
RUN catkin config \
    --extend /opt/ros/$ROS_DISTRO && \
  catkin build \
    project

# install kivy dependencies
RUN apt-get update && apt-get install -y \
    python-pip \
    build-essential \
    git \
    python \
    python-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

# install audio and video kivy dependencies
RUN apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good

# install kivy for python 3
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:kivy-team/kivy && \
    apt-get update && \
    sudo apt-get install -y python3-kivy

# install vnc server
RUN apt-get update && apt-get install -y \
  x11vnc \
  xvfb && \
  mkdir ~/.vnc

# append vnc server command to setup.bash
RUN echo 'x11vnc -forever -create' >> $ROS_WS/devel/setup.bash

# source ros package from entrypoint
RUN echo 'export ROS_MASTER_URI=http://master_node:11311' >> $ROS_WS/devel/setup.bash && \
    sed --in-place --expression \
    '$isource "$ROS_WS/devel/setup.bash"' \
    /ros_entrypoint.sh

CMD ["rosrun","project","main.py"]

#https://answers.ros.org/question/312577/catkin_make-command-not-found-executing-by-a-dockerfile/ ruffsl is a saint
