import sys, math

# Определяем количество наборов, которые мы можем получить
def count(c, t, n): # c - склад; t - товар; n - количество видов материалов
    res = []
    for i in range(n):
        # макс. кол-во из выбранного материала
        res.append(max(c) if t[i] == 0 else c[i]//t[i]) 
    return min(res) # возвращаем мин. кол-во из выбранного материала

# Корректируем количество товаров на складе в соответствии с кол-вом наборов cnt
def sklad(c, t, n, cnt): # c - склад; t - товар; n - кол-во видов; cnt - кол-во товара
    res = c.copy()
    for i in range(n): res[i] -= t[i] * cnt
    return res # Остаток материалов на складе

# Вычисляем, можно ли создать кол-во наборов cntx + cnty    
def countxy(c, x, y, n, cntx, cnty): 
    # c - склад; x,y - товары; cntx, cnty - количество наборов x,y 
    res = c.copy()
    res = sklad(res, x, n, cntx)
    res = sklad(res, y, n, cnty)
    #print("res", res)
    if min(res) < 0: return 0
    return cntx + cnty
    
# В Цикле прогоняем задачу countxy
def forcountxy(c, x, y, n, cntx, cnty):
    # c - склад; x,y - товары; cntx, cnty - максимальное количество наборов x,y 
    maxx, maxy = 0, 0   # макс кол-во по каждому виду товара
    maxn = 0;           # макс общее количество товаров
    for dx in range(cntx+1):
        for dy in range(cnty+1):
            res = countxy(c, x, y, n, dx, dy)
            if res > maxn: 
                maxn = res
                maxx = dx
                maxy = dy
    return maxx, maxy

# main
n = int(sys.stdin.readline())
c = [int(a) for a in sys.stdin.readline().split()]
x = [int(a) for a in sys.stdin.readline().split()]
y = [int(a) for a in sys.stdin.readline().split()]
mt = [0, 0] # Макс. кол-во наборов, когда весь склад в твоём распоряжении
rt = [0, 0] # Результирующее количество каждого товара
#print(n, c, x, y, mt, rt)

# Считаем макс кол-во штук одного набора товара
mt[0] = count(c, x, n)
mt[1] = count(c, y, n)
# print("mt", mt)

rt[0], rt[1] = forcountxy(c, x, y, n, mt[0], mt[1])
print(rt, c, mt)

# Результат
# print("rt", rt)
print(rt[0] + rt[1])