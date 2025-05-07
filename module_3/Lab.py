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
