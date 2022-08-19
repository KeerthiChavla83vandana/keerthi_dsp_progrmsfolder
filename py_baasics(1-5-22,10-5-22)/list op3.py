Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
j=[3,5,8,23]
D=["c","py","c#",6]
name=[]
print(type(name))
SyntaxError: multiple statements found while compiling a single statement
D=["c","py","c#",8]
name=[]
print(type(D))
<class 'list'>
print(type(name))
<class 'list'>

print("acceing list elements")
acceing list elements
# accening using INDEXING SLICING
print(j[0])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(j[0])
NameError: name 'j' is not defined
D[0]
'c'
len(j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    len(j)
NameError: name 'j' is not defined
j=[3,5,8,23]
j[ : ]
[3, 5, 8, 23]
len(j)
4
len(name)
0
name[ : ]
[]
len(D)
4
D[ :len(D)]
['c', 'py', 'c#', 8]
j[0:5]
[3, 5, 8, 23]
j[2:3]
[8]
D[-1]
8
j[-2]  #negitive indexing
8
D[-4:-1]
['c', 'py', 'c#']
D[-3:-2]
['py']
d[-4: ]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d[-4: ]
NameError: name 'd' is not defined. Did you mean: 'D'?
D[-4: ]
['c', 'py', 'c#', 8]
D[-4:]
['c', 'py', 'c#', 8]
j[1]
5
j[1]="mom"
print(j)
[3, 'mom', 8, 23]
j[2]=10 #UPDATING LIST VALUES USING INDEX
print(j)
[3, 'mom', 10, 23]
D+j
print(D+j)


