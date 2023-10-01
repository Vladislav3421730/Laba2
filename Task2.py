import pyautogui
pyautogui.moveTo(500, 800)

def function_for_task2(argument):
    if isinstance(argument, list):
            unique_list = list()
            for item in argument:
                if item not in unique_list:
                    unique_list.append(item)
            argument = unique_list
            print(f'Список после удаления повторяющихся элементов {argument}')
            try:
                index = -1
                for el in argument:
                    if el > 0:
                        index = argument.index(el)
                        break
                if index == -1:
                    print("В списке нет положительных элементов")
                elif index == len(argument) - 1:
                    print("Положительный элемент был последним")
                elif index != -1:
                    sum_of_elements = 0
                    for i in range(index + 1, len(argument)):
                        sum_of_elements = sum_of_elements + argument[i]
                print(f'Сумма элементов после первого положительного {sum_of_elements}')
            except TypeError:
                print(" В листе есть элементы типа string, найти сумму невозможно")
    elif isinstance(argument, dict):
        try:
            argument = dict(sorted(argument.items(), key=lambda x: x[1], reverse=True))
        except TypeError:
            print("Значения словаря содержать элементы типа string, сортирвка невозможна")
        print(argument)
    elif isinstance(argument, int):
        if argument == 1:
            print("Число равно одному")
            return
        result = 0
        for i in range(1, argument):
            if argument % i == 0:
                result = result + 1
        if result == 1:
            print(f'Число {argument} является простым')
        else:
            print(f'Число {argument} не является простым')
    elif isinstance(argument, str):
        print(argument)
        argument = [ord(char) for char in argument]
        print("Строка в Unicode")
        print(argument)


function_for_task2([1, 3, 34, 23, 4, 3, 2])
function_for_task2(['f', 'g', 3, 3, 'g', 9])
function_for_task2({1: 3, 3: 9, 5: 4, 3: 7, 6: 3 })
function_for_task2(67)
function_for_task2(23)
function_for_task2("Hellow world")
function_for_task2("Hellow python")