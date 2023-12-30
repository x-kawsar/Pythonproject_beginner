
file = open('students.txt', 'r')


for line in file:
    print(line)

file.close()




file = open('hello.html', 'w')


text = '<h1>Hello World</h1>'

result = file.write(text)
file.close()










