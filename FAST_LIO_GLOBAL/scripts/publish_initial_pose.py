#!/usr/bin/env python3
# coding=utf8
from __future__ import print_function, division, absolute_import

import argparse

import rospy
import tf.transformations
from geometry_msgs.msg import Pose, Point, Quaternion, PoseWithCovarianceStamped

from sensor_msgs.msg import PointCloud2

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('x', type=float)
    # parser.add_argument('y', type=float)
    # parser.add_argument('z', type=float)
    # parser.add_argument('yaw', type=float)
    # parser.add_argument('pitch', type=float)
    # parser.add_argument('roll', type=float)
    # args = parser.parse_args()

    rospy.init_node('publish_initial_pose')
    pub_pose = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)

    # 转换为pose
    # quat = tf.transformations.quaternion_from_euler(args.roll, args.pitch, args.yaw)
    # xyz = [args.x, args.y, args.z]
    quat = tf.transformations.quaternion_from_euler(0, 0, 0)
    xyz = [0, 0, 0]

    initial_pose = PoseWithCovarianceStamped()
    initial_pose.pose.pose = Pose(Point(*xyz), Quaternion(*quat))
    initial_pose.header.stamp = rospy.Time().now()
    initial_pose.header.frame_id = 'map'
    rospy.wait_for_message('pcd_map', PointCloud2)
    rospy.sleep(10)
    rospy.loginfo('Initial Pose: {} {} {} {} {} {}'.format(
        0, 0, 0, 0, 0, 0, ))
    pub_pose.publish(initial_pose)
