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
print(result1)
print(result2)

