## 3.1.3 Exercises – Comparison Questions

| Question # | Code Sample     | Result | Explanation |
|------------|------------------|--------|-------------|
| 1          | `2 == 2`         | `True` | Of course, 2 is equal to 2. Python will answer `True`. Remember, `True` and `False` are Python keywords. |
| 2          | `2 == 2.`        | `True` | Python is able to convert the integer value into its real (float) equivalent. So, `2 == 2.0` is `True`. |
| 3          | `1 == 2`         | `False`| This is easy. `1` is not equal to `2`, so the result is `False`. |




### imp programme
```
// question
x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

// output4
four
five

```


### img programe for loop
```
1)
for i in range(2, 8, 3):
    print("The value of i is currently", i)


// output
The value of i is currently 2
The value of i is currently 5


2)
for i in range(1, 1):
    print("The value of i is currently", i)

// Note :-
the range()'s second argument must be greater than the first.


3)
for i in range(2, 1):
    print("The value of i is currently", i)
 
// no oxecute
```


### continous and breack in python
```
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")




//output

The break instruction:
Inside the loop. 1
Inside the loop. 2
Outside the loop.

The continue instruction:
Inside the loop. 1
Inside the loop. 2
Inside the loop. 4
Inside the loop. 5
Outside the loop.
```

### else in for ,while loop
```
1)
for i in range(5):
    print(i)
else:
    print("else:", i)

// output
0
1
2
3
4
else: 4






2)
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

// output
else: 111



3)
n = range(4)
 
for num in n:
    print(num - 1)
else:
    print(num)

// output
-1
0
1
2
3


4)
for i in range(0, 6, 3):
    print(i)

//output
0
3

```



## 3.3 section
```
1)
log = i and j


// output
log: True


```




### 3.3.4 Bitwise operators

```
& (ampersand) ‒ bitwise conjunction;
| (bar) ‒ bitwise disjunction;
~ (tilde) ‒ bitwise negation;
^ (caret) ‒ bitwise exclusive or (xor).
```


### Imp Programmer
```
1)
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)


// output
17 68 8


Note:

17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)




2)
x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

//output
False



3)
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)

// output



4)
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)

// output
0 5 -5 1 1 16

// Note : explaination this answer you will get below code
```



# Bitwise Operator Example in Python

This README explains the results of various bitwise operations in Python with variables `x = 4` and `y = 1`.

## 🔢 Variable Assignments

| Variable | Operation     | Description                                                                                     | Binary Involved         | Result |
|----------|----------------|-------------------------------------------------------------------------------------------------|--------------------------|--------|
| a        | `x & y`        | Bitwise AND: Only 1 if both bits are 1.                                                         | `0100 & 0001 = 0000`     | 0      |
| b        | `x | y`        | Bitwise OR: 1 if at least one of the bits is 1.                                                 | `0100 | 0001 = 0101`     | 5      |
| c        | `~x`           | Bitwise NOT: Inverts the bits and returns `-x - 1` (two's complement).                          | `~0100 = -0101`          | -5     |
| d        | `x ^ 5`        | Bitwise XOR: 1 if bits are different.                                                           | `0100 ^ 0101 = 0001`     | 1      |
| e        | `x >> 2`       | Right shift by 2: Moves bits 2 places to the right.                                             | `0100 >> 2 = 0001`       | 1      |
| f        | `x << 2`       | Left shift by 2: Moves bits 2 places to the left.                                               | `0100 << 2 = 10000`      | 16     |

## 🧠 Explanation of Bitwise NOT (`~x`)

Python uses two's complement to represent negative numbers. For `x = 4`:

- Binary of 4: `00000100`
- Inverting bits: `11111011`
- This is `-5` in two's complement representation.

So, `~4 = -5`

## ⚙️ Operator Precedence in Python

Operator precedence determines the order in which operations are performed. Bitwise operators have lower precedence than arithmetic operators but higher than comparison operators.

### Example:
```
python
result = 5 + 2 << 1  # Equivalent to: (5 + 2) << 1
```




## python list 
```
1)
numbers = [111, 7, 2, 1]
print(numbers[-1])

// output
1


2)
numbers = [111, 7, 2, 1]
print(numbers[-2])

// output
2




3)
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append(4)

print(len(numbers))
print(numbers)
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

// output
4
[111, 7, 2, 1]
5
[111, 7, 2, 1, 4]
6
[222, 111, 7, 2, 1, 4]



4)
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

// output
[5, 4, 3, 2, 1]




5)
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
 
del my_list  # deletes the whole list

```



### img quize
```
1)
lst = []
del lst
print(lst)

// output
NameError: name 'lst' is not defined


2)
a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst)

// output
[' ', 'C', 'B', 'A']

```


### very imp programme
```
1)
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

// output
[2]



2)
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

// output
[1]



3)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

//output
[8, 6, 4]


4)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

// output
[]



5)
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

// output
[10, 4, 2]



6)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)

// output
['C']


7)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2
 
print(list_3)

// output
['B', 'C']


8)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[:]
print(list_3)

//output
[]



9)
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

// output
['A', 'B', 'C']

```




### advanced list
```
1)
squares = [x ** 2 for x in range(10)]

// output
 (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)



2)
odds = [x for x in [1,2,3,4,5,6,7,8] if x % 2 != 0 ]

// output
[1, 3, 5, 7]




Note :-
1)
List comprehension allows you to create new lists from existing ones in a concise and elegant way. The syntax of a list comprehension looks as follows:
[expression for element in list if conditional]

```



## module 3 final quize

# Programming Questions and Answers

This file contains programming questions, their answers, explanations, and relevant code snippets. Below are the questions from 0 to 20.

| **Question** | **Answer** | **Explanation** | **Code** |
|--------------|------------|-----------------|----------|
| **Q0: What operator checks if two values are equal?** | `==` | The `==` operator checks whether two values are equal. | ```python\nx = 1\ny = 1\nprint(x == y)  # True, as both are equal\n``` |
| **Q1: What will be the value assigned to x in the following code?** | `True` | The expression `x = x == x` assigns the result of `x == x`, which is `True`, to `x`. | ```python\nx = 1\nx = x == x\nprint(x)  # Output is True\n``` |
| **Q2: How many times will `*` be printed in this loop?** | `two` | The loop runs twice because `i` increments by 2 in each iteration: starting at 0, then incrementing by 2 to 2. | ```python\ni = 0\nwhile i <= 3:\n    i += 2\n    print("*")  # Prints * twice\n``` |
| **Q3: What is the output of this loop?** | `zero` | The loop breaks immediately because `i` is even (i.e., `i % 2 == 0`), so the condition `if i % 2 == 0` evaluates to `True`, triggering the `break`. | ```python\ni = 0\nwhile i <= 5:\n    i += 1\n    if i % 2 == 0:\n        break\n    print("*")  # Only prints * once\n``` |
| **Q4: How many hashes will be printed?** | `one` | The `for` loop iterates once, and the `else` block also executes after the loop completes, printing one hash. | ```python\nfor i in range(1):\n    print("#")\nelse:\n    print("#")  # One hash is printed\n``` |
| **Q5: How many hashes will this loop print?** | `three` | The loop only prints three hashes because `if var % 2 == 0` skips even numbers, and `continue` causes the loop to skip the current iteration for those numbers. | ```python\nvar = 0\nwhile var < 6:\n    var += 1\n    if var % 2 == 0:\n        continue\n    print("#")  # Three hashes will be printed\n``` |
| **Q6: How many times will `#` be printed in this loop?** | `one` | The loop runs once with the left-shift operation (`<<`), which doubles the value of `var` each time. Only the first `#` is printed before the condition `var < 10` fails. | ```python\nvar = 1\nwhile var < 10:\n    print("#")\n    var = var << 1  # Left shift doubles the value\n``` |
| **Q7: What will be the value assigned to the variable x?** | `True` | The expression `y < z and z > y or y > z and z < y` evaluates to `True` based on logical operator precedence. | ```python\nz = 10\ny = 0\nx = y < z and z > y or y > z and z < y\nprint(x)  # Output is True\n``` |
| **Q8: What is the output of the following snippet?** | `3` | The output is `my_list[my_list[-1]]` where `my_list[-1]` is `-2`. Hence, `my_list[-2]` evaluates to `-1`, resulting in the printed value of `3`. | ```python\nmy_list = [3, 1, -2]\nprint(my_list[my_list[-1]])  # Output is 3\n``` |
| **Q9: What is the output of the following snippet?** | `2` | The slice `my_list[-3:-2]` extracts a sublist starting from the third-to-last element to the second-to-last element, which is just `[2]`. | ```python\nmy_list = [1, 2, 3, 4]\nprint(my_list[-3:-2])  # Output is [2]\n``` |
| **Q10: What happens after this code is executed?** | `doesn't change the list` | The assignment swaps the first and third elements, but the length of the list remains unchanged. | ```python\nvals = [0, 1, 2]\nvals[0], vals[2] = vals[2], vals[0]\nprint(vals)  # Output is [2, 1, 0]\n``` |
| **Q11: What is the result of this operation?** | `4` | After performing the `insert(0, 1)` and `del vals[1]` operations, the list will have values `[1, 1, 2, 3]`. The sum of these elements is `4`. | ```python\nvals = [0, 1, 2]\nvals.insert(0, 1)\ndel vals[1]\nprint(sum(vals))  # Output is 4\n``` |
| **Q12: Which statement is true?** | `nums and vals refer to the same list` | Both `nums` and `vals` reference the same list. Deleting an element from `vals` will affect `nums`. | ```python\nnums = [1, 2, 3]\nvals = nums\ndel vals[1:2]\nprint(nums)  # Output is [1, 3], same as vals\n``` |
| **Q13: What is the output of this code?** | `nums is longer than vals` | After deleting an element from `vals`, `nums` still has the original length. | ```python\nnums = [1, 2, 3]\nvals = nums\ndel vals[1:2]\nprint(len(nums))  # Output is 2\nprint(len(vals))  # Output is 2\n``` |
| **Q14: What is the result of the slicing operation?** | `nums and vals are two different lists` | After slicing, `vals` is a new list, which is not the same as `nums`. | ```python\nnums = [1, 2, 3]\nvals = nums[-1:-2]\nprint(nums)  # Output is [1, 2, 3]\nprint(vals)  # Output is []\n``` |
| **Q15: What is the output of the following snippet?** | `nums and vals are two different lists` | The slicing creates a new list and `vals` is different from `nums`. | ```python\nnums = [1, 2, 3]\nvals = nums[-1:-2]\nprint(nums)  # Output is [1, 2, 3]\nprint(vals)  # Output is []\n``` |
| **Q16: What will this code output?** | `[3, 2, 1]` | The loop inserts values at the start of `my_list_2` in reverse order, resulting in the list `[3, 2, 1]`. | ```python\nmy_list_1 = [1, 2, 3]\nmy_list_2 = []\nfor v in my_list_1:\n    my_list_2.insert(0, v)\nprint(my_list_2)  # Output is [3, 2, 1]\n``` |
| **Q17: What is the output of this snippet?** | `[1, 2, 3, 1, 2, 3]` | The loop inserts values at the start of the list `my_list`, repeating the elements of `my_list_1`. | ```python\nmy_list = [1, 2, 3]\nfor v in range(len(my_list)):\n    my_list.insert(1, my_list[v])\nprint(my_list)  # Output is [1, 2, 3, 1, 2, 3]\n``` |
| **Q18: How many elements will be in `my_list` after execution?** | `three` | The list comprehension generates three values: `-1`, `0`, and `1`. | ```python\nmy_list = [i for i in range(-1, 2)]\nprint(len(my_list))  # Output is 3\n``` |
| **Q19: What is the output of the following code?** | `6` | The sum of diagonal elements in the 2D list `t` results in 6. | ```python\nt = [[3-i for i in range(3)] for j in range(3)]\ns = 0\nfor i in range(3):\n    s += t[i][i]\nprint(s)  # Output is 6\n``` |
| **Q20: What will happen when this code is executed?** | `the snippet will cause a runtime error` | The code attempts to access an out-of-bounds index `my_list[2]`, which will cause a runtime error because the list has fewer elements. | ```python\nmy_list = [1, 2]\nprint(my_list[2])  # Will raise IndexError\n``` |



