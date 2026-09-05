# cook your dish here
import sys, math

# main
n, q  = [int(a) for a in sys.stdin.readline().split()]
s = sys.stdin.readline()[:n]
# sp = [[int(a) for a in sys.stdin.readline().split()] for _ in range(q)]
# print(n, q, s, sp)

# # Цикл по командам
# for k, i in sp:
#     if k == 2: 
#         # print(k, i, s[i-1], s)
#         print(s[i-1])
#     if k == 1: 
#         # print(k, i, s, end=" | ")
#         s = s[-1*(i):] + s[:-1*(i)]
#         # print(s)

# # Цикл по командам
# d = 0 # смещение
# for k, i in sp:
#     if k == 2: 
#         p = (d+i-1) % n
#         print(s[p])
#         # print(k, i, d, p, s[p], s, d+i-1)
#     if k == 1: 
#         d -= i
#         # print(k, i, d)

# Цикл по командам
d = 0 # смещение
for _ in range(q):
    k, i = sys.stdin.readline().split()
    k, i = int(k), int(i)
    if k == 2: 
        p = (d+i-1) % n
        print(s[p])
        # print(k, i, d, p, s[p], s, d+i-1)
    if k == 1: 
        d -= i
        # print(k, i, d)
