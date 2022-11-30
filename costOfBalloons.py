t = int(input())
for i in range(t):
    p,g  = list(map(int, input().split(' ')))
    n = int(input())
    s1 = 0
    s2 = 0
    for i in range(n):
        a,b  = list(map(int, input().split(' ')))
        s1 += a
        s2 += b
    ans = min((s1 * p + s2 * g),(s1 * g + s2 * p))
    print(ans)