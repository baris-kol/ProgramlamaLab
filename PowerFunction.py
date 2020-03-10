#Power Function 
"""def Power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        t=1
        for i in range (b):
            t=t*a
        return t

a = int(input("Deger:"))
b = int(input("Üssü:"))
print("Sonuç: ",Power(a,b))
"""
#Recursive Power Function
def Power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    if(b>1):
       return Power(a,b-1)*a
      2
a = int(input("Deger:"))
b = int(input("Üssü:"))
print("Sonuç: ",Power(a,b))

        