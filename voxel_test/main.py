from turtle import *
from time import time
from alg_math import *
from camera import camera
from voxel import voxel
from math import *
import matrices

title("Voxel test")
hideturtle()
tracer(0)

canvas = getcanvas()
screen = getscreen()
running = True
delta = 0.0000000000000000000001

to_radians = lambda x: x / (180 / pi)

class WatchKey:
     def __init__(self, key):
        self.key = key
        self.down = False
        screen.onkeyrelease(self.key_release, key)
        screen.onkeypress(self.key_press, key)

     def key_release(self):
        self.down = False

     def key_press(self):
        self.down = True

def th(val):
	result = ('%X' % val)
	if len(result) < 2:	result = '0' + result
	return result

def draw_dot(pos : vec2, size : float, col : vec3):
   penup()
   goto(pos.x * window_width() / 2, pos.y * window_height() / 2)
   pendown()
   color(f"#{th(int(col.x*255))}{th(int(col.y*255))}{th(int(col.z*255))}")
   dot(size * window_width())

main_camera = camera(vec3(0, 1, 0), vec3(0, 0, 0), 90, 0.1, 100.0)
voxel_list = [voxel(vec3(1, 0, 10.0), vec3(0.6, 0.0, 1.0)), voxel(vec3(0, 0, 10.0), vec3(1.0, 0.8, 1.0)), voxel(vec3(-1, 0, 10.0), vec3(0.6, 0.8, 0.0)), voxel(vec3(-1, 0, 11.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 0, 11.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 0, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(0, 0, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 0, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 1, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 1, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 2, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(0, 2, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 2, 12.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 2, 11.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 2, 11.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 2, 10.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(0, 2, 10.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 2, 10.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(-1, 1, 10.0), vec3(0.6, 0.8, 1.0)), voxel(vec3(1, 1, 10.0), vec3(0.6, 0.8, 1.0))]
voxel_size = 1

back = WatchKey("s")
forward = WatchKey("w")
left = WatchKey("a")
right = WatchKey("d")
up = WatchKey("q")
down = WatchKey("e")

turn_left = WatchKey("Left")
turn_right = WatchKey("Right")

turn_up = WatchKey("Up")
turn_down = WatchKey("Down")

def logic():
   main_camera.rot.x = min(max(main_camera.rot.x, -90), 90)
   main_camera.rot.y = main_camera.rot.y % 360
   speed = 5

   if forward.down:	main_camera.pos += vec3(sin(to_radians(main_camera.rot.y)) * delta * speed, -sin(to_radians(main_camera.rot.x)) * delta * speed, cos(to_radians(main_camera.rot.y)) * delta * speed)
   if back.down:	main_camera.pos -= vec3(sin(to_radians(main_camera.rot.y)) * delta * speed, -sin(to_radians(main_camera.rot.x)) * delta * speed, cos(to_radians(main_camera.rot.y)) * delta * speed)
   if left.down:	main_camera.pos -= vec3(cos(to_radians(main_camera.rot.y)) * delta * speed, 0, -sin(to_radians(main_camera.rot.y)) * delta * speed)
   if right.down:	main_camera.pos += vec3(cos(to_radians(main_camera.rot.y)) * delta * speed, 0, -sin(to_radians(main_camera.rot.y)) * delta * speed)
   if up.down:	main_camera.pos += vec3(0, delta * speed, 0)
   if down.down:	main_camera.pos -= vec3(0, delta * speed, 0)

   if turn_left.down:	main_camera.rot.y -= delta * 90
   if turn_right.down:	main_camera.rot.y += delta * 90

   if turn_up.down:	main_camera.rot.x -= delta * 90
   if turn_down.down:	main_camera.rot.x += delta * 90

def draw():

   aspect = window_width()/window_height()
   f = 1 / tan(to_radians(main_camera.fov/2))

   projected_voxels = []
   for vox in voxel_list:
      releative_pos = matrices.rotation(vec3(-main_camera.rot.x, -main_camera.rot.y, -main_camera.rot.z)) * (vox.pos * vec3(voxel_size, voxel_size, voxel_size) - main_camera.pos)
      projected_pos = releative_pos
      z_distance = (releative_pos.z - main_camera.near) / (main_camera.far - main_camera.near)
      if z_distance < 0 or z_distance > 1:	continue
      projected_pos *= vec3(f, aspect * f, 1)
      projected_pos /= projected_pos.z
      projected_size = (f / releative_pos.z / 2) * voxel_size
      if (projected_pos.x < -(1+projected_size) or projected_pos.x > 1+projected_size) or (projected_pos.y < -(1+projected_size) or projected_pos.y > 1+projected_size):	continue
      projected_voxels.append(voxel(vec4(projected_pos.x, projected_pos.y, z_distance, projected_size), vox.col))

   projected_voxels.sort()
   projected_voxels = projected_voxels[::-1]

   for projected_vox in projected_voxels:
      draw_dot(projected_vox.pos.to_vec3().to_vec2(), projected_vox.pos.w, projected_vox.col)

screen.setup(900, 900)

while running:
     time1 = time()
     logic()
     listen()
     clear()
     draw()
     update()
     delta = time() - time1