import random
from queue import Queue
class Printer:
  def __init__(self,ppm):
    self.pagerate = ppm
    self.currentTask = None
    self.timeRemaining = 0

  def tick(self):
    if self.currentTask != None:
      self.timeRemaining -= 1
      if self.timeRemaining <= 0:
        self.currentTask = None

  def isbusy(self):
    if self.currentTask != None:
      return True
    else:
      return False

  def startNext(self, newtask):
    self.currentTask = newtask
    self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
  def __init__(self,time):
    self.timestamp = time
    self.pages = random.randrange(1,21)

  def getStamp(self):
    return self.timestamp

  def getPages(self):
    return self.pages

  def waittime(self, currenttime):
    return currenttime - self.timestamp

def simulation(numSeconds, ppm):
  labprinter = Printer(ppm)
  printQueue = Queue()
  waitingtimes = []

  for currentSecond in range(numSeconds):
    if newPrintTask():
      task = Task(currentSecond)
      printQueue.enqueue(task)

    if (not labprinter.isbusy()) and (not printQueue.isEmpty()):
      nexttask = printQueue.dequeue()
      waitingtimes.append(nexttask.waittime(currentSecond))
      labprinter.startNext(nexttask)

    labprinter.tick()

  averageWait = sum(waitingtimes)/len(waitingtimes)
  print("Average Wait %6.2f secs %3d taks remaining"%(averageWait,printQueue.size()))

def newPrintTask():
  num = random.randrange(1,181)
  if num == 180:
    return True
  else:
    return False

for i in range(10):
  simulation(3600,15)