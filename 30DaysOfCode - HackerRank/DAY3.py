"""
Task
Given an integer n, 
perform the following conditional actions:

1.If  is odd, print Weird
2.If  is even and in the inclusive range of  to , print Not Weird
3.If  is even and in the inclusive range of  to , print Weird
4.If  is even and greater than , print Not Weird
5.Complete the stub code provided in your editor to print whether or not  is weird.
"""
n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not weird")
    elif n in range(6, 21):
        print("Weird")
    elif n in range(21, 101):
        print("Not Weird")