"""ROS 2 wrapper for the demo-only delivery mission state machine."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from .state_machine import MissionStateMachine


class MissionManager(Node):
    def __init__(self):
        super().__init__('delivery_mission_manager')
        self.declare_parameter('demo_duration_sec', 5.0)
        self.demo_duration_sec = float(
            self.get_parameter('demo_duration_sec').value
        )
        if self.demo_duration_sec <= 0:
            raise ValueError('demo_duration_sec must be greater than zero')

        self.machine = MissionStateMachine()
        self.status_pub = self.create_publisher(String, '/delivery/status', 10)
        self.goal_sub = self.create_subscription(
            String, '/delivery/goal', self.goal_callback, 10
        )
        self.timer = None
        self.get_logger().info(
            'Mission manager ready. Demo state machine only; no robot motion/Nav2.'
        )
        self.publish_status('IDLE: waiting for a destination')

    def publish_status(self, text):
        msg = String()
        msg.data = text
        self.status_pub.publish(msg)
        self.get_logger().info(text)

    def goal_callback(self, msg):
        accepted, response = self.machine.submit_goal(msg.data)
        self.publish_status(response)
        if not accepted:
            return

        self.publish_status(self.machine.start())
        self.timer = self.create_timer(
            self.demo_duration_sec, self.complete_demo_callback
        )

    def complete_demo_callback(self):
        if self.timer is not None:
            self.timer.cancel()
            self.destroy_timer(self.timer)
            self.timer = None
        self.publish_status(self.machine.complete_demo())


def main(args=None):
    rclpy.init(args=args)
    node = MissionManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
