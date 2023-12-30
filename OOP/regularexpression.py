import re

# re.match() re.findall()

pattern = r"colour"
text = 'My favorite colour is Red. I love blue colour as well'

rp = re.sub(pattern,'color', text)
rp2 = re.sub(pattern,'color', text,count=1)

print(rp)
print(rp2)





