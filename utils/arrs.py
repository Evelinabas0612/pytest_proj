"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """
    if index < 0:
        return default
    elif len(array) == 0:
        return default
    elif type(array) is not list:
        return "Отсутствует список"
    elif type(index) is not int:
        return "Индекс не целое число"
    elif array[index] is None:
        return "В списке элемент None"

    return array[index]


def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    if type(normalized_start) is not int:
        return "Начальный индекс не целое число"

    if type(normalized_end) is not int:
        return "Конечный индекс не целое число"

    if type(coll) is not list:
        return "Отсутствует список"

    return coll[normalized_start:normalized_end]
