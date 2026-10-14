import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # 1. Setup paths
    pkg_dir = get_package_share_directory('robot_cleaner_sim')
    
    # Process URDF xacro to XML
    xacro_file = os.path.join(pkg_dir, 'urdf', 'robot.urdf.xacro')
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    world_file = os.path.join(pkg_dir, 'worlds', 'cleaner_world.sdf')
    bridge_cfg = os.path.join(pkg_dir, 'config', 'bridge.yaml')
    rviz_cfg = os.path.join(pkg_dir, 'config', 'robot.rviz')

    # 2. Declare launch arguments
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation clock if true')
    headless_arg = DeclareLaunchArgument('headless', default_value='false', description='Whether to execute Gazebo in headless mode (without GUI)')
    rviz_arg = DeclareLaunchArgument('rviz', default_value='true', description='Whether to launch RViz2')

    use_sim_time = LaunchConfiguration('use_sim_time')

    # Build gz_args based on headless argument
    gz_args = PythonExpression([
        "'-s -r ' if '", LaunchConfiguration('headless'), "' == 'true' else '-r '",
        f"'{world_file}'"
    ])

    # 3. Define Nodes and Processes

    # Gazebo Sim
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': gz_args,
            'on_exit_shutdown': 'true'
        }.items(),
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_raw,
            'use_sim_time': use_sim_time
        }]
    )

    # Spawn Robot
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_cleaner_bot',
        arguments=[
            '-name', 'cleaner_bot',
            '-string', robot_description_raw,
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.1'
        ],
        output='screen'
    )

    # Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': bridge_cfg,
            'use_sim_time': use_sim_time
        }],
        output='screen'
    )

    # RViz2
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_cfg],
        condition=IfCondition(LaunchConfiguration('rviz')),
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        use_sim_time_arg,
        headless_arg,
        rviz_arg,
        gz_sim,
        robot_state_publisher,
        spawn_robot,
        bridge,
        rviz2
    ])
