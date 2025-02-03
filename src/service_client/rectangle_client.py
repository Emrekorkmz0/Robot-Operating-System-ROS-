#!/usr/bin/env python


import sys
import rospy
from ros_basics_tutorials.srv import RectangleArea
from ros_basics_tutorials.srv import RectangleAreaRequest
from ros_basics_tutorials.srv import RectangleAreaResponse





def find_are_and_env(a,b,c,d):
    rospy.wait_for_service('find_area_and_env')

    try:
        find_a_e=rospy.ServiceProxy('find_area_and_env',RectangleArea)
        response=find_a_e(a,b,c,d)
        return response.area,response.env
    

    except rospy.ServiceException:
        pass

def usage():
    return


if __name__== '__main__':
    if len(sys.argv) ==5 :
        a=sys.argv[1]
        b=sys.argv[2]
        c=sys.argv[3]
        d=sys.argv[4]
    
    print(f"Requesting a-b-c-d respectively: {a} {b} {c} {d}")
    area,env=find_are_and_env(a,b,c,d)
    print(f"Result of area and env: {area}  {env}")
