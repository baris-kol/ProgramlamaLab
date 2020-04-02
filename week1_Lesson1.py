import random

print(random.random())

def get_n_random_numbers(n=10,minimum=-5,maximum=5):
    numbers=[]
    for i in range (n):
        numbers.append(random.randint(minimum,maximum))
    return numbers

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if (item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

def my_frequency_with_list_of_tuples(list1):
    frequency_list = []
    for i in range(len(list1)):
        s=False
        for j in range(len(frequency_list)):
            if (list1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list1[i],1])
    return frequency_list
        
my_list = get_n_random_numbers()
my_sorted_list = sorted(my_list)
print(my_sorted_list)

result1 = my_frequency_with_dict(my_sorted_list) 
result2 = my_frequency_with_list_of_tuples(my_sorted_list)
print(result1),print(result2)

##############################################################################
print("LESSON 2")

def mode_(my_hist_d):
    frequency_max = -1
    mode = -1 
    for key in my_hist_d.keys():
       # print(key,my_hist_d[key])
        if  my_hist_d[key]>frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return frequency_max,mode

def mode_tuples(my_hist_list):
    frequency_max = -1
    mode = -1
    for item,frequency in my_hist_list:
       # print(item,frequency)
        if frequency>frequency_max:
            frequency_max = frequency
            mode = item
    return mode,frequency_max
    

my_list_1 = get_n_random_numbers(5,-2,2)
my_hist_d = my_frequency_with_dict(my_list_1)

print(my_hist_d)

print(mode_(my_hist_d))

print("mode of list with histogram (a list of tuples))")
    
my_list_2 = get_n_random_numbers(10)
my_hist_l = my_frequency_with_list_of_tuples(my_list_2)
print(my_hist_l)
print(mode_tuples(my_hist_l))

#############################################################################

print("LESSON 3")

def my_linear_search(my_list,item_search):
    found=(-1,-1)
    n = len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found = (my_list[indis],indis)
    return found

def mean_of_list(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_=t/s
    return mean_

def  my_bubble_sort(my_list):
    n=len(my_list)
    print(my_list)
    for i in range (n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

def my_binary_search(my_list, item_search):
    found = (-1,-1)
    low = 0 
    high = len(my_list)-1
    
    while low <= high:
        mid = (low+high) // 2
        
        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found

def median_(my_list):
    my_list_2 = my_bubble_sort(my_list)
    print(my_list_2)
    n=len(my_list_2)
    if n%2 == 1:
        middle = int(n/2)+1
        median = my_list_2[middle-1]
       
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median = (middle_1 + middle_2)/2
        
    return median 

        
        
my_list = get_n_random_numbers(10,-5,5)
print(my_list)

print(my_linear_search(my_list,4))

print(mean_of_list(my_list))

print(my_bubble_sort(my_list))

print(my_binary_search(my_list,4))

#Median of a list

size = input("dizi boyutu giriniz:")
size = int(size)
my_list_ = get_n_random_numbers(size)

print(median_(my_list_))
