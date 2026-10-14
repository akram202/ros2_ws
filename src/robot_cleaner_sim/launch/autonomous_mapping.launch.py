import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, TimerAction, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_sim = get_package_share_directory('robot_cleaner_sim')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')

    # Environment safeguards for rendering and backend
    set_ogre_backend = SetEnvironmentVariable('GZ_RENDERING_ENGINE_BACKEND', 'ogre')
    software_rendering_arg = DeclareLaunchArgument(
        'software_rendering', default_value='1',
        description='Set LIBGL_ALWAYS_SOFTWARE=1 for rendering compatibility'
    )
    set_software_rendering = SetEnvironmentVariable(
        'LIBGL_ALWAYS_SOFTWARE',
        LaunchConfiguration('software_rendering')
    )

    headless_arg = DeclareLaunchArgument('headless', default_value='false', description='Run Gazebo headless')
    rviz_arg = DeclareLaunchArgument('rviz', default_value='true', description='Open RViz')

    # 1. Base Simulation (Gazebo + RSP + Bridge + RViz2) at t = 0
    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_sim, 'launch', 'simulation.launch.py')
        ),
        launch_arguments={
            'headless': LaunchConfiguration('headless'),
            'rviz': LaunchConfiguration('rviz')
        }.items()
    )

    # 2. SLAM Toolbox delayed by 6.0 seconds to allow physics & tf to stabilize
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )
    delayed_slam = TimerAction(
        period=6.0,
        actions=[slam_launch]
    )

    # 3. Nav2 (navigation_launch.py) & Frontier Exploration (explore node) delayed by 10.0 seconds
    nav2_params_file = os.path.join(pkg_sim, 'config', 'nav2_params.yaml')
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'params_file': nav2_params_file,
            'autostart': 'true'
        }.items()
    )

    explore_node = Node(
        package='explore_lite',
        executable='explore',
        name='explore_node',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'robot_base_frame': 'base_footprint',
            'costmap_topic': 'global_costmap/costmap_raw',
            'costmap_updates_topic': 'global_costmap/costmap_raw_updates',
            'min_frontier_size': 0.5,
            'planner_frequency': 0.33,
            'progress_timeout': 30.0
        }],
        remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
    )

    delayed_nav2_and_explore = TimerAction(
        period=10.0,
        actions=[nav2_launch, explore_node]
    )

    return LaunchDescription([
        set_ogre_backend,
        software_rendering_arg,
        set_software_rendering,
        headless_arg,
        rviz_arg,
        sim_launch,
        delayed_slam,
        delayed_nav2_and_explore
    ])
