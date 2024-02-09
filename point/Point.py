""""LA classe point"""
from math import *
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    """"La distance d'un point par rapport à un autre point point """
    def distance(self,point):
        return (sqrt((self.x-point.x)**2+(self.y-point.y)**2))
    """La distance entre deux points"""


def distance(point1,point2):
    return(point1.distance(point2))

p1=Point(12,-23)
p2=Point()
print( "la distance est{} m".format(distance(p1,p2)))