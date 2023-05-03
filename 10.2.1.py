try:
    BRUCE_WILLIS = 42

    input_data = input('Введите строку: ')

    leeloo = int(input_data[4])

    result = BRUCE_WILLIS / leeloo

    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError as exc:
    print(type(exc), 'Невозможно преобразовать к числу')

except IndexError as exc:
    print(type(exc), 'Выход за границы списка')

except Exception as exc:
    print(type(exc), 'Поймано исключение')
