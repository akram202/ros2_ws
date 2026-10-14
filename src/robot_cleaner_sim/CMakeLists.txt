cmake_minimum_required(VERSION 3.8)
project(robot_cleaner_sim)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

install(DIRECTORY
  urdf
  worlds
  launch
  config
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  robot_cleaner_sim/simple_nav2_server.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
