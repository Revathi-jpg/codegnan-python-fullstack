Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[7:]
[3, 7, 0]
>>> a([7:])
SyntaxError: invalid syntax
>>> a1=a[:5]
>>> a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> c=a2+a1
>>> c
[0, 3, 4, 6, 7, 1, 2, 5, 8, 9]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> d=a1+a2
>>> d
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> d=a2+a1
>>> d
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> ###task-2
>>> a=["codegnan","python"]
>>> a.upper()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> ##output --> ["CODEGNAN","PYTHON"]
>>> b=str(a)
>>> b
"['codegnan', 'python']"
b.upper()
"['CODEGNAN', 'PYTHON']"
a=list(b)
a
['[', "'", 'c', 'o', 'd', 'e', 'g', 'n', 'a', 'n', "'", ',', ' ', "'", 'p', 'y', 't', 'h', 'o', 'n', "'", ']']
###task-3
a=[2,5,7,10,15]
##output-->[2,5,7,8,9,10,15]
a.sort()
a
[2, 5, 7, 10, 15]
a=[2,5,7,9,10,15]
a.insert(3,8)
a
[2, 5, 7, 8, 9, 10, 15]
###task-4
a=(10,20,30,40)
#output-->(10,20,30,40,50)
b=list(a)
b
[10, 20, 30, 40]
b.append(50)
b
[10, 20, 30, 40, 50]
c=tuple(b)
c
(10, 20, 30, 40, 50)
####task--5
a=[2,3,4,5,6]
#output[2,3,4,5,6,"c","o","d","e"]
a.extend("c","o","d","e")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.extend("c","o","d","e")
TypeError: list.extend() takes exactly one argument (4 given)
a.extend("code")
a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e']
###task--5
#swapping of two variables
a=10
b=20
#replace
a.replace(b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.replace(b)
AttributeError: 'int' object has no attribute 'replace'
