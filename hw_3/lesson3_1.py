# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
# их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_division(var_1, var_2):
    return None if var_2 == 0 else var_1 / var_2


num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
print(my_division(num_1, num_2))
