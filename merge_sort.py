def split(a):
    '''
    This function splits the input into two lists
    - Inputs:
        a: the list to be splitted.
    '''
    n = len(a)
    if n <= 1:
        return({}, a)
    return(a[:int(n/2)], a[int(n/2):])

def merge(b, c):
    '''
    This function merges two sorted lists
    The result is a sorted list.
    '''
    b_counter = 0
    c_counter = 0
    d = list()
    total_length = len(b) + len(c)
    for k in range(total_length):
        # If all b's elements have already been added
        # We just have to add c's left elements
        if b_counter == len(b):
            d.extend(c[c_counter:])
            return(d)
        # If all c's elements have already been added
        # We just have to add b's left elements
        elif c_counter == len(c):
            d.extend(b[b_counter:])
            return(d)
        # Naive comparison
        elif b[b_counter] <= c[c_counter]:
            d.append(b[b_counter])
            b_counter += 1
        elif c[c_counter] <= b[b_counter]:
            d.append(c[c_counter])
            c_counter += 1
    return(d)
    
def merge_sort(a):
    '''
    This function takes a list as an input
    and returns a sorted list. This is done
    following these steps:
        - split the input array => b and c
        - Recursively sort b and c
        - Merge the result
    '''
    # Base case
    if len(a) == 1:
        return(a)
        
    # First, we split a
    b, c = split(a)
    # We recursively sort b and c
    # and then we merge the result
    return(merge(merge_sort(b), merge_sort(c)))
    
merge_sort([4,1,5,6,3,2])
