from node import Node

class UnorderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count +=1
      current = current.getNext()
    return count

  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found

  def append(self,item):
    current = self.head
    found = False
    while current.getNext() != None:
      current = current.getNext()
    current.setNext(item)

  def remove(self,item):
    current = self.head
    previous = None
    found = False
    
    if self.search(item) == False:
      return 'There is no such item'

    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
   
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

mylist = UnorderedList()
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
print mylist.remove(31)
print(mylist.size())
print(mylist.search(93))