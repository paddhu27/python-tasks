list=input("enter elements separated by spaces\n")
arr=list.split()
s_ele=input("enter a element that you want to find : ")
n=len(arr)
def bubbleSort(arr):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def binary_search(arr,s_ele):
    low= 0
    high= len(arr) - 1
    mid = 0
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==s_ele):
            return mid
        elif(s_ele<arr[mid]):
            high=mid-1
        elif(s_ele>arr[mid]):
            low=mid+1
    return -1
r= binary_search(arr,s_ele)
if r!= -1:
    print("Element is present at index", r)
else:
    print("Element is not present in array")