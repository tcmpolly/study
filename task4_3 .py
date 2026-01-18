# Получаем высоту ёлки и символ
height = int(input("Введите высоту ёлки: "))
symbol = input("Введите символ для ёлки: ")

print(f"\nЁлка высотой {height}, символ: '{symbol}'")
print()

# Верхний ствол - всегда по центру
print(" " * (height + 1) + "||")  # Ствол смещен на (высота + 1) пробелов

# Рисуем ярусы ёлки
for level in range(1, height + 1):
    # Количество символов с каждой стороны = номеру уровня
    left_symbols = symbol * level
    right_symbols = symbol * level
    
    # Формируем всю строку
    row = left_symbols + "||" + right_symbols
    
    # Выводим с отступами для центрирования
    # Отступ = высота - уровень
    indent = " " * (height - level + 1)
    print(indent + row)

# Нижний ствол (такой же как верхний)
print(" " * (height + 1) + "||")