Q 1)
3.2.14   LAB   Essentials of the while loop
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
Test your code using the data we've provided.


Test Data:


#1
Sample input:
6
Expected output:
The height of the pyramid: 3

#2
Sample input:
20
Expected output:
The height of the pyramid: 5

#3
Sample input:
1000
Expected output:
The height of the pyramid: 44

#4
Sample input:
2
Expected output:
The height of the pyramid: 1


// code by me
blocks = int(input("Enter the number of blocks: "))

# Write your code here.
i = 1
if blocks==0:
    print(f'The height of the pyramid: {0}')
else:
    while(1):
        if (blocks // i) >= 1 :
            blocks=blocks - i
        else:
            break;
    
        i += 1

print("The height of the pyramid:", i-1)



// code by chatgpt
blocks = int(input("Enter the number of blocks: "))
height = 0
used_blocks = 0
next_layer = 1

while used_blocks + next_layer <= blocks:
    used_blocks += next_layer
    height += 1
    next_layer += 1

print("The height of the pyramid:", height)








Q 2)

3.2.15   LAB   Collatz's hypothesis
Scenario
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.
Test your code using the data we've provided.


Test Data:

#1
Sample input:
15
Expected output:
46
46
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17


#2
Sample input:
16
Expected output:
8
4
2
1
steps = 4


#3
Sample input:
1023
Expected output:
3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
173
260
130
65
196
98
49
148
74
37
37
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
steps = 62





// code by me
n = int(input())

i = 0
while(1):
    i += 1
    if (n == 1):
        break;
    elif (n%2==0):
        n = n//2
    else:
        n = 3*n + 1
    print(n)

print('steps = ',i)








Q3 )
3.5.2 Sortingby bubble sort

// code
my_list = [12,34,2,6,23]
swape = True
print(my_list)
while(swape):
    swape = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            swape = True
            my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]

print(my_list)
