m = int(input())
lst = list(map(int,input().split()))
string = ""

for i in range(len(lst)):
    digit = (lst[i])%10
    string += str(digit)  
if int(string) % 10 == 0:
    print("Yes")
else:
    print("No") 
