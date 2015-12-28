from stack import Stack
import string

def infixToPostfix(expr):
  prec = {"(": 1, "+": 2, "-": 2, "*":3, "/": 3, "^": 4}
  opStack = Stack()
  tokensList = expr.split()
  result = ""

  for token in tokensList:
    if (token in string.ascii_uppercase) or token.isdigit():
      result += token
    elif token == "(":
      opStack.push(token)
    elif token == ")":
      toptoken = opStack.pop()
      while toptoken != "(":
        result += toptoken
        toptoken = opStack.pop()
    else:
      while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
        result += opStack.pop()
      opStack.push(token)

  while not opStack.isEmpty():
    result += opStack.pop()

  return result    

def postfixEval(expr):
  operandStack = Stack()
  tokensList = expr.split()

  for token in tokensList:
    if token.isdigit():
      operandStack.push(int(token))
  
    else:
      op2 = operandStack.pop()
      op1 = operandStack.pop()
      result = domath(token,op1, op2)
      operandStack.push(result)

  if not operandStack.isEmpty():
    return operandStack.pop()

      
def domath(op, a,b):
  if op == "*":
    return a * b
  elif op == "/":
    return float(a) / float(b)
  elif op == "+":
    return a + b
  else:
    return a - b

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print infixToPostfix("( A + B ) * ( C + D )")
print infixToPostfix("( A + B ) * C")
print infixToPostfix("5 * 3 ^ ( 4 - 2 )")

print(postfixEval('7 8 + 3 2 + /'))
print infixToPostfix('10 + 3 * 5 / ( 16 - 4 )')
print postfixEval('17 10 + 3 * 9 /')