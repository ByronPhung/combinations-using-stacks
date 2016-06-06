#===============================================================================
#  File        : main.py
#  Project     : Combinations Using Stacks
#  Description : Calculate combinations using stacks and recursive removal.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#                Gregory Lynch
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

#-------------------------------------------------------------------------------
#  Custom Modules
#-------------------------------------------------------------------------------

# Simulate stacks.
# Reference: stack.py
from stack import Stack

#===============================================================================
#  Functions
#===============================================================================

def main():
    """Execute the main program.

    Keyword arguments:
    <None>
    """
    # Let the user change input infinitely until cancelled.
    while True:
        # Get space-separated input for n and r.
        inputs = input("\nINPUT:: Enter n & r for nCr (separated by spaces): ")
        input_list = inputs.split()
        len_input_list = len(input_list)

        # If the input is not 2 (n & r), then display an error.
        if (len_input_list != 2):
            # If the input is less than 2, then inform the user to input at
            # least 2.
            if (len_input_list < 2):
                print("ERROR:: Not enough inputs (current: " + str(len_input_list) + ").")
                print("        Please input 2 inputs for n & r separated by spaces.")
            # Otherwise, inform the user to input only 2 inputs.
            else:
                print("ERROR:: Too many inputs (current: " + str(len_input_list) + ").")
                print("        Please input only 2 inputs for n & r separated by spaces.")
            # Restart the input loop.
            continue

        # Define n & r from the input.
        n = int(input_list[0])
        r = int(input_list[1])

        # If n is less than r, then display an error and restart the input loop.
        if n < r:
            print("ERROR:: r cannot be greater than n (n = " + str(n) + ", n = " + str(r) + ").")
            continue

        # Otherwise, print the combination of n & r.
        print("C(" + str(n) + ", " + str(r) + ") = " + str(combination(n, r)))

def combination(n, r):
    """Calculate the combination, or n choose r.

    Keyword arguments:
    n -- Number of things
    r -- How many times n is taken at a time
    """
    # Initialize default combination value and address.
    combination_value = 0
    address = 10

    # Create a stack that can hold enough values. 100 is arbitrary.
    s = Stack(100)

    # Push initial values into the stack.
    s.push(20)
    s.push(r)
    s.push(n)
    s.push(combination_value)

    # While the stack is not empty, compute the combination value.
    while not s.is_empty():
        # If address is 10, then calculate the combination value.
        if address is 10:
            # Get the current combination value, n, and r from the stack.
            combination_value = s.pop()
            n = s.pop()
            r = s.pop()

            # If r == 0 or r == n, then get the next address, increment the
            # combination value by 1, and push the new combination value back
            # into the stack.
            if r is 0 or r is n:
                address = s.pop()
                s.push(combination_value + 1)
            # Otherwise, push the recursive definition of a combination back
            # into the stack, i.e., C(n - 1, r - 1) + C(n - 1, r).
            else:
                s.push(r - 1)
                s.push(n - 1)
                s.push(10)
                s.push(r)
                s.push(n - 1)
                s.push(combination_value)

        # Else if the address is 20, then return the combination value stored
        # at the top of the stack.
        elif address is 20:
            combination_value = s.pop()

    # Return the combination value.
    return combination_value

#===============================================================================
#  Main Execution
#===============================================================================

main()