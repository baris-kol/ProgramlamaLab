#Alt Diziler Arasında Toplamı Max olan Dizi
def max(List_1):
    
    max = 0
    for i in range(8):    
        for j in range(i,8):
           # print(i,j)
           t=0
           for k in range (i,j):
               t =  t + List_1[k]
               if t>max:
                   max = t
                   
    return max
#print(max()) //Sonuç (11)

#ancak for k in range (i,j) döngüsüne ihtşyaç yoktur.

def maxList(List_1):
    maxSum = 0
    n=len(List_1)
    for i in range(n):    
        t=0
        for j in range(i,n):
           # print(i,j)
           t =  t + List_1[j]
           if t>maxSum:
              maxSum = t
             
    return maxSum

List_1=[4,-3,5,-2,-1,2,6,-2]
print(maxList(List_1))