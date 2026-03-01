import random
import time

coins = 100

def game():
    print("Включать подсказки?", '\n', "1 - ДА", '\n', "2 - НЕТ")
    helps_toggle = get_number("Ответ: ")

    radius = get_number("Число в радиусе: ")
    while radius > 100:
        print("Радиус должен быть меньше 100!")
        radius = get_number("Число в радиусе: ")

    trys = get_number("Количество попыток: ")
    while trys > 100:
        print("Попытки должныть быть меньше 100!")
        trys = get_number("Количество попыток: ")

#----------------------------------------------------------------
    randNum = random.randint(0, radius)

    start_time = time.perf_counter()
    time.sleep(60)
    end_time = time.perf_counter()

    execution_time = int(end_time - start_time)

    while True:
        ans = get_number("Введите число: ")

        if ans == randNum:
            print("вы выиграли!, вы угадали число за", 60 - execution_time, "секунд")
            menu()

        elif trys == 1 or execution_time == 60:
            print("Вы проиграли(")
            menu()

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

def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка! Пожалуйста, введите число!")

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



