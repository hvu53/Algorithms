class Deque:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self,item):
    self.items.append(item)

  def removeFront(self):
    return self.items.pop()

  def addRear(self,item):
    self.items.insert(0,item)

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

# d = Deque()
# print d.isEmpty()
# print d.addRear(4)
# print d.addRear('dog')
# print d.addFront('cat')
# print d.addFront(True)
# print d.__dict__
# print d.size()
# print d.isEmpty()
# d.removeRear()
# d.removeFront()
# print d.__dict__