#Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка  элементов нужно использовать функцию input().
meaning=input("Введите данные через пробел: ").split()

for i in range(0,len(meaning)-1,2):
    meaning[i], meaning[i+1]=meaning[i+1], meaning[i]

print(meaning)