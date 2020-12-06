#Задание №5

revenue = int(input('Введите значение выручки: \n>>> '))
expenses = int(input('Введите значение издержек: \n>>> '))

if revenue > expenses:
    profit = revenue - expenses
    print(f'Фирма отработала с прибылью. Прибыль составила {profit} у.е.')
    prof_revenue = profit / revenue
    print(f'Рентабельность выручки составила {prof_revenue}')
    staff = int(input('Введите количество сотрудников: \n>>> '))
    profit_for_one = profit // staff
    print (f'Прибыль фирмы в расчете на одного сотрудника составила ≈ {profit_for_one} у.е.\nРасчёт окончен. Всего хорошего!')
else:
        print('Фирма отработала с убытком. Увы.\nДо свидания.')