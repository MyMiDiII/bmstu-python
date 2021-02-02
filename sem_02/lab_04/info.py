from tkinter import *
import tkinter.messagebox as box

def reference(main):
    reference_window = Toplevel(main)

    reference_window.title('Параллельные прямые – Справка')
    reference_window.geometry('570x600+1100+85')
    reference_window.resizable(False, False)
    reference_window.configure(bg = 'grey13')
    
    title = Label(reference_window, text = "ПАРАЛЛЕЛЬНЫЕ ПРЯМЫЕ – СПРАВКА", bg = 'grey13',
              font = ('Impact', 16), fg = 'white')
    title.place(x = 30, y = 10)
    
    #ABOUT PROGRAM
    info_title = Label(reference_window, justify = LEFT, font = ('Lucida Console', 14),
                       text = "О программе", bg = 'grey13', fg = 'white')
    info_title.place(x = 20, y = 60)

    info = Label(reference_window, justify = LEFT, font = ('Times New Roman', 12), text =
                'Программа  находит  две  различные  точки  из заданного\nмножества   точек  А ' +
                ' такие,  что  проходящая  через  них\nпрямая параллельна наибольшему ' +
                'количеству прямых из\nзаданного множества прямых B.', bg = 'grey13', fg = 'white')
    info.place(x = 25, y = 90)

    #INPUT
    input_title = Label(reference_window, justify = LEFT, font = ('Lucida Console', 14),
                       text = "Правила ввода через координаты", bg = 'grey13', fg = 'white')
    input_title.place(x = 20, y = 200)
    
    input_hint = Label(reference_window, justify = LEFT, font = ('Times New Roman', 12), text =
                'Точка    задается    двумя    координатами   через   пробел.\n' +
                'Различные      точки      также    разделяются     пробелами\n' +
                'Например, две точки (6, 7)  и  (1, 9) должны быть введены\nтак:' +
                ' 6 7 1 9\n\n'+
                'Прямая  задается  двумя  точками.  Точки вводятся так же.\n' +
                'Точки   одной  прямой  и  прямые  разделяются  пробелом\n' +
                'Например, две прямые  А:  (6, 7),  (1, 9) и  B:  (0, 0),  (1, 1)\n' +
                'должны быть введены так: 6 7 1 9 0 0 1 1\n', bg = 'grey13', fg = 'white')
    input_hint.place(x = 25, y = 230)

    #DRAW
    draw_title = Label(reference_window, justify = LEFT, font = ('Lucida Console', 14),
                       text = "Правила ввода в окне рисования", bg = 'grey13', fg = 'white')
    draw_title.place(x = 20, y = 460)
    
    draw_hint = Label(reference_window, justify = LEFT, font = ('Times New Roman', 12), text =
                'Точка      вводится     нажатием     левой     кнопки     мыши.\n' +
                'Правая  кнопка  мыши  – для задания первой точки прямой.\n' +
                'Shift  +  правая  кнопка  мыши  –  для задания второй точки\nпрямой.', 
                bg = 'grey13', fg = 'white')
    draw_hint.place(x = 25, y = 490)

    reference_window.mainloop()

def author():
    box.showinfo('Об авторе', 'Маслова Марина.\nИУ7-23Б.')

#выход
def close(what):
    what.destroy()