import time
import multiprocessing

def  read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    files_list = [f'./file {number}.txt' for number in range(1, 5)]

    start_time_linear = time.time()
    for name in files_list:
        read_info(name)
    end_time_linear = time.time()
    print(f'Время выполнения линейного вызова: {end_time_linear - start_time_linear:.6f} секунд')

    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files_list)
    end = time.time()
    print(f'Время выполнения многопроцессного вызова: {end - start:.6f} секунд')
