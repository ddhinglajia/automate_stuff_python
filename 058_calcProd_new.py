#!/usr/bin/env python3
import dis
import time 

def calcProd():
  	# Read the below note in __main__ first.
    # So to carry forward from what I said, this function has already been optimized for you.
    # this is exactly why you need functions. They help optimize bits of code you reuse constantly.
    # These minute optimizations add a lot of time saving to your code.
    import time
    # calculate the product of 100,00 numbers
    product = 1
    for i in range(1,10000):
        product= product * i
    return product

if __name__ == "__main__":
	
    # One reason why it takes lesser to do this is *because*
    
    # the function and its optimization is done before you called the start_time.
    # Python compiles your code to bytecode and then builds something called an AST, an Abstract Syntax Tree, to 
    # determine how the code is run. Hence it is both an interpreted and compiled language.
    # See below.
    startTime = time.perf_counter()
    prod = calcProd()
    endTime = time.perf_counter()
    print('The result is %s digits long.' % (len(str(prod))))
    print('Took %s seconds to calculate.' % (endTime-startTime))
    
    # time taken without calling the fucntion
    startTime = time.perf_counter()
    product = 1 # This optimization is done after your timer has started.
    for i in range(1,10000):  # This optimization is done after your timer has started.
        product= product * i  # This optimization is done after your timer has started.
    endTime = time.perf_counter()  # This optimization is done after your timer has started.
    print('The result is %s digits long.' % (len(str(product))))
    
    # This is the standard way to time functions in Python. It runs what you give some 10k times and gives you the average.
    # import timeit
    # print(timeit.timeit("calcProd()", setup="from __main__ import calcProd"))
    