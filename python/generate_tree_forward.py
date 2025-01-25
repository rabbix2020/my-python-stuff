import sys

file = open("trees_forward.txt", "w")

rules = {"1": "11", "0": "1[0]0", "[" : "[", "]" : "]"}
recursion = ""
axiom = "0"
stack = []

recursion += axiom

count = int(sys.argv[1])
for iterations in range(count):
   new_recursion = ""
   for letter in recursion:
      new_recursion+=rules[letter]
   recursion = new_recursion
print(recursion)
file.write(recursion)