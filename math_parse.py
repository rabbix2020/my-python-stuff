expression_solver = {
 "+": lambda x, y: x + y,
 "-": lambda x, y: x - y,
 "*": lambda x, y: x * y,
 "/": lambda x, y: x / y,
 "^": lambda x, y: x ** y
}

class math_node:
     __slots__ = ["operand", "left", "right"]
     def __init__(self):
        self.operand = None
        self.right = None
        self.left = None

     def __str__(self):
        return f"{self.left} {self.operand} {self.right}"

     def __repr__(self):
        return f"MNODE:{self.left} {self.operand} {self.right}"

def get_tokens(expression : str) -> list:
   tokens = []

   i = 0
   j = 0
   while i < len(expression):
        while expression[i] == " ":
             i += 1

        if expression[i] != "(":
          j = i
          while j < len(expression) and (expression[j] != " "):	j += 1
          tokens.append(expression[i:j])
          i = j + 1
        elif expression[i] == "(":
          j = i
          budget = 0
          while True:
               if expression[j] == "(":	budget += 1
               if expression[j] == ")":	budget -= 1
               j += 1
               if budget == 0:	break
          tokens.append(expression[i:j])
          i = j + 1

   return tokens

def build_expression_tree(tokens : list) -> math_node:
   math_root = math_node()

   if len(tokens) == 1:
     token = tokens[0]
     if token[0] == "(":
       sub_tokens = get_tokens(token[1:-1])
       return build_expression_tree(sub_tokens)
     else:	return float(token)

   for index, token in enumerate(tokens):
      if token == "^":
        math_root.operand = token
        math_root.left = build_expression_tree(tokens[:index])
        math_root.right = build_expression_tree(tokens[index+1:])


   for index, token in enumerate(tokens):
      if token == "*" or token == "/":
        math_root.operand = token
        math_root.left = build_expression_tree(tokens[:index])
        math_root.right = build_expression_tree(tokens[index+1:])

   for index, token in enumerate(tokens):
      if token == "+" or token == "-":
        math_root.operand = token
        math_root.left = build_expression_tree(tokens[:index])
        math_root.right = build_expression_tree(tokens[index+1:])

   return math_root

def solve_expression_tree(root_node : math_node) -> float:
   if type(root_node.left) == math_node and type(root_node.right) == math_node:
     return expression_solver[root_node.operand](solve_expression_tree(root_node.left), solve_expression_tree(root_node.right))

   if type(root_node.left) == float and type(root_node.right) == math_node:
     return expression_solver[root_node.operand](root_node.left, solve_expression_tree(root_node.right))

   if type(root_node.left) == math_node and type(root_node.right) == float:
     return expression_solver[root_node.operand](solve_expression_tree(root_node.left), root_node.right)

   if type(root_node.left) == float and type(root_node.right) == float:
     return expression_solver[root_node.operand](root_node.left, root_node.right)

math_expression = input()

tokens = get_tokens(math_expression)
tree = build_expression_tree(tokens)

result = solve_expression_tree(tree)
print(result)