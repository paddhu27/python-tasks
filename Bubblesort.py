s=input("enter the list of values of list ,seperated by commas")
arr=s.split()
print("the unsorted array is",arr)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubbleSort(arr))
