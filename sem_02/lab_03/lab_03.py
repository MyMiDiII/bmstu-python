''' Лабораторная работа №3
    "Исследование методов сортировки."

    Назначение:
    1) сортировка списка методом пирамидальной сортировки;
    2) замер времени сортировки списков разных размерностей;
    3) построение графика зависимости времени сортировки от размерности
       списка.
'''

from tkinter import *
import tkinter.messagebox as box
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter

#функции для сортировки
def heapify(arr, n, i):
    num = i - 1
    i_f = 2 * num + 1
    i_s = 2 * num + 2
    
    while i_f < n:
        if i_s < n:
            if arr[i_f] > arr[i_s]:
                max_i = i_f
            else:
                max_i = i_s
        else:
            max_i = i_f
        
        if arr[num] < arr[max_i]:
            arr[num], arr[max_i] = arr[max_i], arr[num]
            num = max_i
            i_f = 2 * num + 1
            i_s = 2 * num + 2
        else:
            break
                
def buildHeap(arr,n):
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)

def heapsort(a):
    size = len(a)
    buildHeap(a, size)
    last = size - 1

    for i in range(size):
        a[0], a[last] = a[last], a[0]
        b = a[:last]
        heapify(b, last, 1)
        a = b + a[last:]
        last -= 1

    return a

def sort():
    try:
        a = list(map(int, entry_list.get().split()))
    
        if len(a) > 10:
            box.showerror("len > 10", "Превышена длина списка (max 10)")
        else:
            a = heapsort(a)
            sort_window = Toplevel(window)
            sort_window.title('Отсортированный список.')
            sort_window.geometry('250x300+500+50')
            sort_window.resizable(False, False)

            sort_canvas = Canvas(sort_window, width = 250, height = 300,
                                 bg = 'snow')
            
            sort_canvas.create_text(125, 20, text = 'Отсортированный список',
                   justify = CENTER, font = ('Impact', 16))

            text1 = Text(sort_window, font=('Courier New', 14))

            for i in range(len(a)):
                row = str(a[i])
                text1.insert('end', '{:^19}'.format(row) + '\n')
            
            text1.configure(state = DISABLED)
            text1.place(x = 20, y = 40, height = 225, width = 210)

            sort_canvas.place(x = 0, y = 0)

            sort_window.mainloop()
    except:
        box.showerror("Неверные данные", "Проверьте корректность введенных" +
                      " данных.\n Элементы списка -- целые числа")

#фунцкии для замера времени
def create_ordered_array(n):
    a = []

    for i in range(n):
        a.append(i)

    return a

def create_random_array(n):
    a = []

    for i in range(n):
        a.append(randint(-1000, 1000))

    return a

def get_time():
    try:
        n1 = int(entry_n1.get())
        n2 = int(entry_n2.get())
        n3 = int(entry_n3.get())

        if n1 <= 0 or n2 <= 0 or n3 <= 0:
            box.showerror("Ненатуральные числа.", "Размерность списка -- " +
                          "натуральное число.")
            return

        if n1 > 50000 or n2 > 50000 or n3 > 50000:
            answer = box.askyesno(title="Большие размерности",
                                message="Одна или несколько размерностей " +
                                "слишком большие, что может привести к " +
                                "долгой работе программы или её аварийному " +
                                "закрытию.\nХотите продолжить?")
            if answer == False:
                return

        a1 = create_ordered_array(n1)
        a2 = create_ordered_array(n2)
        a3 = create_ordered_array(n3)

        random_a1 = create_random_array(n1)
        random_a2 = create_random_array(n2)
        random_a3 = create_random_array(n3)

        reversed_a1 = list(reversed(a1))
        reversed_a2 = list(reversed(a2))
        reversed_a3 = list(reversed(a3))

        start_1 = perf_counter()
        heapsort(a1)
        finish_1 = perf_counter() - start_1

        start_2 = perf_counter()
        heapsort(a2)
        finish_2 = perf_counter() - start_2

        start_3 = perf_counter()
        heapsort(a3)
        finish_3 = perf_counter() - start_3

        start_4 = perf_counter()
        heapsort(random_a1)
        finish_4 = perf_counter() - start_4

        start_5 = perf_counter()
        heapsort(random_a2)
        finish_5 = perf_counter() - start_5

        start_6 = perf_counter()
        heapsort(random_a3)
        finish_6 = perf_counter() - start_6

        start_7 = perf_counter()
        heapsort(reversed_a1)
        finish_7 = perf_counter() - start_7

        start_8 = perf_counter()
        heapsort(reversed_a2)
        finish_8 = perf_counter() - start_8

        start_9 = perf_counter()
        heapsort(reversed_a3)
        finish_9 = perf_counter() - start_9
    
        table_window = Toplevel(window)
        table_window.title('Время работы.')
        table_window.geometry('500x370+500+50')
        table_window.resizable(False, False)

        table_canvas = Canvas(table_window, width = 500, height = 370,
                              bg = 'snow')
            
        table_canvas.create_text(250, 20, text = 'Время работы',
                     justify = CENTER, font = ('Impact', 16))

        table_canvas.create_line(20, 50, 480, 50)
        table_canvas.create_line(20, 90, 480, 90)
        table_canvas.create_line(20, 170, 480, 170)
        table_canvas.create_line(20, 250, 480, 250)
        table_canvas.create_line(20, 330, 480, 330)
        table_canvas.create_line(20, 50, 20, 330)
        table_canvas.create_line(135, 50, 135, 330)
        table_canvas.create_line(250, 50, 250, 330)
        table_canvas.create_line(365, 50, 365, 330)
        table_canvas.create_line(480, 50, 480, 330)

        table_canvas.create_text(80, 70, text = 'N =',
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(80, 130, text = 'Упорядоченный\nсписок',
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(80, 210, text = 'Случайный\nсписок',
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(80, 290, text = 'Список,\nупорядоченный\n'
                                 + 'в обратном\nпорядке',
                     justify = CENTER, font = ('Arial', 10))
    
        table_canvas.create_text(195, 70, text = str(n1),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(310, 70, text = str(n2),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(425, 70, text = str(n3),
                     justify = CENTER, font = ('Arial', 10))

        table_canvas.create_text(195, 130, text = '{:^20.3g}'.format(finish_1),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(310, 130, text = '{:^20.3g}'.format(finish_2),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(425, 130, text = '{:^20.3g}'.format(finish_3),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(195, 210, text = '{:^20.3g}'.format(finish_4),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(310, 210, text = '{:^20.3g}'.format(finish_5),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(425, 210, text = '{:^20.3g}'.format(finish_6),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(195, 290, text = '{:^20.3g}'.format(finish_7),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(310, 290, text = '{:^20.3g}'.format(finish_8),
                     justify = CENTER, font = ('Arial', 10))
        table_canvas.create_text(425, 290, text = '{:^20.3g}'.format(finish_9),
                     justify = CENTER, font = ('Arial', 10))

        table_canvas.place(x = 0, y = 0)
    except:
        box.showerror("Нецелочисленные данные.", "Размерность списка -- " +
                          "натуральное число.")

#функции для построения графика
def graphic():
    try:
        begin = int(entry_begin.get())
        end = int(entry_end.get())

        if begin > 0 and end > 0:
            if begin >= end:
                box.showerror("Неверный отрезок", "Начало должно быть меньше "+
                              "конца.")
                return

            if begin > 50000 or end > 50000:
                answer = box.askyesno(title="Большие размерности",
                                message="Одна или несколько размерностей " +
                                "слишком большие, что может привести к " +
                                "долгой работе программы или её аварийному " +
                                "закрытию.\nХотите продолжить?")
                if answer == False:
                    return

            step = (end - begin) // 9

            if (step >= 1):
                ns = []
                count = 0
                for i in range(begin, end + 1, step):
                    ns.append(i)
                    count += 1
                    if count == 10:
                        break

                times = []
                for i in range(10):
                    a = create_random_array(ns[i])
                    start = perf_counter()
                    heapsort(a)
                    finish = start - perf_counter()
                    times.append(abs(finish))

                plt.close(1)
                plt.get_current_fig_manager().canvas.set_window_title(
                          'График зависимости времени от размерности списка.')
                plt.plot(ns, times, label = 'time(N)')
                plt.title('График зависимости времени от размерности списка.')
                plt.xlabel('N')
                plt.ylabel('time')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
            else:
                box.showerror("Неверный отрезок", "На заданном отрезке нет " +
                              "десяти натуральных чисел")
        else:
            box.showerror("Ненатуральные числа.", "Размерность списка -- " +
                          "натуральное число.")
    except:
        box.showerror("Нецелочисленные данные.", "Размерность списка -- " +
                          "натуральное число.")

#СПРАВКА

#информация о программе
def info():
    box.showinfo('О программе.',
                 '1) Сортировка списков малых размерностей.\n' +
                 '2) Время работы для разных типов списков и размерностей.\n' +
                 '3) График зависимости времени работы от размерности списка.')

#интформация об авторе
def author():
    box.showinfo('Об авторе', 'Маслова Марина.\nИУ7-23Б.')

#выход
def close():
    window.destroy()

#ОКНО
window = Tk()
window.title('Пирамидальная сортировка.')
window.geometry('400x490+100+50')
window.resizable(False, False)

#меню
menu = Menu()

info_menu = Menu()
info_menu.add_command(label = 'О программе', command = info)
info_menu.add_command(label = 'Об авторе', command = author)

menu.add_cascade(label = "Справка", menu = info_menu)
menu.add_command(label = 'Выход', command = close)

window.config(menu=menu)

#ИНТЕРФЕЙС
canvas = Canvas(window, width = 700, height = 500)

background = PhotoImage(file = 'main.png')
canvas.create_image(0, 0, image = background, anchor = NW)

canvas.create_text(200, 20, text = 'Пирамидальная сортировка',
                   justify = CENTER, font = ('Impact', 18))

#сортировка списка до 10 элементов
canvas.create_text(200, 50, text = 'Сортировка списка до 10 элементов',
                   justify = CENTER, font = ('Comic Sans MS', 16))
canvas.create_text(90, 80, text = 'Введите список: ',
                   font = ('Times New Roman', 14))
entry_list = Entry(window, font = 'Calibri 12')
entry_list.place(x = 20, y = 100, width = 220)
button_sort = Button(window, text = 'Отсортировать', bg = 'snow',
                     command = sort)
button_sort.place(x = 260, y = 75, width = 120, height = 50)

#замер времени
canvas.create_text(200, 160, text = 'Замер времени для трех разных\n' +
                   ' размерностей списка',
                   justify = CENTER, font = ('Comic Sans MS', 16))
canvas.create_text(110, 205, text = 'Введите размерности:', justify = LEFT,
                   font = ('Times New Roman', 14))
canvas.create_text(45, 235, text = 'N1 =', font = ('Times New Roman', 14))
entry_n1 = Entry(window, font = 'Calibri 12')
entry_n1.place(x = 70, y = 222.5, width = 175)

canvas.create_text(45, 265, text = 'N2 =', font = ('Times New Roman', 14))
entry_n2 = Entry(window, font = 'Calibri 12')
entry_n2.place(x = 70, y = 252.5, width = 175)

canvas.create_text(45, 295, text = 'N3 =', font = ('Times New Roman', 14))
entry_n3 = Entry(window, font = 'Calibri 12')
entry_n3.place(x = 70, y = 282.5, width = 175)

button_sort = Button(window, text = 'Сделать\nзамер\nвремени', bg = 'snow',
                     command = get_time)
button_sort.place(x = 260, y = 223, width = 120, height = 85)

#построение графика
canvas.create_text(200, 350, text = 'График зависимости времени\nсортировки' +
                   ' от размерности списка',
                   justify = CENTER, font = ('Comic Sans MS', 16))
canvas.create_text(175, 400, text = 'Введите отрезок размерностей списка:',
                   justify = LEFT, font = ('Times New Roman', 14))
canvas.create_text(50, 425, text = 'Начало:',
                   justify = LEFT, font = ('Times New Roman', 14))
canvas.create_text(46, 455, text = 'Конец:',
                   justify = LEFT, font = ('Times New Roman', 14))
entry_begin = Entry(window, font = 'Calibri 12')
entry_begin.place(x = 85, y = 415, width = 160)
entry_end = Entry(window, font = 'Calibri 12')
entry_end.place(x = 85, y = 445, width = 160)

button_sort = Button(window, text = 'Построить график', bg = 'snow',
                     command = graphic)
button_sort.place(x = 260, y = 415, width = 120, height = 55)

canvas.place(x = 0, y = 0)

window.mainloop()
