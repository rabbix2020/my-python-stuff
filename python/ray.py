from math import sin, cos, tan, atan, radians, degrees, pi
from time import time
import turtle

sam = turtle.Turtle()
sam.hideturtle()
turtle.tracer(0)

SCREENWIDTH = turtle.window_width()
SCREENHEIGHT = turtle.window_height()

def rgb_to_hex(r, g, b):
   return "#{:02x}{:02x}{:02x}".format(r,g,b)

class vec2:
     def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

     def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

     def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

     def __mul__(self, other):
        return vec2(self.x * other, self.y * other)

     def length(self):
        return ((self.x)**2+(self.y)**2)**0.5

class camera:
     def __init__(self, pos : vec2, angle : float, fov : float, depth : int):
        self.pos = pos
        self.angle = angle
        self.fov = fov
        self.depth = depth

def draw_line(start: vec2, end: vec2):
   sam.penup()
   sam.goto(start.x, start.y)
   sam.pendown()
   sam.goto(end.x, end.y)

cam = camera(vec2(6.5, 3.5), 0, 90, 15)

map = ["##############",
       "#............#",
       "#....#...#...#",
       "#............#",
       "#........#...#",
       "##############"]

def map_collision(pos: vec2):
   try:
      return map[int(pos.y)][int(pos.x)] == '#'
   except:	return False

def raycast(pos: vec2, angle: float):
   horizontal_ray = pos
   vertical_ray = pos
   angle %= 360
   angle = radians(angle)
   tan_angle = tan(angle)

   in_cell_pos = vec2(pos.x % 1, pos.y % 1)

   # VERTICAL START POSISITON
   if angle == 0:
     vertical_ray += vec2(1-in_cell_pos.x, 0)
   elif angle < pi/2 or angle > 1.5 * pi:
     vertical_ray += vec2(1-in_cell_pos.x, (1-in_cell_pos.x) * tan_angle)
   else:
     vertical_ray -= vec2(in_cell_pos.x+1e-6, (in_cell_pos.x+1e-6) * tan_angle)

   # HORIZONTAL START POSISITON
   if angle == 0 or angle == pi:
     pass
   elif angle < pi:
       horizontal_ray += vec2((1-in_cell_pos.y) / tan_angle, 1-in_cell_pos.y)
   else:
       horizontal_ray -= vec2((in_cell_pos.y+1e-6) / tan_angle, (in_cell_pos.y+1e-6))

   for depth in range(cam.depth):
      if map_collision(vertical_ray):
        break

      # VERTICAL RAY
      if angle == 0:
        vertical_ray += vec2(1, 0)
      elif angle < pi/2 or angle > 1.5 * pi:
        vertical_ray += vec2(1, tan_angle)
      else:
        vertical_ray -= vec2(1, tan_angle)

   for depth in range(cam.depth):
      # HORIZONTAL RAY
      if map_collision(horizontal_ray):
        break

      if angle == 0 or angle == pi:
        pass
      elif angle < pi:
        horizontal_ray += vec2(1 / tan_angle, 1)
      else:	horizontal_ray -= vec2(1 / tan_angle, 1)

   if angle == 0 or angle == pi:
     return vertical_ray
   elif angle == 1.5 * pi or angle == pi/2:
     return horizontal_ray
   else:
     vertical_length = (vertical_ray-pos).length()
     horizontal_length = (horizontal_ray-pos).length()

     return horizontal_ray if horizontal_length < vertical_length else vertical_ray

focal_length = (SCREENWIDTH/2) / tan(radians(cam.fov/2))

while True:
     sam.clear()
     for x in range(0, SCREENWIDTH):
        screen_angle = degrees(atan( (x-SCREENWIDTH/2) / focal_length ))

        ray_angle = cam.angle + screen_angle
        hit = raycast(cam.pos, ray_angle)

        distance = (hit-cam.pos).length()
        projected_distance = distance * cos(radians(screen_angle))
        sam.color( rgb_to_hex(int(hit.x % 1 * 255), int(hit.y % 1 * 255), 255))
        draw_line(vec2(x-SCREENWIDTH/2, -(SCREENHEIGHT/projected_distance)/2), vec2(x-SCREENWIDTH/2,(SCREENHEIGHT/projected_distance)/2))

     turtle.update()