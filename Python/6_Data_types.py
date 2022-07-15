
'''6.1 Числовые типы данных: int, float
Площадь треугольника
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.'''
a = float(input())
b = float(input())
print((1 / 2) * a * b)

'''Две старушки
Две старушки идут навстречу друг другу с постоянными скоростями V_1V 
 Определите, через какое время старушки встретятся, если расстояние между ними равно SS км.'''
S = float(input())
V1 = float(input())
V2 = float(input())
print(S / (V1 + V2))

'''Обратное число
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль,
 то вывести «Обратного числа не существует» (без кавычек).'''
n = float(input())
if n == 0:
    print('Обратного числа не существует')
else:
    print(1 / n)
    
'''451 градус по Фаренгейту 
У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет, 
какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

Используйте формулу для перевода: C = \dfrac{5}{9}\left(F - 32\right)C= 
.'''
F = float(input())
C = (5 / 9) * (F - 32)
print(C)

'''Dog age
На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих 
годах.'''
n = int(input())
if n <= 2:
    print(n * 10.5)
else:
    print((n - 2) * 4 + 21)
    
'''Первая цифра после точки
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.'''
n = float(input())
print(int((n * 10) % 10))

'''Дробная часть
Дано положительное действительное число. Выведите его дробную часть.'''
n = float(input())
print(n % 1)

'''Наибольшее и наименьшее
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))

'''Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.'''
a = int(input())
b = int(input())
c = int(input())
x = max(a, b, c)
y = min(a, b, c)
z = (a + b + c) - x - y
print(x)
print(z)
print(y)

'''Интересное число
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».'''
n = int(input())
a = n // 100
b = (n % 100) // 10
c = n % 10
x = max(a, b, c)
y = min(a, b, c)
z = (a + b + c) - x - y
if x - y == z:
    print('Число интересное')
else:
    print('Число неинтересное')
    
'''Абсолютная сумма
Даны пять чисел a_1, \, a_2, \, a_3, \, a_4, \, a_5a 

 . Напишите программу, которая вычисляет сумму их модулей |a_1| + |a_2| +|a_3| +|a_4| + |a_5|∣a 

 ∣.'''
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
A = abs(a)
B = abs(b)
C = abs(c)
D = abs(d)
E = abs(e)
print(A + B + C + D + E)

'''Манхэттенское расстояние
Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить 
сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
На плоскости манхэттенское расстояние между двумя точками (p_{1}; \, p_{2})(p 
Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.'''
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))


'''6.2 Строковый тип данных
Напишите программу, которая выводит текст:
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
print('"Python is a great language!"' + ', said Fred. "' + "I don't ever remember having " + 'this much fun before."')

'''What's Your Name?
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:'''
firstname = str(input())
lastname = str(input())
print('Hello ' + firstname + ' ' + lastname + '! You just delved into Python')

'''Футбольная команда
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».'''
team = input()
length = len(team)
print('Футбольная команда ' + team + ' имеет длину ' + str(length) + ' символов')

'''Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.'''
a = input()
b = input()
c = input()
if (len(a) < len(b) < len(c)) or (len(a) < len(c) < len(b)):
    print(a)
if (len(b) < len(a) < len(c)) or (len(b) < len(c) < len(a)):
    print(b)
if (len(c) < len(a) < len(b)) or (len(c) < len(b) < len(a)):
    print(c)
if (len(a) > len(b) > len(c)) or (len(a) > len(c) > len(b)):
    print(a)
if (len(b) > len(a) > len(c)) or (len(b) > len(c) > len(a)):
    print(b)
if (len(c) > len(a) > len(b)) or (len(c) > len(b) > len(a)):
    print(c)
    
'''Арифметические строки
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую 
арифметическую прогрессию.'''
a, b, c = input(), input(), input()
A = len(a)
B = len(b)
C = len(c)
x = max(A, B, C)
y = min(A, B, C)
z = (A + B + C) - x - y
if x - z == z - y:
    print('YES')
else:
    print('NO')
    
'''Цвет настроения синий
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.'''
n = input()
if 'синий' in n:
    print('YES')
else:
    print('NO')
    
'''Отдыхаем ли?
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.'''
s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')
    
'''Корректный email
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email 
адреса.'''
s = input()
if '@' in s and '.' in s:
    print('YES')
else:
    print('NO')
    
    
'''6.3 Модуль math
Евклидово расстояние
На плоскости евклидово расстояние между двумя точками (x_{1}; \, y_{1})(x 

 ) определяется так \rho = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}ρ= '''
import math

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

p = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

print(math.sqrt(p))

===
import math

x1, y1, x2, y2 = (float(input()) for _ in range(4)) 

print(math.dist((x1, y1), (x2, y2)))

'''Площадь и длина
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.'''
from math import pi

R = float(input())
S = pi * R ** 2
C = 2 * pi * R
print(S)
print(C)

'''Средние значения
В математике выделяют следующие средние значения:
среднее арифметическое чисел aa и bb: \dfrac{a+b}{2} 
 
среднее геометрическое чисел aa и bb: \sqrt{a\cdot b} 
 
среднее гармоническое чисел aa и bb: \dfrac{2ab}{a+b} 
 
среднее квадратичное чисел aa и bb: \sqrt{\dfrac{a^2+b^2}{2}} '''
import math

x, y = float(input()), float(input())

a = (x + y) / 2
b = math.sqrt(x * y)
c = (2 * x * y) / (x + y)
d = math.sqrt((x ** 2 + y ** 2) / 2)

print(a)
print(b)
print(c)
print(d)

'''Тригонометрическое выражение
Напишите программу, вычисляющую значение тригонометрического выражения
\sin x + \cos x + \tan^2 x
sinx+cosx+tan 
2
 x
 по заданному числу градусов xx.'''
from math import *

x = float(input())
y = radians(x)
z = sin(y) + cos(y) + tan(y) ** 2

print(z)

'''Пол и потолок
Напишите программу, вычисляющую значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xx.'''
from math import *

x = float(input())
y = ceil(x) + floor(x)

print(y)

'''Квадратное уравнение 🌶️🌶️
Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения 
ax^2 + bx + c = 0.
ax 
2
 +bx+c=0.'''
from math import *

a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print('Нет корней')
elif D == 0:
    print(- b / (2 * a))
elif D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)    
    print(min(x1, x2))
    print(max(x1, x2))

'''Правильный многоугольник
Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь 
правильного многоугольника с длиной стороны aa и количеством сторон nn вычисляется по формуле: 
S = \dfrac{n \cdot a^2}{4\tg \left(\dfrac{\pi}{n}\right)}
 
Даны два числа: натуральное число nn и вещественное число aa. Напишите программу, которая находит площадь указанного правильного многоугольника.'''
from math import *

n, a = int(input()), float(input())
S = (n * a * a) / (4 * tan(pi / n))

print(S)


