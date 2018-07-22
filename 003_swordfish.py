# program to demonstrate use continue in a loop

while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe What is the password (it is a fish.)' )
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')
