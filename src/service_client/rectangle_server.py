#!/usr/bin/env python

import rospy
import time
from ros_basics_tutorials.srv import RectangleArea
from ros_basics_tutorials.srv import RectangleAreaRequest
from ros_basics_tutorials.srv import RectangleAreaResponse



def handle_area_and_env(request):
    print(f"Requests  {request.a}--{request.b}--{request.c}-{request.d}")

    time.sleep(3)

    area_response=RectangleAreaResponse(request.a*request.b)
    env_response=RectangleAreaResponse(request.a + request.b + request.c + request.d)

    return area_response,env_response

def area_and_env():
    rospy.init_node("find_area_and_env_node")

    rospy.Service("find_area_and_env",RectangleArea,handle_area_and_env)

    print("Ready to calculation")
    rospy.spin()


if __name__=='__main__':
    area_and_env()
