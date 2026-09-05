# Генератор паролей
from random import random, randint, choice, shuffle

# Проверка на валидность ответа Да/Нет
def isValidQ(txt):
    if txt.lower() in answers_y or txt.lower() in answers_n or txt.lower() in answers_q: return True
    else: return False
# Проверка на валидность длины пароля (от 4 символов)
def isValidN(txt):
    if txt.isdigit(): 
        n = int(txt)
        if n >= 4: return True
        else: return False
    else: return False


# main (Определение переменных)
answers_y = ["да" , "y", "yes"]
answers_n = ["нет", "n", "no" ]
answers_q = ['q', 'quit', 'exit', 'вых', 'выход', 'конец', 'вых.']
vard = "0123456789"                 # digits
varl = "abcdefghijklmnopqrstuvwxyz" # lowercase_letters
varu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # uppercase_letters
varp = "!#$%&*+-=?@^_"              # punctuation
lenpass = 8;    # Длина пароля
var = "" # Набор символов для пароля
isExit = False
isValid = False
dlaplen = "11118" # Пароль по умолчанию [цифры,нижний,верхний,спец,цлина]
qw = "" # Ответы на задаваемые вопросы

# main (Определение переменных)
while not isExit:
    print("Добрый день, я генаратор паролей.")
    print("Могу создать пароль любой длины и сложности.")
    print(f'Для выхода из программы напишите "Выход", "q", "Quit", "Exit", или "Конец" ')
    print(f"По умолчанию пароль длиной {lenpass} символов, содержит цифры, символы в верхнем и нижнем регистре и специальные символы.")
    
    # Проверка на необходимость настройки сложности пароля
    while not isValid:
        qw = input('\nЖелаете ли вы создать такой пароль? [Да/Нет]')
        if not isValidQ(qw): print("\nПроверка ответа не прошла. Попробуйте ответить снова.")
        else: break

    # Настройка маски пароля
    if qw.lower() in answers_n:
        dlaplen = ""
        print(f"\nНастройка пароля. <{dlaplen}> <{qw}>")
        
        # Цифры
        while not isValid and not isExit:
            qw = input('\nЖелаете ли вы включить в пароль цифры? [Да/Нет]')
            if not isValidQ(qw): print("\nПроверка ответа не прошла.")
            else: break
        if qw.lower() not in answers_q:
            if qw.lower() in answers_y: dlaplen += "1"
            if qw.lower() in answers_n: dlaplen += "0"
        else: isExit = True
            
        # Нижний
        while not isValid and not isExit:
            qw = input('\nЖелаете ли вы включить в пароль нижний регистр? [Да/Нет]')
            if not isValidQ(qw): print("\nПроверка ответа не прошла.")
            else: break
        if qw.lower() not in answers_q:
            if qw.lower() in answers_y: dlaplen += "1"
            if qw.lower() in answers_n: dlaplen += "0"
        else: isExit = True
            
        # Верхний
        while not isValid and not isExit:
            qw = input('\nЖелаете ли вы включить в пароль верхний регистр? [Да/Нет]')
            if not isValidQ(qw): print("\nПроверка ответа не прошла.")
            else: break
        if qw.lower() not in answers_q:
            if qw.lower() in answers_y: dlaplen += "1"
            if qw.lower() in answers_n: dlaplen += "0"
        else: isExit = True
            
        # Спец
        while not isValid and not isExit:
            qw = input('\nЖелаете ли вы включить в пароль специальные символы? [Да/Нет]')
            if not isValidQ(qw): print("\nПроверка ответа не прошла.")
            else: break
        if qw.lower() not in answers_q:
            if qw.lower() in answers_y: dlaplen += "1"
            if qw.lower() in answers_n: dlaplen += "0"
        else: isExit = True
            
        # Длина
        while not isValid and not isExit:
            qw = input('\nКакой длины должн быть пароль? [число не менее 4]')
            if not isValidN(qw): print("\nПроверка ответа не прошла.")
            else: break
        if qw.lower() not in answers_q:
            dlaplen += qw
        else: isExit = True

        # Маска пароля
        if qw.lower() not in answers_q:
            print(f"\nНастройка пароля завершена. <{dlaplen}> <{qw}>")
        else: isExit = True

    # Генерация пароля по умолчанию
    elif qw.lower() in answers_y:
        dlaplen = "11118"
        print(f"\nГенерация пароля по умолчанию. <{dlaplen}> <{qw}>")

    # Выход из Генератора паролей
    if qw.lower() in answers_q or isExit:
        print(f"\nВыход. <{qw}>")
        isExit = True
        break
    
    # Приступаем к генерации пароля
    simbols = ""
    password = ""
    if dlaplen[:4] == "0000":
        print("Пароль не может быть пустым! Попробуйте заново.")
    else:
        # Генерация пароля
        if dlaplen[0] == "1": 
            simbols += vard
            password += choice(vard)
        if dlaplen[1] == "1": 
            simbols += varl
            password += choice(varl)
        if dlaplen[2] == "1": 
            simbols += varu
            password += choice(varu)
        if dlaplen[3] == "1": 
            simbols += varp
            password += choice(varp)
        lenpass = int(dlaplen[4:])
        print(simbols)
        print(password, lenpass)
        # Генерируем пароль в цикле
        while len(password) < lenpass:
            password += choice(simbols)
        # Перемешиваем пароль (shuffle не работает со строками, поэтому ничего не перемешиваем)
        print(password, lenpass)

        # Вывод пароля        
        print(f'\nВаш сгенерированный пароль "{password}" длиной {lenpass} символов.\n')
        
        #Запрос на генерацию нового пароля
        while not isValid:
            print(f'Для выхода напишите "Выход", "q", "Quit", "Exit", или "Конец"')
            qw = input('\nЖелаете ли вы создать новый пароль? [Да/Нет]')
            if not isValidQ(qw): print("\nПроверка ответа не прошла.")
            else: break
        
        # Выход из Генератора паролей
        if qw.lower() in answers_q or qw.lower() in answers_n:
            print(f"\nВыход. <{qw}>")
            isExit = True
            break
    
    # На новый цикл    
    print('\n')

print("\nПрограмма генерации паролей закончила работу. До будущих встреч.")
    
