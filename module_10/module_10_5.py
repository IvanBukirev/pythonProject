import time
from multiprocessing import Pool


def read_info(name):
    all_data=[]
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line=f.readline()
            if not line:
                break
            else:
                all_data.append(line)

filenames = [f'file {number}.txt' for number in range(1, 5)]

# start_time1 = time.time()
# for filename in filenames:
#     read_info(filename)
# print(f'время выполнения программы линейным способом: {time.time() - start_time1}') #11.031212091445923

if __name__ == '__main__':
    start_time2 = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(f'время выполнения программы с использованием мультипроцессора: {time.time() - start_time2}') #3.236698627471924

