'''
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
'''

from itertools import count, cycle
import sys


def my_count(start_number, end_number):
    for el in count(start_number):
        if el > end_number:
            break
        else:
            yield el


if 'h' in sys.argv[1:]:
    print('Введите начальное и конечное целые числа через пробел')
else:
    start_number, end_number = sys.argv[1:]
    my_list = [el for el in my_count(int(start_number), int(end_number))]
    print(my_list)


