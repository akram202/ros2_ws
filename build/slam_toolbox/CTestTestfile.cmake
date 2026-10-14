# CMake generated Testfile for 
# Source directory: /home/akram00/ros2_ws/src/slam_toolbox
# Build directory: /home/akram00/ros2_ws/build/slam_toolbox
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[scan_filter_test]=] "/usr/bin/python3" "-u" "/opt/ros/lyrical/share/ament_cmake_test/cmake/run_test.py" "/home/akram00/ros2_ws/build/slam_toolbox/test_results/slam_toolbox/scan_filter_test.gtest.xml" "--package-name" "slam_toolbox" "--output-file" "/home/akram00/ros2_ws/build/slam_toolbox/ament_cmake_gtest/scan_filter_test.txt" "--command" "/home/akram00/ros2_ws/build/slam_toolbox/scan_filter_test" "--gtest_output=xml:/home/akram00/ros2_ws/build/slam_toolbox/test_results/slam_toolbox/scan_filter_test.gtest.xml")
set_tests_properties([=[scan_filter_test]=] PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/akram00/ros2_ws/build/slam_toolbox/scan_filter_test" TIMEOUT "60" WORKING_DIRECTORY "/home/akram00/ros2_ws/build/slam_toolbox" _BACKTRACE_TRIPLES "/opt/ros/lyrical/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/lyrical/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;95;ament_add_test;/opt/ros/lyrical/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/akram00/ros2_ws/src/slam_toolbox/CMakeLists.txt;304;ament_add_gtest;/home/akram00/ros2_ws/src/slam_toolbox/CMakeLists.txt;0;")
subdirs("lib/karto_sdk")
subdirs("slam_toolbox__py")
subdirs("slam_toolbox__rs")
