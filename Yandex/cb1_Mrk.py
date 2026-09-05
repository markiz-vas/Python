import sys

# main 
n = int(sys.stdin.readline())
h, m, s = 0, 0, 0
alls = 0 # общее количество секунд

# суммируем секунды
for _ in range(n):
    mm, ss = sys.stdin.readline().split(":")
    alls += int(mm)*60 + int(ss)
    # print(int(mm), int(ss), alls)

# Вычисляем часы, минуты, секунды
h = alls//3600
m = alls%3600//60
s = alls-h*3600-m*60
print(f"{'0' if h<10 else ''}{h}:{'0' if m<10 else ''}{m}:{'0' if s<10 else ''}{s}")    
