'''Лабораторная работа №1
   "Уточнение корней"
   Вариант 11 (точки перегиба)

   Назначение:
   1)нахождение корней уравнения f(x)=0;
   2)уточнение каждого корня функцией brenth
     из библиотеки scipy.optimize;
   3)уточнение каждого корня функцией brenth,
     реализванной на Python;
   4)сравнение методов уточнения корня по
     времени работы;
   5)построение графика с корнями и точками перегиба

   Переменные, используемые в программе:
   eps, max_iter -- точность и максимальное количество итераций;
   a, b, h -- левая, правая границы отрезка и шаг прохода по нему;
   x_p, x_t -- левая, правая границы шага;
   num_root -- количество найденных корней;
   set_of_root_1, set_of_root_2 -- множества найденных корней для каждого
                                   способа;
   finish_1, finish_2 -- итоговое время работы каждого способа;

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

   (brenth -- метод, использующий стандарную функцию;
    brenth_py -- метод с функцией, реализованной на Python)
'''

from tkinter import *
import tkinter.messagebox as box
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import scipy.misc as der
import scipy.optimize as optimize
from time import perf_counter
from math import *

#функция
def f(x):
    return eval(func_enter.get())

#производная функции
def ddf(x):
    return der.derivative(f, x, n = 2)

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

#уточнение корней для графика
def roots_graph(fun, a, b, h, eps, max_iter):
    x_p = a
    x_t = a + h
    set_of_root_1 = set()
    root_x = []
    root_y = []

    #проход по заданному промежутку
    while x_t < b + h/2:
        if fun(x_p)*fun(x_t) <= 0:
            x0, root_results = optimize.brenth(fun, x_p, x_t, xtol=eps,
                                 maxiter=max_iter, full_output=True,
                                 disp = False)
            if x0 not in set_of_root_1 and root_results.converged:
                root_x.append(x0)
                root_y.append(f(x0))
                set_of_root_1.add(x0)

        x_p = x_t
        if x_t < b and x_t + h > b:
            x_t = b
        else:
            x_t += h

    return root_x, root_y

#уточнение корней для таблицы
def roots_table():
    try:
        a = float(begin_enter.get())
        b = float(end_enter.get())
        h = float(step_enter.get())
        eps = float(eps_enter.get())
        max_iter = int(max_iter_enter.get())
    except:
        box.showerror('Ошибка',
                 'Вводите числа!\n(Количество итераций -- натуральное число)')
    else:
        try:
            if a > b:
                box.showerror('Ошибка',
                           'Начальное значение должно быть меньше конечного!')
            elif not (h > 0):
                box.showerror('Ошибка', 'Шаг должен быть больше нуля!')
            elif not (eps > 0):
                box.showerror('Ошибка', 'Точность должна быть больше нуля!')
            elif max_iter <= 0:
                 box.showerror('Ошибка',
                              'Количество итераций должно быть больше нуля!')
            else:
                windowt = Tk()
                windowt.title('Уточнение корней. Таблица корней.')
                windowt.geometry('700x530+425+50')
                windowt.resizable(False, False)
                windowt.configure(bg = 'azure2')

                tit_2 = Label(windowt, text = 'Таблица корней',
                 font = ('Comic Sans MS', 24), bg = 'azure2')
                tit_2.place(x = 225, y = 10)


                #коды
                hint_1 = Label(windowt, text = 'Коды ошибок:',
                     font = ("Helvetica", 12), bg = 'azure2')
                hint_1.place(x = 60, y = 400)

                hint_2 = Label(windowt, text = '     0 -- нет ошибок;',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_2.place(x = 60, y = 420)
            
                hint_3 = Label(windowt, text = '1 -- точность не была достигнута'
                     '\nза максимальное количество итераций.',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_3.place(x = 60, y = 440)

                #методы
                hint_1 = Label(windowt, text = 'Методы:',
                     font = ("Helvetica", 12), bg = 'azure2')
                hint_1.place(x = 370, y = 400)

                hint_2 = Label(windowt, text = '     brenth -- метод, использующий',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_2.place(x = 370, y = 420)

                hint_2 = Label(windowt, text = 'стандартную функцию;',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_2.place(x = 450, y = 440)
            
                hint_3 = Label(windowt, text = '     brenth_py -- метод с функцией,',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_3.place(x = 370, y = 460)

                hint_3 = Label(windowt, text = 'реализованной на Python.',
                     font = ("Times New Roman", 12), bg = 'azure2')
                hint_3.place(x = 450, y = 480)

                #таблица
                tree = ttk.Treeview(windowt)
                tree["columns"] = ("0","1", "2", "3", "4", "5", "6", "7", "8")
                tree.heading("#0", text="", anchor='w')
                tree.heading("0", text="№", anchor='w')
                tree.heading("1", text="Метод", anchor='w')
                tree.heading("2", text="Левая граница", anchor='w')
                tree.heading("3", text="Правая граница", anchor='w')
                tree.heading("4", text="Корень", anchor='w')
                tree.heading("5", text="Функция", anchor='w')
                tree.heading("6", text="Итерации", anchor='w')
                tree.heading("7", text="Время", anchor='w')
                tree.heading("8", text="Ошибка", anchor='w')

                tree.column("#0", width=0, minwidth=0, stretch = False)
                tree.column("0", width=30, minwidth=30, stretch = False)
                tree.column("1", width=62, minwidth=62, stretch = False)
                tree.column("2", width=90, minwidth=90, stretch = False)
                tree.column("3", width=96, minwidth=96, stretch = False)
                tree.column("4", width=80, minwidth=80, stretch = False)
                tree.column("5", width=70, minwidth=70, stretch = False)
                tree.column("6", width=64, minwidth=64, stretch = False)
                tree.column("7", width=70, minwidth=70, stretch = False)
                tree.column("8", width=60, minwidth=60, stretch = False)

                tree.place(x = 35, y = 70, height = 300, width = 630)

                sb_h = Scrollbar(tree, orient = 'horizontal',
                                 command = tree.xview)
                sb_v = Scrollbar(tree, orient = 'vertical',
                                 command = tree.yview)
            
                tree.configure(xscrollcommand=sb_h.set)
                tree.configure(yscrollcommand=sb_v.set)

                sb_h.pack(side = 'bottom', fill = 'x')
                sb_v.pack(side = 'right', fill = 'y')

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
                    if f(x_p)*f(x_t) <= 0:
                        num_root += 1

                        #стандартная функция
                        start_1 = perf_counter()
                        x0_1, root_results = optimize.brenth(f, x_p, x_t,
                                             xtol=eps, maxiter=max_iter,
                                             full_output=True, disp = False)
                        finish_1 = perf_counter() - start_1
                        if x0_1 not in set_of_root_1:
                            if root_results.converged:
                                mistake_1 = 0
                            else:
                                mistake_1 = 1
                            iters_1 = root_results.iterations
                            if f(x_p) == 0 or f(x_t) == 0:
                                iters_1 = 0
                            if iters_1 > max_iter:
                                mistake_1 = 1

                            #форматирование
                            if -10000<x_p<10000:
                                l = '{:8.2g}'.format(x_p)
                            else:
                                l ='{:8.1e}'.format(x_p)
                            if -10000<x_t<10000:
                                r = '{:8.2g}'.format(x_t)
                            else:
                                r = '{:8.1e}'.format(x_t)
                            if mistake_1 == 0:
                                if -1000<x0_1<1000:
                                    x = '{:12.6f}'.format(x0_1)
                                else:
                                    x ='{:12.4e}'.format(x0_1)
                                y ='{:8.0e}'.format(f(x0_1))
                                iters = str(iters_1)
                                t = '{:8.1e} ms'.format(finish_1)
                                mis = str(mistake_1)

                            else:
                                x = '--'
                                y = '--'
                                iters = '--'
                                t = '--'
                                mis = '1'

                            #вставка в таблицу
                            tree.insert("", "end", text = '',
                                        values = (str(num_root),"brenth", l,
                                                  r, x, y, iters, t, mis))

                            set_of_root_1.add(x0_1)
                        else:
                            num_root -= 1

                        #функция, реализованная на Python
                        start_2 = perf_counter()
                        x0_2, iters_2, mistake_2 = brenth_py(f, x_p, x_t,
                                                            eps, max_iter)
                        finish_2 = perf_counter() - start_2
                        if x0_1 not in set_of_root_2:
                            if mistake_2 == 0:
                                if -1000<x0_2<1000:
                                    x = '{:12.6f}'.format(x0_2)
                                else:
                                    x ='{:12.4e}'.format(x0_2)
                                y ='{:8.0e}'.format(f(x0_2))
                                iters = str(iters_2)
                                t = '{:8.1e} ms'.format(finish_2)
                                mis = str(mistake_2)

                            else:
                                x = '--'
                                y = '--'
                                iters = '--'
                                t = '--'
                                mis = '1'

                            #вставка в таблицу
                            tree.insert("", "end", text = '',
                                        values = ('',"brenth_py", l, r,
                                                 x, y, iters, t, mis))
                            set_of_root_2.add(x0_2)

                    x_p = x_t
                    if x_t < b and x_t + h > b:
                        x_t = b
                    else:
                        x_t += h
                if num_root == 0:
                    box.showinfo('Корни.', 'На заданном промежутке корней нет!')

                windowt.mainloop()
        except:
            box.showerror('Ошибка', 'Неверная функция!')
        

#создание и вывод графика
def graph():
    try:
        a = float(begin_enter.get())
        b = float(end_enter.get())
        h = float(step_enter.get())
        eps = float(eps_enter.get())
        max_iter = int(max_iter_enter.get())
    except:
        box.showerror('Ошибка',
                 'Вводите числа!\n(Количество итераций -- натуральное число)')
    else:
        try:
            if a > b:
                box.showerror('Ошибка',
                           'Начальное значение должно быть меньше конечного!')
            elif not (h > 0):
                box.showerror('Ошибка', 'Шаг должен быть больше нуля!')
            elif not (eps > 0):
                box.showerror('Ошибка', 'Точность должна быть больше нуля!')
            elif max_iter <= 0:
                 box.showerror('Ошибка',
                              'Количество итераций должно быть больше нуля!')
            else:
                xn = a
                x = []
                y = []
                s = 0.01
                if (b - a < 0.01):
                    s = (b - a) / 100
                while xn < b + s/2:
                    x.append(xn)
                    y.append(f(xn))
                    xn += s

                p_x, p_y = roots_graph(ddf, a, b, s, 1e-3, 1000)
                r_x, r_y = roots_graph(f, a, b, h, eps, max_iter)
                plt.close(1)
                plt.get_current_fig_manager().canvas.set_window_title(
                    'Уточнение корней. График функции.')
                plt.plot(x, y, label = 'f(x)')
                plt.plot(p_x, p_y, 'mo', label = 'Точки перегиба')
                plt.plot(r_x, r_y, 'ro', label = 'Корни')
                plt.title('График функции')
                plt.xlabel('x')
                plt.ylabel('y = $' + func_enter.get() + '$')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
        except:
            box.showerror('Ошибка', 'Неверная функция!')

#первоначальный интерфейс
window = Tk()
window.title('Уточнение корней. Ввод.')
window.geometry('325x530+100+50')
window.resizable(False, False)
window.configure(bg = 'OliveDrab1')

#заголовок
tit_1 = Label(window, text = 'Уточнение корней функции\nметодом brenth',
             font = ('Comic Sans MS', 16), bg = 'OliveDrab1')
tit_1.place(x = 27, y = 10)

#ввод
func_hint = Label(window, text = 'Функция: ',
                  font = ('Times New Roman', 14), bg = 'OliveDrab1')
func_enter = Entry(window, font = 'Calibri 12')
func_enter.insert(0, 'sin(x) + 0.5')
func_hint.place(x = 40, y = 80)
func_enter.place(x = 40, y = 110, height = 20, width = 240)

begin_hint = Label(window, text = 'Начальное значение:',
                   font = ('Times New Roman', 14), bg = 'OliveDrab1')
begin_enter = Entry(window, font = 'Calibri 12')
begin_hint.place(x = 40, y = 140)
begin_enter.place(x = 40, y = 170, height = 20, width = 240)
                 
end_hint = Label(window, text = 'Конечное значение:',
                 font = ("Times New Roman", 14), bg = 'OliveDrab1')
end_enter = Entry(window, font = 'Calibri 12')
end_hint.place(x = 40, y = 200)
end_enter.place(x = 40, y = 230, height = 20, width = 240)
                 
step_hint = Label(window, text = 'Шаг прохода:',
                 font = ("Times New Roman", 14), bg = 'OliveDrab1')
step_enter = Entry(window, font = 'Calibri 12')
step_hint.place(x = 40, y = 260)
step_enter.place(x = 40, y = 290, height = 20, width = 240)

eps_hint = Label(window, text = 'Точность:',
                 font = ("Times New Roman", 14), bg = 'OliveDrab1')
eps_enter = Entry(window, font = 'Calibri 12')
eps_enter.insert(0, '1e-3')
eps_hint.place(x = 40, y = 320)
eps_enter.place(x = 40, y = 350, height = 20, width = 240)

max_iter_hint_1 = Label(window, text = 'Максимальное количество',
                 font = ("Times New Roman", 14), bg = 'OliveDrab1')
max_iter_hint_2 = Label(window, text = 'итераций:',
                 font = ("Times New Roman", 14), bg = 'OliveDrab1')
max_iter_enter = Entry(window, font = 'Calibri 12')
max_iter_enter.insert(0, '100')
max_iter_hint_1.place(x = 40, y = 380)
max_iter_hint_2.place(x = 40, y = 400)
max_iter_enter.place(x = 40, y = 430, height = 20, width = 240)

#кнопки
btn_table = Button(window, text = 'Таблица\nкорней',
                   command = roots_table)
btn_table.place(x = 25, y = 470, height = 40, width = 125)

btn_graph = Button(window, text = 'График\nфункции',
                   command = graph)
btn_graph.place(x = 175, y = 470, height = 40, width = 125)
    
window.mainloop()
