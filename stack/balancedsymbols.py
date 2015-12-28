from stack import Stack

def parChecker(parStr):
  stack = Stack()
  for par in parStr:
    if par in '([{':
      stack.push(par)
    elif par in (')]}'):
      if matches(stack.peek(),par):
        stack.pop()

  if stack.isEmpty():
    return True
  else:
    return False

def matches(open,close):
  opens = "([{"
  closes = ")]}"
  return opens.index(open) == closes.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))