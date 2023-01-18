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

    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('realsense2_camera'), 'launch'),
            '/rs_launch.py']),
            launch_arguments = {
                'align_depth.enable': 'true',
                'pointcloud.enable': 'true',
 #               'enable_sync': 'true',
                'base_frame_id': 'camera_link',
                'publish_tf': 'true',
                'unite_imu_method': '2',
                'enable_gyro': 'true',
                'enable_accel': 'true',
            }.items()
        )

    #
    # TFs aren't publishing for a reason from the realsense to other nodes:
    # https://github.com/IntelRealSense/realsense-ros#limitations
    #

    imu_filter = Node(
            package='imu_filter_madgwick',
            executable ='imu_filter_madgwick_node',
            parameters = [
                {'use_mag': False},
                {'fixed_frame': "camera_imu_frame"},
                {'publish_tf': False},
                {'world_frame': "enu"},
            ],
            remappings = [
                ('/imu/data_raw', '/camera/imu'),
                ('/imu/data', '/rtabmap/imu'),
            ]
        )

    static_transformation = Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static',
            arguments = [
                '--x', '0.0', 
                '--y', '0.0', 
                '--z', '0.0', 
                '--yaw', '0.0', 
                '--pitch', '0.0', 
                '--roll', '0.0', 
                '--frame-id', 'base_link', 
                '--child-frame-id', 'odom'
            ]
        )
        
    
    return LaunchDescription([
        realsense_launch, imu_filter#, static_transformation
    ])