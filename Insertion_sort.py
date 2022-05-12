s=input("enter the list of values of list ,seperated by commas")
arr=s.split()
print("the unsorted array is",arr)
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
print("the sorted array is",insertionSort(arr))
