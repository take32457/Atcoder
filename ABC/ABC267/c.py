N,M = map(int,input().split())
A = list(map(int,input().split()))

B = list()
C = list()

temp = 0
temp1 = 0

for i in range(M):
    temp +=  A[i] * (i + 1)
    temp1 += A[i]
B.append(temp)
C.append(temp1)

for i in range(N - M):
    B.append(B[i] - C[i] + A[i + M] * M)
    C.append(C[i] + A[i + M] - A[i])


print(max(B))