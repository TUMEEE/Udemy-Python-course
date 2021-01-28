"""
Task
Given an array, A, of N  integers, print A's elements in reverse order as a single line of space-separated numbers.
"""
N = int(input())
arr = list(map(int, (input().strip().split())[:N:]))
arr1 = arr[::-1]
for i in range(len(arr1)):
    print(arr1[i], end=" ")