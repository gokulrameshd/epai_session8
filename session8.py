from math import *



def check_doc_string(fn):
    '''
    This function takes in funtion and checks for the doc string
    if no. of character doc string is greater than 50 it returns True,
    else it returns False.
    '''
    def check(fn):
        length_docstring = len(fn.__doc__)
        if length_docstring > 50:
#             print(True)
            return (True)
        else :
#             print(False)
            return (False)
    ret = check(fn)
    return ret 


def get_next_fib():
    """
    This function returns the next 
    fibonacci number
     """
    f = 1
    count = 0
    def add():
        nonlocal f
        nonlocal count
        f = round(f*(1 + sqrt(5))/2.0)
#         total = total + number
        count = count + 1
        return f
    return add

def add(a, b):
    """
    This function returns addition 
    of two numbers.
    """
    return a + b
def mul(a, b):
    """
    This function returns multiplication 
    of two numbers.
    """
    return a*b
def div(a,b):
    """
    This function returns division
    of two numbers.
    """
    return a/b

counters = {}
def counter_1(fn):
    """
    This function performs a counter function.
    This function takes in function and arguments
    and updates the global counter whenever the function 
    is executed.
    """
    cnt = {}
    cnt[str(fn.__name__)] = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt[str(fn.__name__)] += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt[str(fn.__name__)]))
        print(cnt)
#         c = cnt
        global counters
        counters[str(fn.__name__)] = cnt[str(fn.__name__)]
        return fn(*args, **kwargs) 
    return inner

def counter_2(fn,counters):
    """
    This function performs a counter function.
    This function takes in function and arguments(counter dictionary)
    and updates the global counter whenever the function 
    is executed.
    This global counter is separate dictionary , which is passed along with the function.
    """
    cnt = counters 
    def inner(*args, **kwargs):
        try:
            cnt[str(fn.__name__)] += 1
        except:
            cnt[str(fn.__name__)] = 1
            
        print('{0} has been called {1} times'.format(fn.__name__, cnt[str(fn.__name__)]))
        print(cnt)
#         c = cnt
        global counters
        counters[str(fn.__name__)] = cnt[str(fn.__name__)]
        return fn(*args, **kwargs)
     
    return inner