from datetime import datetime
import multiprocessing

def read_info(name):
    all_data=[]
    with open(name, 'r') as file:
        k = file.readline()
        while k != '':
            all_data.append(k)
            k = file.readline()

if __name__ == '__main__':
    start = datetime.now()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    end = datetime.now()
    time=end - start
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    a = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    b = datetime.now()
    print(time)
    print(b-a)
