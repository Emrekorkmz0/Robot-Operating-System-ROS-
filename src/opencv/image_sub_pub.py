#!/usr/bin/env python


import rospy
import cv2 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys

#to convert ros to cv2
bridge= CvBridge()


def image_callback(ros_image):
    print('got an image')

    global bridge

    try:
        cv_image=bridge.imgmsg_to_cv2(ros_image)
    except CvBridgeError:
        pass

    (row,col,channel)=cv_image.shape

    if col>200 and row>200 :
        cv2.circle(cv_image,(100,100),90,255)
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_image,'Webcam Activated',(10,350),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("Frame",cv_image)


def main(args):
    rospy.init_node('image_converter',anonymous=True)

    #for turtlebot3 waffle
    #image_topic="/camera/rgb/image_raw/compressed"
    #for usb cam
    #image_topic="/usb_cam/image_raw"

    image_sub=rospy.Subscriber('/usb_cam/image_raw',Image,image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    cv2.destroyAllWindows()


if __name__=='__main__':
    main(sys.argv)
