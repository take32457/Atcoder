N,M,T = map(int,input().split())
A = list(map(int,input().split()))
XY = []
j  = 0
flag = True
for i in range(M):
    XY.append(list(map(int,input().split())))
for i in range(N -1):
    if j < M:
        if XY[j][0] - 1 == i:
            T += XY[j][1]
            j += 1
    T -= A[i]
    if T <= 0:
        flag = False
        break
    

if flag:
    print("Yes")
else:
    print("No")