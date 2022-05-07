list=input("enter elements separated by spaces\n")
arr=list.split()
c=1
m=[]
count=0
for i in range(0, len(arr)):
    if arr[i] not in m:
        for j in range(i+1, len(arr)):    
            if(arr[i] == arr[j]):
                c=c+1
        if c>1:
            print(arr[i],"repeated for",c,"times in the given list")
            count=count+1
        m.append(arr[i])
        c=1
print("the total number of duplicates in the given data is",count)
        
    
