l = int(input())
n = int(input())
for _ in range(n):
    a,b = list(map(int,input().split()))
    if (a >= l and b >= l and a == b):
        print("ACCEPTED")
    elif a >= l and b >= l:
        print("CROP IT")
    elif (a <= l or b <= l) or (a <= l and b >= l) or (a >= l and b <= l):
        print("UPLOAD ANOTHER")