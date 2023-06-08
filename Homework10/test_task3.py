# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
            pytest.param(-6, -2, 3, marks=pytest.mark.skip('Нельзя вводить отрицательные значения')),
            pytest.param(5, 5, 1),
            ], ids=['skip',
                    'smoke'])
def test_all(a, b, result):
    assert all_division(a, b) == result
