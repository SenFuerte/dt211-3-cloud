n = 1000 #initial the 1000 numbers
result = 0
for x in range(1,n): #cross all numbers of n
 if (x % 3 == 0) or (x % 5 == 0): #if the number is a multiple of 3 or 5
   result = result + x			  #then it add all numbers to result

print(result) # print the sum of all the multiples of 3 and 5 below 1000
