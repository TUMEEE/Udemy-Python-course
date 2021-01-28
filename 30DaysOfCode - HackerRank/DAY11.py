"""
Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
Hourglass:
1 1 1
   1
1 1 1
Input:
Given a 6x6 2D Array, A:
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
Output:
print the maximum hourglass sum.
"""
# data = [list(map(int, input().strip().split()[:6:])) for i in range(6)]
data = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
BigData = []
SmallData = []


def Func(data):
    SmallData = []
    for i in range(3):
        for j in range(3):
            SmallData.append(data[i][j])
    del SmallData[3]
    SmallData.insert(3, 0)
    del SmallData[5]
    SmallData.insert(5, 0)
    return SmallData


def maxx(data):
    prev = sum(data[0])
    for i in range(len(data)):
        if prev < sum(data[i]):
            prev = sum(data[i])
        else:
            continue
    return prev


k = 0
for _ in range(4):
    for i in range(4):
        for j in range(3):
            SmallData.append(data[j + k][:3])
        BigData.append(Func(SmallData))
        SmallData.clear()
        k += 1
    for q in range(6):
        del data[q][0]
    k = 0

result = maxx(BigData)
print(result)


# res = []
# data = [list(map(int, input().strip().split()[:6:])) for i in range(6)]
# for x in range(0, 4):
#     for y in range(0, 4):
#         s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
#         res.append(s)

# print(max(res))