from collections import deque
'''
books = []

books.append('C')
books.append('C++')
books.append('Python')


print(books)

books.pop()
print('Now the top book is',books[-1])

books.pop()

print('Now the top book is',books[-1])

books.pop()
if not books:
    print('No books left')
'''
bank = deque(['Kawsar', 'Hasan', 'Alhaz'])

print(bank)

bank.popleft()

print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print('No Person Left')





