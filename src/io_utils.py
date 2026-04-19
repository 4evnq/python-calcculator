def read_data(filepath: str) -> list[float]:
    """Зчитує числові дані з файлу."""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    data.append(float(line))
        return data
    except FileNotFoundError:
        print(f"Помилка: Файл '{filepath}' не знайдено!")
        return []

def save_data(filepath: str, text: str) -> None:
   
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f" Результати успішно збережено у файл '{filepath}'")
    except IOError:
        print(f"Помилка: Не вдалося зберегти файл '{filepath}'")