# Получаем два числа от пользователя
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(f"\nЧисла от {A} до {B}:")

# Проверяем, какое число больше
if A < B:
    # Выводим в порядке возрастания
    print("Порядок: ВОЗРАСТАНИЕ")
    for number in range(A, B + 1):
        print(number, end=" ")
else:
    # Выводим в порядке убывания
    print("Порядок: УБЫВАНИЕ")
    for number in range(A, B - 1, -1):
        print(number, end=" ")

print()  # Переход на новую строку