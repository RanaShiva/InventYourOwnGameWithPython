# A Program that tells jokes!
import time
import sys

print('What do you get when you cross a snowman with a vampire?')
input()
print('Frostbite!')
print()

print('What do dentists call an astronaut\'s cavity?')
input()
print('A black hole!')
print()

print('Knock Knock.')
input()

print("Who's there?")
input()

print('Interrupting cow.')
input()

print('Interrupting cow wh' , end = '')
print('-MOO!')
print()

print('_______________________________________')
print()

print('Want more jokes?')
print('Calculate 42/2')
while True:
	try:
		number = int(input())
		break
	except:
		print("Only numbers allowed! Try again:")

if(number == 21):
    print('Correct!')
    print('What do you call an acid with an attitude?')
    input()
    print('A mean-o-acid!')
    print()
else:
    print('Do play again!')
    print('BYE!!')
    time.sleep(2)
    sys.exit()


print('Want more jokes?')
print('Calculate 0/21')

while True:
	try:
		number = int(input())
		break
	except:
		print("Only numbers allowed! Try again:")

if(number == 0):
    print('Correct!')
    print('What do you call a bear with no teeth?')
    input()
    print('A gummy bear!')
    print()
else:
    print('Do play again!')
    print('BYE!!')
    time.sleep(2)
    sys.exit()


print('Want more jokes?')
print('Calculate 9*21')

while True:
	try:
		number = int(input())
		break
	except:
		print("Only numbers allowed! Try again:")

if(number == 189):
    print('Correct!')
    print('What do you call a priest who becomes a lawyer?')
    input()
    print('A father-in-law!')
    print()
else:
    print('Do play again!')
    print('BYE!!')
    time.sleep(2)
    sys.exit()
    
    
print('Want more jokes?')
print('Calculate 777-349')

while True:
	try:
		number = int(input())
		break
	except:
		print("Only numbers allowed! Try again:")

if(number == 428):
    print('Correct!')
    print('What do you call a pile of cats?')
    input()
    print('A meow-ntain!')
    print()
else:
    print('Do play again!')
    print('BYE!!')
    time.sleep(2)
    sys.exit()

print('That\'s all I have for now!')
print('BYE CHAMPION!!')
time.sleep(4)
