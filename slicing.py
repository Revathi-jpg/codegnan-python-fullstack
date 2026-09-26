Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> b="work hard until you succeed"
>>> b[10:15]
'until'
>>> b[5:9]
'hard'
>>> b[0:4]
'work'
>>> b[16:19]
'you'
>>> b[20:26]
'succee'
>>> b[20:27]
'succeed'
>>> c="time is very precious"
>>> c[13:21]
'precious'
>>> c[8:12]
'very'
>>> c[0:4]
'time'
>>> c[5:7]
'is'
>>> a="I love python"
>>> a[-12:-8]
' lov'
>>> a[-12:-9]
' lo'
>>> a[-12:-7]
' love'
>>> a[-7:]
' python'
>>> b="today is weekend"
>>> b[-17:-12]
'toda'
>>> b[-17:-11]
'today'
>>> b[-12:-9]
'y i'
>>> b[-11:-8]
' is'
>>> b[-8:]
' weekend'
>>> b[-7:]
'weekend'
>>> 