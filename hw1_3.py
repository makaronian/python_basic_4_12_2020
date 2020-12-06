#Задание №3

user_number = int(input('Введите пожалуйста число:\n>>> '))
user_number = str(user_number) #Объявляем вводимое число в формате строки

result1 = user_number + user_number #Складываем строки
result2 = user_number + user_number + user_number

result3 = int(result1) #Склеенные строки объявляем как целое число
result4 = int(result2)

result5 = int(user_number) + result3 + result4 #Итог
print(result5)