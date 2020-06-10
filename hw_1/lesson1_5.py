# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Укажите вашу выручку: '))
costs = int(input('Укажите вашу издержки: '))

if revenue == costs:
    print(f'Вы отработали в 0')
elif revenue > costs:
    income = revenue - costs
    profitability = income / revenue
    print(f"Чудно, у вас прибыль! Ваша рентабельность: {profitability}")
    employees_number = int(input('Укажите количество ваших сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {income/employees_number}')
else:
    print(f'Простите, но вы работаете в убыток...')