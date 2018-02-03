import math

nl = int(input())
sl = [int(i) for i in input().split(" ")]
ac = 0
ra = 0
ob = 0
eps = 0.0000001

for i in range(len(sl)):
    for j in range(i + 1, len(sl)):
        for k in range(j + 1, len(sl)):
            a = sl[i]
            b = sl[j]
            c = sl[k]
            s = (a + b - c) * (a + c - b) * (c + b - a)

            if s < eps:
                continue

            try:
                C = math.acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))
                B = math.asin((b * math.sin(C)) / c)
                A = math.pi - B - C
                if math.pi / 2 in [A, B, C]:
                    ra += 1
                elif max([A, B, C]) > math.pi / 2:
                    ob += 1
                else:
                    ac += 1
            except:
                continue

print(ac, ra, ob)
