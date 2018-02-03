D = int(input())
B = int(input())

dock = [0] * D
for di in range(B):
    wanted_dock = int(input())
    while wanted_dock > 0:
        if not dock[wanted_dock - 1]:
            dock[wanted_dock - 1] = 1
            break
        wanted_dock -= 1
    else:
        break

print(sum(dock))
