number_str = input("Введите натуральное число: ")

# Проверяем, что введено число 
if not number_str.isdigit():
    print("Ошибка: введите натуральное число!")
else:
    max_digit = '0'  # начальное значение — самая маленькая цифра

    for digit in number_str:  # перебираем каждую цифру как символ
        if digit > max_digit:
            max_digit = digit

    print(f"Наибольшая цифра в числе {number_str} — это {max_digit}.")