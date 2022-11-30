s = input()
if s[2] not in ["A","E","I","O","U","Y"]:
    a = (int(s[0]) + int(s[1])) % 2 == 0
    b = (int(s[3]) + int(s[4])) % 2 == 0
    c = (int(s[4]) + int(s[5])) % 2 == 0
    d = (int(s[7]) + int(s[8])) % 2 == 0
    if a and b and c and d:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")