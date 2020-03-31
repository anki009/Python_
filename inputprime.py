import sys
import isprime

try:
    n = int(sys.argv[1])
except:
    print("please enter valid input")
    
res = isprime.test_prime(n)
if res:
    print(n,"is prime number")
else:
    print(n,"is not prime number")