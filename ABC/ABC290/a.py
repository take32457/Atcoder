N , M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

score = 0

for value in B:
    score += A[value-1]

print(score)