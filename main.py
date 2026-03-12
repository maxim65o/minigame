import random
import time
import threading

coins = 100

#функция таймера
def timer():
    while True:
        time.sleep(30)
        print("Вы проиграли!")
        menu()
        t.cancel()

t = threading.Thread(target=timer)

#проверка ввода на число
def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка! Пожалуйста, введите число!")

def game():
    start = time.time()
#Задача параметров
    print("Включать подсказки?", '\n', "1 - ДА", '\n', "2 - НЕТ")
    helps_toggle = get_number("Ответ: ")

    radius = get_number("Число в радиусе: ")
    while radius > 100 or radius < 10:
        print("Радиус должен быть меньше 100 и больше 10!")
        radius = get_number("Число в радиусе: ")

    stav = get_number("Введите ставку: ")
    while coins < stav:
        print("Недостаточно монет!")
        stav = get_number("Введите ставку: ")

    trys = random.uniform(radius / 2, radius)
    trys = round(trys)

#основной модуль
    randNum = random.randint(0, radius)

    t = threading.Thread(target=timer)
    t.start()
    while True:
        ans = get_number("Введите число: ")

        if ans == randNum:
            win(start, stav)
            menu()
            t.cancel()

        elif trys == 0:
            print("Вы проиграли!")
            menu()
            t.cancel()

        else:
            if helps_toggle == 1:
                help = 0
                if randNum < ans:
                    help = "меньше"

                if randNum > ans:
                    help = "больше"

                print("Ты не угадал, загаданное число", help, ",но у тебя еще", trys, "попыток")
                trys -= 1
            else:
                print("Ты не угадал загаданное число, но у тебя еще", trys, "попыток")
                trys -= 1
                continue

def win(start_time, stavk):
    win_time = time.time() - start_time
    win_time = round(win_time)
    bonus = 50

    if win_time < 15:
        bonus -= win_time * 2

    else:
        bonus = 0

        bonus -= (win_time - 15) * 2

    winer = stavk * 2 + stavk / 100 * bonus
    winer = round(winer)

    coins =+ winer

    print('\n', "ваш выигрыш:", winer)
    print(" Ваш бонус:", bonus)
    print(" Вы выиграли за", win_time, "секунд")
    print(" Ваш баланс:", coins - stavk + winer, '\n')

#меню
def menu():
    while True:
        print("Привет, это игра - угадай число, здесь ты должен угадывать число в выбранном диапозоне")

        print('\n', "1 - ИГРАТЬ", '\n' ,"2 - СТОП", '\n' " 3 - ПРОФИЛЬ")

        choise = input("Выберите действие: ")

        if choise == '1':
            game()

        if choise == '2':
            break

        if choise == '3':
            print("баланс:",  coins)




menu()




