def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2,3))


def cube(x):
    return x*x*x
rx = cube(5)
print(rx)





lf = (lambda a,b : a*a + 2*a*b + b*b)(3,4)
print(lf)

lb = (lambda x: x*x*x)(3)
print(lb)
