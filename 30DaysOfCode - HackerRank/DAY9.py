"""
Today, we are learning about an algorithmic concept called recursion.

Recursive Method for Calculating Factorial

Function Description:
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following parameter:
int n: an integer

Returns
int: the factorial of n

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, 
you will get a score of 0.

Input Format

A single integer,  n(the argument to pass to factorial).

"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
result = factorial(n)
print(result)