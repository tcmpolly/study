def decimal_to_binary(decimal_num):
    """Переводит десятичное число в двоичное."""
    if decimal_num == 0:
        return "0"
    
    binary = ""  # строка для хранения двоичного представления
    
    while decimal_num > 0:
        remainder = decimal_num % 2  # остаток от деления на 2
        binary = str(remainder) + binary  # добавляем остаток слева
        decimal_num //= 2  # целочисленное деление на 2
    
    return binary


# Запрашиваем число у пользователя
num = int(input("Введите десятичное число: "))
binary_result = decimal_to_binary(num)

print(f"{num} в двоичной системе: {binary_result}")