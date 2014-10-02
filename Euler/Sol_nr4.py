def isPalindrome(num):
    return str(num) == str(num)[::-1] # check if its a Palindrom

def largest(start, end):
    z = 0
    for x in range(end, start, -1):
        for y in range(end,start, -1):
            if isPalindrome(x*y): # if its true 
                if x*y > z:       # and x*y is bigger then z 
                    z = x*y	  # update z
    return z
print largest(100,999)
