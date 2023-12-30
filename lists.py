subjects = ['C', 'C++', 'C#', 'Java', 'Python', 'Basic', 'CSS', 'Python', 'Python','PHP']

subjects.append('PHP')
subjects.remove('PHP')
subjects.insert(2,'HTML')

subjects2 = subjects.copy()

subjects.sort()
subjects.reverse()
subjects.pop()
subjects.clear()

pos = subjects2.count('Python')

print(pos)



