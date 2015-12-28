# implement a stack using python list
# assume the the end of the list hold the top element of the list
#last in, first out
class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) -1]

  def size(self):
    return len(self.items)

# s=Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print s.peek()
# s.push(False)
# print s.size()
# print s.isEmpty()
# s.push(8.4)
# print s.pop()
# print s.pop()
# print s.size()

def revstring(mystr):
    stack = Stack()
    for i in mystr:
      stack.push(i)
    r = ''
    while not stack.isEmpty():
      r+= stack.pop()
    return r

# print (revstring('apple') == 'elppa')
