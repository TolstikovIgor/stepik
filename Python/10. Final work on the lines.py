    
'''10. Итоговая работа на строки
10.2 Часть 2
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена длина строки s.'''
s = 'Python rocks!'
print(len(s))

'''Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы был выведен четвертый символ строки s.'''
s = 'Python rocks!'
print(s[3:4])

'''Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы были выведены символы строки s со 2 по 5 включительно'''
s = 'Python rocks!'
print(s[1:5])

'''Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s без ведущих и замыкающих
 пробельных символов.'''
s = '    Python rocks!     '
print(s.strip())

'''Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s заглавными буквами
 (в верхнем регистре).'''
s = 'Python rocks!'
print(s.upper())

'''Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s в которой символ
 «o» заменен на символ «@».'''
s = 'Python rocks!'
print(s.replace('o', '@'))

'''Каждый третий
На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть
 символы с индексами 0, 3, 6, ....'''
s = input()
a = len(s)
for i in range(a):
    if i % 3 != 0:
       print(s[i], end='')
       
'''Замени меня полностью
На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».'''
s = input()
print(s.replace('1', 'one'))

'''Удали меня полностью
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».'''
s = input()

'''Второе вхождение
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква
«f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.'''
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
elif s.count('f') > 1:
    a = s.replace('f', '0', 1)
    print(a.find('f'))
    
'''Переворот
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая
возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h»'''
s = input()
a = s.find('h') + 1
b = s.rfind('h')
c = s[a:b]
d = c[::-1]
print(s[:s.find('h') + 1], c[::-1], s[s.rfind('h'):], sep='')

