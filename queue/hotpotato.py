from queue import Queue

def hotPotato(namelist,num):
  simqueue = Queue()
  for name in namelist:
    simqueue.enqueue(name)

  while simqueue.size() >1:
    for i in range(num):
      frontchild = simqueue.dequeue()
      simqueue.enqueue(frontchild)

    simqueue.dequeue()
  return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))  