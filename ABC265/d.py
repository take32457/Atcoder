#解けていないコード

def binary_search(S,st):
    length = len(S)
    head = 0
    mid = int((head + length) /2)
    while head <= length:
        if S[mid] == st:
            return mid
        elif st > S[mid]:
            head = mid + 1
        else:
            length = mid - 1
        
        mid = int((head + length) /2)
    return -1
    



N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
S = [0]
j = 1
D = 0
for i in A:
    S.append(i + S[j-1])
    j += 1

for x in range(1,N + 1):
    temp = binary_search(S,S[x] + P)
    if  temp == -1:
        print("No")
        exit()
    else:
        D = temp
        print(D)
        break
for x in range(D,N + 1):
    temp = binary_search(S,S[x] + Q)
    if  temp == -1:
        print("No")
        exit()
    else:
        D = temp
        print(D)
        break

for x in range(D,N + 1):
    temp = binary_search(S,S[x] + R)
    if  temp == -1:
        print("No")
        exit()
    else:
        print(temp)
        break
print("Yes")
