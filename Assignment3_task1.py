"""
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""


def factorial(n):
    fact=1  
    while n>1:
        fact=fact*n
        n=n-1
    return fact


if __name__ == "__main__":
    n=int(input("Enter a number to calculate its factorial: "))
    fact=factorial(n)
    print(f"The factorial of {n} is : {fact}")
