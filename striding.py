Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> b="machine learning"
>>> a[::4]
'd e'
>>> b[::4]
'miln'
>>> b[::6]
'men'
>>> b[::2]
'mcielann'
>>> b[5:]
'ne learning'
>>> b[:9]
'machine l'
>>> a[::7}
SyntaxError: invalid syntax
>>> a[::7]
'di'
>>> b[::7]
'm n'
>>> c="cloud computing"
>>> c[2:14:4]
'ocu'
>>> c[5:13:3}
SyntaxError: invalid syntax
>>> c[15:3:3]
''
>>> c[5:13:3]
' mt'
>>> c[4:12:2]
'dcmu'
>>> d="python course"
>>> d[-1:-11:-2]
'ero o'
>>> d[-2:-12:-3]
'sont'
>>> d[8:4:2]
''
>>> d[::-1]
'esruoc nohtyp'
>>> 