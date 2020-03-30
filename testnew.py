'''
checks testcases are true or failed
'''
import unittest
import isprime

class TestPrime(unittest.TestCase):
    def test_one(self):
        num1 = input("enter number to check if it is prime or not: ")
        result = isprime.test_prime(num1)
        if result:
            print"Number is prime"
            self.assertEqual(result, True)
        else:
            print"Number is not prime"
            self.assertEqual(result, False)       
if __name__ == "__main__":
    unittest.main()
    