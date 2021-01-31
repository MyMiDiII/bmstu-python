'''Лабораторная работа №10
   "Меню для работы с записями в файле"

   Назначение:
   1)выбор файла для работы;
   2)создание в нём нового набора записей;
   3)добавление записей в файл;
   4)вывод всех запсей;
   5)поиск по одному полю;
   6)поиск по двум полям.

   Переменные, используемые в программе:
   name_of_file -- имя выбранного файла;
   choice -- выбранный пункт меню;
   last_name, name, year, raz -- данные спортсмена;
   zap -- запись одного спортсмена;
   ans, ans2, ans1_1, ans_12, ans_2, ans_21 -- ответы
   пользователя на вопросы программы;
   file -- файл, с которым проиходит работа;
   i, j -- номер поля и количество записей;
   el -- значение поля текущей записи;
   st, row -- текущая запись.

   Тестовый пример:
   Входные данные:
   1
   Sport.txt
   4
   0
   Выходные данные:
   ┌─────────────────────────┬────────────────┬──────────────┬───────────────────┐
   │ФАМИЛИЯ                  │ИМЯ             │ГОД РОЖДЕНИЯ  │РАЗРЯД ИЛИ ЗВАНИЕ  │
   ├─────────────────────────┼────────────────┼──────────────┼───────────────────┤
   │Улыбин                   │Аркадий         │2011          │1 юн. р.           │
   └─────────────────────────┴────────────────┴──────────────┴───────────────────┘

'''
#печать шапки таблицы
def print_hat():
    print('┌','─'*25,'┬','─'*16,'┬','─'*14,'┬','─'*19,'┐',sep = '')
    print('│ФАМИЛИЯ                  ', end = '')
    print('│ИМЯ             ', end = '')
    print('│ГОД РОЖДЕНИЯ  ', end = '')
    print('│РАЗРЯД ИЛИ ЗВАНИЕ  │')
    print('├','─'*25,'┼','─'*16,'┼','─'*14,'┼','─'*19,'┤', sep = '')

#ввод записи и добавление её в файл
def print_sportsmen(f):
    print('Введите данные по новым спортcменам:')
    while True:
        print('Фамилия:', end=' ')
        last_name = input()
        print('Имя:', end=' ')
        name = input()
        print('Год рождения: ', end=' ')
        year = input()
        print('Разряд или звание:', end=' ')
        raz = input()
        zap = last_name + ' ' + name + ' ' + year + ' ' + raz
        f.write(zap)
        f.write('\n')
        print()
        print('Добавить ещё одного спортсмена? (0 - Нет; 1 - Да)')
        ans = input()
        if ans == '0':
            break
#печать записи
def print_row(row):
    i = 1
    for el in row.split(' ', 3):
        if i == 1:
            print('│{:<25}'.format(el), end='')
        elif i == 2:
            print('│{:<16}'.format(el), end='')
        elif i == 3:
            print('│{:<14}'.format(el), end='')
        else:
            print('│{:<19}│'.format(el[:len(el) - 1]))
        i += 1

#выбор файла
def choice_of_file():
    global name_of_file
    print('   Выбор файла.')
    print()
    print('Введите имя файла.')
    print('Если файл лежит в папке, отличной от папки программы,\n'
          'укажите полное имя файла (указав путь к нему): ')
    name_of_file = input()
    try:
        file = open(name_of_file)
        file.close()
    except:
        try:
            file = open(name_of_file, 'w')
            file.close()
        except:
            print('Файл не найден и не может быть создан')
        

#новые записи
def new_lines():
    global name_of_file
    print('    Создание в файле нового набора записей.')
    print()
    file = open(name_of_file, 'w')
    print_sportsmen(file)
    file.close()

#добавление записей
def new_line():
    global name_of_file
    print('    Добавление записей в файл.')
    print()
    file = open(name_of_file)
    st = file.read()
    file.close()
    file = open(name_of_file, 'w')
    if len(st.split()) != 0:
        file.write(st)
    print_sportsmen(file)
    file.close()

#вывод
def print_file():
    global name_of_file
    print('    Вывод всех записей в файле.')
    print()
    file = open(name_of_file)
    if len(file.read().split()) == 0:
        print('В файле нет записей.')
    else:
        file.close()
        file = open(name_of_file)
        print_hat()
        for st in file:
            print_row(st)
        print('└','─'*25,'┴','─'*16,'┴','─'*14,'┴','─'*19,'┘', sep = '')
    file.close()

#поиск по одному полю
def find_1():
    global name_of_file
    print('    Поиск по одному полю.')
    print()
    print('Выберете поле для поиска:')
    print('  1 - Фамилия')
    print('  2 - Имя')
    print('  3 - Год рождения')
    print('  4 - Разряд или звание')
    ans = int(input())
    print('Введите значение поля:')
    ans2 = input()
    file = open(name_of_file)
    j = 0
    for st in file:
        if st.split()[ans-1] == ans2:
            if j == 0:
                print(' '*30, 'Найденные записи.')
                print_hat()
            print_row(st)
            j += 1
    if j == 0:
        print('Записей не найдено.')
    else:
        print('└','─'*25,'┴','─'*16,'┴','─'*14,'┴','─'*19,'┘', sep = '')
        
#поиск по двум полям
def find_2():
    print('    Поиск по двум полям.')
    print('Выберете 2 различных поля для поиска:')
    print('  1 - Фамилия')
    print('  2 - Имя')
    print('  3 - Год рождения')
    print('  4 - Разряд или звание')
    print('Введите номер 1-го поля:')
    ans_1 = int(input())
    print('Введите значение 1-го поля:')
    ans_12 = input()
    print('Введите номер 2-го поля:')
    ans_2 = int(input())
    while ans_2 == ans_1:
        print('Введены 2 одинаковых поля.')
        print('Повторите ввод:')
        ans_2 = int(input())
    print('Введите значение 2-го поля:')
    ans_22 = input()
    file = open(name_of_file)
    j = 0
    for st in file:
        if st.split()[ans_1-1] == ans_12 and st.split()[ans_2-1] == ans_22:
            if j == 0:
                print(' '*30, 'Найденные записи.')
                print_hat()
            print_row(st)
            j += 1
    if j == 0:
        print('Записей не найдено.')
    else:
        print('└','─'*25,'┴','─'*16,'┴','─'*14,'┴','─'*19,'┘', sep = '')

name_of_file = 'Names.txt'
print('     Спортсмены.')
while True:
    print('        МЕНЮ        ')
    print()
    print('  1 - Выбор файла (по умолчанию "Names.txt")\n'
          '  2 - Создание в файле нового набора записей\n'
          '  3 - Добавление записей в файл\n'
          '  4 - Вывод всех записей в файле\n'
          '  5 - Поиск по одному полю\n'
          '  6 - Поиск по двум полям\n\n'
          '  0 - Выход\n')
    choice = int(input('Выберете пункт меню: '))
    print()
    if choice == 1:
        choice_of_file()
    elif choice == 2:
        new_lines()
    elif choice == 3:
        new_line()
    elif choice == 4:
        print_file()
    elif choice == 5:
        find_1()
    elif choice == 6:
        find_2()
    elif choice == 0:
        print('Спасибо за использование программы!')
        break
    else:
        print('В меню нет данного пункта.')
    print()
