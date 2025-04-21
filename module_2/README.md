## Module 2.1


### IMG Programe
#### Built-in F() in Python
``
//  Python 3.8 comes with 69 built-in functions.
https://docs.python.org/3/library/functions.html
``


#### sep and end ka concept
```
// 1) code
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

// Output
My_name_is*Monty*Python.*



// 2) code
print("Programming","Essentials","in",sep="***",end="...")
print("Python")

// Output
Programming***Essentials***in...Python
```



Quicz of 2.1.15 
```
// 1)
print("My\nname\nis\nBond.", end=" ")
print("James Bond.")

// output
My
name
is
Bond. James Bond.




// 2)
print(sep="&", "fish", "chips")


// output  error
  File "main.py", line 1
    print(sep="&", "fish", "chips")
                  ^
SyntaxError: positional argument follows keyword argument




// 3)

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')


// output

  File "main.py", line 5
    print('"Greg's book."')
                 ^
SyntaxError: invalid syntax


// Line 5 will raise SyntaxError, because the ' symbol in the Greg's book. string requires an escape character.
```




## Module 2.2

### IMG Programme
```
//1) code inwhich we use scientific notation that is 'E' or 'e'. 
print(3E8)

// output
300000000.0



// 2) code 
print(6.62607*(10)**-34)   //  that means 6.62607 x 10^34

// output
6.62607e-34


// 3) print(11e7)
// output :-  110000000.0


// code 4) 
print(0.0000000000000000000001)

// output
1e-22
```

### strings 
```
1)
print("I like \"Monty Python\"")

// output
I like "Monty Python"



print('I like "Monty Python"')   // here do not need to escape but this code is also working.

// output :-
I like "Monty Python"

```


### Boolean
```
// question
print(True > False)
print(True < False)

// output :-
True
False
```






### 📘 Python Literals and Number Systems  

#### 🔹 What is a Literal?

A **literal** is a fixed value written directly in the code.  
It represents data like numbers, strings, or boolean values that **do not change**.  
Literals are the most basic building blocks in any Python program.

---

##### 📌 Python Literals Table

| **Type**                | **Description**                                                                | **Example**                             |
|-------------------------|--------------------------------------------------------------------------------|-----------------------------------------|
| Numeric Literal         | Fixed numbers without quotes                                                   | `123`, `-5`                              |
| String Literal          | Text enclosed in quotes                                                        | `"Hello"`, `'Python'`                   |
| Binary Number           | Base-2 numbers (uses `0b` prefix)                                              | `0b1010` → `10`                          |
| Octal Number            | Base-8 numbers (uses `0o` prefix)                                              | `0o10` → `8`                             |
| Hexadecimal Number      | Base-16 numbers (uses `0x` prefix, includes A-F)                               | `0x1A` → `26`                            |
| Integer (int)           | Whole number, no decimal part                                                  | `256`, `-1`                              |
| Float (floating-point)  | Number with a decimal/fractional part                                          | `1.27`, `-3.14`                          |
| String with Apostrophe  | Use escape character or opposite quotes                                        | `'I\'m happy.'`, `"I'm happy."`         |
| String with Quotes      | Wrap double quotes in single quotes                                            | `'He said "Python"'`                    |
| Boolean                 | Represents truth values                                                        | `True`, `False`                         |
| Boolean as Number       | `True` is `1`, `False` is `0`                                                  | `int(True)` → `1`, `int(False)` → `0`   |
| None Literal            | Represents absence of value (`NoneType`)                                       | `value = None`                          |

---

> ✅ This table summarizes the **common types of literals** in Python, along with clear examples for quick understanding.





### Quize of 2.2.8
```

Question 1: What types of literals are the following two examples?
"Hello ", "007"

// output
They're both strings/string literals.


Question 2: What types of literals are the following four examples?
"1.5", 2.0, 528, False

// output
The first is a string, the second is a numerical literal (a float), the third is a numerical literal (an integer), and the fourth is a boolean literal.


Question 3: What is the decimal value of the following binary number?
1011
// output
It's 11, because (2**0) + (2**1) + (2**3) = 11

```

### oprator 2.3

```

1) 
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)



// output
8
8.0
8.0
8.0

Note :-
Remember: It's possible to formulate the following rules based on this result:

when both ** arguments are integers, the result is an integer, too;
when at least one ** argument is a float, the result is a float, too.
This is an important distinction to remember.





2)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


// output
2.0
2.0
2.0
2.0


3)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

// output
2
2.0
2.0
2.0





4)
print(6 // 4)
print(6. // 4)


// output
1
1.0

5) verry important
print(-6 // 4)
print(6. // -4)

// output
-2
-2.0



Note :-
Note: some of the values are negative. This will obviously affect the result. But how?
The result is two negative twos. The real (not rounded) result is -1.5 in both cases. However, the results are the subjects of rounding. The rounding goes toward the lesser integer value, and the lesser integer value is -2, hence: -2 and -2.0.





6)
print(12 % 4.5)


//output
3.0

because
3.0 – not 3 but 3.0. The rule still works:

12 // 4.5 gives 2.0,
2.0 * 4.5 gives 9.0,
12 - 9.0 gives 3.0.



7)
0%0

output :-
error

8)
1%0

output :-
error


```



### Imp concept

```
1)
print(9 % 6 % 2)

// output
1

Note :-
The result should be 1. This operator has left-sided binding.


2)
print(2 ** 2 ** 3)

// outtput
256

The result clearly shows that the exponentiation operator uses right-sided binding.



3)
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

// output
-9
-8
-9


4) img

print(2 * 3 % 5)

// output
1
```




### ⚙️ Python Operators (Truncated List - Basic Overview)

> Operators are **symbols** used to perform operations on variables and values.  
> Below is a **partial list** of Python operators, ordered by **priority (precedence)** — from **highest (1)** to **lowest (4)**.

| **Priority** | **Operator**  | **Type**         | **Description**                                    | **Example**                   |
|--------------|---------------|------------------|----------------------------------------------------|-------------------------------|
| 1 (Highest)  | `**`          | Arithmetic       | Exponentiation                                     | `2 ** 3` → `8`                |
| 2            | `+`, `-`      | Unary Arithmetic | Unary plus and minus (sign operators)             | `+5`, `-10`                   |
| 3            | `*`, `/`, `%` | Arithmetic       | Multiplication, Division, Modulus                  | `4 * 2` → `8`, `10 % 3` → `1` |
| 4 (Lowest)   | `+`, `-`      | Arithmetic       | Binary Addition, Subtraction                       | `5 + 3` → `8`, `7 - 2` → `5`  |

---

#### 🔹 Notes:
- **Unary operators** like `+` and `-` apply to a single value (e.g., `-x`).
- **Binary operators** like `+`, `-`, `*`, `/` apply between two values.
- Operators listed earlier in the table have **higher precedence** and are evaluated **first**.
- The precedence affects how complex expressions are evaluated without parentheses.

---

📘 **We will expand this table** as you learn more operators like comparison (`>`, `<`), logical (`and`, `or`), assignment (`=`, `+=`), etc.








### 📘 Section 2.3.4 – Python Operators Summary

#### ✅ Key Takeaways Table

| **#** | **Concept**               | **Explanation**                                                                                   | **Example**                                |
|------:|---------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1    | **Expression**             | A combination of values, variables, and operators that evaluates to a result.                     | `1 + 2` → `3`                               |
| 2    | **Operator**               | Special symbols that perform operations on values.                                                | `x * y` → Multiplies `x` and `y`           |
| 3    | **Arithmetic Operators**   | `+`, `-`, `*`, `/`, `%`, `**`, `//`                                                               | See below                                  |
|      | `+`                        | Addition                                                                                          | `3 + 2` → `5`                               |
|      | `-`                        | Subtraction                                                                                       | `5 - 3` → `2`                               |
|      | `*`                        | Multiplication                                                                                    | `4 * 2` → `8`                               |
|      | `/`                        | Division (always returns float)                                                                   | `5 / 2` → `2.5`                             |
|      | `%`                        | Modulus (remainder)                                                                               | `5 % 2` → `1`                               |
|      | `**`                       | Exponentiation (power)                                                                            | `2 ** 3` → `8`                              |
|      | `//`                       | Floor division (rounds down to nearest whole number)                                              | `3 // 2.0` → `1.0`                          |
| 4    | **Unary Operator**         | Operates on **one** operand                                                                       | `-1`, `+3`                                  |
| 5    | **Binary Operator**        | Operates on **two** operands                                                                      | `4 + 5`, `12 % 5`                           |
| 6    | **Operator Precedence**    | Order of operation execution from **highest** to **lowest**                                       | See next row                               |
|      | `**`                       | Exponentiation (highest)                                                                          | `2 ** 3` → `8`                              |
|      | `+`, `-` (unary)           | Unary sign                                                                                         | `-2`, `+3`, `4 ** -1` → `0.25`              |
|      | `*`, `/`, `%`              | Multiplication, Division, Modulus                                                                 | `10 / 2`, `6 % 4`                           |
|      | `+`, `-` (binary)          | Addition, Subtraction (lowest)                                                                    | `4 + 2`, `5 - 1`                            |
| 7    | **Parentheses**            | Subexpressions in parentheses are always calculated **first**                                     | `15 - 1 * (5 * (1 + 2))` → `0`              |
| 8    | **Right-Side Binding**     | `**` binds **right-to-left**                                                                      | `2 ** 2 ** 3` → `2 ** (2 ** 3)` → `256`     |









### Quize of 

```
1)
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

// output
-0.5 0.5 0 -1

2)
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
// output
-2 2 512




```


## Python Variable Naming Rules

| Rule No. | Rule Description                                                                 |
|----------|----------------------------------------------------------------------------------|
| 1        | Can contain **letters (A-Z, a-z)**, **digits (0-9)**, and **underscores (_) only**. |
| 2        | Must **begin with a letter** or underscore (`_`). Cannot start with a digit.     |
| 3        | **Underscore (`_`) is considered a letter** in Python.                          |
| 4        | Variable names are **case-sensitive** (`name` and `Name` are different).         |
| 5        | Cannot use **Python reserved keywords** (e.g., `if`, `for`, `while`, `class`).   |
| 6        | No limit on length, but use **meaningful and concise names** for readability.    |

> ✅ Valid Example: `user_name`, `UserAge1`, `_privateVar`  
> ❌ Invalid Example: `1name`, `for`, `user-name`

_Note: These rules also apply to function names._





### img concept
```
Toh confusion sirf itna hai:
a / 2 * b → left to right → answer is 9.0
a /= 2 * b → first 2 * b, then divide → answer is 1.0
Tu ekdum sahi soch raha hai — bas assignment wale case mein expression pehle evaluate hota hai.
```





### module final 2  Python Quiz Questions and Answers

| Question No. | Question                                                                                       | Answer             |
|--------------|------------------------------------------------------------------------------------------------|--------------------|
| 1            | The `\n` digraph forces the print() function to:                                                 | break the output line |
| 2            | The meaning of the keyword parameter is determined by:                                          | the argument's name specified along with its value |
| 3            | The value twenty point twelve times ten raised to the power of eight should be written as:       | 20.12E8            |
| 4            | The 0o prefix means that the number after it is denoted as:                                     | octal              |
| 5            | The ** operator:                                                                                | performs exponentiation |
| 6            | The result of the following division: 1 / 1                                                     | is equal to 1.0    |
| 7            | Which of the following statements are true? (Select two answers)                                | The ** operator uses right-sided binding, The right argument of the % operator cannot be zero |
| 8            | Left-sided binding determines that the result of the following expression: 1 // 2 * 3          | is equal to 0      |
| 9            | Which of the following variable names are illegal? (Select two answers)                         | True, and          |
| 10           | The print() function can output values of:                                                      | any number of arguments (including zero) |
| 11           | What is the output of the following snippet?                                                     | 24                 |
| 12           | What is the output of the following snippet if the user enters two lines containing 2 and 4?    | 24                 |
| 13           | What is the output of the following snippet if the user enters two lines containing 2 and 4?    | 8.0                |
| 14           | What is the output of the following snippet?                                                     | the code will cause a runtime error |
| 15           | What is the output of the following snippet?                                                     | 1                   |
| 16           | What is the output of the following snippet if the user enters two lines containing 3 and 6?    | 333333             |
| 17           | What is the output of the following snippet?                                                     | 1*1*1               |
| 18           | What is the output of the following snippet?                                                     | the snippet will cause an execution error |
| 19           | What is the output of the following snippet?                                                     | 17.5               |
| 20           | What is the output of the following snippet if the user enters two lines containing 2 and 4?    | 6                   |

---

### Operator Precedence in Python

Operator precedence determines the order in which operations are performed in an expression. The operators with higher precedence are evaluated first. Here's a basic order:

1. **Exponentiation (`**`)**
2. **Unary + and - (positive and negative)**
3. **Multiplication, Division, Floor division, Modulus (`*`, `/`, `//`, `%`)**
4. **Addition and Subtraction (`+`, `-`)**
5. **Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)**
6. **Logical operators (`and`, `or`)**

### Example:

```python
x = 2 + 3 * 4 ** 2 // 3  # Order of operations is important
