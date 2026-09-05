import sys

# a, b, x, y, f, fx, fy, r = [input() for i in range(list(map(int, input().split()))[0])], [], 0, 0, 0, 0, 0, '-1'
# while 0 <= x < len(a) and 0 <= y < len(a[0]) and f != 1:
#     if a[x][y] == 'U' or a[x][y] == 'D': x, fx, fy = [x-1, 1, 0] if a[x][y] == 'U' else [x+1, -1, 0]
#     if a[x][y] == 'R' or a[x][y] == 'L': y, fy, fx = [y+1, -1, 0] if a[x][y] == 'R' else [y+1, -1, 0]
#     if str(x)+' '+str(y) in b: f = 1
#     b.append(str(x)+' '+str(y))
# if f == 0: r = str(x+1+fx)+' '+str(y+1+fy)
# print(r)

n = sys.stdin.readline()
n = n.split()
n = list(map(int, n))
frt = n[0]

a = [sys.stdin.readline() for i in range(frt)]
b = []
x = 0
y = 0
f = 0
fx = 0
fy = 0
r = '-1'

while 0 <= x < len(a) and 0 <= y < len(a[0]) and f != 1:
    if a[x][y] == 'U':
        x, fx, fy = x-1, 1, 0
    elif a[x][y] == 'D':
        x, fx, fy = x+1, -1, 0
    elif a[x][y] == 'R':
        y, fy, fx = y+1, -1, 0
    elif a[x][y] == 'L':
        y, fy, fx = y-1, +1, 0
    coord = str(x) + ' ' + str(y)

    if coord in b:
        f = 1
    b.append(coord)

if f == 0:
    r = str(x+1+fx)+' '+str(y+1+fy)

print(r)
