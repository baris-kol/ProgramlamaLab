#insertion sort code

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
List_1 = [4,-3,5,-2,-1,2,6,-2]
print(insertionSort(List_1))

#Shell Sort Code

def ShellSort(arr):
    n=len(arr)
    gap = n//2
    while gap>0:
        for i in range (gap,n):
            temp = arr[i]
            j = i
            while j>= gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap //= 2

List_1 = [4,-3,5,-2,-1,2,6,-2]
print(insertionSort(List_1))