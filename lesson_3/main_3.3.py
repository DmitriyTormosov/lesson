#Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(arg_1, arg_2, arg_3):
    num=[]
    num.append(arg_1)
    num.append(arg_2)
    num.append(arg_3)
    num.sort()
    a=num[-1]+num[-2]
    return a

print(my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Введите третий аргумент: '))))