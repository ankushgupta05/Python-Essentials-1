# Python-Essentials-1






1.0 Welcome to Python Essentials 1
```
1.0.1 Learn Python – the language of today and tomorrow
1.0.2 About the course
1.0.3 Syllabus
1.0.4 Prepare for the PCEP-30-0x exam

```


1.1 Section 1 – Introduction to Programming

```
1.1.1 How does a computer program work?
1.1.2 Natural languages vs. programming languages
1.1.3 What makes a language?
1.1.4 Machine language vs. high-level language
1.1.5 Compilation vs. Interpretation
```


1.2 Section 2 – Introduction to Python
```
1.2.1 Python – a tool, not a reptile
1.2.2 Who created Python?
1.2.3 A hobby programming project
1.2.4 What makes Python so special?
1.2.5 Python rivals?
1.2.6 Where can we see Python in action?
1.2.7 Why not Python?
1.2.8 There is more than one Python
1.2.9 Python implementations
```

1.3 Section 3 – Downloading and Installing Python
```
1.3.1 Begin your Python journey
1.3.2 How to download, install, and configure Python
1.3.3 Starting your work with Python
1.3.4 Your very first program before your first program...
1.3.5 How to spoil and fix your code
```






# Note:- CPython kya hai?
 ```
CPython is the implementation of Python language — basically, it’s the actual software that runs your Python code.

CPython is written in C language, iska naam bhi isi wajah se "CPython" rakha gaya hai.

Jab aap terminal me python ya python3 likh ke code run karte ho, toh aap asal me CPython interpreter hi chala rahe hote ho.

Ye implementation Python ke rules (syntax, behavior) ko follow karta hai — jaise PSF (Python Software Foundation) ne define kiya hai.

💡 Think of CPython as the engine that powers your Python programs.
```


# Note:- Python 2
```
print "Hello World"  # No parentheses
```

# Note:- Python 3
```
print("Hello World")  # Parentheses required
```


# Note :- CPython kya hai
```
CPython is the original and official implementation of the Python programming language.
It is written in the C language and maintained by the Python Software Foundation (PSF).
Jab aap terminal me python ya python3 likhte ho, aap mostly CPython hi chala rahe hote ho.
Ye sabse stable, popular aur widely supported version hai
```



## Note :-
```
💬 Summary in One Line Each:
✅ CPython – Official and most-used Python interpreter.

🚀 Cython – Make Python code faster by compiling to C.

☕ Jython – Use Python in Java apps (runs on JVM).

⚡ PyPy – Fastest Python using Just-in-Time compiler.

🧩 MicroPython – Run Python on small hardware devices (IoT).
```





## Python Implementations Comparison

| **Implementation** | **Purpose / Use Case** | **Special Features** | **Example** |
|--------------------|------------------------|-----------------------|-------------|
| **CPython (C-language Python)** | ✅ Most commonly used and official version of Python<br>✅ Suitable for everyday development like web development, scripting, automation, etc. | 🔹 Written in C programming language<br>🔹 Maintained by Python Software Foundation (PSF)<br>🔹 Supports almost all Python libraries and tools | 📌 Basic Python usage:<br>`print("Hello from CPython")`<br>📌 Used in: Django, Flask, Jupyter, etc. |
| **Cython (C-Extension Python)** | ✅ Used to increase performance of Python code, especially useful in scientific computing, loops, data processing, and machine learning | 🔹 Converts Python code into C language for speed<br>🔹 Offers optional static typing<br>🔹 Helps write hybrid Python + C programs | 📌 Example (Cython function):<br>```cython<br>cpdef int fast_square(int x):<br>    return x * x```<br>📌 Used in: Pandas, Scikit-learn, NumPy |
| **Jython (Java Python)** | ✅ Lets you write Python code that runs on Java Virtual Machine (JVM)<br>✅ Useful when you want to integrate with Java code or use Java libraries | 🔹 Written in Java language<br>🔹 Allows Python scripts to interact with Java classes, GUIs, frameworks<br>🔹 Works well in Java-based enterprise environments | 📌 Java GUI using Python:<br>```python<br>from java.awt import Frame<br>f = Frame("Hello Jython")<br>f.setVisible(True)``` |
| **PyPy (Python Python – Just-in-Time Compiler)** | ✅ Best for CPU-heavy and performance-critical applications like games, simulations, web scraping | 🔹 Uses JIT (Just-In-Time) compiler to run Python code much faster<br>🔹 No code change needed — just use PyPy instead of Python<br>🔹 Compatible with most Python 3 code | 📌 Run script with PyPy:<br>`pypy myscript.py`<br>📌 Used for: speed optimization without code rewriting |
| **MicroPython (Microcontroller Python)** | ✅ Used in embedded systems, IoT (Internet of Things), hardware-level programming<br>✅ Runs on tiny devices like sensors, boards, microcontrollers | 🔹 Lightweight Python interpreter (very small memory footprint)<br>🔹 Works on microchips like ESP32, Raspberry Pi Pico, Arduino<br>🔹 Designed for real-time low-power devices | 📌 Control LED on ESP32:<br>```python<br>from machine import Pin<br>led = Pin(2, Pin.OUT)<br>led.value(1)```<br>📌 Used in: Smart home gadgets, Wearables, Sensors |








## ✅ What Makes a Language? – Easy Table

| **Element**       | **Meaning (Simple)**                            | **Examples** |
|-------------------|--------------------------------------------------|--------------|
| **Alphabet**       | Basic letters or symbols used to form words      | 🔤 English: A–Z<br>🔢 Programming: A–Z, 0–9, +, -, *, /, () etc. |
| **Lexis (Words)**  | Valid words from the language's dictionary       | ✅ `computer` is a word<br>❌ `cmoptrue` is not<br>✅ Python: `print`, `if` |
| **Syntax**         | Rules for writing correct sentence structure     | ✅ `print("Hello")`<br>❌ `print "Hello"` (Wrong in Python 3) |
| **Semantics**      | Logical meaning of a sentence                    | ✅ `"I ate a doughnut"`<br>❌ `"A doughnut ate me"` (Funny but illogical) |




## 🧠 Code Levels Explained (with Example)

| **Level**         | **Code Example**              | **Who Understands It**        | **Description** |
|-------------------|-------------------------------|-------------------------------|------------------|
| **High-Level Code** | `print("Hello")` (Python)     | 👩‍💻 Humans (Programmers)       | Easy to read/write. Used in Python, Java, C, etc. |
| **Assembly Code**   | `MOV AL, 61h`                 | 🧑‍🔧 Assembly Programmers       | Low-level readable commands close to machine code. |
| **Machine Code**    | `10110000 01100001`           | 🧠 CPU (Processor)             | Binary (0s and 1s) — directly executed by the computer hardware. |




## Module 1 Sabhi Vikalp Question

| **Question** | **Answer** | **Explanation** | **Example** |
|--------------|------------|-----------------|-------------|
| What do you call a command-line interpreter which lets you interact with your OS and execute Python commands and scripts? | A console | A console (or terminal) is where you type commands and interact with the system. It allows you to run Python code. | In Terminal (macOS/Linux) or Command Prompt (Windows), you type `python myscript.py` to run Python code. |
| What is CPython? | It's the default, reference implementation of Python, written in the C language | CPython is the most widely used version of Python, implemented in C, and is maintained by the Python Software Foundation (PSF). | If you install Python from python.org, you are using CPython. |
| What is the expected behavior of the following program? `print("Hello!")` | The program will output `Hello!` to the screen | The print function outputs the string to the screen. The quotation marks will not appear in the output. | Output: `Hello!` |
| What do you call a file containing a program written in a high-level programming language? | A source file | A source file is where the program code is written in a high-level language (like Python). | A Python file is a `.py` file, such as `my_program.py`. |
| What is true about compilation? (Select two answers) | The code is converted directly into machine code executable by the processor<br>It tends to be faster than interpretation | Compilation converts code into machine-readable instructions and usually results in faster execution than interpretation. | Example: `gcc program.c -o program` compiles C code into an executable. |
| What is a script? | It's a text file that contains instructions which make up a Python program | A script is a file that contains written code, typically to automate tasks or execute a sequence of instructions. | Example: A Python script named `example.py` with `print("Hello")`. |
| What is the best definition of a high-level programming language? | It's a language that allows you to write instructions in a human-readable way | High-level languages are abstracted from the hardware, making them easier to understand and use. | Python, Java, and JavaScript are high-level languages. |
| What is machine code? | It's the lowest-level code that is directly executed by the CPU | Machine code consists of binary instructions that the processor can directly execute without any further translation. | `10110000 01100001` is machine code, interpreted by the CPU. |
| What is true about interpretation? (Select two answers) | The source code is translated line by line<br>You don’t need a separate file to distribute | An interpreter runs the program directly without compiling it into machine code, translating line by line. | Example: Running `python script.py` directly without compiling. |
| What is the expected behavior of the following program? `x = 5 + 3`<br>`print(x)` | The program will output 8 to the screen | The variable `x` will store the result of `5 + 3`, and `print(x)` will output the value of `x`. | Output: `8` |



