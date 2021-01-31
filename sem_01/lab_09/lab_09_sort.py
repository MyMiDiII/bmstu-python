'''Лабораторная работа №9
   "Файлы и процедры"

   Назначение:
   1)запись вводимых чисел в файл;
   2)сортировка полученного файла по неубыванию методом пузырька;
   3)вывод содержимого файла на экран.

   Переменные, используемые в программе:
   d, g, g1, g2 -- имена файлов;
   G, G1, G2, G3 -- файлы;
   k -- количество элементов;
   i, end -- счетчики;
   a -- текущий элемент при вводе;
   st, dop_st -- текущая строка и предыдущая.

   Тестовый пример:
   Входные данные:
   3
   2
   3
   1
   Выходные данные:
   Исходный файл:
   2
   3
   1

   Преобразованный (отсортированный) файл:
   1
   2
   3
'''

#процедура ввода элементов файла
def Indata(g):
    G = open(g, 'w')
    global k
    k = int(input('Введите количество элементов'
                  ' (k<=7, k-натуральное): '))
    print('Введите k =',k,'элементов для записи в файл (по одному в строке):')
    for i in range(k):
        a = int(input())
        G.write(str(a))
        G.write('\n')
    G.close()

#процедура сортировки файла
def Cor(g):
    global k
    end = k
    g1 = g
    g2 = 'dop.txt'
    while end > k%2:
        G = open(g1)
        G2 = open(g2, 'w')
        i = 1
        #проход по файлу с перемещением наибольшего элемента в конец
        for st in G:
            if i <= end:
                if i == 1:
                    dop_st = st
                else:
                    if int(st) > int(dop_st):
                        G2.write(dop_st)
                        dop_st = st
                    else:
                        G2.write(st)
                if i == end:
                    G2.write(dop_st)
            else:
                G2.write(st)
            i += 1
        G.close()
        G2.close()
        g1, g2 = g2, g1
        end -= 1

#процедура вывода файла
def OutF(g):
    G3 = open(g)
    print(G3.read())
    G3.close()

k = 0
d = 'd.txt'
Indata(d)

print()
print('Исходный файл:')
OutF(d)

Cor(d)

print('Преобразованный (отсортированный) файл:')
OutF(d)