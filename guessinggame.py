import  random

# usernumber = int(input('Enter the number betwen 1 to 5 : '))
#
# rnnumber = random.randint(1,5)

#for largest number
#random.random() * 100

for x in range(1,6):
    guessNumber = int(input('Enter the number betwen 1 to 5 : '))

    randomNumber = random.randint(1, 5)
    if guessNumber == randomNumber:
        print('You Won')
    else:
        print('You Lose')
        print('Random number was ', randomNumber)