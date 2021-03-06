#vector transformation
#
#@author:Rahul Ghuge
#  This module let you transform geometry in 2d coordinate
#"""
import math
def normalize_vector(p1,p2):
    '''
     p1 and p2 are start and end points of line.
     the function normalize the vector and returns
     unit length
    '''
    px=p2[0]-p1[0]
    py=p2[1]-p1[1]
    mgn=math.sqrt((px*px)+(py*py))
    return [px/mgn,py/mgn]
def resize_vector(p1,p2,length):
    ''' This function resize the vector into desired manitude.
        p1,p2 are start and end points of line and length is
        magnitude that you would like your vector to be resize.
    '''
    nv=normalize_vector(p1,p2)
    return [(nv[0]*length)+p1[0],(nv[1]*length)+p1[1]]
def magnitude(p1,p2):
    '''
      Return manitude of vector magnitude.
    '''
    px=p2[0]-p1[0]
    py=p2[1]-p1[1]
    return math.sqrt((px*px)+(py*py))
