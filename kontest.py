from datetime import datetime
import multiprocessing

def read_info(name):
    all_data=[]
    with open(name, 'r') as file:
        k = file.readline()
        while k != '':
            all_data.append(k)
            k = file.readline()


start = datetime.now()
read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')
end = datetime.now()
print(end - start)
filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)
