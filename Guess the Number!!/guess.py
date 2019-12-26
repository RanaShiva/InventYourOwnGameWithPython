# This is a Guess the Number game.
import random

guessesTaken = 6

print('I should guess the number starting from:')
start = int(input())
print('And ending to:')
end = int(input())
if start > end:
    print('ERROR IN THE RANGE')
    exit(-1)

if(end - start <= 20):
    print('Difficulty Level: EASY')
elif(end - start <= 50):
    print('Difficulty Level: NORMAL')
elif(end - start <= 100):
    print('Difficulty Level: HARD')
else:
    print('WOAH that is EXTREME LEVEL')

print('Hello! What is your name?')
myName = input()


print('Well, ' + myName + ', I am thinking of a number between ' + str(start) + ' and ' + str(end) + '.')
print('You have 6 guesses')

number = random.randint(start,end)

while guessesTaken :
    print('Take YOUR guess : ' + str(7 - guessesTaken))
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken - 1

    if guess < start or guess > end:
        print('Guess should be between ' + str(start) + ' and ' + str(end) + '.')
        guessesTaken = guessesTaken + 1
        continue
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' +guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
        
