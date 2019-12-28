# A game of our hero wandering in the dragon realm

import random
import time

coins = 0
totalCoins = 0

def displayIntro():
    print('''You are in land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()



print('What is your name my LORD:')
name = input()
print('Welcome my LORD, ' + name+ '.')
print('Allow me introduce you to this world.\n')



def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' :
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    global coins
    global totalCoins
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
        coins = random.randint(1,1000)
        print('You got', coins, 'coins.')
    else:
        print('Gobbles you down in one bite!')
        print('You were able to collect', totalCoins, 'coins.')
        print('________________________________________________')
        coins = 0
        
    return coins


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    money = checkCave(caveNumber)
    if(money):
        totalCoins = totalCoins + money
    else:
        totalCoins = 0
    print('\nDo you want to play again? (yes or no)')
    playAgain = input()
    print('..........................................')
if(totalCoins):   
    print('You collected:', totalCoins, "coins.")

print('Thanks for playing!!')
print('We will miss you MY LORD!!!')
