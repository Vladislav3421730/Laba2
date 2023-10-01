import pyautogui
pyautogui.moveTo(500,800)
def divide(a, b):
    try:
        result = a // b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: неверный тип данных!")
        return None
    else:
        print("Результат:", result)
        return result
    finally:
        print("Завершение блока try-except-finally")

while True:
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        result = divide(num1, num2)
        if result is not None:
            print("Результат деления:", result)
    except ValueError:
        print("Ошибка: введите целое число!")
    finally:
        response = input("Хотите продолжить (да/нет)? ")
        if response != "да":
            print("Программа завершена.")
            break
