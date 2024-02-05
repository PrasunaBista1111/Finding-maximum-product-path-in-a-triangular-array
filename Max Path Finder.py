
# PseudoCode
'''
# Function to read input from a file specified in the command line arguments
Function read():
    input_file = sys.argv[1]  # Get the input file name from command line arguments
    Open input_file in read mode
    Read the first line to get the integer n (number of rows of the triangular array)
    Read the remaining lines to populate a 2D list named numbers with triangular array values
    Close the input file
    Return the 2D list numbers

# Main algorithm for finding the maximum product and route
Function prodDP(numbers):
    Initialize a 2D list d_program to store intermediate results, having the same dimensions as numbers
    Set d_program[0][0] to numbers[0][0]

    # Dynamic programming to calculate the maximum product for each element
    For i from 1 to len(numbers) - 1:
        For j from 0 to len(numbers[i]) - 1:
            If j > 0:
                Set left_product to d_program[i-1][j-1]
            Else:
                Set left_product to 1  # If no left element, set to 1
            
            If j < len(numbers[i-1]):
                Set above_product to d_program[i-1][j]
            Else:
                Set above_product to 1  # If no above element, set to 1
            
            Set d_program[i][j] to numbers[i][j] multiplied by the maximum of left_product and above_product

    # Find the maximum product in the last row of d_program
    Set maximum_product to the maximum value in the last row of d_program

    # Backtrack to find the route that yields the maximum product
    Initialize an empty list route
    Set j to the index of maximum_product in the last row of d_program
    For i from len(numbers) - 1 to 0:
        Insert numbers[i][j] at the beginning of route
        If i > 0:
            If j > 0 and d_program[i][j] is the result of multiplying numbers[i][j] with d_program[i-1][j-1]:
                Decrement j by 1
            Else:
                Set j to its current value

    Return maximum_product and route

# Function to write the output to a file named "Output.txt"
Function output_function(maximum_product, route):
    Open "Output.txt" in write mode
    Write maximum_product followed by a newline
    Write the elements of route separated by spaces

# Function to coordinate the execution of other functions
Function start():
    Call read() and store the result in value
    Call prodDP(value) and store the results in maximum_product and route
    Call output_function(maximum_product, route)


Call start()

'''
import sys

def read():    
    input_f =sys.argv[1]
    with open(input_f, "r") as f:
        n = int(f.readline().strip()) 
        numbers = [list(map(int, line.strip().split())) for line in f.readlines()]  
        return numbers

# This is the main algorithm for finding the solutions
def prodDP(numbers):
    d_program = [[0] * len(row) for row in numbers]
    d_program[0][0] = numbers[0][0] 
    
    for i in range(1, len(numbers)):
        for j in range(len(numbers[i])):
            # Recurrence relation: d_program[i][j] = numbers[i][j] * max(d_program[i-1][j-1], d_program[i-1][j])
            d_program[i][j] = numbers[i][j] * max(d_program[i-1][j-1] if j > 0 else 1, d_program[i-1][j] if j < len(numbers[i-1]) else 1)
    
    maximum_product = max(d_program[-1])
    route = []
    j = d_program[-1].index(maximum_product)
    for i in range(len(numbers) - 1, -1, -1):
        route.insert(0, numbers[i][j])
        if i > 0:
            j = j - 1 if j > 0 and d_program[i][j] == numbers[i][j] * d_program[i-1][j-1] else j
    
    return maximum_product, route

# This function writes output to the file Output.txt
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



    
