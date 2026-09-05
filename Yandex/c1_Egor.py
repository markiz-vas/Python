import sys
# h, w = [int(x) for x in input().split()]
# m = [list(input()) for _ in range(h)]
h, w = [int(x) for x in sys.stdin.readline().split()]
s = ""
for _ in range(h):
    s = s + input()
# print(h, w, s)
res = -1 # цикл
h1, w1 = 0, 0 # корды текущего положения
h2, w2 = 0, 0 # корды следующего положения
count = 0 # счётчик шагов
while count < (h*w+2):
    # Увеличиваем счетчик пройденных шагов
    count += 1
    # Получаем указатель "Куда идти"
    k = s[h1*w+w1]
    if   k == 'U':
        h2 -= 1
    elif k == 'D':
        h2 += 1
    elif k == 'R':
        w2 += 1
    elif k == 'L':
        w2 -= 1
    # Проверка "Находимся ли мы в пределах карты?"
    if 1 <= h2+1 <= h and 1 <= w2+1 <= w:
        # Мы на карте
        h1, w1 = h2, w2
    else:
        # Мы покинули карту (пришли)
        #print(h1+1, w1+1)
        res = f"{h1+1} {w1+1}"
        break
print(res)
    

# for h0 in range(h):
#     for w0 in range(w):
#         #print(f"{h0+1} {w0+1} {s[h0*w+w0]}")
#         print(s[h0*w+w0], end='')
#     print()