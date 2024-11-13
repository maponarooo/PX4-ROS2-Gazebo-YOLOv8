# Basic ROS 2 program to subscribe to real-time streaming 
# video from your built-in webcam
# Author:
# - 쿼드(QUAD)드론연구소
# - https://github.com/maponarooo/PX4-ROS2-Gazebo-YOLOv8
  
# Import the necessary libraries
import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
from ultralytics import YOLO # YOLO library

# YOLOv8 모델 사용
model = YOLO('yolov8m.pt')


class ImageSubscriber(Node):
  """
  Node 클래스의 서브클래스인 ImageSubscriber 클래스를 생성.
  """
  def __init__(self):
    # Node 클래스 생성자
    super().__init__('image_subscriber')
      
    # Subscriber를 생성.
    # 이 구독자는 video_frames 토픽으로 부터 이미지를 받아오고 큐 사이즈는 10개로 정의.
    self.subscription = self.create_subscription(
      Image, 
      'camera', 
      self.listener_callback, 
      10)
    self.subscription # prevent unused variable warning
      
    # ROS의 이미지를 OpenCV 이미지로 변경하기 위해 사용
    self.br = CvBridge()
   
  def listener_callback(self, data):
    """
    Callback function.
    """
    # 메시지를 콘솔에 뿌려준다.
    self.get_logger().info('Receiving video frame')
 
    # ROS의 이미지를 OpenCV 이미지로 변경
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding="bgr8")
    image = current_frame
    # 객체 인식
    results = model.predict(image, classes=[0, 2])
    img = results[0].plot()
    # 결과를 보여줌
    cv2.imshow('Detected Frame', img)    
    cv2.waitKey(1)
  
def main(args=None):
  
  # rclpy library 초기화
  rclpy.init(args=args)
  
  # 노드 생성
  image_subscriber = ImageSubscriber()
  
  # Spin 노드
  rclpy.spin(image_subscriber)
  
  # 노드 종료
  image_subscriber.destroy_node()
  
  # ROS 프로그램 종료
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
