#!/usr/bin/env python

import rospy
import os
from std_msgs.msg import String


def getInfoCB(data):
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)


def talker():
    pub = rospy.Publisher(os.getenv('MY_ID') + '_telemetry', String, queue_size=10)
    rospy.init_node('chatter', anonymous=True)

    comm_list = os.getenv('COMM_LIST')
    comm_list.split(":")
    for id in comm_list:
        rospy.Subscriber(id + '_telemetry', String, getInfoCB)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "hello_world from " + os.getenv('MY_ID') + " at %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
