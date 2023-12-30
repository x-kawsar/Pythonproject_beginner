
'''def student(*details):
    print(details)

student(10, 'Kawsar', 3.58)'''

'''

# x args
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)

'''

# xxargs

def student(**details):
    print(details['name'])

student(id=101, name='kawsar', age=23)
student(id=99, name='Hasan', age=20)






