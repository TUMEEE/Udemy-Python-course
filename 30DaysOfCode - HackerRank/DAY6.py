"""
Task
Given a string,S, of length  N that is indexed from 0 to N-1, print its even-indexed and odd-indexed 
characters as 2 space-separated strings on a single line (see the Sample below for more detail).
"""
even = []
odd = []
T = int(input())
data = [input() for i in range(T)]
for i in range(T):
    for inde, j in enumerate(data[i]):
        if inde % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    print("".join(even) + " " + "".join(odd))
    even = []
    odd = []