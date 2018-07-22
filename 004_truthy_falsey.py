# program to demonstrate how to prevent entering null values for input

name=''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests =int(input())
if numOfGuests:
    print('Be sure to have enugh room for all your guests')
print('Done')
