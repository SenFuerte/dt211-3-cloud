def fibbo(x):  #define a method 
 if (x == 0): # catch number 0
  return 0
 elif x == 1: # catch number 1
  return 1
 else:
  return (fibbo(x-1) + fibbo(x-2)) # use the method recursive sothat it calls himself

for z in range(1,1000): #for loop to find the number which is greater then 4kk
 if fibbo(z) >= 4000000:
   print(z-1)  # print the number
   break	# number is found break the for loop
