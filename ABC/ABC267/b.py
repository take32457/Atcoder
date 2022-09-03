S = input()
if S[0] == '1':
    print("No")
    exit()

a = {'7' : 1,'4':2,'8' :3,'2' :3,'1':4,'5':4,'3':5,'9':5,'6':6,'10':7}
ans = {}
ans = list(ans)
for i in range(1,len(S) + 1):
    if S[i - 1] == '1':
        ans.append(a[str(i)])

ans = set(ans)

ans = sorted(ans)

if len(ans) == 0:
    print('No')
    exit()

for i in range(1,len(ans)):
    if ans [i] - ans[i - 1] != 1:
        print('Yes')
        exit()
    

print('No')

