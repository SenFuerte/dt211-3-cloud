maximum = 1415 #it s defined as the upperroot of 2000000, it doesnt work with 1414.
eratostenes = [True for i in range(1,10000001)] # the real size is 10 000 000 just in acse and to avoid segmentation faults (tricky)
eratostenes[0] = eratostenes[1] = False # following the eratostenes sieve


for i in range(2,maximum): # we only need to check the root of our number, mathematic proprieties
   if eratostenes[i]:
      for j in xrange(2*i,(maximum*maximum)+1,i): #it s time to remove the numbers that have any multiple among the range
          eratostenes[j] = False
#once we ve done the sieve we can sum all the prime numbers bellow 2million, stored in suma_prime

suma_prime = 0

for i in range(1,2000000):
   if eratostenes[i]:
      suma_prime+=i

print suma_prime 
