from utils import arrs
import pytest

# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def fixt(): # имя фикстуры любое
    return [1, 2, 3]

def test_get(fixt):
    assert arrs.get(fixt, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get("None", 0, "test") == "Отсутствует список"
    assert arrs.get(fixt, 5.4, "test") == "Индекс не целое число"
    assert arrs.get([1, 2, "python"], 2, "test") != "test"
    assert arrs.get([1, 2, None], 2, "test") == "В списке элемент None"
    assert arrs.get(fixt, -1) == None






def test_slice(fixt):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(fixt, 1) == [2, 3]
    assert arrs.my_slice(fixt, 1.1, 3) == "Начальный индекс не целое число"
    assert arrs.my_slice(fixt, 1, 3.1) == "Конечный индекс не целое число"
    assert arrs.my_slice("None", 1, 3) == "Отсутствует список"
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(fixt, -1) == [3]
    assert arrs.my_slice(fixt, 1, -3) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, -3) == []
    assert arrs.my_slice([1, 2], -3, -1) == [1]
    assert arrs.my_slice([1, 2, "test", 3], 1, 3) == [2, "test"]

