#histogram
def my_h(List_1):
    my_d = dict()
    for item in List_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=item+1
    return my_d

#İçinde n adet tekrar eden sayı var mı?
    
def lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    return -1


List_1 = [2,3,4,6,2,5,6,6,6,6,6,6,6,2]
print(my_h(List_1))
print(lookup(my_h(List_1),3))

