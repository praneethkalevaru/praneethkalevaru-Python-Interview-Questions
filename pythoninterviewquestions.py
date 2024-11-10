"""Remove duplicate elements from given list """
l=[10,20,30,40,10,20,20,40]
l2=[] # to add unique elements
for i in l:
    if i not in l2:
        l2.append(i) #append() method is used to add elements to end of the list
print(l2)

"""How to Reverse a String in Python"""
s="panthpythons"
s1="" # To add Reverse string
for i in s:
    s1=i+s1
print(s1)
"""  s1=i+s1 This line is the core of the reversal process. For each character i in s, it updates s1 by adding i to the front of s1. By placing i before s1, each new character from s is added at the beginning of s1, reversing the character order as the loop progresses."""