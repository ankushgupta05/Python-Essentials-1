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



