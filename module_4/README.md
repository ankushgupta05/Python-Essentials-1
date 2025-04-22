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




6)
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # Write your code here.
    print('d1 : ',d1)
    print('d2 : ',d2)


// output
d1 :  {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 :  {'Mary Louis': 'A', 'Patrick White': 'C'}
d1 :  {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 :  {'Mary Louis': 'A', 'Patrick White': 'C'}



7)
colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

// output
white : (255, 255, 255)
grey : (128, 128, 128)
red : (255, 0, 0)
green : (0, 128, 0)


```


### Exception in python
```
1)
try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")

Very bad input...



2)
value = input("Enter a value: ")
print(10/value)

// output
TypeError


```





# Questions, Answers, and Explanations

| **Question** | **Code** | **Answer** | **Explanation** |
|--------------|----------|------------|-----------------|
| **1) Which one of the following lines properly starts a parameterless function definition?** | ```python def fun(): ``` | `def fun():` | This is the correct syntax for defining a function without parameters. |
| **2) A function defined in the following way: `def function(x=0): return x`. May be invoked with exactly one argument or may be invoked without any argument.** | ```python def function(x=0): return x ``` | `may be invoked with exactly one argument, may be invoked without any argument` | The function has a default value for 'x', so it can be called with or without an argument. |
| **3) A built-in function is a function which:** | ```python # have not code ``` | `comes with Python, and is an integral part of Python` | A built-in function is part of Python and doesn't need to be imported. |
| **4) The fact that tuples belong to sequence types means that:** | ```python # have not code ``` | `they can be indexed and sliced like lists` | Tuples can be indexed and sliced like lists, but they are immutable. |
| **5) What is the output of the following snippet?** | ```python def f(x): if x == 0: return 0 return x + f(x - 1) print(f(3)) ``` | `6` | The function calculates the sum of numbers from 3 to 0, resulting in 6. |
| **6) What is the output of the following snippet?** | ```python def fun(x): x += 1 return x x = 2 x = fun(x + 1) print(x) ``` | `5` | The function increments 'x', and the final value of 'x' is 5. |
| **7) What code would you insert instead of the comment to obtain the expected output?** | ```python dictionary = {} my_list = ['a', 'b', 'c', 'd'] for i in range(len(my_list) - 1): dictionary[my_list[i]] = (my_list[i], ) for i in sorted(dictionary.keys()): k = dictionary[i] # Insert your code here. ``` | `print(k[0])` | You need to print the first element of the tuple in the dictionary. |
| **8) The following snippet is erroneous:** | ```python def func(a, b): return a ** a print(func(2)) ``` | `is erroneous` | The function requires two arguments, but only one is provided. |
| **9) The following snippet will output 16:** | ```python def func_1(a): return a ** a def func_2(a): return func_1(a) * func_1(a) print(func_2(2)) ``` | `16` | The function calculates 2 raised to the power of 2 and then squares the result (4 * 4). |
| **10) Which of the following lines properly starts a function using two parameters, both with zeroed default values?** | ```python def fun(a=0, b=0): ``` | `def fun(a=0, b=0):` | This is the correct syntax for defining a function with two parameters that both have default values of 0. |
| **11) Which of the following statements are true? (Select two answers)** | ```python # have not code ``` | `The None value can be compared with variables, The None value can be assigned to variables` | None can be assigned to variables and compared with other variables in Python. |
| **12) What is the output of the following snippet?** | ```python def fun(x): if x % 2 == 0: return 1 else: return print(fun(fun(2)) + 1) ``` | `2` | The first call to 'fun(2)' returns 1, then 'fun(1)' returns None, resulting in 'None + 1' causing an error. |
| **13) What is the output of the following snippet?** | ```python def fun(x): global y y = x * x return y fun(2) print(y) ``` | `4` | The function assigns the square of 2 to the global variable 'y', which is then printed. |
| **14) What is the output of the following snippet?** | ```python def any(): print(var + 1, end='') var = 1 any() print(var) ``` | `11` | The value of 'var' is 1, so the first print statement outputs '2', followed by the second print statement outputting '1'. |
| **15) Assuming that my_tuple is a correctly created tuple, the fact that tuples are immutable means that the following instruction:** | ```python my_tuple[1] = my_tuple[1] + my_tuple[0] ``` | `is illegal` | Tuples are immutable, so you cannot modify their elements after creation. |
| **16) What is the output of the following snippet?** | ```python my_list = ['Mary', 'had', 'a', 'little', 'lamb'] def my_list(my_list): del my_list[3] my_list[3] = 'ram' print(my_list(my_list)) ``` | `['Mary', 'had', 'a', 'ram']` | The function deletes the item at index 3 and replaces it with 'ram'. |
| **17) What is the output of the following snippet?** | ```python def fun(x, y, z): return x + 2 * y + 3 * z print(fun(0, z=1, y=3)) ``` | `9` | The function evaluates the expression `x + 2 * y + 3 * z` with the given arguments. |
| **18) What is the output of the following code?** | ```python dictionary = {'one': 'two', 'three': 'one', 'two': 'three'} v = dictionary['one'] for k in range(len(dictionary)): v = dictionary[v] print(v) ``` | `two` | The loop updates 'v' as it follows the dictionary's values and prints 'two'. |
| **19) What is the output of the following code?** | ```python tup = (1, 2, 4, 8) tup = tup[1:-1] tup = tup[0] print(tup) ``` | `2` | The tuple is sliced and the first element of the resulting tuple is assigned to 'tup'. |
| **20) What is the output of the following code?** | ```python try: value = int(input("Enter a value: ")) print(value/value) except ValueError: print("Bad input...") except ZeroDivisionError: print("Very bad input...") except: print("Booo!") ``` | `Very bad input...` | The exception handling will catch the ZeroDivisionError and print "Very bad input..." if you try dividing by zero. |

---

### Exception Handling in Python

| **Example** | **Code** | **Output** |
|-------------|----------|------------|
| **1) Handling ValueError and ZeroDivisionError** | ```python try: value = int(input("Enter a value: ")) print(value/value) except ValueError: print("Bad input...") except ZeroDivisionError: print("Very bad input...") except: print("Booo!") ``` | `Very bad input...` |
| **2) TypeError when performing unsupported operation** | ```python value = input("Enter a value: ") print(10/value) ``` | `TypeError` |










