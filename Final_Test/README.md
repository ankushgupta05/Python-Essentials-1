# Python Programming Questions and Answers

This document contains questions related to Python programming, their answers, and explanations where applicable.

---

| **Question No** | **Question** | **Answer** | **Explanation** |
|-----------------|--------------|------------|-----------------|
| **1** | What is the output of the following snippet? <br> ```python my_list = [1, 2] <br> for v in range(2): <br> my_list.insert(-1, my_list[v]) <br> print(my_list) ``` | **[1, 2, 1, 2]** | In the loop, values of `my_list[0]` and `my_list[1]` (i.e., `1` and `2`) are inserted at the second-to-last position (`-1`). |
| **2** | The meaning of a positional argument is determined by: | **its position within the argument list** | Positional arguments are matched with parameters in the order they are passed in the function call. |
| **3** | Which of the following sentences are true about the code? (Select two answers) <br> ```python nums = [1, 2, 3] <br> vals = nums ``` | **nums and vals are different names of the same list** <br> **nums has the same length as vals** | Both `nums` and `vals` refer to the same list, so they have the same length. |
| **4** | An operator able to check whether two values are not equal is coded as: | **!=** | `!=` is the inequality operator in Python. |
| **5** | The following snippet: <br> ```python def function_1(a): <br> return None <br> def function_2(a): <br> return function_1(a) * function_1(a) <br> print(function_2(2)) ``` | **will cause a runtime error** | `function_1` returns `None`, and multiplying `None` by `None` will cause a `TypeError`. |
| **6** | The result of the following division: <br> `1 // 2` | **is equal to 0** | Integer division `//` returns the quotient, discarding the remainder. |
| **7** | The following snippet: <br> ```python def func(a, b): <br> return b ** a <br> print(func(b=2, 2)) ``` | **is erroneous** | The code incorrectly uses keyword arguments before positional ones. |
| **8** | What value will be assigned to the x variable? <br> ```python z = 0 <br> y = 10 <br> x = y < z and z > y or y < z and z < y ``` | **False** | The expression evaluates as `False` because both `y < z` and `z > y` are false. |
| **9** | Which of the following variable names are illegal and will cause the SyntaxError exception? (Select two answers) | **In**, **in** | `in` is a reserved keyword in Python. |
| **10** | What is the output of the following snippet? <br> ```python my_list = [x * x for x in range(5)] <br> def fun(lst): <br> del lst[lst[2]] <br> return lst <br> print(fun(my_list)) ``` | **[0, 1, 4, 9]** | The function deletes the element at index 4 (the value of `lst[2]`), so the list becomes `[0, 1, 4, 9]`. |
| **11** | What is the output of the following piece of code? <br> ```python x = 1 <br> y = 2 <br> x, y, z = x, x, y <br> z, y, z = x, y, z <br> print(x, y, z) ``` | **1 2 1** | The values of `x`, `y`, and `z` are assigned based on the tuple unpacking. |
| **12** | What will be the output of the following snippet? <br> ```python a = 1 <br> b = 0 <br> a = a ^ b <br> b = a ^ b <br> a = a ^ b <br> print(a, b) ``` | **1 0** | This code swaps the values of `a` and `b` using the XOR operator. |
| **13** | What is the output of the following snippet? <br> ```python def fun(x): <br> if x % 2 == 0: <br> return 1 <br> else: <br> return 2 <br> print(fun(fun(2))) ``` | **2** | `fun(2)` returns `1`, and then `fun(1)` returns `2`. |
| **14** | Take a look at the snippet and choose the true statement: <br> ```python nums = [1, 2, 3] <br> vals = nums <br> del vals[:] ``` | **nums is longer than vals** | The statement `del vals[:]` removes all elements from `vals`, so `nums` is empty, but `vals` becomes an empty list as well. |
| **15** | What is the output of the following piece of code if the user enters two lines containing 3 and 2 respectively? <br> ```python x = int(input()) <br> y = int(input()) <br> x = x % y <br> x = x % y <br> y = y % x <br> print(y) ``` | **1** | The modulo operations yield `x = 1` and `y = 1`. |
| **16** | What is the output of the following piece of code if the user enters two lines containing 3 and 6 respectively? <br> ```python y = input() <br> x = input() <br> print(x + y) ``` | **36** | The `input()` function returns strings, so concatenating `"3"` and `"6"` results in `"36"`. |
| **17** | What is the output of the following piece of code? <br> ```python print("a", "b", "c", sep="sep") ``` | **asepbsepc** | The `sep` argument separates the printed values with the specified string, so it prints `asepbsepc`. |
| **18** | What is the output of the following piece of code? <br> ```python x = 1 // 5 + 1 / 5 <br> print(x) ``` | **0.2** | The result is calculated as integer division `1 // 5` yielding `0`, and `1 / 5` yielding `0.2`. |
| **19** | Assuming that `my_tuple` is a correctly created tuple, the fact that tuples are immutable means that the following instruction: <br> ```python my_tuple[1] = my_tuple[1] + my_tuple[0] ``` | **is illegal** | Tuples are immutable, so you cannot change their elements after they are created. |
| **20** | What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively? <br> ```python x = float(input()) <br> y = float(input()) <br> print(y ** (1 / x)) ``` | **2.0** | The expression calculates the square root of 4, which results in 2.0. |

---

### Continue for the remaining questions...
