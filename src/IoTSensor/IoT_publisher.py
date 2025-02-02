#!/usr/bin/env python

import rospy
from ros_basics_tutorials.msg import IoTSensor


pub=rospy.Publisher('iot_sensor_topic',IoTSensor,queue_size=10)

rospy.init_node('iot_sensor_publisher_node',anonymous=True)

rate=rospy.Rate(1)



while not rospy.is_shutdown():
    iot_sensor=IoTSensor()

    iot_sensor.id=1
    iot_sensor.name="iot_parking_01"
    iot_sensor.temprature=25.33
    iot_sensor.humidity=33.41

    #we make loginfo twice because both are different type of arg
    rospy.loginfo("I publish:")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
