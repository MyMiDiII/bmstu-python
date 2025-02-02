'''Лабораторная работа №5
   "Вычисление суммы бесконечного ряда"

   Назначение: 
   вычислить сумму бесконечного ряда с заданной точностью.

   Переменные, используемые в программе:
   eps -- точность вычисления;
   x -- аргумент;
   n, step -- начальное значение и шаг для печати;
   m -- максимальное количество циклов;
   el, nn, sm -- текущий элемент, его номер и сумма;
   ch -- вспомогателная переменная для вычисления элемента;
   k -- количество выведенных элементов;
   sh, table -- способ выхода из цикла.
   

   Тестовый пример:
   Входные данные:
   1e-4
   0.1
   1
   1
   20
   Выходные данные:
   ┌─────────────┬───────────────┐
   │    Число    │    Текущая    │
   │    членов   │     сумма     │
   ├─────────────┼───────────────┤
   │          1  │     0.100000  │
   └─────────────┴───────────────┘
   Количество членов, входящих в сумму: 2
   Сумма ряда: 0.099833
'''

print('Вычисление суммы бесконечного ряда.')
eps = float(input('Введите точность вычисления суммы: '))
x = float(input('Введите аргумент x: '))
n = int(input('Введите начальное значение для печати (натуральное): '))
step = int(input('Введите шаг для печати (натуральное): '))
m = int(input('Введите максимальное количество циклов (натуральное): '))
print()

sm = 0
el = x
ch = 1
nn = 1
k = 0
sh = True
table = False

while abs(el) > eps:
    sm += el
    ch += 2
    el = -el*x*x*(ch-2)*(ch-2)/ch/(ch-1)

    #вывод необходимых значений
    if nn == step*k + n and abs(el) > eps:
        if nn == n:
            print('┌─────────────┬───────────────┐')
            print('│    Число    │    Текущая    │')
            print('│    членов   │     сумма     │')
            print('├─────────────┼───────────────┤')
            table = True
        if abs(sm) < 10:
            print('│  {:9d}  │  {:11.6f}  │'.format(nn,sm))
        elif abs(sm) < 1000:
            print('│  {:9d}  │  {:11.4f}  │'.format(nn,sm))
        elif abs(sm) < 10000:
            print('│  {:9d}  │  {:11.2f}  │'.format(nn,sm))
        else:
            print('│  {:9d}  │  {:11.2e}  │'.format(nn,sm))
        k+=1

    if abs(el) == float('inf'):
        sh = False
        break

    #выход из цикла при превышении m
    if abs(el) > eps and nn == m:
        break
    nn += 1

if table:
    print('└─────────────┴───────────────┘')
else:
    print('Ряд сошёлся раньше заданного начального значения.')

if nn != m and sh:
    print('Количество членов, входящих в сумму:', nn-1)
    print('Сумма ряда:', '{:9.6f}'.format(sm))
else:
    if not sh:
        print('Элементы ряда при n >', nn, '- большие числа.')
        print('За', nn, 'циклов ряд не сошёлся.')
    else:
        print('За', m, 'циклов ряд не сошёлся.')
