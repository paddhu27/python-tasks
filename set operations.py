s1=input("enter the list of values of list 1,seperated by commas")
l1=s1.split()
s2=input("enter the list of values of list 2,seperated by commas")
l2=s2.split()
#union operation
union=[]
print(l1)
print(l2)
for i in l1:
    if i not in union:
        union.append(i)
for i in l2:
    if i not in union:
        union.append(i)
union.sort()
print("the union of two lists is\t",union)

#intersection operation
intersection=[]
for i in l1:
    for j in l2:
        if i==j:
            intersection.append(i)
intersection.sort()
print("the intersection of two lists is\t",intersection)

#A-B
dif1_2=[]
for i in l1:
        if i not in l2:
            dif1_2.append(i)
dif1_2.sort()
print("the difference of l1 -l2 is\t",dif1_2)

#B-A
dif2_1=[]
for i in l2:
        if i not in l1:
            dif2_1.append(i)
dif2_1.sort()
print("the difference of l1 -l2 is\t",dif2_1)
