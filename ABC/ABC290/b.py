N,K = map(int,input().split())

S = input()

ans = ""

for c in S:
    if c == "o" and K > 0:
        ans += "o"
        K-=1
    else:
        ans+="x"
    
print(ans)