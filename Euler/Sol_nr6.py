squRes = 0
sumOfSquares = 0

def squareOfTheSum(nr): # define a method to calculate the square of the sum
  global squRes    # squRes have to be global for use in this method.
  for i in range(1, nr+1):
    squRes = squRes + i # add all numbers to squRes
  return (squRes * squRes) # square the added numbers

def sumOfTheSquares(num):	#define a method to calculate the sum of the square
   global sumOfSquares    # like squRes
   for x in range(1, num+1):
    sumOfSquares = sumOfSquares + (x * x) # first square the number and then add it to sumOfSquares
   return sumOfSquares

squareOfSum = squareOfTheSum(100)
sumOfSqua = sumOfTheSquares(100)



print(squareOfSum - sumOfSqua)
