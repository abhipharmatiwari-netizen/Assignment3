"""
1. Asks the user for a number as input.
2. Uses the math module to calculate the:
    Square root of the number
    Natural logarithm (log base e) of the number
    Sine of the number (in radians)
3.  Displays the calculated results.
"""

import math

num=float(input("Enter a number: "))
sqrt_val=math.sqrt(num)
log_val=math.log(num)
sine_val=math.sin(num)

print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural logarithm (log base e) of {num} is: {log_val}")
print(f"Sine of {num} (in radians) is: {sine_val}")