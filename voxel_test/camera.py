from alg_math import vec3, mat4
from math import tan, pi

to_radians = lambda x: x / (180 / pi)

class camera:
     def __init__(self, pos : vec3, rot : vec3, fov : float, near : float, far : float):
        self.pos = pos
        self.rot = rot
        self.fov = fov
        self.near = near
        self.far = far