from tkinter import *
import tkinter.messagebox as box

R = 3

def clear(enter1, enter2, field, points, lines, window):
    enter1.delete(0, 'end')
    enter2.delete(0, 'end')
    field.delete('all')
    points.clear()
    lines.clear()
    c = Label(window, bg = 'grey13',
                       font = ("Times New Roman", 16), fg = 'white')
    c.place(x = 260, y = 230, height = 30, width = 640)

def draw_line(line, field):
    x = line[0]
    x1 = line[2]
    y = line[1]
    y1 = line[3]
    if (x == x1 and y == y1):
        return
    elif x == x1:
        xb = x
        yb = 0
        xe = x
        ye = 570
    elif y == y1:
        xb = 0
        yb = y
        xe = 840
        ye = y
    else:
        xb = 0
        yb = -x * (y1 - y) / (x1 - x) + y
        xe = 840
        ye = (xe - x) * (y1 - y) / (x1 - x) + y
    field.create_line(xb, yb, xe, ye, fill = 'cyan')

def draw_result_line(line, field):
    x = line[0]
    x1 = line[2]
    y = line[1]
    y1 = line[3]
    if (x == x1 and y == y1):
        return
    elif x == x1:
        xb = x
        yb = 0
        xe = x
        ye = 570
    elif y == y1:
        xb = 0
        yb = y
        xe = 840
        ye = y
    else:
        xb = 0
        yb = -x * (y1 - y) / (x1 - x) + y
        xe = 840
        ye = (xe - x) * (y1 - y) / (x1 - x) + y
    field.create_line(xb, yb, xe, ye, fill = 'orange')

def draw_point(point, field):
    x = point[0]
    y = point[1]
    field.create_oval(x - R, y - R, x + R, y + R, fill = 'green yellow')

def draw_result_point(point, field):
    x = point[0]
    y = point[1]
    field.create_oval(x - R, y - R, x + R, y + R, fill = 'red')

def point(event, field, points):
    x = event.x
    y = event.y
    points.append([x, y])
    draw_point(points[len(points) - 1], field)

def line1(event, field, lines):
    x = event.x
    y = event.y
    lines.append([x, y, -1, -1])

def line(event, field, lines):
    len_lines = len(lines)
    x = event.x
    y = event.y
    if len_lines and lines[len_lines - 1][2] == -1:
        lines[len_lines - 1][2] = x
        lines[len_lines - 1][3] = y
        x1 = lines[len_lines - 1][0]
        y1 = lines[len_lines - 1][1]
        if x == x1 and y == y1:
            lines.pop
            return
        else:
            draw_line(lines[len_lines - 1], field)

def wrong_coordinats():
    box.showinfo('Неверные координаты.', 'Координаты – целые неотрицательные числа.')

def wrong_x():
    box.showinfo('Неверные координаты.', '0 <= x <= 840')

def wrong_y():
    box.showinfo('Неверные координаты.', '0 <= y <= 570')

def wrong_number():
    box.showinfo('Неверные координаты.', 'Неверное количество координат')

def fill_array(array, total, length, field):
    if len(array) % length != 0:
        wrong_number()
        return
    next_elem = []
    for i in array:
        if i < 0:
            wrong_coordinats()
            return
        if len(next_elem) % 2 == 0 and i > 840:
            wrong_x()
            return
        if len(next_elem) % 2 == 1 and i > 570:
            wrong_y()
            return
        next_elem.append(i)
        if len(next_elem) == length:
            if length == 2:
                draw_point(next_elem, field)
            if length == 4:
                draw_line(next_elem, field)
            total.append(next_elem)
            next_elem = []

def show(field, in_points, in_lines, points, lines):
    try:
        p_arr = list(map(int, in_points.get().split()))
        l_arr = list(map(int, in_lines.get().split()))

        fill_array(p_arr, points, 2, field)
        fill_array(l_arr, lines, 4, field)
    except:
        wrong_coordinats()

def is_parallel(point1, point2, line):
    xp1 = point1[0]
    yp1 = point1[1]
    xp2 = point2[0]
    yp2 = point2[1]
    xl1 = line[0]
    yl1 = line[1]
    xl2 = line[2]
    yl2 = line[3]

    return abs((xp1 - xp2) * (yl1 - yl2) - (yp1 - yp2) * (xl1 - xl2)) < 6000

def solve(points, lines, field, window):
    len_p = len(points)

    result_point_1 = []
    result_point_2 = []
    result_line = []
    max_num = 0
    for i in range(len_p):
        for j in range(i + 1, len_p):
            if points[i] != points[j]:
                num = 0
                for k in lines:
                    if is_parallel(points[i], points[j], k):
                        num += 1
                if num > max_num:
                    max_num = num
                    result_point_1 = points[i]
                    result_point_2 = points[j]
                    result_line = points[i] + points[j]
    if max_num != 0:
        draw_result_point(result_point_1, field)
        draw_result_point(result_point_2, field)
        draw_result_line(result_line, field)
        result = Label(window, text = 'A(%d,%d) и B(%d, %d)' % (result_point_1[0], result_point_1[1],
                       result_point_2[0], result_point_2[1]), bg = 'grey13',
                       font = ("Times New Roman", 16), fg = 'white')
        result.place(x = 360, y = 230, height = 30, width = 400)
    else:
        result = Label(window, text = 'Точки не найдены', bg = 'grey13',
                       font = ("Times New Roman", 16), fg = 'white')
        result.place(x = 360, y = 230, height = 30, width = 250)
    