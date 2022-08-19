Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d=[3,5,8,10,23]
j=["c","py","jaga","chelli"]
print("concatination of lists")
concatination of lists
d+j
[3, 5, 8, 10, 23, 'c', 'py', 'jaga', 'chelli']
print(j+d)
['c', 'py', 'jaga', 'chelli', 3, 5, 8, 10, 23]
print(d*3)  #repitation
[3, 5, 8, 10, 23, 3, 5, 8, 10, 23, 3, 5, 8, 10, 23]
len(d+j)
9
len(d-j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len(d-j)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
len(d)
5
len(j)
4
print("c" in j) #membership,whether the given is the list or not
True

print(4 in d)
False
 print(10 in d)
 
SyntaxError: unexpected indent
print(10 in d)
True

#APPENDING
name=[]
name.append(5.3) #add element at the end of the list
print(name)
[5.3]
print(name.append("aswini"))
None
print(name)
[5.3, 'aswini']
name.append("venky")
print(name)
[5.3, 'aswini', 'venky']

j.append("sadasiddu")
print(j)
['c', 'py', 'jaga', 'chelli', 'sadasiddu']
d.extend(4.8,22,3)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d.extend(4.8,22,3)
TypeError: list.extend() takes exactly one argument (3 given)
d.extend([4.5,8])
print(d)
[3, 5, 8, 10, 23, 4.5, 8]
j.extend(["prassu","gopi"])
print(j)
['c', 'py', 'jaga', 'chelli', 'sadasiddu', 'prassu', 'gopi']
len(j)
7
name.extend("biryani",22])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
name.extend(["biryani",22])
print(name)
[5.3, 'aswini', 'venky', 'biryani', 22]
r=name #COPING list TO ANOTHER LIST
print(r)
[5.3, 'aswini', 'venky', 'biryani', 22]

del name[4]
print(name)
[5.3, 'aswini', 'venky', 'biryani']
print(r)
[5.3, 'aswini', 'venky', 'biryani']
r.extend(["beans",9])
print(name)
[5.3, 'aswini', 'venky', 'biryani', 'beans', 9]
print(r)
[5.3, 'aswini', 'venky', 'biryani', 'beans', 9]
# IF THERE IS ANY CHANGES IN r THEN name LIST ALSO CHANGES
d.sort()
print(d)
[3, 4.5, 5, 8, 8, 10, 23]
print("SORTING LIST")
SORTING LIST

print(j)
['c', 'py', 'jaga', 'chelli', 'sadasiddu', 'prassu', 'gopi']
print(j.sort())
None
print(j)
['c', 'chelli', 'gopi', 'jaga', 'prassu', 'py', 'sadasiddu']
name.sort()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    name.sort()
TypeError: '<' not supported between instances of 'str' and 'float'

print("reversing list")
reversing list
print(d)
[3, 4.5, 5, 8, 8, 10, 23]
d.revers()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d.revers()
AttributeError: 'list' object has no attribute 'revers'. Did you mean: 'reverse'?
d.reverse()
print(d)
[23, 10, 8, 8, 5, 4.5, 3]
print(name)
[5.3, 'aswini', 'venky', 'biryani', 'beans', 9]
name.reverse()
print(name)
[9, 'beans', 'biryani', 'venky', 'aswini', 5.3]
name[3]
'venky'
name[2]
'biryani'
# reverse method reverses the list
# reverse method reverses the list
d.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
d.sort(reverse=True)
print(d)
[23, 10, 8, 8, 5, 4.5, 3]
d.sort(reverse=False)
print(d)
[3, 4.5, 5, 8, 8, 10, 23]
d.count(8)
2
j.count(4.3)
0
print(name.count("venky"))
1
