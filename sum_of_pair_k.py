list=input("enter elements separated by spaces\n")
arr=list.split()
sol_set=0
n=len(arr)
print(n)
print(arr)
sum=int(input("enter the sum:"))
for i in range(0,n):
    for j in range(0,n):
        if(int(arr[i])+int(arr[j])==sum):
            print("values are",arr[i],",",arr[j])
            sol_set=sol_set+1
if(sol_set>=1):
    print("the solution set is exist")
else:
    print("solution set does not exist")
