#----OOPS---
#class contains attributes,variables,methods,functions that can manipulate data
#a calss is the blue print of an object
#an object is an intiation of a class
#methods are functions defined inside the body of the class
#4 pillar of oops
#1.ploymorphism--we have 4 type
                           #1.operator overload
                           #2.operator overiding
                           #3.method overload
                           #4.method overriding
#2.inheritance--we have 5 types
                           #1.single inheritance
                           #2.multiple 
#3.multilevel4.heirachy5.hybird
#super()
#3.encapusaltion---we have 3 types
                            #1.public
                            #2.protected_
                            #3.private__
#4.abstract---we have 2 types
                    #1.abstract class
                    #2.abstract method



#syntax
'''class classname():
    #attributes
    name="revathi"
    age=22
    place="vja"
    def fname(method_name):
        print("statements...")
a=classname()
print(dir(a))
a.fname()'''


#class decalaration
'''class Details:
    name="revathi"
    age=22
    place="vja"
    def Display(self):
        print(self.name,self.age,self.place)
        
a=Details()
print(dir(a))
a.Display()'''

#class instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("revathi",22,"vja")
b=details()
b.data("radhi",24,"hyd")
b.display()
a.display()'''


#object initialization---construtor
'''class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("neeru",26,"vizag")
print(dir(a))
a.display()'''


#runtime--
'''class details():
    
    def __init__(self):
        
        self.name=(input("enter your name:"))
        self.age=(int(input("enter age:")))
        self.place=(input("enter place:"))
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''
                        

'''class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(name=(input("enter your name:")),age=(int(input("enter age:"))),place=(input("enter place:")))

print(dir(a))
a.display()'''


#--7/11/26--
#difference between _ and __:
#when user wants to create variable with __ our python interpeter treats it as a special variable to avoid name conflictes with methods and innerclasses

'''class Employee():
    def __init__(self):
        self.name ="revathi"
        self._mailid="revathi@23gmail.com"
        self.__salary=20000#private variable
class Employee1():
    def __init__(self):
        self.name ="radhika"
        self._mailid="radhi@23gmail.com"
        self.__salary=30000#private variable

class Employee2():
    def __init__(self):
        self.name ="neeru"
        self._mailid="neeru@23gmail.com"
        self.__salary=30000#private variable 
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee__salary)

b=Employee1()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._Employee1__salary)

c=Employee2()
print(dir(c))
print(c.name)
print(c._mailid)
print(c._Employee2__salary)'''




#4-pillar of oops--
#ploymorphosim-----

#operator  overloading---same operator based on datatype its behaviour will change
'''a=2;b=5
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(1))
print(a.__mul__(3))
#print(a.__div__(101))
print(a.__pow__(2))
print(a.__le__(1))
print(a.__ge__(0))
a=[1,2,3,4,5];b=[5,6,7,8,9,10]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(5))
a="code";b="gnan"
print(a+b)
a="python";b="course"
print(a.__add__(" "+b).title())
print("revathi".__add__(" "+"sana").title())'''


# operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(5)
#without class
x=6
y=3
print(x+y)'''


#method overloading()
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("sum:",a+b+c)
        elif a!=None and b!=None:
            print("product:",a*b)
        else:
            print("program ends...")
x=new()
x.sum()
x.sum(2,3,4)
x.sum(4,7)'''


'''class new():
    def sum(self,a=5,b=8,c=3):
        if a!=6 and b!=7 and c!=7:
            print("sum:",a+b+c)
        elif a!=5 and b!=8:
            print("product:",a*b)
        else:
            print("program ends...")
x=new()
x.sum()'''


#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


#task--
'''class Car():
    def vehicle(self):
        print("car is a vehical")
class Bike():
    def vehicle(self):
        print("bike is a vehicle")

a=Car()
b=Bike()
a.vehicle()
b.vehicle()'''


#--9/11/26----























  


