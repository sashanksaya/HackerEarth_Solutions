def getMatch(n):
    if n in [2, 3, 5]:
        return 5
    elif n in [0, 6, 9]:
        return 6
    elif n == 1:
        return 2
    elif n == 4:
        return 4
    elif n == 8:
        return 7
    elif n == 7:
        return 3


def getMax(n):
    if n % 2 == 0:
        return "1" * (n//2)
    else:
        s = "7" + ("1" * ((n-3)//2))
        return s


t = int(input())
for i in range(t):
    n = input()
    m = 0
    for i in n:
        m += getMatch(int(i))
    print(getMax(m))
