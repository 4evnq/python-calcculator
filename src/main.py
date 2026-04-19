from io_utils import read_data, save_data
from analysis import calc_average, calc_median, calc_minimum, calc_maximum

def main():
    print("=== Консольний калькулятор статистичних показників ===")
    
    data = read_data("data/input.txt")
    
    if not data:
        print("Програму завершено через відсутність або помилку даних.")
        return

    avg_val = calc_average(data)
    med_val = calc_median(data)
    min_val = calc_minimum(data)
    max_val = calc_maximum(data)

    result = (
        f"Статистика за наданими даними:\n"
        f"-------------------------------\n"
        f"Середнє значення : {avg_val:.2f}\n"
        f"Медіана          : {med_val:.2f}\n"
        f"Мінімум          : {min_val:.2f}\n"
        f"Максимум         : {max_val:.2f}\n"
        f"-------------------------------\n"
    )
    
    print("\n" + result)
    
    save_data("data/output.txt", result)

if __name__ == "__main__":
    main()