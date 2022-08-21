H,W = map(int,input().split())
G = []
visited = [[0,0]]
point = [0,0] #y座標 x座標
flag = True
ans = True
def is_moved(xy,c):
    if c == "U" and xy[0] != 0:
        G[point[0]][point[1]] = " "
        xy[0] -= 1
        return xy
    if c == "D" and xy[0] != H -1:
        G[point[0]][point[1]] = " "
        xy[0] += 1
        return xy
    if c == "L" and xy[1] != 0:
        G[point[0]][point[1]] = " "
        xy[1] -= 1
        return xy
    if c == "R" and xy[1] != W - 1:
        G[point[0]][point[1]] = " "
        xy[1] += 1
        return xy
    if c == " ":
        return 2
    return -1

for i in range(H):
    G.append(list(input()))

while flag:
    temp = is_moved(point,G[point[0]][point[1]]) 
    if temp == 2:
        ans = False
        flag = False
    elif temp == -1:
        flag = False
    else:
        arr = [temp[0],temp[1]]
        visited.append(arr)
if ans:
    print(str(visited[-1][0] + 1) +" " + str(visited[-1][1] + 1))
else:
    print(-1)