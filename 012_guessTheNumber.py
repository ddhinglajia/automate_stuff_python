# This is a guess the number game

import random
secretNumber = random.randint(1,20)
print ('I a thinking of a number between 1 to 20')

#ask the player to guess six times
for guessTaken in range (1,7):
    print('Take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('Yout guess is low')
    elif guess > secretNumber:
        print ('Your guess is high')
    else:
        break # this is th condition where th guess us right

if guess == secretNumber:
    print('Good job you guessed my number in ' + str(guessTaken) + ' guesses')
else:
    print('Nope the number i was thinking was ' + str(secretNumber))
