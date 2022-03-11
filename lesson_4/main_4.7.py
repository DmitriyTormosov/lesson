# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.


def my_f(n):
    fact_num=1
    if n == 0:
        yield f'Факториал {n}=1'
    for i in range(1, n + 1):
        fact_num = fact_num * i
        yield f'Факториал {i} = {fact_num}'

for el in  my_f(int(input(" Введите число факториала: "))):
    print(el)