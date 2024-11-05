import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SecretMessage(Node):

    def __init__(self):
        super().__init__('secret_message')
        self.message1 = self.create_publisher(String, 'message_alpha', 10)
        self.message2 = self.create_publisher(String, 'message_beta', 10)
        self.message3 = self.create_publisher(String, 'message_gamma', 10)
        self.message4 = self.create_publisher(String, 'message_delta', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.subscription = self.create_subscription(
            String,
            'submit_decode',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        pair = msg.split(':')
        if pair[1] == "leohungry":
            print(pair[0] + " finished alpha")
        elif pair[1] == "iwantinnout":
            print(pair[0] + " finished beta")
        elif pair[1] == "mayberaisingcanes":
            print(pair[0] + " finished gamma")
        elif pair[1] == "actuallychickfila":
            print(pair[0] + " finished delta")
        else:
            print(pair[0] + " messed up")
            

    def timer_callback(self):
        msg = String()

        msg.data = 'pislyrkvc'
        self.message1.publish(msg)

        msg.data = 'lzdqwlqqrxw'
        self.message2.publish(msg)

        msg.data = 'ocadgtckukpiecpgu'
        self.message3.publish(msg)

        msg.data = 'bduvbmmzdijdlgjmb'
        self.message4.publish(msg)

        self.i += 1
        print('Publishing Round: "%s"' % self.i)


def main(args=None):
    rclpy.init(args=args)

    secret_message = SecretMessage()

    rclpy.spin(secret_message)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    secret_message.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()