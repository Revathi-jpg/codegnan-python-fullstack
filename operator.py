Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operators
>>> #arithematic
>>> a=2
>>> b=9
>>> print(a+b)
11
>>> print(a-b)
-7
>>> print(a*b)
18
>>> print(a/b)
0.2222222222222222
>>> print(a//b)
0
>>> print(a**b)
512
>>> print(a%b)
2
>>> #assignment
>>> a=6
>>> b=4
>>> print(a+b)
10
>>> a+=b
>>> a
10
>>> a-=b
>>> a
6
>>> a*=b
>>> a
24
>>> a/=b
>>> a
6.0
>>> a//=b
>>> a
1.0
>>> a**=b
>>> a
1.0
>>> a%=b
>>> a
1.0
>>> b+=2
>>> b
6
>>> b-=6
>>> b
0
>>> b**=5
>>> b
0
>>> b=6
>>> b
6
>>> b//=7
>>> b
0
>>> b=5
>>> b
5
>>> b*=5
>>> b
25
>>> b%=8
>>> b
1
>>> #comparision
>>> a=7
>>> b=9
>>> a<b
True
>>> b>a
True
>>> b!=a
True
>>> a!=b
True
>>> a==b
False
>>> a<=b
True
>>> a>=b
False
>>> #logical
>>> a=5
>>> b=8
>>> a<b and a>b
False
>>> a!=b and a==b
False
>>> a<=b and a>=b
False
>>> #logical (OR)
>>> a=6
>>> a=2
>>> b=7
>>> a<b and a>b
False
>>> a<=b or a==b
True
>>> a<b or a>b
True
>>> a!=b or a>b
True
>>> a not b
SyntaxError: invalid syntax
>>> a not in b
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a not in b
TypeError: argument of type 'int' is not iterable
>>> #identify
>>> a=5
>>> type(a) is int
True
>>> type(a) is not int
False
>>> type(a) is float
False
>>> a="revathi"
>>> type(a) is int
False
>>> type(a) is  float
False
>>> type(a) is str
True
>>> type(a) is bool
False
>>> type(a) is  not int
True
>>> type(a) is complex
False
>>> a=5+6j
>>> type(a) is int
False
>>> type(a) is float
False
>>> type(a) is bool
False
>>> type(a) is str
False
>>> type(a) is complex
True
>>> a=9.8
>>> type(a) is int
False
>>> type(a) is str
False
>>> type(a) is not float
False
>>> type(a) is float
True
>>> type(a) is bool
False
>>> a=True
>>> type(a) is int
False
>>> type(a) is bool
True
>>> type(a) is not str
True
>>> #Membership
>>> a=2,3,4,5,6,7,8
>>> 9 in a
False
>>> 5 in a
True
>>> 25 not in a
True
>>> yes in a
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    yes in a
NameError: name 'yes' is not defined
>>> "yes" in a
False
>>> #bitwise
>>> a=8
>>> b=5
>>> a&b
0
>>> bin(3)
'0b11'
>>> bin(8)
'0b1000'
>>> bin(5)
'0b101'
>>> a=4
>>> b=7
>>> bin(a)
'0b100'
>>> bin(b)
'0b111'
>>> a&b
4
>>> #or |
>>> a|b
7
>>> a=6
>>> b=3
>>> a|b
7
>>> #not
>>> a~b
SyntaxError: invalid syntax
>>> ~a
-7
>>> a=7
>>> -(a+1)
-8
>>> a=6
>>> -(a+1)
-7
>>> a=-9
>>> -(a+1)
8
>>> a=4
>>> -(a+1)
-5
>>> a=-6
>>> -(a+1)
5
>>> #xor (^)
>>> a=5
>>> b=6
>>> a^b
3
>>> a=7
>>> b=8
>>> a^b
15
>>> b^a
15
>>> a=3
>>> b=4
>>> a^b
7
>>> #left shift
>>> a=7
>>> a<<3
56
>>> a>>2
1
>>> a=8
>>> bin(a)
'0b1000'
>>> a<<4
128
>>> a=6
>>> bina(a)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    bina(a)
NameError: name 'bina' is not defined
>>> a<<3
48
>>> #right shift
>>> a=9
>>> a>>3
1
>>> a=6
>>> a>>7
0
>>> a=8
>>> a>>4
0
>>> 