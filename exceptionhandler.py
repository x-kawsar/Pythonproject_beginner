'''try:
    list = [20,0,30]

    result = list[0] / list[3]

    print(result)
    print('Done')
except ZeroDivisionError:
    print('Deviding by zero is not possible')

finally:

    print('Successfull')

'''

'''try:
    num1 = int(input('Enter first number : '))
    num2 = int(input('Enter second number : '))

    result = num1 / num2

    print(result)

except (ValueError, ZeroDivisionError):
    print('You have entered wrong input')

finally:
    print('Thanks')'''


def voter(age):
    if age < 18:
        raise ValueError('Invalid Voter')
    return 'You are allowed to vote'


try:
    print(voter(17))
except ValueError as err:
    print(err)



















