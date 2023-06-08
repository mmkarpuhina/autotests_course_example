# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import pytest
from datetime import datetime


@pytest.fixture()
def all_time():
    start_time = datetime.now()
    print(f'\n Начало выполнения {start_time}')
    yield
    end_time = datetime.now()
    print(f'\n Конец выполнения {end_time}')


@pytest.fixture()
def work_time():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    our_time = end_time - start_time
    print(f"\n Время выполнения {our_time}")
