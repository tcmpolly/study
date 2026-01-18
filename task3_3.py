import random

# Генерируем случайное число от 1 до 10
secret_number = random.randint(1, 10)
attempts = 3  # Количество попыток

print("Игра: Угадай число от 1 до 10")
print(f"У тебя есть {attempts} попытки")

# Цикл на 3 попытки
for attempt in range(1, attempts + 1):
    print(f"\nПопытка №{attempt}")
    
    # Получаем предположение игрока
    guess = int(input("Твоё предположение: "))
    
    # Проверяем угадал ли
    if guess == secret_number:
        print(f"Поздравляю! Ты угадал число {secret_number}!")
        print(f"Потребовалось попыток: {attempt}")
        break  # Выходим из цикла, если угадал
        
    # Если не угадал, подсказываем
    elif guess < secret_number:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")
    
    # Если это последняя попытка и не угадали
    if attempt == attempts:
        print(f"\nПопытки закончились!")
        print(f"Загаданное число было: {secret_number}")