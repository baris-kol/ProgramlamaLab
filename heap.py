"""
180401073-Barış KOL
Github:     
"""
def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
        
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

def insertItemToHeap(myheap_1,item):
    myheap_1=myheap_1.copy()
    myheap_1.append(item)
    insertedHeap=heapsort(myheap_1)
    return insertedHeap
    
def removeItemFrom(myheap_1,item):
    myheap_1 = myheap_1.copy()
    for i in range (len(myheap_1)-1):
        if(myheap_1[i] == item):
            myheap_1[i], myheap_1[-1] = myheap_1[-1], myheap_1[i] 
            del(myheap_1[-1])
            removedHeap = heapsort(myheap_1)
    return removedHeap  
  
my_array_1 = [8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1)

my_array_2 = [8,10,3,4,7,15,1,2,16]
my_heap_array=heapsort(my_array_2)
print(my_heap_array)

insertionHeap=insertItemToHeap(my_array_2,9)
print(insertionHeap)

RemovedHeap=removeItemFrom(insertionHeap,8)
print(RemovedHeap)