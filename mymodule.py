'''def greetings(name):
    print("welcome",name)'''

'''a=4
b=7
print(a+b)'''

'''a=int(input("a value"))
b=int(input(b value"))
print(a+b)'''

'''details={"idnos":[1,2,3,4],
         "names":["neeru","revathi","roshna   ","radhi"],
         "marks":[100,90,80,70]}'''
#-----30/10/26----
'''if__name=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    print(a)'''


'''def dummy():
    if __name__=="__main__":
        print("This program is run as script")
    else:
        print("This program is run as module")
dummy() '''


#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.log(10))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.sqrt(2))
print(math.pow(2,4))
print(math.ceil(2.9))
print(math.floor(4.8))'''
 
'''from math import pi,sqrt,log
print(pi,sqrt(2),log(20))'''
#print(math.pi)---error no need to call everytime math here while using from key


#sys module---system module

'''import sys
print(sys.path)
for i in sys.path:          #to print one by one 
    print(i)

print(sys.version)'''


#os module----
'''import os
print(os.path)
print(os.getcwd())   #cwd--current working directory
print(os.listdir())'''
'''print(os.mkdir("file"))
print(os.listdir())
print(os.chdir("C:\\Users\\DELL\\Downloads\\codegnan"))
print(os.listdir())  '''




#random module
#def---to generate randon numbers in python,randint() function is used  and this function is defined in random module

#sample()
'''import random
a=random.sample(range(20,50),6)
print(a)'''


#randint()
'''import random
a=random.randint(20,60)
print(a)'''

#choice()

'''import random
b=[2,8,4,7,1,5]
a=random.choice(b)
print(a)'''


#task-----ludo--dice
'''import random
while True:
    int(input("Enter the roll of dice:"))
    b=random.randint(1,6)
    print(b)
    option=input("roll again?(y/n)")
    
    if option==y:
        continue
        
    else:
        break'''

#31/10/26--------------------
#calendar-----

'''import calendar
year=2027
month=6
print(calendar.month(year,month))'''


'''import calendar
year=2027
print(calendar.calendar(year))'''


'''import calendar
year=int(input("enter the year:"))
month =int(input("enter the month:"))
print(calendar.month(year,month))'''

'''import calendar
year=int(input("enter the year"))
print(calendar.calendar(year))'''
    
#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time
b=time.localtime(a)
print(b)

print(f"today.date is: {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is: {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"year is: {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

#2/11/26

#regex or regular expressions --


#sequence characters
'''\w-- it matches alphanumeric
\W-- it matches non-alphanumeric
\d-- it matches any  digit
\D-- it matches non digit
\s -- it represent white spaces
\S--- it represents non white spaces'''

#compile(),search(),findall(),split(),sub()


import re
#a="map mat cat money cash capm code maths mug dog donkey "
'''b=re.compile(r"m\w\w\w\w")
print(b)'''


#search()
'''c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''

#findall()
'''e=re.findall(r"m\w+",a)
print(e)'''

'''d=re.findall(r"d\w+",a)
print(d)'''

'''h=re.findall(r"c\w+",a)
print(h)'''


#split()
'''b=re.split(r"m",a)
print(b)

m=re.split(r"\s",a)
print(m)'''


#sub()--we can replace a word 
'''c=re.sub(r"m","t",a)
print(c)'''


'''b="a123 b345 c26"
c=re.findall(r"\d+",b)
print(c)'''
'''m="year 2026  month nov  date 2 "
n=re.findall(r"\d+",m)
print(n)'''





























