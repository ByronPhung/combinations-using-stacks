#===============================================================================
#  File        : stack.py
#  Project     : Combinations Using Stacks
#  Description : Simulate stacks.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#                Gregory Lynch
#===============================================================================

#===============================================================================
#  Global Constants
#===============================================================================

# Define the default max size of the stack for when there is no user-defined
# value.
DEFAULT_MAX_SIZE = 4

#===============================================================================
#  Class Definition
#===============================================================================

class Stack(object):
    """Simulate stacks.

    Keyword arguments:
    max_size -- Max size of stack
    """
    def __init__(self, max_size):
        # If no max size is defined, then use the default size.
        if max_size is None:
            self.__max_size = DEFAULT_MAX_SIZE
            self.__stack_ptr = DEFAULT_MAX_SIZE
        # Otherwise, use the defined size.
        else:
            self.__max_size = max_size
            self.__stack_ptr = max_size
        # Create a data list of the max size.
        self.__data = [None] * self.__max_size

    def is_empty(self):
        """Check if the stack is empty.

        Keyword arguments:
        <None>
        """
        return self.__max_size is self.__stack_ptr

    def is_full(self):
        """Check if the stack is full.

        Keyword arguments:
        <None>
        """
        return self.__stack_ptr is 0

    def peek(self):
        """Get the value of the top of the stack without removing it.

        Keyword arguments:
        <None>
        """
        # If the stack is empty, then display an error and return a junk value.
        if self.is_empty():
            print("ERROR:: Stack is empty.")
            return self.__data[0]
        # Otherwise, return the top of the stack without removing it.
        else:
            return self.__data[self.__stack_ptr]

    def push(self, value):
        """Store the specified value into the stack.

        Keyword arguments:
        value -- Value to store in stack
        """
        # If the stack is full, then display an error.
        if self.is_full():
            print("ERROR:: Stack is full.")
        # Otherwise, push the value into the stack.
        else:
            self.__stack_ptr = self.__stack_ptr - 1
            self.__data[self.__stack_ptr] = value

    def pop(self):
        """Get the value of the top of the stack and remove it.

        Keyword arguments:
        <None>
        """
        # If the stack is empty, then display an error and return a junk value.
        if self.is_empty():
            print("ERROR:: Stack is empty.")
            return self.__data[0]
        # Otherwise, return the top of the stack and remove it.
        else:
            value = self.__data[self.__stack_ptr]
            self.__stack_ptr = self.__stack_ptr + 1
            return value

    def num_elements(self):
        """Get the number of elements in the stack.

        Keyword arguments:
        <None>
        """
        return self.__max_size - self.__stack_ptr