# Шифр Цезаря (AveCaesar)
# В Русском языке нет буквы Ё и даже нет буквы ё. Всем Ave Caesar
# Ы Ймккгзе шафгю жюл ъмгыф Ё б эщяю жюл ъмгыф ё. Ыкюе Ave Caesar

# Проверка на валидность ответа Да/Нет
def isValidQ(txt):
    txt = txt.strip()
    if txt.lower() in answers_y or txt.lower() in answers_n or txt.lower() in answers_q: return True
    else: return False
# Проверка на валидность сдвига
def isValidN(txt):
    txt = txt.strip()
    if txt[0] == "-": txt = txt[1:] # знак '-' допустим первым символом в числе
    if txt.isdigit(): return True
    else: return False
# Функция кодирования Шифр Цезаря
def AveCaesar(txt, sdvig, isRus):   # txt - исходный текст, sdvig - величина сдвига, isRus - Русский или Английский
    shifr = ""
    for c in txt:
        t = ord(c)                      # Получаем цифровой код символа
        if isRus:                       # Русский язык
            if AnR <= t <= ZnR:         # Нижний регистр
                t += sdvig              # Сдвиг
                if t > ZnR: t -= dR     # Корректировка, если вышли за границу диапазона
            elif AvR <= t <= ZvR:       # Верхний регистр
                t += sdvig              # Сдвиг
                if t > ZvR: t -= dR     # Корректировка, если вышли за границу диапазона
        else: # not isRus               # Английский язык
            if AnE <= t <= ZnE:         # Нижний регистр
                t += sdvig              # Сдвиг
                if t > ZnE: t -= dE     # Корректировка, если вышли за границу диапазона
            elif AvE <= t <= ZvE:       # Верхний регистр
                t += sdvig              # Сдвиг
                if t > ZvE: t -= dE     # Корректировка, если вышли за границу диапазона
        shifr += chr(t)                 # Переводим цифровой код символа в символ и добавляем его к шифру
    return shifr

# main (Определение переменных)
answers_y = ["да" , "y", "yes", "encrypt", "ru", "rus", "рус", "русский", "зашифровать"]
answers_n = ["нет", "n", "no" , "decrypt", "eng", "engl", "англ", "английский", "расшифровать"]
answers_q = ['q', 'quit', 'exit', 'вых', 'выход', 'конец', 'вых.', 'казнить']
isExit = False
isValid = False
qw = ""         # Ответы на задаваемые вопросы
sdvig = 0       # Величина сдвига (шаг шифра)
isRus = True    # True - Русский # False - Английский
isShifr = True  # True - Шифруем # False - Рассшифровываем
AnE, ZnE = ord('a'), ord('z')   # Границы таблицы символов в Английском языке нижний регистр
AvE, ZvE = ord('A'), ord('Z')   # Границы таблицы символов в Английском языке верхний регистр
AnR, ZnR = ord('а'), ord('я')   # Границы таблицы символов в Русском языке нижний регистр
AvR, ZvR = ord('А'), ord('Я')   # Границы таблицы символов в Русском языке верхний регистр
dE = ZnE - AnE + 1  # Количество символов в Английском языке
dR = ZnR - AnR + 1  # Количество символов в Русском языке
text    = ""    # Исходный текст (расшифрованный)
shifr   = ""    # Зашифрованный текст

# for i in range(27):
#    print("0" if i<10 else "", i, " - ", AveCaesar('Hawnj pk swhg xabkna ukq nqj.', i, False), sep="")
#isExit = True



# main (Определение переменных)
while not isExit:
    print('Добрый день, я "Шифр Цезаря", программа по зашифровыванию текста.')
    print(f'Для выхода из программы напишите "Выход", "q", "Quit", "Exit", или "Конец" ')
    
    # Шифрование или расшифровка
    while not isValid:
        qw = input('\nЖелаете ли вы зашифровать [Да/encrypt] или расшифровать [Нет/decrypt] текст?  ')
        if not isValidQ(qw): print("Проверка ответа не прошла.")
        else: break
    if qw.lower() in answers_q or isExit: isExit  = True     # Выход 
    if qw.lower() in answers_y or isExit: isShifr = True     # Шифруем
    if qw.lower() in answers_n or isExit: isShifr = False    # Расшифровываем
    if not isExit:
        if isShifr: print(f'Перехожу в режим зашифровывания (encrypt) текста.  <{qw}>')
        else:       print(f'Перехожу в режим расшифровывания (decrypt) текста.  <{qw}>')

    # Русский или Английский алфавит
    while not isValid and not isExit:
        qw = input('\nИспользуем Русский [Да/Ru] или Английский [Нет/Eng] алфавит?  ')
        if not isValidQ(qw): print("Проверка ответа не прошла.")
        else: break
    if qw.lower() in answers_q or isExit: isExit  = True     # Выход 
    if qw.lower() in answers_y or isExit: isRus   = True     # Русский
    if qw.lower() in answers_n or isExit: isRus   = False    # Английский
    if not isExit:
        if isRus:   print(f'Работаю с Русским алфавитом. Всего {dR} символа. Букву Ё игнорирую.  <{qw}>')
        else:       print(f'Работаю с Английским алфавитом. Всего {dE} символов. <{qw}>')

    # Сдвиг
    while not isValid and not isExit:
        qw = input('\nВведите сдвиг шифра:  ')
        if qw.lower() in answers_q: break   # Выход
        if not isValidN(qw): print("Проверка ответа не прошла.")
        else: break
    if qw.lower() in answers_q or isExit: isExit  = True     # Выход 
    else: 
        sdvig = int(qw)
        txt1 =  "закодированию" if isShifr else "расскодированию"
        txt2 =  "Русском"       if isRus   else "Английском"
        print(f'Я получил сдвиг <{sdvig}>. Готов к {txt1} на {txt2} языке. ', end="")
        # Обработка шифра (ширф всегда положителен и находится в границах длины алфавита)
        if not isShifr: sdvig *= -1 # Меняем знак сдвига
        d = dR if isRus else dE # Длина алфавита
        while sdvig <  0: sdvig += d # Приводим сдвиг к условию ( 0 <= sdvig < d)
        while sdvig >= d: sdvig -= d # Приводим сдвиг к условию ( 0 <= sdvig < d)
        print(f' <{sdvig}>\n')

    # Текст для обработки
    if not isExit:
        qw = input('\nВведите текст для обработки:  ')
    if qw.lower() in answers_q or isExit: isExit  = True     # Выход 
    else: 
        if isShifr: text  = qw
        else:       shifr = qw

    if not isExit:
        if isShifr: 
            print(f'\nТекст для закодирования: "{text}"')
            shifr = AveCaesar(text, sdvig, isRus)
            print(f'Получившийся шифр: "{shifr}"\n\n')
        else:       
            print(f'\n\Шифр для раскодирования: "{shifr}"')
            text = AveCaesar(shifr, sdvig, isRus)
            print(f'Получившийся текст: "{text}"\n\n')

    # Выход из бесконечного цикла
    if isExit:
        print(f"\nВыход. <{qw}>")
        isExit = True
        break
   
    # На новый цикл    
    print('\n')

print("\nШифровальщик Цезаря был казнён за допущенные ошибки. Ищите нового...")