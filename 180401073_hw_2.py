import sys
import os
new = os.getcwd()
my_List=[]
my_word_list=[]
leaving_list=[]
my_month_list = []
hist_list =[]
def insertionSort(arr):
    n=len(arr)
    for i in range (1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

def my_doc(path):
    f=open(path,'r') 
    contents=f.readlines()
    for line in contents:
        words = line.split(";")
        my_List.append(words)
        
    f.close()
    for i in my_List:
        my_word_list.append(i[3])
    for j in my_word_list:
        month = j.split("-")
        leaving_list.append(month)
    for k in leaving_list:
        my_month_list.append(k[1])
    insertion_month = insertionSort(my_month_list)
    return insertion_month

def count_elements(elements):
     hist = {}
     for i in elements:
         hist[i] = hist.get(i, 0) + 1
     return hist
 
def mode_(my_hist_d):
    frequency_max = -1
    mode = -1 
    for key in my_hist_d.keys():
       # print(key,my_hist_d[key])
        if  my_hist_d[key]>frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode
def median_(my_list):
    n=len(my_list)
    if n%2 == 1:
        middle = int(n/2)+1
        median = my_list[middle-1]
       
    else:
        middle_1=my_list[int(n/2)]
        middle_2=my_list[int(n/2)+1]
        median = (middle_1 + middle_2)/2
        
    return median 

def average_(my_hist_list):
    total = 0
    counter = 0
    for i in my_hist_list:
        total += i
        counter += 1
    result = total / counter
    return result
    
path = sys.argv[1]
outputpath = sys.argv[2]
os.chdir(path)
dosyalar = os.listdir()
for dosya in dosyalar:
    if os.path.exists("input_hw_2.csv"):
        dosya = "input_hw_2.csv"
        elements = my_doc(dosya)


elements = [int(i) for i in elements]
my_=count_elements(elements)
for i in my_:
    hist_list.append(my_[i])
strmode=str(mode_(my_))
strmedian=str(median_(hist_list))
straverage=str(average_(hist_list))
L=["Mode: ",strmode,"\nMedian: ",strmedian,"\nOrtalama: ",straverage]
os.chdir(new)
os.mkdir(outputpath)
if os.path.exists(outputpath):
       os.chdir(outputpath)

file1 = open("180401073_hw_2_output.txt","a")
file1.writelines(L)
file1.close()
