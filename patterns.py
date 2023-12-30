# n = 9
# for i in range(n+1):
#
#     print((2*i-1)*'*')
'''
n = int(input("Enter a row Number: "))
for x in range(n+1):
    for y in range(n-x):
        print(" ",end="")
    for z in range(x):
        print("*",end="")
    print()

'''

n = 4
for x in range(n+1):
    for y in range(n-x):
        print(' ', end="")
    for z in range(x):
        print('*', end='')
    print()







