'''
function resturns nuber is prime or not
'''
def test_prime(arg):
    if arg == 1:
        return True
    elif arg == 2:
        return True
    else:
        for i in range(2, arg):
            if arg % i == 0:
                return False
        return True
    