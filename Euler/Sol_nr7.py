def isprime(n):
   n = abs(int(n))
   if n < 2:
     return False
   if n == 2:
     return True
   if not n & 1:
     return False
   for x in range(3, int(n ** 0.5) + 1, 2):
     if n % x == 0:
        return False
     return True


def main():
    Switch = 1
    number = 1
    primes = 1
    while Switch == 1:
       if isprime(number):
          primes += 1
       if primes == 10001:
         print number
         Switch = 0
       number += 2


main()
