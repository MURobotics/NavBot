#!/usr/bin/env python3
# Copyright 2021 iRobot Corporation. All Rights Reserved.
# @author Rodrigo Jose Causarano Nunez (rcausaran@irobot.com)
#
# Launch Create(R) 3 in Gazebo and optionally also in RViz.

import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.substitutions import Command
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('state_publisher_launch'),
        'config',
        'params.yaml'
    )

    urdf_file_name = "handheld.urdf.xacro"
    urdf = str(Path(get_package_share_directory('handheld_description'),"urdf", urdf_file_name).resolve())

    robot_description = ParameterValue(Command(['xacro ', str(urdf)]), value_type=str)

    state_publisher = Node(
        package ='robot_state_publisher',
        executable ='robot_state_publisher',
        # remappings = [
        #     ('/imu/data_raw', '/camera/imu'),
        #     ('/imu/data', '/rtabmap/imu'),
        # ],
        parameters = [{'robot_description': robot_description}],
        arguments = [urdf]
    )
         
    return LaunchDescription([
        state_publisher
    ])