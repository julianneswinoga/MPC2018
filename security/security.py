import random

N = int(input())
M = [int(i) for i in input().split(' ')]

print(int(len(M) * (1 if random.random() > 0.5 else 2)))