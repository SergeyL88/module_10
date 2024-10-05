from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count: int, file_name: str):
    for iter in range(1, word_count+1):
        with open(file_name, 'a') as file_:
            file_.write(f'Какое-то слово № {iter}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


file_1 = Thread(target=write_words, args=(10, 'example1.txt'))
file_2 = Thread(target=write_words, args=(30, 'example2.txt'))
file_3 = Thread(target=write_words, args=(200, 'example3.txt'))
file_4 = Thread(target=write_words, args=(100, 'example4.txt'))

start_time = datetime.now()

file_1.start()
file_2.start()
file_3.start()
file_4.start()

file_1.join()
file_2.join()
file_3.join()
file_4.join()

stop_time = datetime.now()
print(f'Работа потоков {stop_time - start_time}')


file_5 = Thread(target=write_words, args=(10, 'example5.txt'))
file_6 = Thread(target=write_words, args=(30, 'example6.txt'))
file_7 = Thread(target=write_words, args=(200, 'example7.txt'))
file_8 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = datetime.now()

file_5.start()
file_6.start()
file_7.start()
file_8.start()

file_5.join()
file_6.join()
file_7.join()
file_8.join()

stop_time = datetime.now()
print(f'Работа потоков {stop_time - start_time}')
