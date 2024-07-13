def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, mode='r+', encoding='utf-8')
    line = 1
    for string in strings:
        strings_positions[(line, file.tell())] = string
        file.write(string + '\n')
        line += 1
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)