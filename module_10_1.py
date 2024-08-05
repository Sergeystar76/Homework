from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count):
            file.write(f'Какое-то слово № {word}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()
th_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
th_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
th_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
th_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

th_1.start()
th_2.start()
th_3.start()
th_4.start()

th_1.join()
th_2.join()
th_3.join()
th_4.join()


time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')