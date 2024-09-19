from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
ret=lambda fort, dort: fort==dort
result=list(map(ret, first, second))
print(result)
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for i in range(len(data_set)):
            with open(file_name, 'a') as file:
                if i!=0:
                    file.write('\n'+str(data_set[i]))
                elif i==0:
                    file.write(str(data_set[i]))
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
class MysticBall:
    def __init__(self, *spisok):
        self.spisok=spisok
    def __call__(self, *spisok):
        return choice(self.spisok)
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
