X,Y,N = map(int,input().split())
ans = 0
temp = N % 3
temp3 = int(N / 3)
if 3 * X < Y:
    ans += temp3 * X * 3
else:
    ans += temp3 * Y

ans += temp * X
print(ans)
