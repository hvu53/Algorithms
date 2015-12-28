class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self,newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext


# temp = Node(93)
# temp.setNext(54)
# print temp.getData()
# print temp.getNext()