class vec2:
     def __init__(self, x, y):
        self.x = x
        self.y = y

     def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

     def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

     def __mul__(self, other):
        return vec2(self.x * other.x, self.y * other.y)

     def __truediv__(self, other):
        return vec2(self.x / other, self.y / other)

     def __str__(self):
        return f"{self.x}, {self.y}"

     def length(self):
        return (self.x**2 + self.y**2)**0.5

     def normalize(self):	return self / self.length()

class mat2:
     def __init__(self, a, b, c, d):
        self.array = [[a, b], [c, d]]

     def __mul__(self, other):
        if type(other) == mat2:

           return mat2( (self.array[0][0]*other.array[0][0]) + (self.array[0][1]*other.array[1][0]), (self.array[0][0]*other.array[0][1]) + (self.array[0][1]*other.array[1][1]),
                        (self.array[1][0]*other.array[0][0]) + (self.array[1][1]*other.array[1][0]), (self.array[1][0]*other.array[0][1]) + (self.array[1][1]*other.array[1][1]))

        if type(other) == vec2:
                 return vec2(self.array[0][0] * other.x + self.array[0][1] * other.y, self.array[1][0] * other.x + self.array[1][1] * other.y)

     def __str__(self):
        return f"{self.array[0]}\n{self.array[1]}"

class mat2:
     def __init__(self, a, b, c, d):
        self.array = [[a, b], [c, d]]

     def __mul__(self, other):
        if type(other) == mat2:

           return mat2( (self.array[0][0]*other.array[0][0]) + (self.array[0][1]*other.array[1][0]), (self.array[0][0]*other.array[0][1]) + (self.array[0][1]*other.array[1][1]),
                        (self.array[1][0]*other.array[0][0]) + (self.array[1][1]*other.array[1][0]), (self.array[1][0]*other.array[0][1]) + (self.array[1][1]*other.array[1][1]))

        if type(other) == vec2:
                 return vec2(self.array[0][0] * other.x + self.array[0][1] * other.y,
                             self.array[1][0] * other.x + self.array[1][1] * other.y)

     def __str__(self):
        return f"{self.array[0]}\n{self.array[1]}"

class vec3:
     def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

     def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

     def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

     def __mul__(self, other):
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)

     def __truediv__(self, other):
        return vec3(self.x / other, self.y / other, self.z / other)

     def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

     def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

     def normalize(self):	return self / self.length()

     def to_vec2(self):
        return vec2(self.x, self.y)

     def to_vec4(self):
        return vec4(self.x, self.y, self.z, 1)

class mat3:
     def __init__(self, a, b, c, d, e, f, g, h, i):
        self.array = [[a, b, c], [d, e, f], [g, h, i]]

     def __mul__(self, other):
        if type(other) == mat3:

           return mat3((self.array[0][0]*other.array[0][0]) + (self.array[0][1]*other.array[1][0]) + (self.array[0][2]*other.array[2][0]), (self.array[0][0]*other.array[0][1]) + (self.array[0][1]*other.array[1][1]) + (self.array[0][2]*other.array[2][1]), (self.array[0][0]*other.array[0][2]) + (self.array[0][1]*other.array[1][2]) + (self.array[0][2]*other.array[2][2]),
                       (self.array[1][0]*other.array[0][0]) + (self.array[1][1]*other.array[1][0]) + (self.array[1][2]*other.array[2][0]), (self.array[1][0]*other.array[0][1]) + (self.array[1][1]*other.array[1][1]) + (self.array[1][2]*other.array[2][1]), (self.array[1][0]*other.array[0][2]) + (self.array[1][1]*other.array[1][2]) + (self.array[1][2]*other.array[2][2]),
                       (self.array[2][0]*other.array[0][0]) + (self.array[2][1]*other.array[1][0]) + (self.array[2][2]*other.array[2][0]), (self.array[2][0]*other.array[0][1]) + (self.array[2][1]*other.array[1][1]) + (self.array[2][2]*other.array[2][1]), (self.array[2][0]*other.array[0][2]) + (self.array[2][1]*other.array[1][2]) + (self.array[2][2]*other.array[2][2]))

        if type(other) == vec3:
                 return vec3(self.array[0][0] * other.x + self.array[0][1] * other.y + self.array[0][2] * other.z,
                             self.array[1][0] * other.x + self.array[1][1] * other.y + self.array[1][2] * other.z,
                             self.array[2][0] * other.x + self.array[2][1] * other.y + self.array[2][2] * other.z)

     def __str__(self):
        return f"{self.array[0]}\n{self.array[1]}\n{self.array[2]}"

class vec4:
     def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

     def __add__(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

     def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

     def __mul__(self, other):
        return vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

     def __truediv__(self, other):
        return vec4(self.x / other, self.y / other, self.z / other, self.w / other)

     def __str__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.w}"

     def length(self):
        return (self.x**2 + self.y**2 + self.z**2 + self.w**2)**0.5

     def normalize(self):	return self / self.length()

     def to_vec3(self):
        return vec3(self.x, self.y, self.z)

class mat4:
     def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.array = [[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]

     def __mul__(self, other):
        if type(other) == mat4:

           return mat4((self.array[0][0]*other.array[0][0]) + (self.array[0][1]*other.array[1][0]) + (self.array[0][2]*other.array[2][0]) + (self.array[0][3]*other.array[3][0]), (self.array[0][0]*other.array[0][1]) + (self.array[0][1]*other.array[1][1]) + (self.array[0][2]*other.array[2][1]) + (self.array[0][3]*other.array[3][1]), (self.array[0][0]*other.array[0][2]) + (self.array[0][1]*other.array[1][2]) + (self.array[0][2]*other.array[2][2]) + (self.array[0][3]*other.array[3][2]), (self.array[0][0]*other.array[0][3]) + (self.array[0][1]*other.array[1][3]) + (self.array[0][2]*other.array[2][3]) + (self.array[0][3]*other.array[3][3]),
                       (self.array[1][0]*other.array[0][0]) + (self.array[1][1]*other.array[1][0]) + (self.array[1][2]*other.array[2][0]) + (self.array[1][3]*other.array[3][0]), (self.array[1][0]*other.array[0][1]) + (self.array[1][1]*other.array[1][1]) + (self.array[1][2]*other.array[2][1]) + (self.array[1][3]*other.array[3][1]), (self.array[1][0]*other.array[0][2]) + (self.array[1][1]*other.array[1][2]) + (self.array[1][2]*other.array[2][2]) + (self.array[1][3]*other.array[3][2]), (self.array[1][0]*other.array[0][3]) + (self.array[1][1]*other.array[1][3]) + (self.array[1][2]*other.array[2][3]) + (self.array[1][3]*other.array[3][3]),
                       (self.array[2][0]*other.array[0][0]) + (self.array[2][1]*other.array[1][0]) + (self.array[2][2]*other.array[2][0]) + (self.array[2][3]*other.array[3][0]), (self.array[2][0]*other.array[0][1]) + (self.array[2][1]*other.array[1][1]) + (self.array[2][2]*other.array[2][1]) + (self.array[2][3]*other.array[3][1]), (self.array[2][0]*other.array[0][2]) + (self.array[2][1]*other.array[1][2]) + (self.array[2][2]*other.array[2][2]) + (self.array[2][3]*other.array[3][2]), (self.array[2][0]*other.array[0][3]) + (self.array[2][1]*other.array[1][3]) + (self.array[2][2]*other.array[2][3]) + (self.array[2][3]*other.array[3][3]),
                       (self.array[3][0]*other.array[0][0]) + (self.array[3][1]*other.array[1][0]) + (self.array[3][2]*other.array[2][0]) + (self.array[3][3]*other.array[3][0]), (self.array[3][0]*other.array[0][1]) + (self.array[3][1]*other.array[1][1]) + (self.array[3][2]*other.array[2][1]) + (self.array[3][3]*other.array[3][1]), (self.array[3][0]*other.array[0][2]) + (self.array[3][1]*other.array[1][2]) + (self.array[3][2]*other.array[2][2]) + (self.array[3][3]*other.array[3][2]), (self.array[3][0]*other.array[0][3]) + (self.array[3][1]*other.array[1][3]) + (self.array[3][2]*other.array[2][3]) + (self.array[3][3]*other.array[3][3]))

        if type(other) == vec4:
                 return vec4(self.array[0][0] * other.x + self.array[0][1] * other.y + self.array[0][2] * other.z + self.array[0][3] * other.w,
                             self.array[1][0] * other.x + self.array[1][1] * other.y + self.array[1][2] * other.z + self.array[1][3] * other.w,
                             self.array[2][0] * other.x + self.array[2][1] * other.y + self.array[2][2] * other.z + self.array[2][3] * other.w,
                             self.array[3][0] * other.x + self.array[3][1] * other.y + self.array[3][2] * other.z + self.array[3][3] * other.w)

     def __str__(self):
        return f"{self.array[0]}\n{self.array[1]}\n{self.array[2]}\n{self.array[3]}"