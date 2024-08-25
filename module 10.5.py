# Задача "Многопроцессное считывание":

import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        line = file.readline()
        all_data.append(line)
        if not line:
            break
    file.close


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.

# Линейный вызов
# time_start = datetime.now()
# for i in filenames:
#    read_info(i)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(time_res)

# Многопроцессный
if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)