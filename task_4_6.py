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


def my_count(start, end):
    for el in count(start):
        if el > end:
            break
        else:
            yield el



if 'h' in sys.argv[1:]:
    print('Введите начальное и конечное целые числа списка и число его повторений через пробел')
else:
    start_number, end_number, end_cycle = sys.argv[1:]
    # start_number, end_number = sys.argv[1:]
# start_number, end_number, end_cycle = 1, 10, 10
    my_list1 = [el for el in my_count(int(start_number), int(end_number))]
    print(my_list1)

    user_count = 0
    for el in cycle(my_list1):
        if user_count > int(end_cycle) - 1:
            break
        print(el)
        user_count += 1
