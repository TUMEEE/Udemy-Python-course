"""
Task
Given a base- 10 integer, n, convert it to binary (base-2). 
Then find and print the base- integer denoting the maximum number of consecutive 1's in n's binary representation. 
When working with different bases, it is common to show the base as a subscript.
"""


def To2(n):
    arr = []
    while n != 0:
        arr.append(n % 2)
        n = n // 2
    return arr[::-1]


n = int(input())
data = To2(n)
count = 0
maxx = 0
for i in range(len(data)):
    if data[i] and 1 == 1:
        count += 1
        if count > maxx:
            maxx = count
    else:
        if count > maxx:
            maxx = count
            count = 0
        else:
            count = 0
print(maxx)