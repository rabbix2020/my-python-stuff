import sys

file = open("trees_recursion.txt", "w")

rules = {"1": "11", "0": "1[0]0", "[" : "[", "]" : "]"}
count = int(sys.argv[1])
recursion = ""
axiom = "0"
stack = []

recursion = ""

def make_iterations(rule, iteration):
   global recursion
   if iteration == count:
    print(rules[rule], end="")
    ##file.write(rules[rule])
    return rule

   for letter in rules[rule]:
      make_iterations(letter, iteration+1)

make_iterations(axiom, 0)