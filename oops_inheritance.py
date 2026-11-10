#9/11/26---
#inheritance---
#single inheritance--single parent ,single child
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is ",RBI.cash+cls.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritance--two parents,single child
'''class Father():
    height=5.2
    def Tall(self):
        print("height is",self.height)
        print("height is",Father.height)
class Mother():
    weight=45
    def strong(kg):
        print("weight is",kg.weight)
        print("weight is",Mother.weight)
class Kid(Father,Mother):
    dob="1/1/25"
    def Birth(year):
        
        print("DOB IS",year.dob)
        print("DOB IS:",Kid.dob)
        
a=Kid()
a.Tall()
a.strong()
a.Birth()'''

#or--
'''class Father():
   
    def Height(self):
        print("5.5 inches")
        
class Mother():
    
    def weight(self):
        print("weight is 60 kgs")
        
class Kid(Father,Mother):
    
    def Birth(year):
        print("DOB IS: just born..")

a=Kid()
a.Height()
a.weight()
a.Birth()'''


#multilevel -inheritance---

'''class Grandparent():
   
    def Land(self):
        print("10acres")
        
class Parent(Grandparent):
    
    def House(self):
        print("house--2 buildings")
        
class child(Parent):
    
    def Vehicle(self):
        print("I have Car..")


a=child()
a.Land()
a.House()
a.Vehicle()'''

#Hierarchical----it means 1 parent class is inherited by multiple child class 


'''class Employee():
   
    def Company(self):
        print("WIPRO")
        
class Trainer(Employee):
    
    def Teaching(self):
        print("python")
        
class Develop(Employee):
    
    def code(self):
        print("will do coding part")


a=Develop()
b=Trainer()
b.Teaching()

a.Company()
a.code()
b.Company()'''

#10/11/26
#hybrid------- it is combination of both heirarchical and mutliple inheritance


'''class Person():
    def details(self):
        print("name:revathi,id:101")
class Student(Person):
    def learn(self):
        print("learns python")
        
class Trainer(Person):
    def teach(self):
        print("coding")
        
class program_manager(Student,Trainer):
    def manager(self):
        print("it manages both student & trainer")
a=program_manager()
a.manager()
a.teach()
a.learn()
a.details() '''


#super()----
  
class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
obj=child("revathi",22)
obj.name
obj.age


































        
