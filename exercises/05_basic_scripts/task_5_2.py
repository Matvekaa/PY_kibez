# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def draw(l):
	for i in l:
		print(i.ljust(10), end='')
		print('  ', end='')
	print()
	

ip_str, mask_str = input('введите IP-сети: ').split('/')
ip_list = [i for i in ip_str.split('.')]
print('Network:')
draw(ip_list)
ip_bin_list = [str(bin(int(i)))[2:].rjust(8, '0') for i in ip_list]
draw(ip_bin_list)
print('Mask:\n/' + str(mask_str))

mask_str_bin = ('1' * int(mask_str)) + ('0' * (32 - int(mask_str)))
mask_list_oct = [mask_str_bin[i * 8:(i + 1) * 8]for i in range(4)]
mask_list_int = [str(int(i, 2)) for i in mask_list_oct]
draw(mask_list_int)
draw(mask_list_oct)
