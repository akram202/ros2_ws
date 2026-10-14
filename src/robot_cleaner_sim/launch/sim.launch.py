import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Get the package directory
    pkg_dir = get_package_share_directory('robot_cleaner_sim')

    # Process URDF xacro to XML
    xacro_file = os.path.join(pkg_dir, 'urdf', 'robot.urdf.xacro')
    robot_desc = xacro.process_file(xacro_file).toxml()

    # Define paths for simulation world and bridge config
    world_file = os.path.join(pkg_dir, 'worlds', 'cleaner_world.sdf')
    bridge_cfg = os.path.join(pkg_dir, 'config', 'bridge.yaml')
    rviz_cfg = os.path.join(pkg_dir, 'config', 'robot.rviz')

    return LaunchDescription([
        # Declare arguments (if any)
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        ),

        # 1. Gazebo Sim Process
        # Launches the simulator with our walled world in running mode (-r)
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_file],
            output='screen'
        ),

        # 2. Robot State Publisher
        # Reads URDF/Xacro and publishes state/TF of fixed joints (e.g. chassis, laser)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_desc,
                'use_sim_time': True
            }]
        ),

        # 3. Spawn Robot in Gazebo Sim
        # Calls the 'create' service in ros_gz_sim to spawn the robot model
        Node(
            package='ros_gz_sim',
            executable='create',
            name='spawn_cleaner_bot',
            arguments=[
                '-name', 'cleaner_bot',
                '-string', robot_desc,
                '-x', '0.0',
                '-y', '0.0',
                '-z', '0.1'  # slight altitude to spawn safely
            ],
            output='screen'
        ),

        # 4. ROS-Gazebo Parameter Bridge
        # Leverages the parameter_bridge config file to route topics bi-directionally
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='ros_gz_bridge',
            arguments=['--ros-args', '-p', f'config_file:={bridge_cfg}'],
            output='screen'
        ),

        # 5. Pre-configured RViz2
        # Launches RViz with our custom visualization layout (laserscan, grid, tf, odometry)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_cfg],
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),
    ])
