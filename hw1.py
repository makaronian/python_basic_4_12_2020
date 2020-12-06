#Задание №1

#Объявление переменных типа int
first_number = 8
second_number = 88
print(first_number + second_number)

third_number = (input('Введите целое число:\n>>> '))
if third_number.isdigit():
    third_number = int(third_number)
    print(f'Вы ввели {third_number}.')
else:
    print('Ошибка ввода, вводите число.')
    exit()


#Объявление переменных типа str
first_string = 'Hello world!'
second_string = 'Hello again!'
third_string = input('Введите текст:\n>>> ')
print(f'Вы ввели {third_string}.')













