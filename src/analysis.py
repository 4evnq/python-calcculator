def check_data(data: list[float]) -> bool:
    """Перевіряє, чи не порожній список даних."""
    if not data:
        print("Помилка: Список даних порожній. Неможливо виконати обчислення.")
        return False
    return True

def calc_average(data: list[float]) -> float:
    """Обчислює середнє арифметичне."""
    if not check_data(data): return 0.0
    return sum(data) / len(data)

def calc_median(data: list[float]) -> float:
    """Обчислює медіану."""
    if not check_data(data): return 0.0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    return sorted_data[mid]

def calc_minimum(data: list[float]) -> float:
    """Повертає мінімальне значення."""
    if not check_data(data): return 0.0
    return min(data)

def calc_maximum(data: list[float]) -> float:
    """Повертає максимальне значення."""
    if not check_data(data): return 0.0
    return max(data)