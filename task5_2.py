# Функция для вывода чисел от start до end
def print_numbers(start, end):
    """Выводит все числа от start до end включительно."""
    print(f"Числа от {start} до {end}:")
    
    if start < end:
        # Возрастающий порядок
        for number in range(start, end + 1):
            print(number, end=" ")
    else:
        # Убывающий порядок
        for number in range(start, end - 1, -1):
            print(number, end=" ")
    print()  # Переход на новую строку

# Основная программа
print("=" * 40)
print("ВЫВОД ЧИСЕЛ В ДИАПАЗОНЕ (с функцией)")
print("=" * 40)

# Получаем данные от пользователя
A = int(input("Введите начальное число (A): "))
B = int(input("Введите конечное число (B): "))

# Вызываем функцию
print_numbers(A, B)

# Дополнительные вызовы для демонстрации
print("\nДополнительные примеры:")
print_numbers(1, 5)     # 1 2 3 4 5
print_numbers(10, 5)    # 10 9 8 7 6 5
print_numbers(-3, 3)    # -3 -2 -1 0 1 2 3