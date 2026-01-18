# Открываем файл для записи
filename = "номер_группы.txt"

# Спрашиваем сколько записей ввести
n = int(input("Сколько студентов вы хотите добавить? "))

# Открываем файл для записи
with open(filename, 'w', encoding='utf-8') as file:
    # Вводим данные n студентов
    for i in range(n):
        print(f"\nСтудент {i+1}:")
        surname = input("Введите фамилию: ")
        email = input("Введите почтовый адрес: ")
        # Записываем в файл
        file.write(f"{surname}: {email}\n")

print(f"\nДанные сохранены в файл {filename}")

# Читаем и выводим данные из файла
print("\nСписок студентов из файла:")
print("-" * 40)
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())