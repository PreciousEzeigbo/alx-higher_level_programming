No writing of codes:

0. Who am I?
mandatory

What function would you use to get the type of an object?

Write the name of the function in the file, without ().

1. Where are you?
mandatory

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
mandatory

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100


3. Right count =
mandatory

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89


4. Right count =
mandatory

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a


5. Right count =+
mandatory

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1


6. Is equal
mandatory

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)


7. Is the same
mandatory

What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)


8. Is really equal
mandatory

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)


9. Is really the same
mandatory

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)


10. And with a list, is it equal
mandatory

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)


11. And with a list, is it the same
mandatory

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)


12. And with a list, is it really equal
mandatory

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)


13. And with a list, is it really the same
mandatory

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)


14. List append
mandatory

What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)


15. List add
mandatory

What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)


16. Integer incrementation
mandatory

What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
17. List incrementation
mandatory

What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)


18. List assignation
mandatory

What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


19. Copy a list object
mandatory

Write a function def copy_list(l): that returns a copy of a list.

    The input list can contain any type of objects
    Your file should be maximum 3-line long (no documentation needed)
    You are not allowed to import any module

guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 

20. Tuple or not?
mandatory

a = ()

Is a a tuple? Answer with Yes or No.

21. Tuple or not?
mandatory

a = (1, 2)

Is a a tuple? Answer with Yes or No.

22. Tuple or not?
mandatory

a = (1)

Is a a tuple? Answer with Yes or No.

23. Tuple or not?
mandatory

a = (1, )

Is a a tuple? Answer with Yes or No.

24. Who I am?
mandatory

What does this script print?

a = (1)
b = (1)
a is b


25. Tuple or not
mandatory

What does this script print?

a = (1, 2)
b = (1, 2)
a is b


26. Empty is not empty
mandatory

What does this script print?

a = ()
b = ()
a is b


27. Still the same?
mandatory

>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?
mandatory

>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

Will the last line of this script print 139926795932424? Answer with Yes or No.

29. #pythonic
#advanced

Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

    Format: see example
    Your file should be maximum 4-line long (no documentation needed)
    You are not allowed to import any module

guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 

30. Low memory cost
#advanced

Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

    You are not allowed to import any module

guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 

31. int 1/3
#advanced

julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 

Assuming we are using a CPython implementation of Python3 with default options/configuration:

    How many int objects are created by the execution of the first line of the script? (103-line1.txt)
    How many int objects are created by the execution of the second line of the script (103-line2.txt)


32. int 2/3
#advanced

julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 

Assuming we are using a CPython implementation of Python3 with default options/configuration:

    How many int objects are created by the execution of the first line of the script? (104-line1.txt)
    How many int objects are created by the execution of the second line of the script (104-line2.txt)
    After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
    After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
    How many int objects are created by the execution of the last line of the script (104-line5.txt)


33. int 3/3
#advanced

julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 

34. Clear strings
#advanced

guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$ 

