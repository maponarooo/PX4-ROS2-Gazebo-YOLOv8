# PX4-ROS2-Gazebo-YOLOv8
Aerial Object Detection using a Drone with PX4 Autopilot and ROS 2. PX4 SITL and Gazebo Garden used for Simulation. YOLOv8 used for Object Detection.

## Demo
[https://github.com/monemati/PX4-ROS2-Gazebo-YOLOv8/assets/58460889/fab19f49-0be6-43ea-a4e4-8e9bc8d59af9](https://youtu.be/WqNVXrTJ0ac)

## Run
### Fly using Keyboard
You need several terminals.
```commandline
Terminal #1:
cd ~/Micro-XRCE-DDS-Agent
MicroXRCEAgent udp4 -p 8888

Terminal #2:
cd ~/PX4-Autopilot
PX4_SYS_AUTOSTART=4002 PX4_GZ_MODEL_POSE="268.08,-128.22,3.86,0.00,0,-0.7" PX4_GZ_MODEL=x500_depth ./build/px4_sitl_default/bin/px4

Terminal #3:
ros2 run ros_gz_image image_bridge /camera

Terminal #4:
source ~/px4-venv/bin/activate
cd ~/PX4-ROS2-Gazebo-YOLOv8
python uav_camera_det.py

Terminal #5:
source ~/px4-venv/bin/activate
cd ~/PX4-ROS2-Gazebo-YOLOv8
python keyboard-mavsdk-test.py
```
When you run the last command a blank window will open for reading inputs from keyboard. focus on that window by clicking on it, then hit "r" on keyboard to arm the drone, and use WASD and Up-Down-Left-Right on the keyboard for flying, and use "l" for landing.

### Fly using ROS 2
You need several terminals.
```commandline
Terminal #1:
cd ~/Micro-XRCE-DDS-Agent
MicroXRCEAgent udp4 -p 8888

Terminal #2:
cd ~/PX4-Autopilot
PX4_SYS_AUTOSTART=4002 PX4_GZ_MODEL_POSE="283.08,-136.22,3.86,0.00,0,-0.7" PX4_GZ_MODEL=x500_depth ./build/px4_sitl_default/bin/px4

Terminal #3:
ros2 run ros_gz_image image_bridge /camera

Terminal #4:
source ~/px4-venv/bin/activate
cd ~/PX4-ROS2-Gazebo-YOLOv8
python uav_camera_det.py

Terminal #5:
cd ~/ws_offboard_control
source /opt/ros/humble/setup.bash
source install/local_setup.bash
ros2 run px4_ros_com offboard_control
```

## Acknowledgement
- https://github.com/PX4/PX4-Autopilot
- https://github.com/ultralytics/ultralytics
- https://www.ros.org/
- https://gazebosim.org/
