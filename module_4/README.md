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


### img quize in 4.2.7
```
1)
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)

// output :-
adding(4, 3, c = 2) 





2)
Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3


def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error


Note :- 
def add_numbers(a, b=2, c):

Isme dikkat yeh hai ki:
b=2 ke paas default value hai (yaani agar koi value na de toh bhi chalega),
par uske baad c aaya jiske paas default value nahi hai.
Python ko yeh pasand nahi — uska rule hai:
"Jinke paas value default se set nahi hai (zaroori hain), unhe pehle likho. Aur jinke paas default value hai (optional hain), unko baad mein rakho."

// sahi formate niche hai

def add_numbers(a, c, b=2):  # ✔️ sahi order
    print(a + b + c)

add_numbers(a=1, c=3)  # Output: 6


def add_numbers(a, b=2, c=3):  # ✔️ sabke paas default hai
    print(a + b + c)

add_numbers(a=1, c=4)  # Output: 7


```


### Quize in 4.4.1
```
1)
def scope_test():
    x = 123


scope_test()
print(x)


// output
NameError: name 'x' is not defined


2)
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

// output
Do I know that variable? 1
1



3)
def my_function():
    var = 2
    print("Do I know that variable?", var)
 
 
var = 1
my_function()
print(var)

// output
Do I know that variable? 2
1



4)
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

// output
Do I know that variable? 2
2



5)
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

//output
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [0, 1]
Print #4: [2, 3]
Print #5: [2, 3]



6)
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

// output
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]
```

### img programme
```
1)
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

// output
(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)



2)
tuple_1 = 1, 2, 4, 8
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

// output
(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)


3)
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


// output
9
(1, 10, 100, 1000, 10000)
(1, 10, 100, 1, 10, 100, 1, 10, 100)
True
True




4)
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
print(len(t1), len(t2), len(t3))


// output
(2,) (3, 123) (1,)
1 2 1




5)
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

// output
{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
{'boss': 5551234567, 'Suzy': 22657854310}
{}
```


















