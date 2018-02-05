import math
inp = [int(i) for i in input().split(" ")]
ppos = inp[1:]
vert = inp[0]
#print (vert, ppos)
corners = []
for i in range(vert):
    temp = input().split(" ")
    corners.append([int(temp[0]), int(temp[1])])
mp = []
for i in range(-1, len(corners)-1):
    tempx = (corners[i][0] + corners[i+1][0])/2
    tempy = (corners[i][1] + corners[i+1][1])/2
    mp.append([tempx, tempy])
distance = 0
for i in range(-1,len(corners)-1):
    print (mp[i], mp[i+1],(math.sqrt(math.pow(mp[i+1][0]-mp[i][0],2)+math.pow(mp[i+1][1]-mp[i][1], 2))))
    distance+=(math.sqrt(math.pow(mp[i+1][0]-mp[i][0],2)+math.pow(mp[i+1][1]-mp[i][1], 2)))
print(round(distance, 2))
