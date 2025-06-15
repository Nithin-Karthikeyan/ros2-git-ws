import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped



class Relay2(Node):
    def __init__(self):
        super().__init__("relay_2")
        self.subscriber = self.create_subscription(AckermannDriveStamped, '/drive_relay', self.process_data, 10)

    
    def process_data(self, rec_msg):        
        self.get_logger().info(f"Speed: {rec_msg.drive.speed}, Steering Angle: {rec_msg.drive.steering_angle}")
        


        

def main(args = None):
    rclpy.init(args = args)
    node = Relay2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()