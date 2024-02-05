# Finding-maximum-product-path-in-a-triangular-array
﻿This Python programimplements a dynamic programming-based solution to compute the maximum product path in a triangular array. 

 Other Files & Folder

Input.txt:  The input file containing the triangular array. The first line contains an integer n, representing the number of rows in the triangle. The following n lines describe the rows of the triangle.

Output.txt: The output file where the resultant maximum product (as an integer) and the sequence of numbers that achieve it from top to bottom are written.

Tests: A folder containing  Test cases ,where inputs are taken from Input1.txt,input2.txt,Input3.txt and the output is written in different output file respectively.

The program is executed with command-line arguments specifying the input files.


The recurrence relation embodied by the dynamic programming algorithm is:

d_program[i][j] = numbers[i][j] + max(d_program[i-1][j-1], d_program[i-1][j])

where,
numbers[i][j] is the value of the current element in the triangular array.
d_program[i-1][j-1] is the value of the element immediately above and to the left in the dynamic programming table.
d_program[i-1][j] is the value of the element immediately above in the dynamic programming table.
max(d_program[i-1][j-1], d_program[i-1][j]): We take the maximum value between the element immediately above and to the left (d_program[i-1][j-1]) and the element immediately above (d_program[i-1][j]).
numbers[i][j] + max(d_program[i-1][j-1], d_program[i-1][j]): We add the current element's value to the maximum value calculated above.

Asymptotic time complexity of the algorithm:

The Asymptotic Time complexity of the algorithm is O(n^2) as calculated below :

'import sys': This takes constant time

Read Function
def read():    
    input_f = sys.argv[1]
    with open(input_f, "r") as f:
        n = int(f.readline().strip()) 
        numbers = [list(map(int, line.strip().split())) for line in f.readlines()]  
        return numbers 

Time complexity of read function:The time complexity of the read function is dominated by the list comprehension, making it O(n) where 'n' is the number of lines in the file.

Function for Main Algorithm (prodDP) 

def prodDP(numbers):
    d_program = [[0] * len(row) for row in numbers]
    d_program[0][0] = numbers[0][0] 
    
    for i in range(1, len(numbers)):
        for j in range(len(numbers[i])):
            # Recurrence relation: d_program[i][j] = numbers[i][j] * max(d_program[i-1][j-1] if j > 0 else 1, d_program[i-1][j] if j < len(numbers[i-1]) else 1)
            d_program[i][j] = numbers[i][j] * max(d_program[i-1][j-1] if j > 0 else 1, d_program[i-1][j] if j < len(numbers[i-1]) else 1)
    
    maximum_product = max(d_program[-1])
    route = []
    j = d_program[-1].index(maximum_product)
    for i in range(len(numbers) - 1, -1, -1):
        route.insert(0, numbers[i][j])
        if i > 0:
            j = j - 1 if j > 0 and d_program[i][j] == numbers[i][j] * d_program[i-1][j-1] else j
    
    return maximum_product, route


    Time complexity of prodDP:The prodDP function constructs a 2D list, which takes O(n^2) time (where 'n' is the number of rows). The double-loop iteration through the triangular array also has a time complexity of O(n^2). The prodDP function constructs a 2D list, which takes O(n^2) time (where 'n' is the number of rows). The double-loop iteration through the triangular array also has a time complexity of O(n^2). As a result, the overall time complexity of the prodDP function is O(n^2)., the overall time complexity of the prodDP function is O(n^2).

Output Function and main execution:

def output_function(maximum_product, route):
    with open("Output.txt", "w") as f:
        f.write(str(maximum_product) + "\n")
        f.write(" ".join(map(str, route)))

# This function handles other functions sequentially 
def start():
    value = read()
    maximum_product, route = prodDP(value)
    output_function(maximum_product, route)

start()

Time complexity of Output Function and Main execution: output_function(maximum_product, route): Writing to a file has a constant time complexity.
start(): Calling the read function, running the main algorithm with prodDP, and writing the output have a time complexity of O(n^2) due to the prodDP function.

Overall, the dominant time complexity is determined by the nested loops in the prodDP function, making the overall time complexity of the program O(n^2), where n is the number of rows in the input triangular array.
