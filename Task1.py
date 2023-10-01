def function_for_counting_terms():
    total = 0
    number = 0
    while total < 4:
        total = total + 1 / (number + 1)
        number = number + 1
    return number

print(f'Количество слагаемых в - {function_for_counting_terms()}')