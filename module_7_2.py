def custom_write(file_name, strings):             # создаем функцию
    strings_positions = {}                        # создаем список для строк
    file = open(file_name, 'w', encoding='utf-8') # открываем файл для записи с кодировкой
    for i, j in enumerate(strings, 1):            # условие для функции пронумерованного объекта
            post = file.tell()                    # выставляем номер байта начало строки
            file.write(j + '\n')                  # записываем файл
            strings_positions[(i, post)] = j      # записываем результат в виде кортежа
    return strings_positions                      # возвращаем результат в виде словаря


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)