from multiprocessing import Pool
import time


def read_info(name:str):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            r = file.readline()
            all_data.append(r)
            if r == '':
                break

def count_time():
    start_time = time.time()
    yield
    end_time = time.time()
    result_time = round(end_time - start_time, 2)
    print(f'Время выполнения программы: {result_time}.')


files = [f'./file {n}.txt' for n in range(1, 5)]
#Линейный вызов
if __name__ == '__main__':
    for _ in count_time():
        for _ in (read_info(f) for f in files):
            pass


#Многопроцессный
    for _ in count_time():
        with Pool(8) as p:
            p.map(read_info, files)


