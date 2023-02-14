mylist=["Sun","Mon","Tue","Wed"]
mylist.reverse()
print(mylist)

def remove_duplicate(mylist):
        s=set(mylist)
        print(list(s))
remove_duplicate([1,2,2,2,3,3,3,4,4,5])

str="Hi! How are you? Krish Kumar"
count=0
for i in str.split(' '):
    count+=1
print(count-1)

print([num for num in range(147,210) if num%7==0])

name=[ "rahul", "aswin", "abi"]
marks = [80, 90, 70]
my_dict={}
for x,y in zip(name,marks):
        my_dict[x]=y
print("Old dictionary: ",my_dict)
k=input("Enter the key:")
v=input("Enter the value:")
try:
    if(k not in my_dict.keys()):
        my_dict[k]=v
    else:
        raise Exception("KeyAlreadyPreasentException")
except Exception:
    print("Key already present")
else:
    print("New dictionary: ",my_dict)

"""Do this in a function. 
 1. class: A initialize with 2 values x and y
     methods: a)  add, -> add and return x and y
              b) sub, -> find x - y
              c) swap 
 2. class B -> subclass of A
     methods: a) sub -> Check if x < y. Then swap x and y. Then call A's sub function.
              b) swap -> swap x and y. """



class A:
    def __init__(self,x,y,temp=0):
        self.x=x
        self.y=y
        self.temp=temp
    def add(self):
        print("________________________Class A________________________")
        print(f"Addition of given numbers {self.x} and {self.y}:",self.x+self.y)
    def sub(self):
        print(f"Subtraction of given numbers {self.x} and {self.y}:",self.x-self.y)
    def swap(self):
        print("________Swapping ________")
        print(f"Before swapping:{self.x},{self.y}")
        self.temp=self.x
        self.x=self.y
        self.y=self.temp
        print(f"After swapping:{self.x},{self.y}")
class B(A):
    def __init__(self,x,y,temp=0):
        A.__init__(self,x,y,temp=0)
        self.x=x
        self.y=y
        self.temp=temp
    def sub(self):
        print("_________________________Class B________________________")
        if(self.x<self.y):
            print("________Swapping ________")
            print(f"Before swap in class b:{self.x},{self.y}")
            self.temp=self.x
            self.x=self.y
            self.y=self.temp
            print(f"After swapping:{self.x},{self.y}")
            print("____Result of calling sub() from class A____")
            result=A.sub(self)
    def swap(self):
        print("________Swapping ________")
        print(f"Before swapping:{self.x},{self.y}")
        self.temp=self.x
        self.x=self.y
        self.y=self.temp
        print(f"After swapping:{self.x},{self.y}")
a=A(10,2)
a.add()
a.sub()
a.swap()
b=B(5,10)
b.sub()
b.swap()

import re
ip=input("Enter ip address to validate:")
def validate(ip):
  if(re.findall("[0-255]{1,3}.[0-255]{1,3}.[0-255]{1,3}.[0-255]{1,3}",ip)):
        print("Valid ip: ",ip)
  else:
        print("Invalid ip given")
validate(ip)