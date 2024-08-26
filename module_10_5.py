import multiprocessing
import datetime
files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data)


# start_1 = datetime.datetime.now()
# for file in files:
#     read_info(file)
# end_1 = datetime.datetime.now()
# print(f'{end_1 - start_1}(линейный)')


if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')


