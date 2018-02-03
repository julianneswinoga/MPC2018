import math
import threading

nl = int(input())
sl = [int(i) for i in input().split(" ")]
ac = 0
ra = 0
ob = 0
eps = 0.0000001
num_threads = 4


class TriangleThread(threading.Thread):
    def __init__(self, triangles):
        threading.Thread.__init__(self)
        self.triangles = triangles
        self.ra = 0
        self.ob = 0
        self.ac = 0

    def run(self):
        for t in self.triangles:
            a, b, c = t[0], t[1], t[2]
            s = (a + b - c) * (a + c - b) * (c + b - a)
            if s < eps:
                continue
            try:
                C = math.acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))
                B = math.asin((b * math.sin(C)) / c)
                A = math.pi - B - C
                if math.pi / 2 in [A, B, C]:
                    self.ra += 1
                elif max([A, B, C]) > math.pi / 2:
                    self.ob += 1
                else:
                    self.ac += 1
            except:
                continue


all_permuations = []
for i in range(len(sl)):
    for j in range(i + 1, len(sl)):
        for k in range(j + 1, len(sl)):
            all_permuations.append([sl[i], sl[j], sl[k]])
threads = []
chunks = [all_permuations[x:x+num_threads] for x in range(0, len(all_permuations), num_threads)]
for chunk in chunks:
    threads.append(TriangleThread(chunk))

for T in threads:
    T.start()

for T in threads:
    T.join()

print(sum([T.ac for T in threads]), sum([T.ra for T in threads]), sum([T.ob for T in threads]))
