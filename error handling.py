#31/10/26
#error handling
# we 3 types---
              #1.syntax error--compile error
              #2.runtime error--during execution
              #3.logic error--error in logic(it cant be visible)


#syntax error
'''for i in range(10)
    print(i)'''#syntax error[:]

#runtime error

'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''#---->zero division error

#logical error
# in logical error the error we cant see 
'''a=10
b=20
print(a-b)'''

'''a=5
b=7
if a>b:
    print("true")'''



#Exception handling
#we have 4 types:------
                 #1.try--instructions from which we are expecting the exceptions
                 #2.except---expections are raised in try block it will be handle by this block
                 #3.else---optional--   no exceptions
                 #4.finally---always
#zero division error
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is rasied")
    else:
        print("no exception")
    finally:
        print("always excute")'''


'''while True:
    
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is rasied")
    else:
        print("no exception")
    finally:
        print("always excute")'''  

#2/11/26
#file handling


#write()
'''a=open("file.txt","w")
a.write("python course")
a.close()'''

'''a=open("file.text","w")
a.write("python full stack")
a.close()'''


#append()
'''a=open("file.txt","a")
a.write("\n revathi joined from 17 oct")
a.close()'''


'''a=input()
b=open("file.txt","a")
b.write("\n ,a")
b.close()'''


'''a=open("file.txt","w")
b=input("data")
a.write(b)
a.close()'''


#readlines()
a=open("file.txt")
#print(a.read())#it will display entire concepts
#print(a.readline())#it will display first line  
#print(a.read(10))#it will display upto char 10
#print(a.readlines())#it will display with\n




#writelines () it makes every object side by side
'''a=open("file.txt","w")
b=["revathi","radhi","neeru","bhanu"]
a.writelines("\n".join(b))
a.close()'''
'''a=open("task1.py")
print(a.read())'''

a=open(r"C:\Users\DELL\Downloads\codegnan\python\conditions.py")
print(a.read())





          
    
 
