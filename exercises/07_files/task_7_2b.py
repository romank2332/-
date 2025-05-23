# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv

ignore = ["duplex", "alias", "configuration"]

a_file, b_file = argv[1], argv[2]

with open(a_file) as a, open(b_file, 'w') as b:
    for line in a:
        slova =line.split()
        slova_intersect = set(slova) & set(ignore)
        if not line.startswith("!") and not slova_intersect:
            b.write(line)