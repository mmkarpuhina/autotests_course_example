# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47
import datetime


def func_log(file_log='log.txt'):
    """
    Дозаписывает в файл имя вызываемой функции, дату и время вызова.
    :param file_log: По умолчанию задан файл 'log.txt'
    :return: Имя функции, дата, время выполнения по заданному формату в заданном файле.
"""
    def name(funk_name):
        def wrapper():
            with open(file_log, mode='a', encoding='utf-8') as f:
                present_time = datetime.datetime.now()
                format_present_time = present_time.strftime('%d.%m %H:%M:%S')
                f.writelines(f'{funk_name.__name__} вызвана {format_present_time}\n')
        return wrapper
    return name


@func_log()
def func1():
    pass


@func_log(file_log='func2.txt')
def func2():
    pass


func1()
func2()
func1()
