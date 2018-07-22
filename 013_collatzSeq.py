import sys

def collatz(number):
    if (number % 2) == 0:
       return number//2
    elif (number % 2) != 0:
        return 3 * number + 1

print('Enter an integer greater than zero to intiate Collatz Sequence')

#num = int(input())

try:
    num = int(input())
    if num == 0:
        print ('You entered zero')
        sys.exit()
        
    while num != 1 :
        num = collatz(num)
        print (num)
    
except ValueError:
    print('Please enter an integer')

    
