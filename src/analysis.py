def check_data(data: list[float]) -> bool:
    """
    Перевіряє, чи список даних не порожній.
    
    :param data: список числових значень
    :return: True, якщо дані є, інакше False
    """
    if not data:
        print("Помилка: Список даних порожній. Неможливо виконати обчислення.")
        return False
    return True

def calc_average(data: list[float]) -> float:
    """
    Обчислює середнє арифметичне списку чисел.
    
    :param data: список числових значень.
    :return: середнє арифметичне
    """
    if not check_data(data):
        return 0.0
    return sum(data) / len(data)

def calc_median(data: list[float]) -> float:
    """
    Обчислює медіану списку чисел.
    
    :param data: список числових значень.
    :return: медіана
    """
    if not check_data(data):
        return 0.0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    return sorted_data[mid]

def calc_minimum(data: list[float]) -> float:
    """
    Знаходить мінімальне значення у списку.
    
    :param data: список числових значень.
    :return: мінімальне число
    """
    if not check_data(data):
        return 0.0
    return min(data)

def calc_maximum(data: list[float]) -> float:
    """
    Знаходить максимальне значення у списку.
    
    :param data: список числових значень.
    :return: максимальне число
    """
    if not check_data(data):
        return 0.0
    return max(data)