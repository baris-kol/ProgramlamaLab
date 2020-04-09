from sympy import Symbol
from sympy import factor,expand
from sympy import pprint

x = Symbol('x')
y = Symbol('y')

p = x*(x+x)
print(p)

p = (x+2)*(x+3)
print(p)

expr = x**2 - y**2
factors = factor(expr)
print("Factors: ",factors)
expands = expand(factors)
print("Expands: ",expands)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print(factors)
pprint(factors)
series = x 
n=5 
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
print(res)

r = expr.subs({x:1-y})
print(r)

series = x
n=50
x_value = 10
for i in range(2,n+1):
    series = series+(x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print(series_value)