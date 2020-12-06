#Задание №2

user_data = int(input('Введите количество секунд: '))

hours = user_data // 3600
minutes = (user_data - hours * 3600) // 60
seconds = user_data - (hours * 3600 + minutes * 60)

print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")