from math import sin
from turtle import *
from time import *

title("tree")
bgcolor(0, 0, 0)

color("white")
hideturtle()
tracer(0)
penup()
setposition(0, -390)
setheading(90)
pendown()

rules = {"1": "11", "0": "1[0]0", "[" : "[", "]" : "]"}
recursion = ""
axiom = "0"
SPREAD = 45
stack = []

recursion += axiom

for iterations in range(8):
   new_recursion = ""
   for letter in recursion:
      new_recursion+=rules[letter]
   recursion = new_recursion

def draw():
   setposition(0, -390)
   setheading(90)
   clear()
   SPREAD = sin(time()) * 90

   for letter in recursion:
      match letter:
           case "0":
               forward(3)
           case "1":
               forward(3)
           case "[":
               stack.append(heading())
               stack.append(pos())
               left(SPREAD)
           case "]":
               penup()
               setposition(stack.pop())
               setheading(stack.pop())
               right(SPREAD)
               pendown()

while True:
   draw()
   update()