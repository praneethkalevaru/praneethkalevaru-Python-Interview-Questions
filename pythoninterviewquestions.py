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

""" sort the given list without sort method
   input:l=[1,5,3,2,10]
   output: [1,2,3,5,10]"""

l = [1, 5, 3, 2, 10]
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):  # Reduce range to avoid index out of bounds
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print("sorted lis :",l)

"""find maximum element from the list
   input:l=[1,5,3,2,10]
   output: 10
"""
l=[1,5,3,2,10]
num=l[0] # Start with the first element as the maximum
for i in l:
    if i > num: # If current element is greater, update num
        num=i
print("maximum number :",num)


"""find minimun element from the list
   input:l=[1,5,3,2,10]
   output: 10
"""
l=[1,5,3,2,10]
num=l[0] # Start with the first element as the minimum
for i in l:
    if i < num: # If current element is lessthan, update num
        num=i
print("minimum number :",num)

"""Swap key-values from dictionary by using dictionary Comprehension
 input : d={"abc":1,"number":2,"name":"python"}
outpur:	{1:"abc",2:"number","python":"name"}"""

d={"abc":1,"number":2,"name":"python"}
d1 ={ values:keys for keys,values in d.items()} #It  will swap each key-value pair in the dictionary d
print("Swap key-values from dictionary:",d1)


"""Remove empty tuple by using list Comprehension
 input:t1=[(),(),("abc",1,2),3,4,()]
 output:[("abc",1,2),3,4]"""

t1=[(),(),("abc",1,2),3,4,()]
t2=[i for i in t1 if i] #The condition if i keeps only elements that are not empty (non-falsy values).
print("Remove empty tuple:",t2)


""" check prime number
take number from user
   input:7 
   output: is prime

"""
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Is prime")
else:
    print("Not a prime number")


"""factorial of number
take input from user
   input: 5
   output: 120 """
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)


"""print even and odd numbers from list
   input :[1,2,4,7,9,15]
   ouput :[2,4]
"""

l=[1,2,4,7,9,15]
even_list=[]
odd_list=[]
for i in l:
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even numbers : ",even_list)
print("Odd numbers :", odd_list)


"""How to count the each character in sting
   input: str="python"
   output={'p':1,'y':1,'t':1,'h':1,'o':1,'n':1}"""

s = "panthpythons"
d = {}
for i in s:
    if i not in d:
        d[i] = 1  # Add the character as key with its value as the character itself
    else:
        d[i] += 1  # Append the character to the value if it exists already
print(d)


"""Give string is palindrome or Not?
take string from user
inputstring::madam
outpu : is palindrome """

str1=input("Enter the string : ")
empy_string=""
for i in str1:
    empy_string=i+empy_string
if str1==empy_string:
    print("Palindrome")
else:
    print("Not a palindrome")


"""How to Reverse a number in Python
take number from user
input : number = 1234
output :4321"""
num = int(input("Enter a number: "))
reversed_num = 0

while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
    num //= 10  # Remove the last digit from num

print("Reversed number:", reversed_num)

"""Give number palindrome or Not?
take number from user
input number =121
output = is palindrome"""

num = int(input("Enter a number: "))
original_num = num  # Store the original number
reversed_num = 0

# Reverse the number
while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit

# Check if the original number and the reversed number are the same
if original_num == reversed_num:
    print("Given nuumber is Palindrome")
else:
    print("Not a palindrome")


"""decorator in Python
  decorator is a function that takes another function as input and extends or modifies 
  its behavior without changing its actual code
  while calling decorator function we use @decorator method"""

#add two number using decorator function
def my_decorator(func):
    def sum_of_numbers(a,b):
        res=func(a,b)
        return res
    return sum_of_numbers

@my_decorator
def add(a,b):
    return a+b
print(add(10,20))


""" generator function"""
""" At lest one yield keyword is there we consider as generator function .its use for Memory Usage,
while time of calling generator function we use next() method.
if we not use next()  method its print generator object."""
def generator_fun(a, b):
    yield a * b  # The result of a multiplied by b is yielded

# Create a generator object by calling the generator function
mult = generator_fun(10, 20)

# Use next() to get the next value from the generator
print(next(mult))  # This will print 200, as 10 * 20 is 200

""" To print prime number from given range"""
# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop through each number in the range
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # If a divisor is found, break without printing anything
                break
        else:
            # If no divisors were found, print the number as it is prime
            print("Prime number:", num)

"""Reversing Words in a Sentence"""
str="It looks like you're asking about lists in Python! A list is a built-in data structure in Python that allows you to store multiple items in a single variable. Lists are mutable, meaning their content can be changed after they are created"

split_str=str.split(" ")
l=[]
for i in split_str:
    l.append(i[::-1])
res=" ".join(l)
print(res)

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1] 
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1] """

nums=[3,6,9,7,4,5]
target =9
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] ==target:
            l.append([nums[i],nums[j]])
for k in l:
    print(k)
    

""" Find the second highest number from given list"""

l=[333,666,222,111,555,777,999]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l[-2])