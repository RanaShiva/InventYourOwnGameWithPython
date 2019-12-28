# This is a Guess the Number game.
import random
import time
import sys

guessesTaken = 0

print('CAN YOU GUESS THE NUMBER?\n')
print('Welcome! What is your name?')
myName = input()

print('\nWell, ' + myName + '\n')
print('Okay tell me the range between which you would like to guess:')
print('You want to guess the number in the range starting from:')
while True:
    try:
        start = int(input())
        break
    except:
        print('Only numbers allowed')
print('And ending to:')

while True:
    try:
        end = int(input())
        break
    except:
        print('Only numbers allowed')
        
if start >= end:
    print('ERROR IN THE RANGE')
    sys.exit()

if(end - start < 20):
    print('Difficulty Level: EASY')
elif(end - start < 50):
    print('Difficulty Level: NORMAL')
elif(end - start < 100):
    print('Difficulty Level: HARD')
else:
    print('WOAH that is EXTREME LEVEL')


print('Well, ' + myName + ', I am thinking of a number between ' + str(start) + ' and ' + str(end) + '.')
print('You have 6 guesses')

number = random.randint(start,end)

while guessesTaken <= 6 :
    print('Take YOUR guess : ' + str(1 + guessesTaken))
    
    while True:
        try:
            guess = int(input())
            break
        except:
            print('Only numbers allowed')
        
    guessesTaken = guessesTaken + 1

    if guess < start or guess > end:
        print('Guess should be between ' + str(start) + ' and ' + str(end) + '.')
        guessesTaken = guessesTaken - 1
        continue
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' +guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')

time.sleep(4)
        
