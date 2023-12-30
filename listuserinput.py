'''
n = input('Enter a text number : ')
list = n.split()

sum = 0
for num in list:
    sum = sum + int(num)
print(sum)
'''

text = input('Enter  a sentence : ')
numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0

for x in text:
    x.lower()
    if x >= 'a' and x <= 'z':
        numberOfLetters = numberOfLetters + 1
    elif x >= '0' and x <= '9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 1

print('Number of letters : ', numberOfLetters)
print('Number of  digits : ', numberOfDigits)
print('Number of words : ', numberOfWords+1)






