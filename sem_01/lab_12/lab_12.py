'''Лабораторная работа №12
   "Уточнение корней"

   Назначение:
   1)нахождение корней уравнения f(x)=0;
   2)уточнение каждого корня функцией brenth
     из библиотеки scipy.optimize;
   3)уточнение каждого корня функцией brenth,
     реализванной на Python;
   4)сравнение методов уточнения корня по
     времени работы.

   Переменные, используемые в программе:
   eps, max_iter -- точность и максимальное количество итераций;
   a, b, h -- левая, правая границы отрезка и шаг прохода по нему;
   x_p, x_t -- левая, правая границы шага;
   num_root -- количество найденных корней;
   set_of_root_1, set_of_root_2 -- множества найденных корней для каждого
                                   способа;
   result_time_1, result_time_2 -- итоговое время работы каждого способа;

   Тестовый пример:
   Входные данные:
   -1 1
   0.4
   Выходные данные:
   ┌───────┬───────────┬──────────┬──────────┬──────────────┬──────────┬────────────┬────────┐
   │   №   │   Метод   │   Левая  │  Правая  │   Значение   │ Значение │ Количество │  Код   │
   │       │           │  граница │  граница │    корня     │ функции  │  итераций  │ ошибки │
   ├───────┼───────────┼──────────┼──────────┼──────────────┼──────────┼────────────┼────────┤
   │     1 │   brenth  │     -0.2 │      0.2 │     0.000000 │    0e+00 │          2 │      0 │
   │       │ brenth_py │     -0.2 │      0.2 │     0.000000 │    0e+00 │          2 │      0 │
   └───────┴───────────┴──────────┴──────────┴──────────────┴──────────┴────────────┴────────┘
   Коды ошибок:
      0 -- нет ошибок;
      1 -- точность не была достигнута за максимальное количество итераций.

   Время работы со стандартной функцией:  0.00008 ms
   Время работы с функцией, реализованной на Python:  0.00007 ms
'''

import scipy.optimize as optimize
from time import perf_counter
from math import sin, fabs

eps = 1e-3
max_iter = 100

#функция
def fun(x):
    return sin(x) + 0.5

#вывод шапки таблицы
def print_hat():
    print('┌','─'*7,'┬','─'*11,'┬','─'*10,'┬','─'*10,'┬','─'*14,'┬',
          '─'*10,'┬','─'*12,'┬','─'*8,'┐',sep = '')
    #первая строка
    print('│   №   ', end = '')
    print('│   Метод   ', end = '')
    print('│   Левая  ', end = '')
    print('│  Правая  ', end = '')
    print('│   Значение   ', end = '')
    print('│ Значение ', end = '')
    print('│ Количество ', end = '')
    print('│  Код   │')
    
    #вторая строка
    print('│       ', end = '')
    print('│           ', end = '')
    print('│  граница ', end = '')
    print('│  граница ', end = '')
    print('│    корня     ', end = '')
    print('│ функции  ', end = '')
    print('│  итераций  ', end = '')
    print('│ ошибки │')

#вывод строки
def row(num, l, r, x, y, iter, mis):
    print('│ {:5} '.format(num), end = '')
    if num == '':
        print('│ brenth_py ', end = '')
    else:
        print('│   brenth  ', end = '')
    if -10000<l<10000:
        print('│ {:8.2g} '.format(l), end = '')
    else:
        print('│ {:8.1e} '.format(l), end = '')
    if -10000<r<10000:
        print('│ {:8.2g} '.format(r), end = '')
    else:
        print('│ {:8.1e} '.format(r), end = '')
    if mis == 0:
        if -1000<x<1000:
            print('│ {:12.6f} '.format(x), end = '')
        else:
            print('│ {:12.4e} '.format(x), end = '')
        print('│ {:8.0e} │ {:>10} │ {:6} │'.format(y, iter, mis))
    else:
        print('│ {:^12} '.format('--'), end = '')
        print('│ {:^8} │ {:^10} │ {:6} │'.format('--', '--', mis))

#вывод промежуточной линии
def middle():
    print('├','─'*7,'┼','─'*11,'┼','─'*10,'┼','─'*10,'┼','─'*14,'┼',
          '─'*10,'┼','─'*12,'┼','─'*8,'┤', sep = '')

#вывод нижней части таблицы
def print_down():
    print('└','─'*7,'┴','─'*11,'┴','─'*10,'┴','─'*10,'┴','─'*14,'┴',
          '─'*10,'┴','─'*12,'┴','─'*8, '┘', sep = '')

#метод brenth, реализованный на Python
def brenth_py(f, xa, xb, xtol, maxiter):
    rtol = 8.881784197001252e-16
    x_prev = xa
    x_curr= xb
    x_bel = 0.
    f_prev = f(x_prev)
    f_curr = f(x_curr)
    f_bel = 0.
    s_prev = 0.
    s_curr = 0.

    if f_prev*f_curr>0:
        return 0, 0, 2
    if f_prev == 0.:
        return x_prev, 0, 0
    if f_curr == 0.:
        return x_curr, 0, 0
    #алгоритм за максимальное количество итераций
    iters = 0
    for i in range(maxiter):
        iters += 1
        if f_prev*f_curr<0:
            x_bel = x_prev
            f_bel = f_prev
            s_prev = s_curr = x_curr - x_prev

        if fabs(f_bel) < fabs(f_curr):
            x_prev = x_curr
            x_curr = x_bel
            x_bel = x_prev

            f_prev = f_curr
            f_curr = f_bel
            f_bel = f_prev

        delta = (xtol + rtol*fabs(x_curr))/2
        #изменение при половинном делении
        s_bis = (x_bel - x_curr)/2

        #достигнута точность
        if f_curr == 0. or fabs(s_bis) < delta:
            return x_curr, iters, 0
        
        #проверка на возможность выхода за границы отрезка
        #при более быстрых методах
        if fabs(s_prev) > delta and fabs(f_curr) < fabs(f_prev):
            if x_prev == x_bel: #известны 2 точки
                #изменение при секущих
                s_try = -f_curr*(x_curr - x_prev)/(f_curr - f_prev)
            else: #известны 3 точки
                #изменение при гиперболе
                d_prev = (f_prev - f_curr)/(x_prev - x_curr)
                d_bel = (f_bel - f_curr)/(x_bel - x_curr)
                s_try = -f_curr*(f_bel - f_prev)/(f_bel*d_prev - f_prev*d_bel)

            #определение лучшего результата
            if 2*fabs(s_try) < min(fabs(s_prev), 3*fabs(s_bis) - delta):
                #быстрый метод
                s_prev = s_curr
                s_curr = s_try
            else:
                #надежный метод половинного деления
                s_prev = s_bis
                s_curr = s_bis
        else:
            #половинного деления
            s_prev = s_bis
            s_curr = s_bis
        
        x_prev = x_curr
        f_prev = f_curr

        if fabs(s_curr) > delta:
            x_curr += s_curr
        else:
            if s_bis > 0:
                x_curr += delta
            else:
                x_curr -= delta
        f_curr = f(x_curr)
    return x_curr, 0, 1
    
a, b = map(float, input('Введите концы отрезка (через пробел): ').split())
h = float(input('Введите шаг прохода: '))

#общие переменные
x_p = a
x_t = a + h
num_root = 0

#переменные для стандартной функции
set_of_root_1 = set()
result_time_1 = 0

#переменные для реализованной функции
set_of_root_2 = set()
result_time_2 = 0

#проход по заданному промежутку
while x_t < b + h/2:
    if fun(x_p)*fun(x_t) <= 0:
        num_root += 1
        if num_root == 1:
            print_hat()

        #стандартная функция
        start_1 = perf_counter()
        x0_1, root_results = optimize.brenth(fun, x_p, x_t, xtol=eps,
                             maxiter=max_iter, full_output=True, disp = False)
        result_time_1 += perf_counter() - start_1
        if x0_1 not in set_of_root_1:
            middle()
            if root_results.converged:
                mistake_1 = 0
            else:
                mistake_1 = 1
            iters_1 = root_results.iterations
            if fun(x_p) == 0 or fun(x_t) == 0:
                iters_1 = 0
            if iters_1 > max_iter:
                mistake_1 = 1
            row(num_root, x_p, x_t, x0_1, fun(x0_1), iters_1, mistake_1)
            set_of_root_1.add(x0_1)
        else:
            num_root -= 1

        #функция, реализованная на Python
        start_2 = perf_counter()
        x0_2, iters_2, mistake_2 = brenth_py(fun, x_p, x_t, eps, max_iter)
        result_time_2 += perf_counter() - start_2
        if x0_1 not in set_of_root_2:
            row('', x_p, x_t, x0_2, fun(x0_2), iters_2, mistake_2)
            set_of_root_2.add(x0_2)

    x_p = x_t
    x_t += h
if fun(x_p)*fun(b)<0:
    num_root += 1
    if num_root == 1:
        print_hat()

    #стандартная функция
    start_1 = perf_counter()
    x0_1, root_results = optimize.brenth(fun, x_p, b, xtol=eps,
                         maxiter=max_iter, full_output=True, disp = False)
    result_time_1 += perf_counter() - start_1
    if x0_1 not in set_of_root_1:
        middle()
        if root_results.converged:
            mistake_1 = 0
        else:
            mistake_1 = 1
        iters_1 = root_results.iterations
        if fun(x_p) == 0 or fun(b) == 0:
            iters_1 = 0
        if iters_1 > max_iter:
            mistake_1 = 1
        row(num_root, x_p, b, x0_1, fun(x0_1), iters_1, mistake_1)
        set_of_root_1.add(x0_1)
    else:
        num_root -= 1

    #функция, реализованная на Python
    start_2 = perf_counter()
    x0_2, iters_2, mistake_2 = brenth_py(fun, x_p, b, eps, max_iter)
    result_time_2 += perf_counter() - start_2
    if x0_1 not in set_of_root_2:
        row('', x_p, b, x0_2, fun(x0_2), iters_2, mistake_2)
        set_of_root_2.add(x0_2)
if num_root == 0:
    print('Корни на заданном промежутке не найдены.')
else:
    print_down()

print('Коды ошибок:')
print('   0 -- нет ошибок;')
print('   1 -- точность не была достигнута', end = ' ')
print('за максимальное количество итераций.')
print()

print('Суммарное время работы:')
print('    - со стандартной функцией:',
     '{:8.5f}'.format(result_time_1) , 'ms')
print('    - с функцией, реализованной на Python:',
     '{:8.5f}'.format(result_time_2) ,'ms')

print()
print('(brenth -- метод, использующий стандарную функцию;')
print(' brenth_py -- метод с функцией, реализованной на Python)')

