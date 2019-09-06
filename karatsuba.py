def karatsuba(x, y):
    '''
    This implementation supposes that x and y have the
    same length and that it is pair.
    The inputs x and y should also be positive integers.
    One can pad the inputs to force to have the same length
    '''
    n = len(str(x))
    # The base case
    if n == 1:
        return(int(x * y))
    
    # The recursive implementation
    a, b = int(x / 10**(n/2)), int(x % 10**(n/2))
    c, d = int(y / 10**(n/2)), int(y % 10**(n/2))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a+b ,c+d) - ac - bd
    return(int(ac * 10**n + abcd * 10**(n/2) + bd))
    
print(karatsuba(5, 9))
print(karatsuba(50, 90))