from node import Node

class OrderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count +=1
      current = current.getNext()
    return count
      

  def add(self,item):
    current = self.head
    previous = None
    stop = False

    while current != None and not stop:
      if current.getData() > item:
        stop = True
      else:
        previous = current
        current = current.getNext()

    temp = Node(item)
    if previous == None:
      temp.setNext(self.head)
      self.head = temp
    else:
      temp.setNext(current)
      previous.setNext(temp)

  def search(self,item):
    current = self.head
    found = False
    stop = False

    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()

    return found

  def remove(self,item):
    current = self.head
    found = False
    previous = None

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
      
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print mylist.__dict__['head'].__dict__
print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))