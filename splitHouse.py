#-----------------------------USING REGEX--------------------------#
import re
n = int(input())
dob = re.compile(r'HH')
s = input()
res = ""
tod = dob.search(s)
if tod:
    print("NO")
else:
    print("YES")
    for i in range(len(s)):
        if s[i] == ".":
            res += "B"
        else:
            res += "H"
    print(res)


#-----------------------------OR---------------------------------#


n = int(input())
s = input()
aj = False
for i in range(len(s)-1):
    if s[i] == "H" and s[i+1] == "H":
        print("NO")
        aj = True
        break
if not aj:
    print("YES")
    res = s.replace(".","B")
    print(res)
