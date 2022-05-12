s1=input("enter the list of values of list 1,seperated by commas")
l1=s1.split()
s2=input("enter the list of values of list 2,seperated by commas")
l2=s2.split()
def Union(l1, l2):
    list3 = list(set(l1) | set(l2))
    return list3
union=Union(l1,l2)
union.sort()
print("the union of two lists is",union)
def intersect(l1, l2):
    list3 = list(set(l1) & set(l2))
    return list3
intersection=intersect(l1,l2)
intersection.sort()
print("the intersection of two lists is",intersection)
def Diff1(l1, l2):
    return list(set(l1) - set(l2))
diff1=Diff1(l1,l2)
diff1.sort()
print("the difference of list1-list2 is",diff1)
def Diff2(l1, l2):
    return list(set(l2) - set(l1))
diff2=Diff2(l1,l2)
diff2.sort()
print("the difference of list2-list1 is",diff2)
