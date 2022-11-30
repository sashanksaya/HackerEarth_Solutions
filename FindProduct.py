n = int(input())
lst = list(map(int,input().split()))
ans = 1
for i in lst:
    ans = (ans * i) % ((10**9) + 7)

print(ans)