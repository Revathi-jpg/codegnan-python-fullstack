
# FUNCTION---
#1) function is a block of organized,reusable code and that is used to perform a single or multiple tasks
#2) python gives in built func like print or u can make ur own functions and these are called user defined func
#3) func block begins with a def follwed by a func name and paranthesis(())---a,b are arguments 10,20 are parameters

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#func
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#pow **
#modulus %
#int division //

'''def cal(a,b):
    print("the pow is",a**b)
    print("the modulus is",a%b)
    print("the intdiv is",a//b)
cal(2,5)
cal(10,2)'''

'''def add(a,b):
    c=a+b
    print(c)
add(7,8)'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()'''

#fullname
'''def fullname():
    fname=input("enter fname")
    lname=input("enter lname")
    print((fname+" "+lname).title())
fullname()'''

#diff b/w print and return
#print just shows human user o/p in a console
#return is used to terminate the func gives back value from a func

'''def sub(a,b):
    print(a-b)
sub(4,8)'''

'''def sub(a,b):
    return a-b
sub(4,8)'''# no o/p is shown we need print to show


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(5,2)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e #we need to give in 1 line

print(cal(5,2))'''



##TASK----
'''while True:
    def cal():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
        else:
            print("Invalid Option")
    cal()'''
#another method
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif mul():
        mul()
    else:
        print("Invalid Option")'''
                
        
    
#-----23/10/26------

#generators-- no tuple comphersations in above cases if we remove {} and keep ()then outcome is generator
#syntax----a=[expr for var in collection/range)
'''a=[i for i in range(16)]
print(a)
print(type(a))'''
'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))
#print(list(a))
#print(set(a))
#print(tuple(a))'''#for genterators we can
#def--a generators is a function which can be use as an iterative(loop) by producing group of values where we can yield keyword

#yield vs return --- return will terminate the function where as yield can pass function and go on with every success iterative
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b)) '''
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''
#yield v/s return
'''def mygen():
    #return "vij"
    #return "hyd"
    return "vzg"
    return "vij" "hyd" "vzg"
print(mygen())'''
'''def mygen():
    yield "apple"
    yield "grapes"
    yield "mango"
#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d)) error --stop iteration'''



#Task----BMI(real time example)--------
'''while True:
    a=float(input("Enter the Weight:"))
    b=float(input("Enter the Height:"))
    c=a/(b)**2
    if c <=18.5:
        print("under weight")
    elif c>18.5 and c<=24.5 :
        print("Normal weight")
    elif c>24.5 and c<=29.5:
        print("over weight")
    elif c>=30:
        print("obesity")'''


#-------------24/10/26----------
#-------built functions-------------
#fromkeys()---is a method from dictionary
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))--error
b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"revathi")
print(b)
b["o"]="radhi"
print(b)'''

#eval()--it allows user input all data types
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

  
'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#zip()-->we can combine multiple collections into one collections
a=[10,20,30,40,50]
names=["revathi","radhi","neeru","rama","bhanu"]
print(a+names)
b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)
d=set(zip(a,names))
print(d)
e=tuple(zip(a,names))
print(e)
f=dict(zip(a,names))
print(f)

#enumerate()-->we can  give count  to the collections
'''names=["rama","ravi","rita","raju","raghu"]
for i in range(len(names)):
    print(i,names[i])
b=list(enumerate(names))
print(b)
b=dict(enumerate(names,100))
print(b)
c=tuple(enumerate(names))
print(c)
d=set(enumerate(names))
print(d)'''

#map()-->each object from a collection and forms new collection
'''a=[7,4,6,9,3]
b=[2,5,7,10,13]
c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))   
print(d) '''  



#---------27/10/26---------
#annonymous----are nameless functions and we use keyword called as lamda to create annonymous
'''def calculate():
    x=5
    print(2*x+5)
calculate() '''
#syntax---a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''


'''a=int(input("a value:"))
b=lambda x:2*x+5
print(b(a)) '''

#task---
'''a="python"
b=lambda x:str(x)
print(b(a.upper()))'''
'''a="python"
b=lambda x:x.upper()
print(b(a))'''
#2 task
'''a="hello world"
b=lambda a:a.title()
print(b(a))'''

#3 task
'''a=input("fname")
b1=input("lname")
c=a+b1
b=lambda x:str(c)
print(*b(c))'''

'''a=input("fname")
b=input("lname")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=[x for x in input("enter the names").split(",")]
    
c=lambda a,b:(a+" "+b).title()
print(c(a,b))  '''

#task-3--power
'''a=lambda x,y:x**y
print(a(2,4))'''

#filter
'''a=[2,6,8,10,13,15,20,27,40,60,87,100]'''
#if a%2==0:
   # print("even numbers:",a)----error
'''for i in a:
    if i%2==0:
        print(i)'''
'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

a=()
print(type(a))

a={}
print(type(a))'''


#----29/10/26---------

'''a=[[],(),set(),"",{},None,3,3.5,"revathi",7+6j,True,False]
b=list(filter(None,a))
print(b)'''

#map----------
'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the names").split(",")
print(a+b)'''

'''a=[x for x in input("enter the values").split(",")]
print(a)'''

'''a,b=map(str,input("enter the names").split(","))
print(a+b)'''

'''a=int(input("values1")
b=int(input("value2")
print(a+b)'''

      
'''a,b=int(input("enter the values").split(","))
print(a+b)'''#error

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''



'''a=list(map(int,input("values").split(",")))
print(a)'''

'''a=tuple(map(int,input("values").split(",")))
print(a)'''                         
 

'''a=set(map(int,input("values").split(",")))
print(a)'''


'''a=list(map(eval,input("values").split(",")))
print(a)'''

'''a,b=map(eval,input("values").split(","))
print(a)'''


'''a=input("values and pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''



  #modules--
#modules--v/s---library---v/s-----package
#a module is single python flie it consiste python code
#it contains functions,variables and classes
#examples of modules --> math.py,random.py,mymodule.py

#package---
#one or more python files( modules) is known as package
#ex--->numpy,pandas and request

#library---
#a library consists of both moducles and packages
#ex-->numpy,pandas,matplotlit,


#----Note---- every python flie is module and import is keyword and every python flie is saved internally with variable name as __main__












































 






        
        
   

    
    



      
    




    





