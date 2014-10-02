max = 600851475143
i = 2

while i * i < max: 
 while max % i == 0:
   max = max/ i 
  
 i = i + 1

print (max)
