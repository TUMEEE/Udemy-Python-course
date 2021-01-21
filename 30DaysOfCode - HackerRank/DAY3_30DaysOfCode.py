n = int(input())
if n%2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not weird")
    elif n in range(6, 21):
        print("Weird")
    elif n in range(21, 101):
        print("Not Weird")
