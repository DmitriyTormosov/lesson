#Выполнить функцию, которая принимает несколько параметров,
# описывающих данные  пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_f(name_1, surname, age=None, city=None, email=None, tel=None):
    return (f"Уважаемый(ая) {name_1} {surname} Вы родились в {age} году и проживаете в городе {city} , пользуетесь почтой {email} и Ваш номер телефона {tel}")

name=input("Введите Ваше имя: ")
surname=input("Введите Вашу фамилию: ")
age=input("Введите Ваше год рождения: ")
city=input("Введите Ваш город проживания: ")
email=input("Введите Ваш email: ")
tel=input("Введите Ваш номер телефона: ")
print(my_f(name, surname, age, city, email, tel))