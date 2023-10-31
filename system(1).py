import random, time, sys
from tqdm import tqdm
import random as rdm

print("  ___  __       _    __  ___")
print(" /  / /_ / /,/ /_/  /_    / ")
print("/  / /    /'/ /__/ /__   /  ")
ram = int(input("Сколько вы хотите выделить оперативной памяти в КБ: "))
rom = int(input("Сколько вы хотите выделить памяти в КБ: "))
svozr = int(input("Введите ваш возраст: "))
time.sleep(0.1)
print("Загрузка данных:")
for i in tqdm(range(ram)):
    time.sleep(0.1)
print("Подготовка рабочего места:")
for i in tqdm(range(rom)):
    time.sleep(0.1)
print("Загрузка данных:")
for i in tqdm(range(341)):
    time.sleep(0.1)
sname = input("Введите ваше имя: ")
for i in tqdm(range(10)):
    time.sleep(0.1)
    print("загрузка данных пользователя")
for i in tqdm(range(9)):
    time.sleep(0.1)
if svozr > 6:
    for i in tqdm(range(10)):
        time.sleep(0.1)
    cmd = 0
    while cmd == cmd:
        cmd = input(sname + "~$: " )
        if cmd == "help":
            print("HELP - Помощ для тех, кто не разбирается,")
            print("или только начинает использовать эту сисьтему.")
            print("")
            print("RAM = " + ram)
            print("ROM = " + rom)
            print("")
            print("root - открытие панели разработчика")
            print("")
            print("sudo - комманды администратора")
            print("help - показать список комманд")
            print("progs - показать список всех программ")
            print("help sudo - показать список комманд администратора")
        if cmd == "help sudo":
            print("sudo update - перезагрузить сисьтему")
            print("sudo stop - выключить сисьтему")
            print("sudo cn - изменить имя")
        if cmd == "progs":
            print("bt - открыть игру BigTower")
            print("cm - открыть игру cjmpilator")
            print("ssl - открыть игру Камень Ножницы Бумага")
            print("np - открыть NotePad")
            print("tablo - создать таблицу")
            print("math - решить пример")
            print("cr - запустить программу ChangeRandomer")
            print("pg - открыть программу ProGarammer")
            print("time - запустить таймер на 1 минуту")
        if cmd == "sudo":
            print("пропиши help sudo для подробной информации")
        if cmd == "np":
            pr = 0
            while pr != "/stop":
                pr = input("NotePad: ")
                if pr == "/open":
                    print(pr)
                if pr == "/help":
                    print("/stop - закрыть Printer")
        if cmd == "math":
            print("Калькулятор ответ: ", eval(input("Калькулятор решение: ")))
        if cmd == "time":
            time.sleep(60)
            print("ВРЕМЯ ВЫШЛО!!!")
        if cmd == "sudo update":
            sys.argv
        if cmd == "sudo stop":
            sys.exit()
        if cmd == "pg":
            pg = 0
            txt = 0
            while pg != "/stop":
                pg = input("PG: ")
                if pg == "help":
                    print("print - печатать")
                    print("num - вписать цифру")
                    print("start - запустить программу")
                    print("stop - остановить программу")
                    print("/stop - закрыть ProGrammer")
                if pg == "print":
                    txt = input("PG:print: ")
                if pg == "num":
                    txt = int(input("PG:Num: "))
                if pg == "start":
                    ask = 0
                    while ask != "stop":
                        print(txt)
                        ask = str(input())
        if cmd == "cr":
            cr = 0
            rand = 0
            while cr != "/stop":
                cr = input("ChangeRandomer: ")
                if cr == "start":
                    rand = random.randint(1, 100)
                    print(rand)
                if cr == "help":
                    print("start - показ вашего шанса")
                    print("/stop - закрыть программу ChangeRandomer")
        if cmd == "stop":
            print("Не достаточно аргументов, чтобы выполнить данную комманду,")
            print("попробуйте использовать sudo!")
        if cmd == "bt":
            bt = 0
            player = 0
            text = 0
            while bt != "/stop":
                print("Добро пожаловать BigTower")
                time.sleep(0.3)
                print("Вы появились на входе у большой башни")
                print("1) Вы можете войти в нутро")
                print("2) Вы можете уйти от этой башни")
                bt = int(input("BigTower:  "))
                if bt == 2:
                    print("Первая концовка!")
                    bt = "/stop"
                if bt == 1:
                    print("Вы вошли в нутро! И видите 2 двери, со светом и без.")
                    time.sleep(0.3)
                    print("1) Вы можете пойти в дверь со светом")
                    print("2) Вы можете войти в дверь без света")
                    bt = int(input("BigTower:  "))
                    if bt == 1:
                        print("Вы встретили бабушку.")
                        time.sleep(0.3)
                        print("Она угостила вас пирогом, и отпустила домой.")
                        time.sleep(0.3)
                        print("Вторая концовка!")
                        bt = "/stop"
                    if bt == 2:
                        print("Вы видите подвал и Лестницу на второй этаж")
                        time.sleep(0.3)
                        print("1) Пойти в подвал")
                        print("2) Пойти по лестице")
                        bt = int(input("BigTower:  "))
                        if bt == 1:
                            print("Вы спустились в подвал, пройдя 5 метров увидили свет.")
                            time.sleep(0.3)
                            print("Это был выход!")
                            print("Третья концовка!")
                            bt = "/stop"
                        if bt == 2:
                            print("Вы поднялись по лестнице на 2,3,4 этаж.")
                            time.sleep(0.3)
                            print("Вы вышли на крышу!")
                            print("Вы увидили сундук!")
                            time.sleep(0.3)
                            print("1) Подойти и открыть сундук")
                            print("2) Спуститься по лестнице и уйти")
                            bt = int(input("BigTower:  "))
                            if bt == 2:
                                print("Вы ушли.")
                                print("Четвертая концовка!")
                                bt = "/stop"
                            if bt == 1:
                                print("Вы открыли сундук")
                                time.sleep(0.3)
                                print("В нем были сокровища!")
                                time.sleep(0.3)
                                print("1) Взять сокровища и выйти из башни.")
                                bt = int(input("BigTower:  "))
                                if bt == 1:
                                    print("О великий человек смог забрать сокровища!")
                                    time.sleep(0.3)
                                    print("Произнеси же своё имя!")
                                    bt = input("BigTower/Ваше имя:  ")
                                    time.sleep(1)
                                    print("О великий " + bt + " вы смогли одолеть страхи!")
                                    print("И тем самым овладели сокровищами!!!")
                                    print("УРА! Нашему победителю!")
                                    time.sleep(0.5)
                                    print("Поздравляем! Вы прошли игру на лучшую концовку!")
                                    bt = input("BigTower:  ")
        if cmd == "root":
            hp = input("Привет MaxL0Max, если это вы, то введите пароль: ")
            if hp == "#################":
                print("Добро пожаловать в Root SYSTEM!")
                root = 0
                while root != "rleave":
                    root = input("ROOT: ")
                    if root == "help":
                        print("Данные о сисьтеме:")
                        print("RAM = 2 MB")
                        print("Имя: MaxL0Max")
                        print("sys = root")
                        print("")
                        print("rleave - перейти в основной профиль")
                        print("stop - выключить сисьтему")
                        print("update - перезапустить сисьтему")
                        print("")
                    if root == "stop":
                        print("До свиданья!")
                        time.sleep(2)
                        sys.exit()
                    if root == "update":
                        print("Перезапуск.....")
                        time.sleep(2)
                        print("До свиданья!")
                        time.sleep(2)
                        root = "rleave"
            else:
                print ("Пароль неверный!")
        if cmd == "tablo":
            n1 = 0
            n2 = 0
            n3 = 0
            n4 = 0
            n5 = 0
            strs = int(input("Напишите количество столбцов от 1 до 5: "))
            tname = input("Напишите название таблицы: ")
            if strs == 5:
                n1 = input("Первый: ")
                n2 = input("Второй: ")
                n3 = input("Третий: ")
                n4 = input("Четвертый: ")
                n5 = input("Пятый: ")
                print(tname)
                print("1) " + n1)
                print("2) " + n2)
                print("3) " + n3)
                print("4) " + n4)
                print("5) " + n5)
            if strs == 4:
                n1 = input("Первый: ")
                n2 = input("Второй: ")
                n3 = input("Третий: ")
                n4 = input("Четвертый: ")
                print(tname)
                print("1) " + n1)
                print("2) " + n2)
                print("3) " + n3)
                print("4) " + n4)
            if strs == 3:
                n1 = input("Первый: ")
                n2 = input("Второй: ")
                n3 = input("Третий: ")
                print(tname)
                print("1) " + n1)
                print("2) " + n2)
                print("3) " + n3)
            if strs == 2:
                n1 = input()
                n2 = input()
                print(tname)
                print("1) " + n1)
                print("2) " + n2)
            if strs == 1:
                n1 = input()
                print(tname)
                print("1) " + n1)
        if cmd == "sudo cn":
            sname = input("Введите ваше имя: ")
            for i in tqdm(range(10)):
                time.sleep(0.3)
        if cmd == "ssl":
            razissl = 0
            compssl = 0
            plssl = 0
            nssl = 0
            pssl = 0
            porssl = 0
            summassl = 0
            while razissl != 3:
                plssl = str(input("Камень, ножницы или бумага?  >>>" ))
                razissl = (razissl + 1)
                compssl = rdm.randint(1, 3)
                if plssl == "камень":
                    plssl = 1
                if plssl == "ножницы":
                    plssl = 2
                if plssl == "бумага":
                    plssl = 3
                if plssl == compssl:
                    print("ничья!")
                    nssl = (nssl + 1)
                elif plssl == 1 and compssl == 2 \
                        or plssl == 2 and compssl == 3 \
                        or plssl == 3 and compssl == 1:
                    print("Победа!")
                    pssl = (pssl + 1)
                else:
                    print("Поражение...")
                    porssl = (porssl + 1)
            print("Выши результаты:")
            print("Ничьей: " + str(nssl))
            print("Побед: " + str(pssl))
            print("Поражений: " + str(porssl))
        if cmd == "cm":
            n = int(input("Введите количество слов:"))
            try:
                print("".join(input('cm: ')[-i] for i in range(1,n+1)))
            except:
                print(None)
else:
        dcmd = 0
        while dcmd == dcmd:
            dcmd = input("kid: ")
            if dcmd == "помощ":
                print("сн - пожелает вам спокойной ночи")
                print("игра - поиграть в игру")
                print("говорить - поговорить с компьютером")
                print("/стоп - остановить программу")
            if dcmd == "сн":
                print("Спокойной ночи малыш.")
                print("Off system")
                for i in tqdm(range(500)):
                    time.sleep(0.07)
                sys.exit()
            if dcmd == "игра":
                print("Загадай число от 1 до 10, а компьютер попытается отгадать!")
                play = 0
                chislo = 0
                while play != chislo:
                    time.sleep(1)
                    play = int(input("Игра: "))
                    chislo = random.randint(1, 10)
            if dcmd == "говорить":
                govor = 0
                while govor != "/стоп":
                    govor = input("разговорщик: ")
                    if govor == "привет":
                        print("Привет!")
                    if govor == "пока":
                        print("пока мой сладенький")
                    if govor == "кушать":
                        print("спроси об этом у мамочки")
                    if govor == "спать":
                        print("баю баюшки баю, не ложися на краю...")
                        for i in tqdm(range(500)):
                            time.sleep(0.07)
                        govor = "/стоп"
