
N,K = map(int,input().split())
A = list(map(int,input().split()))

curr = 0

A.sort()

for i in range(N):
    if A[i] == curr and curr < K:
        curr+=1
    
print(curr)