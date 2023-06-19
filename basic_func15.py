def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    return (a/b-int(a/b))*b
a=23
b=5
print(int(main(a,b)))