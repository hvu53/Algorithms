#convert from decimal to binary
from stack import Stack

def dectobi(dec):
  remstack = Stack()

  while dec > 0:
    rem = dec % 2
    remstack.push(rem)
    dec = dec // 2

  r = ""
  while not remstack.isEmpty():
    r += str(remstack.pop())
  return r

# take a decimal and any base between 2 and 16 & convert 
def baseConverter(dec,base):
  digits = "0123456789ABCDEF"

  remstack = Stack()

  while dec > 0:
    rem = dec % base
    remstack.push(rem)
    dec = dec // base

  r = ""
  while not remstack.isEmpty():
    r += str(remstack.pop())

  return r

print dectobi(42)
print(baseConverter(26,26))
print(baseConverter(256,16))