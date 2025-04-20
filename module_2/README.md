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





