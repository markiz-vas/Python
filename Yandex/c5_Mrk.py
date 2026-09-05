# cook your dish here
import sys, math

# main
res = "NO"
S = input()
T = input()
di = 0      # смещение
# print(S, T)
flag = False
for i in range(len(S)-1):
    if len(T) <= i+di+1: break          # строка T слижком короткая
    s0, s1 = S[i]   , S[i+1]
    t0, t1 = T[i+di], T[i+di+1]
    if (s0 != t0): break  # строки не совпадают
    # Если на предыдущем шаге соседние символы совпадали, а сейчас нет,
    # то производим смещение строки T (di++) вправо, пока t1 не будет совпадать с t0
    # if flag: print(flag, i, s0, s1)
    if flag: 
        if s0 != s1:
            # print(f"t0<{t0}> t1<{t1}> di<{di}>      lT<{len(T)}> i+di+1<{i+di+1}>")
            while t0 == t1 and len(T) > i+di+2:
                di += 1
                t1 = T[i+di+1]
                # print(f"i<{i}> s0<{s0}> s1<{s1}> di<{di}> t0<{t0}> t1<{t1}> lT<{len(T)}> i+di+1<{i+di+1}>")
    flag = True if s0 == s1 else False # соседние символы совпадают ?
    
    # Проверяем конец строки S
    if flag and i == len(S)-2:
        while t0 == t1 and len(T) > i+di+2:
                di += 1
                t1 = T[i+di+1]
    if i == len(S)-2:        
        if (s1 != t1): break # строки не совпадают
    
    # print(f"i<{i}> s0<{s0}> s1<{s1}> di<{di}> t0<{t0}> t1<{t1}> f<{flag}> lS<{len(S)}> lT<{len(T)}>")
else: res = "YES"
# print(len(S), len(T)-di, len(T), di)
if len(S) < len(T)-di: res = "NO"

# Результат
print(res)