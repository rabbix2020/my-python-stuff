from alg_math import vec3

class voxel:
     def __init__(self, pos : vec3, col : vec3):
        self.pos = pos
        self.col = col

     def __lt__(self, obj):
        return ((self.pos.z) < (obj.pos.z))

     def __gt__(self, obj):
        return ((self.pos.z) > (obj.pos.z))

     def __le__(self, obj):
        return ((self.pos.z) <= (obj.pos.z))

     def __ge__(self, obj):
        return ((self.pos.z) >= (obj.pos.z))

     def __eq__(self, obj):
        return (self.pos.z == obj.pos.z)

     def __repr__(self):
        return f"pos: {self.pos} col: {self.col}"