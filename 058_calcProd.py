#!/usr/bin/env python3

import time

def calcProd():
    # calculate the product of 100,00 numbers
    product = 1
    for i in range(1,10000):
        product= product * i
    return product

startTime = time.time()

prod = calcProd()

endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime-startTime))


# time taken without calling the fucntion

startTime = time.time()

product = 1
for i in range(1,10000):
    product= product * i

endTime = time.time()

print('The result is %s digits long.' % (len(str(product))))
print('Took %s seconds to calculate.' % (endTime-startTime))
