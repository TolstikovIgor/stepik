
'''7.1 Цикл for
Python is awesome
Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.'''
for i in range(10):
    print('Python is awesome!')
    
'''Повторяй за мной 1
Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное 
количество раз.'''
s = input()
n = int(input())

for i in range(n):
    print(s)
    
'''Последовательность символов
Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:'''
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

'''Звездный прямоугольник
На вход программе подается натуральное число nn.
Напишите программу, которая печатает звездный прямоугольник размерами n \times 19n×19.'''
n = int(input())

for i in range(n):
    print('*' * 19)
    
'''Повторяй за мной 2
Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.'''
n = input()
for i in range(10):
    print(i, n)
    
'''Квадрат числа
На вход программе подается натуральное число nn. Напишите программу, которая для каждого из чисел от 00 до nn (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).'''
n = int(input())

for i in range(n+1):
    print('Квадрат числа', i, 'равен', i * i)
    
'''Звездный треугольник
На вход программе подается натуральное число n \, (n \ge 2)n(n≥2) – катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звездный треугольник в соответствии с примером.'''
n = int(input())

for i in range(n):
    print('*' * (n - i))
    
'''Популяция
На вход программе подается три натуральных числа m, \, p, \, nm,p,n:

m:m: стартовое количество организмов;
p:p: среднесуточное увеличение в %;
n:n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, 
начиная с 11 и заканчивая nn-м днем.'''
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)
    
    
'''7.2 Цикл for: функция range
Последовательность чисел 1
Даны два целых числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно.'''
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)
    
'''Последовательность чисел 2 🌶️
Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания, если 
m < nm<n, или в порядке убывания в противном случае.'''
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
        
'''Последовательность чисел 3 🌶️
Даны два целых числа mm и nn (m > nm>n). Напишите программу, которая выводит все нечетные числа от mm до nn включительно в 
порядке убывания.'''
m, n = int(input()), int(input())
if m % 2 == 1:
    for i in range(m, n - 1, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)
        
'''Последовательность чисел 4
Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно 
удовлетворяющие хотя бы одному из условий:

число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.'''
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):
        print(i)
        
'''Таблица умножения
Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.'''
n = int(input())
for i in range(10):
    print(n, 'x', i + 1, '=', n * (i + 1))
    
    
'''7.3 Частые сценарии
Количество чисел
На вход программе подаются два целых числа aa и bb (a \le b)(a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от aa до bb включительно, куб которых оканчивается на 44 или 99.'''
a, b = int(input()), int(input())
counter = 0
for i in range(a, b+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter = counter + 1
print(counter)

'''Сумма чисел
На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел. '''
n = int(input())
total = 0
for i in range(n):
    a = int(input())
    total = total + a
print(total)

'''Асимптотическое приближение
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения'''
from math import *
n = int(input())
total = 0
for i in range(1, n):
    if i / n
    print(m)
