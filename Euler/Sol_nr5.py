def divisible(n):
 counter = 0
 for i in range(1, 21):
  if n % i == 0:
    counter += 1
    if counter == 20:
      return n 
  else:
    return 1

def main():
   n = 2520
   switch = 1
   while switch == 1:
      smallest = divisible(n)
      if smallest != 1:
         print smallest
         switch = 0
      else:
         n += 2520

if __name__ == '__main__':
   main()
