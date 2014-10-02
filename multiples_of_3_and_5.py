from array import *
n = 1000
nums = array('i')
for x in range(1,n):
 if (x % 3 == 0) or (x % 5 == 0):
   print(x)
