Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("set operations")
set operations
s1={1,2,3,4}
s2={6,3,5,8.9}
print("union")
union
s1.union(s2)
{1, 2, 3, 4, 5, 6, 8.9}
s2.intersection(s1)
{3}
s2.union(s1)
{1, 2, 3, 4, 5, 6, 8.9}
s1.intersection(s2)
{3}
s1.difference(s2)
{1, 2, 4}
s2.difference(s1)
{8.9, 5, 6}

#SET OPERATIONS
s1.add(10)
print(s1)
{1, 2, 3, 4, 10}
s2.add(5.3)
print(s2)
{3, 5.3, 5, 6, 8.9}
s1.update({4.2,7})
print(s1)
{1, 2, 3, 4, 4.2, 7, 10}
s2.add(4,9)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s2.add(4,9)
TypeError: set.add() takes exactly one argument (2 given)
s2.add(5)
print(s2)
{3, 5.3, 5, 6, 8.9}
