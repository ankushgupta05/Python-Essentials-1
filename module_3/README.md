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












