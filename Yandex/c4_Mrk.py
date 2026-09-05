# cook your dish here
import sys, math

# main
nn, st = [int(a) for a in sys.stdin.readline().split()]
sx, sy, sz = 10000, 5000, 1000  # nominal
# sx, sy, sz = 10, 5, 1   # nominal
x, y, z = -1, -1, -1    # result
rn, rst = 0, 0          # result
# print(nn, st, sx, sy, sz)
if   st >  nn*sx: x, y, z = -1, -1, -1 # решений нет
elif st == nn*sx: x, y, z = nn,  0,  0 # решение все x
elif st == nn*sy: x, y, z =  0, nn,  0 # решение все y
elif st == nn*sz: x, y, z =  0,  0, nn # решение все z
elif st <  nn*sz: x, y, z = -1, -1, -1 # решений нет
elif nn*sz < st < nn*sy or nn*sy < st < nn*sx:
    x, y, z = 0, 0, 0 # ищем x, y, z
    x = st//sx              # Максимальное количество монет x
    y = st%sx//sy           # Максимальное количество монет y
    z = (st-x*sx-y*sy)//sz  # Остаток монет z
    # print(f"nn<{nn}> st<{st}> x<{x}> y<{y}> z<{z}> xyz<{x+y+z}>")
    if   x+y+z == nn: x, y, z = x, y, z       # решение x, y, z
    elif x+y+z >  nn: x, y, z = -1, -1, -1    # решений нет (недостаточно монет для st)
    elif x+y+z <  nn: 
        # Недостаточно монет, нужен размен
        # print("Недостаточно монет, нужен размен")
        count = 0
        while x+y+z != nn:
            dn = nn-x-y-z 
            # print(f"nn<{nn}> st<{st}> x<{x}> y<{y}> z<{z}> xyz<{x+y+z}> dn<{dn}>")
            if   dn >= (sx-sz)//sz and x>0: # 9 xz
                x -= 1      # размен x
                z += sx//sz # размен z 
            elif dn >= (sy-sz)//sz and y>0: # 4 yz
                y -= 1      # размен y
                z += sy//sz # размен z 
            elif dn >= (sx-sy)//sy and x>0: # 1 xy
                x -= 1      # размен x
                y += sx//sy # размен y 
            elif z >= sx//sz and dn < 0:    # -9 xz
                x += 1      # размен x
                z -= sx//sz # размен z 
            elif z >= sy//sz and dn < 0:    # -4 yz
                y += 1      # размен y
                z -= sy//sz # размен z 
            elif y >= sx//sy and dn < 0:    # -1 yz
                x += 1      # размен x
                y -= sx//sy # размен y 
            else: 
                x, y, z = -1, -1, -1    # решений нет (недостаточно монет для st)
                # print("не могу произвести размен")
                break
            # count += 1
            # if (count > 10): 
                # print("count > 10")
                # break
else: print("ERROR: I don’t know what’s going on here.")

# Результат
print(x, y, z)