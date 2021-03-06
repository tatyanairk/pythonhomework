
__author__ = 'Кистенёва Татьяна Дмитриевна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = int(input("Введите число: "))
mx = 0
b = 0
while a // 10 != 0:
    b = a % 10
    if b >= mx:
        mx = b
    a//=10
print(mx)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
a = a + b 
b = a - b 
a = a - b
print("a =", a, "b =", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math 

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
x1 = 0
x2 = 0
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = -b + math.sqrt(d) / 2 * a 
    x2 = -b - math.sqrt(d) / 2 * a 
    print("корень 1 =", x1, "корень 2 =", x2)
elif d < 0:
    x1 = -b / 2 * a
    print("корней нет")
else:
    print("единствернный корень =", x1)
