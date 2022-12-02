s = input()
res = ""
for i in range(len(s)):
    if s[i].isupper():
        res += s[i].lower()
    else:
        res += s[i].upper()
print(res)