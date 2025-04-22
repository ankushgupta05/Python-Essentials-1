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
| **7** | Which of the following lines correctly invoke the function defined below? (Select two answers) <br> ```python def fun(a, b, c=0): <br> # Body of the function.``` | **fun(b=0, a=0)** <br> **fun(0, 1, 2)** | The function can be invoked using both positional and keyword arguments. |
| **8** | What value will be assigned to the x variable? <br> ```python z = 0 <br> y = 10 <br> x = y < z and z > y or y < z and z < y ``` | **False** | The expression evaluates as `False` because both `y < z` and `z > y` are false. |
| **9** | Which of the following variable names are illegal and will cause the SyntaxError exception? (Select two answers) | **In**, **in** | `in` is a reserved keyword in Python. |
| **10** | What is the output of the following piece of code? <br> ```python my_list = [x * x for x in range(5)] <br> def fun(lst): <br> del lst[lst[2]] <br> return lst <br> print(fun(my_list)) ``` | **[0, 1, 4, 9]** | The function deletes the element at index 4 (the value of `lst[2]`), so the list becomes `[0, 1, 4, 9]`. |
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
| **21** | What is the output of the following code? <br> ```python dct = {'one': 'two', 'three': 'one', 'two': 'three'} <br> v = dct['three'] <br> for k in range(len(dct)): <br> v = dct[v] <br> print(v) ``` | **one** | Starting with `v = dct['three']` (which is 'one'), the loop updates `v` to 'two', then 'one', so the final output is `one`. |
| **22** | How many elements does the lst list contain? <br> ```python lst = [i for i in range(-1, -2)] ``` | **zero** | The range `-1, -2` produces no values, so the list is empty. |
| **23** | Which of the following lines correctly invoke the function defined below? (Select two answers) <br> ```python def fun(a, b, c=0): <br> # Body of the function.``` | **fun(b=0, a=0)** <br> **fun(0, 1, 2)** | The function can be invoked using both positional and keyword arguments. |
| **24** | What is the output of the following snippet? <br> ```python def fun(x, y): <br> if x == y: <br> return x <br> else: <br> return fun(x, y-1) <br> print(fun(0, 3)) ``` | **2** | The recursion keeps reducing `y` until `x == y`. |
| **25** | How many stars (*) will the following snippet send to the console? <br> ```python i = 0 <br> while i < 3: <br>     print("*") <br>     i += 1 ``` | **3** | The loop will print `*` three times, as `i` will range from `0` to `2`. |

---

### Continue for the remaining questions...











# Python Programming Questions and Answers (Continued)

This document contains additional Python programming questions, their answers, and explanations where applicable.

---

| **Question No** | **Question** | **Answer** | **Explanation** |
|-----------------|--------------|------------|-----------------|
| **26** | What is the output of the following snippet? <br> ```python tup = (1, 2, 4, 8) <br> tup = tup[-2:-1] <br> tup = tup[-1] <br> print(tup) ``` | **4** | The slice `tup[-2:-1]` creates a tuple `(4,)`, and `tup[-1]` extracts `4` from it. |
| **27** | What is the output of the following snippet? <br> ```python dd = {"1": "0", "0": "1"} <br> for x in dd.vals(): <br> print(x, end="") ``` | **the code is erroneous (the dict object has no vals() method)** | Python dictionaries have a `values()` method, not `vals()`, so this will raise an error. |
| **28** | What is the output of the following snippet? <br> ```python dct = {} <br> dct['1'] = (1, 2) <br> dct['2'] = (2, 1) <br> for x in dct.keys(): <br> print(dct[x][1], end="") ``` | **21** | The code prints the second element of each tuple in the dictionary: `dct['1'][1]` and `dct['2'][1]`, which are `2` and `1` respectively. |
| **29** | What is the output of the following snippet? <br> ```python def fun(inp=2, out=3): <br> return inp * out <br> print(fun(out=2)) ``` | **4** | The function is called with `out=2`, and the default value of `inp=2` is used. The result is `2 * 2 = 4`. |
| **30** | How many hashes (#) will the following snippet send to the console? <br> ```python lst = [[x for x in range(3)] for y in range(3)] <br> for r in range(3): <br> for c in range(3): <br> if lst[r][c] % 2 != 0: <br> print("#") ``` | **six** | The `if` condition checks for odd numbers, and there are six odd numbers in the list. |
| **31** | What is the output of the following code if the user enters a 0? <br> ```python try: <br> value = input("Enter a value: ") <br> print(int(value)/len(value)) <br> except ValueError: <br> print("Bad input...") <br> except ZeroDivisionError: <br> print("Very bad input...") <br> except TypeError: <br> print("Very very bad input...") <br> except: <br> print("Booo!") ``` | **Very bad input...** | Dividing by the length of `value` when the input is "0" causes a `ZeroDivisionError`. |
| **32** | What is the expected behavior of the following program? <br> ```python try: <br> print(5/0) <br> break <br> except: <br> print("Sorry, something went wrong...") <br> except (ValueError, ZeroDivisionError): <br> print("Too bad...") ``` | **The program will cause a ZeroDivisionError exception and output the following message: Too bad...** | The program attempts to divide by zero, causing `ZeroDivisionError`, and the `except` block for that exception will handle it. |
| **33** | What is the expected behavior of the following program? <br> ```python foo = (1, 2, 3) <br> foo.index(0) ``` | **The program will cause a ValueError exception.** | The `index` method will raise a `ValueError` because `0` is not in the tuple. |
| **34** | Which of the following snippets shows the correct way of handling multiple exceptions in a single except clause? <br> ```python # A: <br> except (TypeError, ValueError, ZeroDivisionError): <br> # Some code. <br> # B: <br> except TypeError, ValueError, ZeroDivisionError: <br> # Some code. <br> # C: <br> except: (TypeError, ValueError, ZeroDivisionError) <br> # Some code. <br> # D: <br> except: TypeError, ValueError, ZeroDivisionError <br> # Some code. <br> # E: <br> except (TypeError, ValueError, ZeroDivisionError) <br> # Some code. <br> # F: <br> except TypeError, ValueError, ZeroDivisionError <br> # Some code. ``` | **A only** | `A` correctly handles multiple exceptions by specifying them in a tuple. |
| **35** | What will happen when you attempt to run the following code? <br> ```python print(Hello, World!) ``` | **The code will raise the SyntaxError exception.** | The string `"Hello, World!"` is not enclosed in quotes, so it will raise a `SyntaxError`. |

---

This concludes the table of Python programming questions, answers, and explanations.

Feel free to modify or use this file as needed in your projects!

