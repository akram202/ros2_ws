#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

class SimpleNav2Server(Node):
    def __init__(self):
        super().__init__('simple_nav2_server')
        
        self._action_server = ActionServer(
            self,
            NavigateToPose,
            'navigate_to_pose',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0
        self.min_obstacle_dist = 10.0

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        orientation = msg.pose.pose.orientation
        siny_cosp = 2.0 * (orientation.w * orientation.z + orientation.x * orientation.y)
        cosy_cosp = 1.0 - 2.0 * (orientation.y * orientation.y + orientation.z * orientation.z)
        self.current_yaw = math.atan2(siny_cosp, cosy_cosp)

    def scan_callback(self, msg):
        if len(msg.ranges) > 0:
            n = len(msg.ranges)
            front_ranges = msg.ranges[int(n*0.375):int(n*0.625)]
            valid_ranges = [r for r in front_ranges if not math.isnan(r) and not math.isinf(r) and r > msg.range_min]
            if valid_ranges:
                self.min_obstacle_dist = min(valid_ranges)
            else:
                self.min_obstacle_dist = 10.0

    def goal_callback(self, goal_request):
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received request to cancel goal')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        goal = goal_handle.request.pose
        target_x = goal.pose.position.x
        target_y = goal.pose.position.y

        twist = Twist()

        while rclpy.ok():
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                twist.linear.x = 0.0
                twist.angular.z = 0.0
                self.cmd_vel_pub.publish(twist)
                return NavigateToPose.Result()

            dx = target_x - self.current_x
            dy = target_y - self.current_y
            distance = math.sqrt(dx*dx + dy*dy)

            if distance < 0.3:
                self.get_logger().info('Goal reached!')
                twist.linear.x = 0.0
                twist.angular.z = 0.0
                self.cmd_vel_pub.publish(twist)
                goal_handle.succeed()
                return NavigateToPose.Result()

            target_angle = math.atan2(dy, dx)
            angle_error = target_angle - self.current_yaw
            while angle_error > math.pi:
                angle_error -= 2.0 * math.pi
            while angle_error < -math.pi:
                angle_error += 2.0 * math.pi

            if self.min_obstacle_dist < 0.35:
                twist.linear.x = 0.0
                twist.angular.z = 0.5
            else:
                if abs(angle_error) > 0.5:
                    twist.linear.x = 0.05
                    twist.angular.z = max(min(1.0 * angle_error, 0.6), -0.6)
                else:
                    twist.linear.x = min(0.3 * distance, 0.35)
                    twist.angular.z = max(min(1.5 * angle_error, 0.8), -0.8)

            self.cmd_vel_pub.publish(twist)
            feedback = NavigateToPose.Feedback()
            goal_handle.publish_feedback(feedback)
            await asyncio_sleep(0.1)

async def asyncio_sleep(duration):
    import asyncio
    await asyncio.sleep(duration)

def main(args=None):
    rclpy.init(args=args)
    server = SimpleNav2Server()
    try:
        rclpy.spin(server)
    except KeyboardInterrupt:
        pass
    server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
