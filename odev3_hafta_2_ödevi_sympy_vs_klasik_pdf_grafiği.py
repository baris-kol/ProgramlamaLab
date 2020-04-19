"""
      Barış KOL 180401073
    Github : https://github.com/baris-kol/ProgramlamaLab
    
    Binomial Distribution
"""
import sympy as sym #sympy kütüphanesi eklendi
from sympy import Symbol 
from sympy import pprint #pprint ile daha güzel bir ekran görüntüsü vermek için gerekli modül eklendi
import matplotlib.pyplot as plt #Bir çizim kütüphanesi


p = Symbol('p') #semboller tanılmandı
x = Symbol('x')
n = Symbol('n')

function0 = sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
function1 = p**x
function2 = (1-p)**(n-x)
fTotal = function0*function1*function2 #Binom dağılım formülü oluşturuldu.
print("Binom Dağılım Formülü: ")
pprint(fTotal)

x_values = [] 
y_values = []

for value in range(0,50):
    y=fTotal.subs({p:0.5,n:50,x:value}).evalf()
    y_values.append(y)
    x_values.append(value) #p ve n değerlerine göre grafik için x'e karşılık y değerleri eklendi

#Matplotlib grafik çizimi
plt.title("Binomial Distribution Plot For n=50 MATPLOTLİB")
plt.plot(x_values,y_values)
plt.show()

#Sympy grafik çizimi
sym.plot(fTotal.subs({p:0.5,n:50}),(x, 0, 50),title='Binomial Distribution Plot For n=50 SYMPLOT')



