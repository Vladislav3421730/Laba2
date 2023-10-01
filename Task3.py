import random
import pyautogui
pyautogui.moveTo(500, 800)
def find_first_negative_row(matrix):
    for i, row in enumerate(matrix):
        if all(element < 0 for element in row):
            return i
    return -1

def made_matrix():
    try:
        cols = int(input("Введите количество строк матрицы : "))
        rows = int(input("Введите количество столбцов матрицы : "))
    except ValueError:
        print("Вы неправильно ввели значения")
        exit(-1)
    matrix1 = [[random.randint(-10, 5) for i in range(cols)] for j in range(rows)]
    return matrix1

our_matrix = made_matrix()
for col in our_matrix:
        print(col)
index = find_first_negative_row(our_matrix)
if index != -1:
    negative_row = our_matrix[index]
    row_sum = sum(negative_row)
    print(f"Первая строка с отрицательными элементами: {negative_row}")
    print(f"Сумма элементов этой строки: {row_sum}")
else:
    print("В матрице нет строки, в которой все элементы отрицательны.")
