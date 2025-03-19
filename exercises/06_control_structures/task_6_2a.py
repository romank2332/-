# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_adr = input("Enter ip address: ")
chasti = ip_adr.split(".")
correct_ip = True

if len(chasti) != 4:
    correct_ip = False
else:
    for octet in chasti:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Неправильный IP-адрес")
else:
    chasti_num = [int(i) for i in chasti]

    if chasti_num[0] in range(1, 224):
        print("unicast")
    elif chasti_num[0] in range(224, 240):
        print("multicast")
    elif ip_adr == "255.255.255.255":
        print("local broadcast")
    elif ip_adr == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")