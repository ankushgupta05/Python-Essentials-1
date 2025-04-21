# 4.1 quize
```
1)
hi()
 
def hi():
    print("hi!")


 // output
 ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
NameError: name 'hi' is not defined

```



### img programmer
```
1)  //  while arguments passed in this way are named positional arguments.
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)



2)  //  Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")




3) //Mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)   // output :- 1 + 2 + 3 = 6
adding(c = 1, a = 2, b = 3)  // output :- 2 + 3 + 1 = 6
adding(3, c = 1, b = 2) // output :- 3 + 2 + 1 = 6
adding(3, a = 1, b = 2)  // output :- TypeError: adding() got multiple values for argument 'a'
adding(4, 3, c = 2) 













```
