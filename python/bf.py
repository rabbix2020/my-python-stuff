from msvcrt import getch
from sys import argv

if len(argv) < 2:
  code = input(">>> ")
else:
  code = open(argv[1], "r").read()

array = [0] * 30000
pointer = 0

blocks = {}
for index, letter in enumerate(code):
   if letter == '[':
     stack = []
     for index2, letter2 in enumerate(code[index:]):
        if letter2 == '[':	stack.append('[')
        if letter2 == ']':	stack.pop()
        if stack == []:	break
     blocks[index] = index+index2
     blocks[index+index2] = index

i_pointer = 0
while i_pointer <= len(code)-1:
     instruction = code[i_pointer]

     match instruction:
          case '>':
              pointer+=1
          case '<':
              pointer-=1
          case '+':
              array[pointer]+=1
          case '-':
              array[pointer]-=1
          case '.':
              print(chr(array[pointer]), end='')
          case ',':
              array[pointer] = ord(getch())
          case '[':
              if array[pointer] == 0:	i_pointer = blocks[i_pointer]
          case ']':
              if array[pointer] != 0:	i_pointer = blocks[i_pointer]
     i_pointer += 1