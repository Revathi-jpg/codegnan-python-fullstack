Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="i am in class"
>>> a[8]+a[9]+
SyntaxError: invalid syntax
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]
'in'
>>> a[1]
' '
>>> a[3]
'm'
>>> a[4]
' '
>>> a[1]+a[4]+a[6]
'  n'
>>> a[1]+a[4]+a[7]
'   '
>>> b="vijayawada is a royal city"
>>> b[16]+b[17]+b[18]b[19]+b[20]
SyntaxError: invalid syntax
>>> b[16]+b[17]+b[18]+b[19]+b[20]
'royal'
>>> b[22]+b[23]+b[24]+b[25]
'city'
>>> b[11]+b[12]
'is'
>>> 
>>> c="vizag is a city of destiny"
>>> c[-1]+c[-2]+c[-3]+
SyntaxError: invalid syntax
>>> c[-7]+c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'destiny'
>>> c[-14]
'i'
>>> c[-15]+c[-14]+c[-13]+c[-12]
'city'
>>> c[-20]+c[-19]
'is'
>>> c[-26]+c[-25]+c[-24]+c[-23]+c[-22]
'vizag'
>>> d="simple is better than complex
SyntaxError: EOL while scanning string literal
>>> d="simple is better than complex"
>>> d[-19]
'b'
>>> d[-19]+d[-18]+d[-17]+d[-16]+d[-15]+d[-14]
'better'
>>> d[-7]+d[-6]+d[-5]+d[-4]+d[-3]+d[-2]+d[-1]
'complex'
>>> d[-29]+d[-28]+d[-27]+d[-26]+d[-25]+d[-24]
'simple'
>>> 