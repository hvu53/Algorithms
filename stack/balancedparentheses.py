from stack import Stack
def parChecker(parstr):
  stack = Stack()
  for par in parstr:
    if par == '(':
      stack.push('(')
    elif par == ')':
      stack.pop()

  return stack.isEmpty()

print parChecker('((()))')
print(parChecker('(()'))
print(parChecker('()'))
