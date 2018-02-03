rc = [int(i) for i in input().split(" ")]
mon = int(input())
monpos = []
for i in range(mon):
    monpos.append([int(j)-1 for j in input().split(" ")])
#print (monpos)
step = [[[0, 0]]]
goal = [rc[0]-1, rc[1]-1]
path = 0
shouldbreak = False
for i in range((rc[0]-1)*(rc[1]-1)+1):
    step.append([])
    for point in step[-2]:
        if (point[0] < rc[0]) and (point[1] < rc[1]):
            if ([point[0]+1, point[1]] not in monpos and point[0]+1 < rc[0]):
                step[-1].append([point[0]+1, point[1]])
            if ([point[0], point[1]+1] not in monpos and point[1]+1 < rc[1]):
                step[-1].append([point[0], point[1]+1])
    #print(step[-1])
    for i in step[-1]:
        if i == goal:
            path+=1
            shouldbreak = True
    if shouldbreak:
        break
#print(rc[0]-1, rc[1]-1)
print(path)
