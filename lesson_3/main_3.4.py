#Программа принимает действительное положительное число x и
# целое отрицательное число y. Выполните возведение числа x в степень y.
#Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    num=x**y
    return num

def my_func_2(x, y):
    y=abs(y-1)#смена знака + 1 проход
    rez=1 #значение для первго прохода
    while y>1: #вход в цикл
        rez=rez * x #умножаем на количество циклов х
        y=y-1
    return (1/rez)


num_x=int(input("Введите положительное число х:"))
num_y=int(input("Введите отрицательное целое число Y:"))

print("Вариант первый:", my_func(num_x, num_y))
print("Вариант через цикл:", my_func_2(num_x, num_y))