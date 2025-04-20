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

```






