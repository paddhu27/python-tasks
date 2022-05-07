list=input("enter elements separated by spaces\n")
arr=list.split()
x=input("enter a element that you want to find : ")
def Linear_search(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1
r=Linear_search(arr,x)
if(r==-1):
    print("searching element is not found")
else:
    print(x,"found at index position ",r)