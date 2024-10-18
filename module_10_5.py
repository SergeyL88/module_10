from datetime import datetime
from multiprocessing import Pool


def read_info(name) -> list:
    all_data: list = []
    for file in name:
        with open('./file 1.txt', 'r') as file_:
            print(file)
            while file_.readline():
                all_data.append(file_.readline())


if __name__ == '__main__':
    file_names = [f'./file {num}.txt' for num in range(1, 5)]

    start = datetime.now()
    read_info(file_names)
    stop = datetime.now()
    duration = stop - start
    print(f'{duration} линейный')


    with Pool(processes=12) as pool:
        start = datetime.now()
        pool.map(read_info, (file_names,))
    stop = datetime.now()
    duration = stop - start
    print(f'{duration} многопроцессный')
