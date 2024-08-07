import os
import time
import multiprocessing


def read_info(name):
    all_data = list()
    for file in os.listdir():
        if file == name:
            with open(file, mode='r', encoding='utf8') as opened_file:
                while True:
                    line = opened_file.readline()
                    all_data.append(line)
                    if not line:
                        break


if __name__ == '__main__':
    start_time = time.time()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    print(round((time.time() - start_time), 2))  # 8.9

    all_files = [
        'file 1.txt',
        'file 2.txt',
        'file 3.txt',
        'file 4.txt'
    ]

    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, all_files)
    print(round((time.time() - start_time), 2))  # 6.85
