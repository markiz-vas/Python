# cook your dish here
import sys, math


# main
nn = int(sys.stdin.readline())
sp = [int(a) for a in sys.stdin.readline().split()]
sp.sort(reverse=True)
a, b, ab = 0, 0, ""
# print(sp, a, b, ab, nn)

# Ищем две пары
for n in sp:
    # print(n, sp, a, b, ab, end=" | ")
    if   ab == ""  and a == 0: a = n     # 1a
    elif ab == ""  and a == n: ab = "a"  # 2a
    elif ab == ""  and a != n: a = n     # 1a
    elif ab == "a" and b == 0: b = n     # 1b
    elif ab == "a" and b == n: ab = "ab" # 2b
    elif ab == "a" and b != n: b = n     # 1b
    elif ab == "ab": break
    # print(a, b, ab, end="\n")

# Результат
print(a*b)