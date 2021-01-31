'''Лабораторная работа №9
   "Множества"

   Назначение:
   нахождение цифр, которые встречаются в заданном
   числе более одного раза.
   
   Переменные, используемые в программе:
   k -- заданое целое число (или его модуль);
   num_all, num_not_once -- множества всех цифр в числе,
   и цифр, встречающихся более одного раза;
   num_of_no -- количество цифр, встречающихся более одного
   раза;
   ch -- текущая цифра числа k;
   x -- элемент множества num_not_once.
   
   Тестовый пример:
   Входные данные:
   112344555
   Выходные данные:
   Цифры, которые встречаются в числе более одного раза:
   1 4 5
'''

k = int(input('Введите целое число K: '))
k = abs(k)
num_all = set()
num_not_once = set()
num_of_no = 0

while k != 0:
    ch = k%10
    if ch in num_all:
        num_not_once.add(ch)
        num_of_no += 1
    else:
        num_all.add(ch)
    k //= 10

if num_of_no != 0:
    print('Цифры, которые встречаются в числе более одного раза:')
    for x in num_not_once:
        print(x, end = ' ')
else:
    print('Все цифры числа встречаются в нём по одному разу.')
