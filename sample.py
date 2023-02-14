#string reverse using slicing
Mystring = "Python Program"
print(Mystring[::-1])

#form a new list by concatenating the given 2 lists
'''Output->['My', 'name', 'is', 'Kelly']'''
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"] 
for x,y in zip(list1,list2):
    print([x+y])

''' Write an example to handle the “IOError” that occurs while opening and
appending some content into a file “sample.txt” in python using
exception handling?'''
''' Wrong path,file name,os operation->IOError'''
try:
    f=open("/home/user1/python assessment/sample.txt","r+")
    c=f.read()
except IOError:
    print("IO error occurred")
else:
    print(c)
    f.close()

'''You have given a Python list. Write a program to find value 20 in the list,
and if it is present, replace it with 200. Only update the first occurrence of
an item.   
Output->[5, 10, 15, 200, 25, 50, 20]'''
list1 = [5, 10, 15, 20, 25, 50, 20] 
i=list1.index(20)
list1[i]=200
print(list1)

'''Concatenate two lists in the following order using list comprehension.
Output-> ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']'''
lst1 = ["Hello ", "take "] 
lst2 = ["Dear", "Sir"] 
for x in lst1:
    for y in lst2:
        print([x+y])

'''Write a python program to find the given mac address is valid or not
using regular expressions.
Input:
01:23:24:5f:2e:1c
Output:
Valid
Input:
00:01:23:ah:1f:2g
Output:
Not Valid'''
import re
mac=input("Enter the mac address:")
if(re.search("[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}",mac)):
    print("Valid")
else:
    print("Not Valid")

'''Write a Python program to convert the given lists into a dictionary in a
way that item from list1 is the key and item from list2 is the value. 
Output->{'Ten': 10, 'Twenty': 20, 'Thirty': 30}'''
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30] 
my_dict={}
for x,y in zip(keys,values):
    my_dict[x]=y
print(my_dict)

'''Write a python program to find the even length words in the given
string.
Output->We taking python assignment.'''
s = "We are taking the python assignment ."
print([word for word in s.split(" ") if len(word)%2==0])

'''Grab the value “hello” from the below dictionary.'''
Dict={"k1":[{"nest_key":["Deep",["Hi", "hello"]]},"World"]}
print(Dict['k1'][0]["nest_key"][1][1])

'''Write a program to find the factorial of a number n using python function
recursion.'''
def fact(n):
 for i in range(0,n):
    if(n==0 or n==1):
        return 1
    else:
         return n*fact(n-1)
print(fact(5))

'''You are given with a list. Create a new list that is having only the even
number in 
  the given list, using lambda and filter function. 
  Output->list2=[10,12,14,16]'''
l1= [10,11,12,13,14,15,16]
l2=filter(lambda x: x%2==0,l1)
print(list(l2))