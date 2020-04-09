import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp
import matplotlib.pyplot as plt
sigma = Symbol('sigma')
x = Symbol('x')
mu = Symbol('mu')

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function = part_1*part_2
pprint(my_gauss_function)

syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution')

x_values = []
y_values = []
for value in range (-50,50):
    y = my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
    x_values.append(value)
    y_values.append(y)
    print(value,y)

plt.plot(x_values,y_values)
plt.show()