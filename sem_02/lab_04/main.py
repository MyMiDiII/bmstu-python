''' Лабораторная работа №4
    "Работа с графическим интерфейсом Canvas"

    Задается множество точек A и множество прямых B.
    Программа находит такие две различные точки,
    что проходящая через них прямая параллельна
    наибольшему количеству прямых из B.
'''

from tkinter import *
from info import *
from commands import *

points = []
lines = []

#ОКНО
window = Tk()
window.title('Параллельные прямые')
window.geometry('900x900+200+50')
window.resizable(False, False)
window.configure(bg = 'grey13')

#ИНТЕРФЕЙС

title = Label(window, text = "ПАРАЛЛЕЛЬНЫЕ ПРЯМЫЕ", bg = 'grey13',
              font = ('Impact', 16), fg = 'white')
title.place(x = 200, y = 10, height = 30, width = 500)

points_hint = Label(window, text = 'Введите точки:', bg = 'grey13',
              font = ("Times New Roman", 16), fg = 'white')
points_hint.place(x = 18, y = 70, height = 30, width = 200)

points_hint = Label(window, text = 'Введите прямые:', bg = 'grey13',
              font = ("Times New Roman", 16), fg = 'white')
points_hint.place(x = 28, y = 115, height = 30, width = 200)

points_enter = Entry(window, font = 'Calibry 14')
points_enter.place(x = 250, y = 70, height = 30, width = 620)

lines_enter = Entry(window, font = 'Calibry 14')
lines_enter.place(x = 250, y = 115, height = 30, width = 620)

clear_btn = Button(window, text = 'Очистить всё', bg = 'navajo white', command = \
                   lambda: clear(points_enter, lines_enter, field, points, lines, window),
                   font = '16')
clear_btn.place(x = 30, y = 170, height = 40, width = 260)

show_btn = Button(window, text = 'Отобразить', bg = 'navajo white', font = '16',
                  command = lambda: show(field, points_enter, lines_enter, points, lines))
show_btn.place(x = 320, y = 170, height = 40, width = 260)

solve_btn = Button(window, text = 'Решить', bg = 'navajo white', 
                   command = lambda: solve(points, lines, field, window), font = '16')
solve_btn.place(x = 610, y = 170, height = 40, width = 260)

answer_hint = Label(window, text = 'Найденные точки:', bg = 'grey13',
                    font = ('Times New Roman', 16), fg = 'white')
answer_hint.place(x = 10, y = 230, height = 30, width = 250)

reference_hint = Label(window, text = 'Правила ввода и пользования:', bg = 'grey13',
                       font = ('Times New Roman', 16), fg = 'white')
reference_hint.place(x = 30, y = 850, height = 30, width = 350)

reference_btn = Button(window, text = 'Справка', bg = 'navajo white',
                       command = lambda: reference(window), font = '16')
reference_btn.place(x = 390, y = 853, height = 30, width = 480)

# МЕНЮ
menu = Menu()

menu.add_command(label = 'Справка', command = lambda: reference(window))

menu.add_command(label = 'Об авторе', command = author)
menu.add_command(label = 'Выход', command = lambda: close(window))

window.config(menu = menu)

# ОКНО РИСОВАНИЯ
field = Canvas(window, height = 570, width = 840, bg = "grey17",
               highlightthickness = 0)
field.place(x = 30, y = 270)

field.bind("<Button-1>", lambda event, f = field, p = points: point(event, f, p))
field.bind("<Button-3>", lambda event, f = field, l = lines: line1(event, f, l))
field.bind("<Shift-Button-3>", lambda event, arg = field, l = lines: line(event, arg, l))

window.mainloop()
