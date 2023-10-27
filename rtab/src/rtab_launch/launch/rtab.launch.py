#
#!/usr/bin/env python3
# Copyright  All Rights Reserved.
# @author 
#
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('rtab_launch'),
        'config',
        'params.yml'
    )

    # front_assembler = ComposableNodeContainer(
    #         name='fusion_container',
    #         namespace='/depth_proc',
    #         package='rclcpp_components',
    #         executable='component_container',
    #         composable_node_descriptions=[
    #             ComposableNode(
    #                 package='rtabmap_ros',
    #                 plugin='rtabmap_ros::PointCloudXyzrgbNode',
    #                 name='fl_fusion',
    #                 remappings=[('rgb/camera_info', '/camera/frontleft/camera_info'),
    #                             ('rgb/image_rect_color', '/camera/frontleft/image'),
    #                             ('/depth_registered/image_rect', '/camera/frontleft/depth_registered/image_rect'),
    #                             ('points', '/fl/cloud/color')],
    #             ),
    #         ],
    #         output='screen', 
    # )

    rear_asembler = Node(
        package ='rtabmap_ros',
        executable ='point_cloud_assembler',
        # remappings = [
        #     ('/rgb/image', '/camera/color/image_raw'),
        #     ('/rgb/camera_info', '/camera/color/camera_info'),
        #     ('/depth/image', '/camera/depth/image_rect_raw'),
        # ],
        parameters = [config],
        arguments = [
            '--delete_db_on_start'
        ]
    )

    # full_laser = 

    # Should just launch the node directly, idk why it's set to find the share directory.... might've been messed with for something else
    rtab_launch = Node(
        package ='rtabmap_ros',
        executable ='rtabmap',
        namespace = '/rtab/',
        name = 'rtab',
        remappings = [
            # ('/rtab/rgb/image', '/color/image_raw'),
            # ('/rtab/rgb/camera_info', '/color/camera_info'),
            # ('/rtab/depth/image', '/depth/image_raw'),
            # ('/rtab/depth/camera_info', '/depth/camera_info'),
            # ('/rtab/infra1/image', '/infra1/image_raw'),
            # ('/rtab/infra1/camera_info', '/infra1/camera_info'),
            # ('/rtab/infra2/image', '/infra2/image_raw'),
            # ('/rtab/infra2/camera_info', '/infra2/camera_info'),
            ('/rtab/odom', '/odom'),
            ('/rtab/scan_cloud', '/depth/color/points'),
        ],
        parameters = [config],
        arguments = [
            '--delete_db_on_start'
        ]
    )
         
    return LaunchDescription([
        rtab_launch#rear_asembler,#, left_proc, right_proc
    ])