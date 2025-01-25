from alg_math import mat3, vec3
from math import *

to_radians = lambda x: x / (180 / pi)

def rotationX(angle : float):
   return mat3(1, 0, 0,
               0, cos(to_radians(angle)), -sin(to_radians(angle)),
               0, sin(to_radians(angle)), cos(to_radians(angle)))

def rotationY(angle : float):
   return mat3(cos(to_radians(angle)), 0, sin(to_radians(angle)),
               0, 1, 0,
               -sin(to_radians(angle)), 0, cos(to_radians(angle)))

def rotationZ(angle : float):
   return mat3(cos(to_radians(angle)), -sin(to_radians(angle)), 0,
               sin(to_radians(angle)), cos(to_radians(angle)), 0,
                0, 0, 1)

def rotation(angles : vec3):
   return rotationX(angles.x) * rotationY(angles.y) * rotationZ(angles.z)