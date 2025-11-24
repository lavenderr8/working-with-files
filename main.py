def file_contents(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for number, line in enumerate(f, start=1):
            print(f"{number}. {line.strip()}")


my_file = 'data.txt'

with open(my_file, 'w', encoding='utf-8') as file:
    file.write("Африканский ёж\n")
    file.write("Ласка\n")
    file.write("Эублефар\n")

print("Содержимое файла:")
file_contents(my_file)

with open(my_file, 'a', encoding='utf-8') as file:
    file.write("Галаго\n")
    file.write("Фенек\n")

print("\nСодержимое файла после добавления:")
file_contents(my_file)

copy_name = 'data_copy.txt'
with open(my_file, 'rb') as src, open(copy_name, 'wb') as dst:
    dst.write(src.read())

print(f"\nФайл успешно скопирован как: {copy_name}")
