

def large(x,y,z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z

result = large(2000,5000,40000)

print(result)






