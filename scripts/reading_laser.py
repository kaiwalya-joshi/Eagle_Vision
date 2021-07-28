#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math


def callback(msg_laser):
    regions = [min(msg_laser.ranges[10], 10),
               min(msg_laser.ranges[360], 10),
               min(msg_laser.ranges[710], 10), ]
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    move = Twist()
    move.linear.x = 0
    move.angular.z = 0
    state_description = ""

    d = 1.5

    if regions[1] >= d and regions[2] >= d:
        state_description = 'case 1 - nothing'
        move = turn_left()
    elif regions[1] < d and regions[2] >=d:
        state_description = 'case 2 - front'
        move = turn_right()
    elif regions[1] >= d and regions[2] < d:
        state_description = 'case 3 - left'
        move = follow_the_wall()
    elif regions[1] < d and regions[2] < d:
        state_description = 'case 4 - left and front'
        move = turn_right()
    else:
        move.linear.x = 0.5
        move.angular.z = 0

    rospy.loginfo(state_description + str(regions))
    pub.publish(move)


def turn_left():
    msg = Twist()
    msg.angular.z = -0.4
    msg.linear.x = 0.0
    return msg


def turn_right():
    msg = Twist()
    msg.angular.z = 0.4
    msg.linear.x = 0.0
    return msg


def follow_the_wall():
    msg = Twist()
    msg.linear.x = 0.5
    msg.angular.z = 0.0
    return msg


def laser():
    while not rospy.is_shutdown():
        rospy.Subscriber('/fouliex_bot/laser/scan', LaserScan, callback)
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('reading_laser')
    try:
        laser()

    except rospy.ROSInterruptException:
        pass
