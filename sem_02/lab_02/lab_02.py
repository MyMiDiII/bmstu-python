'''Лабораторная работа №2
   Калькулятор

   Назначение:
   сложение и вычитание чисел в 16-ричной СС.

   Тестовый пример:
   Ввод:
   123
   123
   Вывод:
   123
   +
   123
   ---
   246
'''

from tkinter import *
import tkinter.messagebox as box

symbols = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',
           '-', '.', '+']

addition_table = \
[['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
 ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','10'],
 ['2','3','4','5','6','7','8','9','A','B','C','D','E','F','10','11'],
 ['3','4','5','6','7','8','9','A','B','C','D','E','F','10','11','12'],
 ['4','5','6','7','8','9','A','B','C','D','E','F','10','11','12','13'],
 ['5','6','7','8','9','A','B','C','D','E','F','10','11','12','13','14'],
 ['6','7','8','9','A','B','C','D','E','F','10','11','12','13','14','15'],
 ['7','8','9','A','B','C','D','E','F','10','11','12','13','14','15','16'],
 ['8','9','A','B','C','D','E','F','10','11','12','13','14','15','16','17'],
 ['9','A','B','C','D','E','F','10','11','12','13','14','15','16','17','18'],
 ['A','B','C','D','E','F','10','11','12','13','14','15','16','17','18','19'],
 ['B','C','D','E','F','10','11','12','13','14','15','16','17','18','19','1A'],
 ['C','D','E','F','10','11','12','13','14','15','16','17','18','19','1A','1B'],
 ['D','E','F','10','11','12','13','14','15','16','17','18','19','1A','1B','1C'],
 ['E','F','10','11','12','13','14','15','16','17','18','19','1A','1B','1C','1D'],
 ['F','10','11','12','13','14','15','16','17','18','19','1A','1B','1C','1D','1E']]

#ДЕЙСТВИЯ

#преобразование результата
def del_zeros(r):
    i = 0
    while r[i] == '0':
        r = r[1:]
        if r == '':
            break;

    if r == '' or r[0] == '.':
        r = '0' + r

    if r.find('.') != -1:
        i = len(r) - 1
        while r[i] == '0':
            r = r[:-1]
            i -= 1

    if r[-1] == '.':
        r = r[:-1]

    return r

#преобразование к нужному виду
def bad_to_good(f, s):
    if (f.find('.') != -1):
        f_b, f_a = f.split('.')
    else:
        f_b = f
        f_a = ''
    if (s.find('.') != -1):
        s_b, s_a = s.split('.')
    else:
        s_b = s
        s_a = ''

    len_f_b = len(f_b)
    len_s_b = len(s_b)

    if (len_f_b > len_s_b):
        s_b = '0' * (len_f_b - len_s_b) + s_b
    else:
        f_b = '0' * (len_s_b - len_f_b) + f_b

    len_f_a = len(f_a)
    len_s_a = len(s_a)

    if (len_f_a > len_s_a):
        s_a = s_a + '0' * (len_f_a - len_s_a)
    else:
        f_a = f_a + '0' * (len_s_a - len_f_a)

    f = f_b + '.' + f_a
    s = s_b + '.' + s_a

    return f, s

#сложение
def plus(f, s):
    f, s = bad_to_good(f, s)
    r = ''
    next = ''

    #собственно сложение
    for i in range(len(f) - 1, -1, -1):
        if f[i] == '.':
            ch = '.'
        else:
            ch = addition_table[symbols.index(f[i])][symbols.index(s[i])]

            #переход из предыдущего разряда
            if next != '':
                if len(ch) == 2:
                    ch = (ch[0] +
                    addition_table[symbols.index(ch[1])][symbols.index('1')])
                else:
                    ch = addition_table[symbols.index(ch)][symbols.index('1')]

            #переход в следующий разряд
            if len(ch) == 2:
                next = ch[0]
                ch = ch[1]
            else:
                next = ''

        r = ch + r

    r = next + r

    r = del_zeros(r)

    return r

#вычитание
def mines(f, s):
    f, s = bad_to_good(f, s)
    sgn = ''
    r = ''

    if f < s:
        f, s = s, f
        sgn = '-'

    for i in range(len(f) - 1, -1, -1):
        if f[i] == '.':
            ch = '.'
        else:
            if symbols.index(f[i]) >= symbols.index(s[i]):
                ch = symbols[addition_table[symbols.index(s[i])].index(f[i])]
            else:
                #поиск ненулевого разряда
                j = i - 1
                if f[j] == '.':
                    j -= 1
                while f[j] == '0':
                    j -= 1
                    if f[j] == '.':
                        j -= 1

                #обновление разрядов
                f = f[:j] + symbols[symbols.index(f[j]) - 1] + f[j+1:]
                j += 1
                if f[j] == '.':
                    j += 1
                while j < i:
                    if f[j] == '.':
                        j += 1
                    f = f[:j] + 'F' + f[j+1:]
                    j += 1
                    
                md = '1' + f[i]
                ch = symbols[addition_table[symbols.index(s[i])].index(md)]

        r = ch + r

    r = del_zeros(r)

    r = sgn + r

    return r

#выполнение выбранного действия
def action(first, second, p_or_m):
    #проверка ввода на корректность
    first = first.strip()
    first = first.upper()
    len_first = len(first)

    error = False
    for i in range(len_first):
        if first[i] not in symbols:
            error = True
            break;
        if first[i] in ['-', '+'] and i != 0:
            error = True


    if first.count('.') > 1:
        error = True

    second = second.strip()
    second = second.upper()
    len_second = len(second)

    for i in range(len_second):
        if second[i] not in symbols:
            error = True
        if second[i] in ['-', '+'] and i != 0:
            error = True

    if second.count('.') > 1:
        error = True

    if (len_second == 0 or len_first == 0 or
        len_first == 1 and first[0] in ['-', '+', '.'] or
        len_second == 1 and second[0] in ['-', '+', '.']):
        error = True

    if error:
        box.showerror('Ошибка ввода', 'Проверьте корректность входных ' +
                      'данных.\n(Необходимо ввести шестнадцатиричные числа,' +
                      '\nможно использовать любой регистр.)')
    else:
        #приведение к нужному виду
        if first[0] == '+':
            first = first[1:]

        if second[0] == '+':
            second = second[1:]

        if first.find('.') != -1:
            while first[-1] == '0':
                first = first[:-1]

        if second.find('.') != -1:
            while second[-1] == '0':
                second = second[:-1]

        if first[-1] == '.':
            first = first[:-1]

        if second[-1] == '.':
            second = second[:-1]

        sgn_f = first[0]
        sgn_s = second[0]

        if p_or_m == '+':
            if sgn_f == '-':
                if sgn_s == '-':
                    result = '-' + plus(first[1:], second[1:])
                else:
                    result = mines(second, first[1:])
            else:
                if sgn_s == '-':
                    result = mines(first, second[1:])
                else:
                    result = plus(first, second)
        else:
            if sgn_f == '-':
                if sgn_s == '-':
                    result = mines(second[1:], first[1:])
                else:
                    result = '-' + plus(first[1:], second)
            else:
                if sgn_s == '-':
                    result = plus(first, second[1:])
                else:
                    result = mines(first, second)

        if (len(first) <= 17 and len(second) <= 17 and len(result) <= 17):
            clear = Label(window, bg = 'dodger blue')
            clear.place(x = 260, y = 224, height = 87, width = 180)
            a = Label(window, text = first, bg = 'dodger blue',
                      font = ('Times New Roman',14), anchor = E)
            b = Label(window, text = second, bg = 'dodger blue',
                      font = ('Times New Roman', 14), anchor = E)
            p = Label(window, text = p_or_m, bg = 'dodger blue',
                      font = ('Times New Roman', 14))
            line = Label(window, bg = 'black')
            r = Label(window, text = result, bg = 'dodger blue',
                      font = ('Times New Roman', 14), anchor = E)

            a.place(x = 280, y = 225, height = 20, width = 160)
            b.place(x = 280, y = 250, height = 20, width = 160)
            p.place(x = 260, y = 238, height = 20, width = 10)
            line.place(x = 280, y = 275, height = 2, width = 160)
            r.place(x = 280, y = 290, height = 20, width = 160)
        else:
            if p_or_m == '+':
                act = 'сложения'
            else:
                act = 'вычитания'
            clear = Label(window, text = 'Cм. окно информации;\n'
                          + 'если вы его закрыли,\nнажмите кнопку действия'
                          + '\nещё раз', bg = 'dodger blue')
            clear.place(x = 260, y = 224, height = 87, width = 180)
            box.showinfo('Превышена длина вывода', 'Результат ' +
                         act + ' чисел\n' + first + '\nи\n' + second +
                         '\nравен\n' + result)

#очистка полей
def clean():
    f_num_enter.delete(0, END)
    s_num_enter.delete(0, END)
    clear = Label(window, bg = 'dodger blue')
    clear.place(x = 260, y = 224, height = 87, width = 180)

#выход
def close():
    window.destroy()

#СПРАВКА

#информация о программе
def info():
    box.showinfo('О программе.',
                'Программа производит сложение\nи вычитание ' +
                'шестнадцатиричных чисел.')

#интформация об авторе
def author():
    box.showinfo('Об авторе', 'Маслова Марина.\nИУ7-23Б.')

#ВВОД В АКТИВНЫЙ ENTRY
current_entry = None

def on_focus(evt):
    global current_entry
    current_entry = evt.widget


def insert(sym):
    if current_entry is None:
        box.showerror('Не выбрано поле ввода', 'Установите курсор в одном ' +
                      'из полей ввода')
    else:
        current_entry.insert(current_entry.index(INSERT), sym)

def delete():
    if current_entry is None:
        box.showerror('Не выбрано поле ввода', 'Установите курсор в одном ' +
                      'из полей ввода')
    else:
        insert = current_entry.index("insert")
        if insert != 0:
            current_entry.delete(insert-1)


#ИНТЕРФЕЙС
window = Tk()
window.title("Калькулятор")
window.geometry("460x320+400+100")
window.resizable(False, False)
window.configure(bg = 'dodger blue')

#меню
menu = Menu()

actions_menu = Menu()
actions_menu.add_command(label = 'Сложение',
                         command = lambda: action(f_num_enter.get(),
                                                  s_num_enter.get(), '+'))
actions_menu.add_command(label = 'Вычитание',
                         command = lambda: action(f_num_enter.get(),
                                                  s_num_enter.get(), '-'))
actions_menu.add_command(label = 'Очистка полей', command = clean)
actions_menu.add_separator()
actions_menu.add_command(label = 'Выход', command = close)

info_menu = Menu()
info_menu.add_command(label = 'О программе', command = info)
info_menu.add_command(label = 'Об авторе', command = author)

menu.add_cascade(label = "Действия", menu = actions_menu)
menu.add_cascade(label = "Справка", menu = info_menu)

window.config(menu=menu)

#кнопки
sym_C = Button(window, text = 'C', bg = 'navajo white',
               command = lambda: insert('C'))
sym_D = Button(window, text = 'D', bg = 'navajo white',
               command = lambda: insert('D'))
sym_E = Button(window, text = 'E', bg = 'navajo white',
               command = lambda: insert('E'))
sym_F = Button(window, text = 'F', bg = 'navajo white',
               command = lambda: insert('F'))
sym_8 = Button(window, text = '8', bg = 'navajo white',
               command = lambda: insert('8'))
sym_9 = Button(window, text = '9', bg = 'navajo white',
               command = lambda: insert('9'))
sym_A = Button(window, text = 'A', bg = 'navajo white',
               command = lambda: insert('A'))
sym_B = Button(window, text = 'B', bg = 'navajo white',
               command = lambda: insert('B'))
sym_4 = Button(window, text = '4', bg = 'navajo white',
               command = lambda: insert('4'))
sym_5 = Button(window, text = '5', bg = 'navajo white',
               command = lambda: insert('5'))
sym_6 = Button(window, text = '6', bg = 'navajo white',
               command = lambda: insert('6'))
sym_7 = Button(window, text = '7', bg = 'navajo white',
               command = lambda: insert('7'))
sym_0 = Button(window, text = '0', bg = 'navajo white',
               command = lambda: insert('0'))
sym_1 = Button(window, text = '1', bg = 'navajo white',
               command = lambda: insert('1'))
sym_2 = Button(window, text = '2', bg = 'navajo white',
               command = lambda: insert('2'))
sym_3 = Button(window, text = '3', bg = 'navajo white',
               command = lambda: insert('3'))
sym_point = Button(window, text = '.', bg = 'navajo white',
               command = lambda: insert('.'))
sym_m = Button(window, text = '-', bg = 'navajo white',
               command = lambda: insert('-'))
sym_backspace = Button(window, text = '<-- Backspace', bg = 'navajo white',
               command = delete)
sym_plus = Button(window, text = 'Сложить', bg = 'navajo white',
                  command = lambda: action(f_num_enter.get(),
                                          s_num_enter.get(), '+'))
sym_minus = Button(window, text = 'Вычесть', bg = 'navajo white',
                   command = lambda: action(f_num_enter.get(),
                                            s_num_enter.get(), '-'))

sym_C.place(x = 20, y = 20, height = 40, width = 40)
sym_D.place(x = 80, y = 20, height = 40, width = 40)
sym_E.place(x = 140, y = 20, height = 40, width = 40)
sym_F.place(x = 200, y = 20, height = 40, width = 40)
sym_8.place(x = 20, y = 80, height = 40, width = 40)
sym_9.place(x = 80, y = 80, height = 40, width = 40)
sym_A.place(x = 140, y = 80, height = 40, width = 40)
sym_B.place(x = 200, y = 80, height = 40, width = 40)
sym_4.place(x = 20, y = 140, height = 40, width = 40)
sym_5.place(x = 80, y = 140, height = 40, width = 40)
sym_6.place(x = 140, y = 140, height = 40, width = 40)
sym_7.place(x = 200, y = 140, height = 40, width = 40)
sym_0.place(x = 20, y = 200, height = 40, width = 40)
sym_1.place(x = 80, y = 200, height = 40, width = 40)
sym_2.place(x = 140, y = 200, height = 40, width = 40)
sym_3.place(x = 200, y = 200, height = 40, width = 40)
sym_point.place(x = 20, y = 260, height = 40, width = 40)
sym_m.place(x = 80, y = 260, height = 40, width = 40)
sym_backspace.place(x = 140, y = 260, height = 40, width = 100)
sym_plus.place(x = 260, y = 155, height = 30, width = 80)
sym_minus.place(x = 360, y = 155, height = 30, width = 80)

#поля ввода и вывода + подсказки
f_num_hint = Label(window, text = 'Первое число:', bg = 'dodger blue',
                   font = ('Times New Roman', 14))
s_num_hint = Label(window, text = 'Второе число:', bg = 'dodger blue',
                   font = ('Times New Roman', 14))
result_hint = Label(window, text = 'Результат:', bg = 'dodger blue',
                   font = ('Times New Roman', 14))

f_num_enter = Entry(window, font = 'Calibri 16')
f_num_enter.bind('<FocusIn>', on_focus)
s_num_enter = Entry(window, font = 'Calibri 16')
s_num_enter.bind('<FocusIn>', on_focus)

f_num_hint.place(x = 260, y = 20, height = 20, width = 120)
f_num_enter.place(x = 260, y = 40, height = 30, width = 180)
s_num_hint.place(x = 260, y = 85, height = 30, width = 120)
s_num_enter.place(x = 260, y = 110, height = 30, width = 180)
result_hint.place(x = 260, y = 200, height = 30, width = 90)

window.mainloop()
