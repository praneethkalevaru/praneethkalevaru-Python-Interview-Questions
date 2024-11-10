"""Remove duplicate elements from given list """
l=[10,20,30,40,10,20,20,40]
l2=[] # to add unique elements
for i in l:
    if i not in l2:
        l2.append(i) #append() method is used to add elements to end of the list
print(l2)