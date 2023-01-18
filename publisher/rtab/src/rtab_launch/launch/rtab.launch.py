#!/usr/bin/env python3
# Copyright 2021 iRobot Corporation. All Rights Reserved.
# @author Rodrigo Jose Causarano Nunez (rcausaran@irobot.com)
#
# Launch Create(R) 3 in Gazebo and optionally also in RViz.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('rtab_launch'),
        'config',
        'params.yaml'
    )

    # Should just launch the node directly, idk why it's set to find the share directory.... might've been messed with for something else
    # Not as much past me here... paster me was correct. rtabmap node -> rgbd_odom node -> rgbd relay node -> rgbd sync node
    rtab_launch = Node(
        package ='rtabmap_ros',
        executable ='rtabmap',
        remappings = [
            ('/rgb/image', '/camera/color/image_raw'),
            ('/rgb/camera_info', '/camera/color/camera_info'),
            ('/depth/image', '/camera/depth/image_rect_raw'),
        ],
        parameters = [config],
        arguments = [
            '--delete_db_on_start'
        ]
    )

    rgbd_odom = Node(
        package ='rtabmap_ros',
        executable ='rgbd_odometry',
        parameters = [config],
        remappings = [
            ('/rgb/image', '/camera/color/image_raw'),
            ('/rgb/camera_info', '/camera/color/camera_info'),
            ('/depth/image', '/camera/depth/image_rect_raw'),
            ('/rgbd_image', '/rgbd_image_relay'),
        ],
    )

    rgbd_relay = Node(
        package ='rtabmap_ros',
        executable ='rgbd_relay',
        parameters = [config],
        # remappings = [
        #     ('/rgb/image ', '/camera/aligned_depth_to_color/image_raw'),
        #     ('/rgb/camera_info', '/camera/color/camera_info'),
        #     ('/depth/image', '/camera/aligned_depth_to_color/image_raw'),
        # ],
    )

    rgbd_sync = Node(
        package ='rtabmap_ros',
        executable ='rgbd_sync',
        parameters = [config],
        remappings = [
            ('/rgb/image', '/camera/color/image_raw'),
            ('/rgb/camera_info', '/camera/color/camera_info'),
            ('/depth/image', '/camera/depth/image_rect_raw'),
        ],
    )
         
    return LaunchDescription([
        rtab_launch, rgbd_odom, rgbd_relay, rgbd_sync
    ])