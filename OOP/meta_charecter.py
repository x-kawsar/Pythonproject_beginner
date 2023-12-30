import  re

pattern = r"[A-Z][a-z][0-9]"

if re.match(pattern, 'Ad0dfg'):
    print('Matched')


