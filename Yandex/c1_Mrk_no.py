import sys
# h, w = [int(x) for x in input().split()]
# m = [list(input()) for _ in range(h)]
h, w = [int(x) for x in sys.stdin.readline().split()]
m = [list(sys.stdin.readline()) for _ in range(h)]
r = [0, 0] # result
t = [0, 0] # temp
#print(*m, sep='\n')
#print(h, w, m, r)
isCircle = False # Флаг наличия кольца
isExit   = False # Флаг вышел за пределы карты
while not isCircle and not isExit:
    c = m[r[0]][r[1]]
    if   c == "+": isCirсle = True
    elif c == "U": t[0] -= 1
    elif c == "D": t[0] += 1
    elif c == "R": t[1] += 1
    elif c == "L": t[1] -= 1
    if not isCircle:
        if t[0] < 0 or t[0] > h-1: isExit = True
        if t[1] < 0 or t[1] > w-1: isExit = True
        m[r[0]][r[1]] = "+"
        if isExit: 
            r[0] += 1
            r[1] += 1
        else: r[0], r[1] = t[0], t[1]
    else: r = [-1]
    # print(f"c<{c}> r<{r}> t<{t}> isC<{isCircle}> isE<{isExit}>")
print(*r)
#print(*m, sep='\n')