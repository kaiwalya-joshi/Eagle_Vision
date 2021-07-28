# Eagle_Vision

This repository is created for **Institute Technical Summer
Project (ITSP).** i.e. arranged by Institute Technical Council(ITC)
of IIT Bombay. This repository consist of codes and images related 3D
mapping with bot.  

## Short Description:
Our Project mainly follows like this:
 - Bot Construction
 - Automation
 - 3D Mapping    
     
### Bot Construction:
We designed a two wheeler bot in a gazebo environment.
The bot is made from scratch with the help of urdf files.
We have connected a LaserScan sensor (Hokuyo) which is used
for automation.We attached the kinect-like RGB-D camera sensor 
in front of our bot which is used for SLAM. The way we
constructed our bot, it gives very good results for teleop 
scripts.

### Automation:
Bot move autonomously in the environment. Laserscan sensor  
basically measures the distance of an obstacle in 180 degrees.
(-90 to +90 degrees) We use this data for automation. We have
made our bot to move both autonomously(using python scripts)
and manually(using teleop scripts)

### 3D Mapping:
For mapping, we used the RTAB-Map(Real-time appearance-based mapping)
package. It is a Graph based SLAM approach based on appearance-based
loop closure detection. It checks how likely an image comes from the
previous location. Appearance based SLAM means that the algorithm will
use the data obtained from vision sensors to localize the position of
the robot and simultaneously map the robot in the environment. Loop
Closures are used to determine if the robot has already seen the 
particular frame before; thus, when the robot moves, the map expands
and the number of images that is compared increases in turn. It thus
creates dense maps.


## Simulation System Setup:
 
Go to the ros official website and follow the installation 
guide of ROS(on Ubuntu) [ROS Installation](http://wiki.ros.org/Installation/Ubuntu)

Clone the repository:

``
cd ~/catkin_ws/src
git clone https://github.com/kaiwalya-joshi/Eagle_Vision
``

Go to the RTAB-Map official webpage and install RTAB-Map
package: [RTAB-Map Installation](https://github.com/introlab/rtabmap_ros#ros2-distribution)

Run catkin_make command

``
cd ~/catkin_ws  
catkin_make
``

source your workspace and make some files executable
````
source devel/setup.bash
roscd fouliex_bot
cd scripts
chmod +x teleop
chmod +x reading_laser.py
````

Now you are ready to execute your project. 

## How to run Simulation:

add `source ~/carkin_ws/devel/setup.bash` at the
bottom of your `.bashrc` file
Run the following coomand in your terminal:


1st terminal:
`roslaunch fouliex_bot fouliex_world.launch`

2nd terminal:
`roslaunch fouliex_bot rviz.launch`

3rd terminal
`roslaunch fouliex_bot mapping.launch`

4th terminal:
`roslaunch fouliex_bot amcl.launch`

### For 3D map with bot (with teleop scripts)

5th terminal:
`roslaunch fouliex_bot teleop.launch`

### For 3D map with automated_bot (with python scripts)

5th terminal:
`rosrun fouliex_bot reading_laer.py`

## Disclaimer 
Fair use of github.com/jerriebright/RTABMAP for RTAB-Map 
package reference.


