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
```












