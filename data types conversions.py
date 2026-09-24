Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 # data types conversions
 
#INT
 
int(5)
5
int(0.6)
0
int("revathi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("revathi")
ValueError: invalid literal for int() with base 10: 'revathi'
int(5+7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

 
#float
float(7)
7.0
float("revathi")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("revathi")
ValueError: could not convert string to float: 'revathi'
float(8.9)
8.9
float(7=8j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
float(7+6j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(7+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(true)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
float(True)
1.0
float(False)
0.0
#string
str(8)
'8'
str(9.7)
'9.7'
str("revathi)
    
SyntaxError: unterminated string literal (detected at line 1)
str("revathi")
    
'revathi'
str(True)
    
'True'
str(False)
...     
'False'
>>> str(8+6j)
...     
'(8+6j)'
>>> #complex
...     
>>> complex(7)
...     
(7+0j)
>>> complex(True)
...     
(1+0j)
>>> complex(False)
...     
0j
>>> complex(9.6)
...     
(9.6+0j)
>>> complex(9+3j)
...     
(9+3j)
>>> complex("revathi")
...     
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("revathi")
ValueError: complex() arg is a malformed string
>>> bool(7)
...     
True
>>> bool("revathi")
...     
True
>>> bool(9.8)
...     
True
>>> bool(False)
...     
False
>>> bool(7+6j)
...     
True
>>> bool(True)
...     
True
