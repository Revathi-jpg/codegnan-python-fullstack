Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#VARIABLES
print(4+8)
12
a=10
print(a)
10
x=50
print(X)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
50
Z=100
print(Z)
100
3=90
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=90
print(a3)
90
5x=9
SyntaxError: invalid decimal literal
a0123456789=100
print(a0123456789)
100
name="revathi"
print(name)
revathi
print("name")
name
city="vij"
print(city)
vij
country="india"
print(country)
india
a=8
b=9
print(a+b)
17
fname="revathi"
lname="sana"
print(fname+lname)
revathisana
print(fname+" "lname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname,lname)
revathi sana
a=4,b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=6,7
print(a+b)
13
a=6
b=8
print(a+b)
14
@=9
SyntaxError: invalid syntax
$=6
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(-a)
-6
print(_a)
100
if=20
SyntaxError: invalid syntax
while=6
SyntaxError: invalid syntax
a=2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=3,4,5
print(a,b,c)
3 4 5
a,b,c=2,3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a,b,c=2,3,4,5,6,7
ValueError: too many values to unpack (expected 3, got 6)
first name="revathi"
SyntaxError: invalid syntax
first_name="revathi"
firstname="revathi"
>>> print(firstname)
revathi
>>> print(first_name)
revathi
>>>  a=3
...  
SyntaxError: unexpected indent
>>> _a=9
>>> print(_a)
9
>>> #unpacking
>>> a=(1,3,2)
>>> print(a)
(1, 3, 2)
>>> a,b,c=(5,6,7)
>>> print(a,b,c)
5 6 7
>>> a=90
>>> print(a)
90
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name="revathi"
>>> print(name)
revathi
>>> NAME="revathi"
>>> print(NAME)
revathi
>>> Name="revathi"
>>> print(Name)
revathi
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c
>>> print(a,b,c)
7 7 7
>>> a=b=c=10
>>> print(a,b)
10 10
