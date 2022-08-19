Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("SIMPLE IF STATEMENTS")
SIMPLE IF STATEMENTS
a=5.3
if a==5.3 :
    print("a =",a)

a = 5.3

name"durga prasanna"
SyntaxError: invalid syntax
name= "durga prasanna"
if name==type(str)
SyntaxError: expected ':'

if name == "durga"
SyntaxError: expected ':'

if name == "durga" :
    print("name is equal to durga")

x=9
if type(x)==int:
    print("X is integer:",x)

X is integer: 9

print("IF -ELSE")
IF -ELSE

N=10
if N == 0
SyntaxError: expected ':'
if N == 0:
    print(N,"is equal to 0")
else: #if , if stment is false then execute else
    print(N,"is not equal to 0")

10 is not equal to 0

print("NESTED IF")
NESTED IF
mom=3
if type(mom)==int:
    if mom==3:
        print("mom value is 3")
    else:
        print("mom value is not 3")
else:
    print("mom is not integer")

mom value is 3

#ex 2
#printing largest among 3 NUMBERS
j=int(input("enter 1st value:"))
enter 1st value:6
h=int(input("enter 2nd value:"))
enter 2nd value:5
v=int(input("enter 3rd value:"))
enter 3rd value:8
if j>h:
    if j>v:
    
        print(j,"j is bigger")
    else:
        print(v,"v is bigger")
else:
    if h>v:
        print(h,"h is bigger")
    else:
        print(v,"v is bigger")

8 v is bigger

# if with ELIF
# CHECKING WHETHER GIVEN NUMBER IS 0 OR +VE OR -VE
f=int(input("enter a value to check:"))
enter a value to check:23
if f == 0:
    print(f,"is equal to 0")
elif f > 0:
    print(f,"is positive number")
else:
    print(f,"is negative number")

23 is positive number

#chek greast among 3 using if with elif
#ex 3
a=8
b=9.4
c=3
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

9.4

#method 2
e=8
k=3
l=22
max=e
if e>max:
    max=b
if c>max:
    
SyntaxError: invalid syntax
if k>max:
    max=c
print(max)
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

#method 2
e=4
k=9
l=23
max=e
if k>max:
    max=k
if l>max:
    
SyntaxError: invalid syntax
a=4
b=9
c=7
max=a
if b>max:
    max=b
if c>max:
    
SyntaxError: invalid syntax

#accesinf element using loop of list
li=[4.6,8,9,10]
for i in range(len(li)):
    print(i,li[i])

0 4.6
1 8
2 9
3 10

#printing n numbers
for i in range(10)
SyntaxError: expected ':'
for i in range(10):
    print(i)

0
1
2
3
4
5
6
7
8
9

#method 2 with step
for i in range(0,20,4):
    print(i)

0
4
8
12
16

#method 3
for i in range(,10,3):
    
SyntaxError: expected ':'
for i in range(1,10,2):
    print(i)

1
3
5
7
9
