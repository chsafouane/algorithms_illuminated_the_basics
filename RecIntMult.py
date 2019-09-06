def RecIntMult(x, y):
    '''
    This implementation supposes that x and y have the
    same length and that it is pair.
    The inputs x and y should also be positive integers.
    One can pad the numbers
    '''
    n = len(str(x))
    # The base case
    if n == 1:
        return(int(x * y))
    
    # The recursive implementation
    a, b = int(x / 10**(n/2)), int(x % 10**(n/2))
    c, d = int(y / 10**(n/2)), int(y % 10**(n/2))
    ac = RecIntMult(a, c)
    bd = RecIntMult(b, d)
    ad = RecIntMult(a ,d)
    bc = RecIntMult(b, c)
    return(int(ac * 10**n + (ad + bc) * 10**(n/2) + bd))
    
print(RecIntMult(5, 9))
print(RecIntMult(50, 90))