D = int(input())
B = int(input())
wanted_dock = []
for _ in range(B):
    wanted_dock.append(int(input()))


dock = [0] * D
for di in range(B):
    while wanted_dock[di] > 0:
        if not dock[wanted_dock[di] - 1]:
            dock[wanted_dock[di] - 1] = 1
            break
        wanted_dock[di] -= 1
    else:
        break

print(sum(dock))
