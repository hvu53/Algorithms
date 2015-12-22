__author__ = "Hoa Vu"
import time
from random import randrange

# def findMin(alist):
#   min = alist[0]
#   for i in alist:
#     issmallest = True
#     for j in alist:
#       if i > j:
#         issmallest = False
#     if issmallest == True:
#       min = i

#   return min

def findMin(alist):
  min = alist[0]
  for i in alist:
    if i < min:
      min = i
  return min

print findMin([5,5,0.5,6,4,2,0])
print findMin([-15,-5,6,4,2,0])

for listSize in range(1000,10001,1000):
  alist = [randrange(100000) for x in range(listSize)]
  start = time.time()
  print findMin(alist)
  end = time.time()
  print("size: %d time: %f" % (listSize, end - start))