from deque import Deque

def palchecker(aStr):
  chardeque = Deque()

  for char in aStr:
    chardeque.addFront(char)

  stillEqual = True
  while chardeque.size() > 1 and stillEqual:
    first = chardeque.removeFront()
    last = chardeque.removeRear()
    if first != last:
      stillEqual = False

  print chardeque.size()
  return stillEqual


#print(palchecker("lsdkjfskf"))
print(palchecker("radar"))