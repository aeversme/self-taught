# Bitwise AND
print(0b10 & 0b11)  # = 2

"""
10
11
__

10 <-- looks at each bit; 0 & 1 = False (0), 1 & 1 = True (1)

Thus, 0b10 & 0b11 = 2.

This operation can also be performed on decimal integers, which are converted to binary for the operation.
"""

# Bitwise OR
print(2 | 3)  # = 3

"""
Bitwise OR returns 1 if either of the bits is 1, and returns 0 only if both bits are 0.
"""


# check if a number is even or odd using bitwise AND
def is_even(n):
    return not n & 1


print(is_even(8))
print(is_even(13))

"""
Performing bitwise AND on an even number and 1 returns False. Inverting with `not` in the function returns True when 
evaluating even numbers.
"""


# check if a number is a power of 2
def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False


print(is_power(6))
print(is_power(8))
