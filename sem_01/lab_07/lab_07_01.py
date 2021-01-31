'''Лабораторная работа №7(часть 1)
   "Формирование одномерного массива по данной матрице"

   Назначение:
   1)сформировать массив из положительных элементов под
   побочной диагональю;
   2)поменять местами первый и максимальный элементы в
   полученном массиве.

   Переменные, используемые в программе:
   n -- количество строк и столбцов квадратной матрицы;
   Y -- квадратная матрица;
   X, m -- массив положительных элеметов под побочной диагональю и его размер;
   i,j -- счетчики для прохода по матрице и массиву;
   mel, nmel -- максимальный элемент и его номер в массиве X.

   Тестовый пример:
   Входные данные:
   3
   1 2 3
   1 2 1
   1 -1 2
   Выходные данные:
   Исходная матрица:
      1.000       2.000       3.000
      1.000       2.000       1.000
      1.000      -1.000       2.000
   Преобразованный(первый элемент на месте максимального,
   максимальный на месте первого) массив положительных элементов
   под побочной диагональю:
      2.000
      1.000
'''

n = int(input('Введите количество строк и столбцов '
              'квадратной матрицы (n<=9, n-натуральное): '))

if n <= 0 or n > 9:
    print('Неверный размер матрицы.')
else:
    if n == 1:
        print('Введите матрицу ',n,'*',n,' по ',n,' элементу в строке:',
              sep = '')
    elif n < 5:
        print('Введите матрицу ',n,'*',n,' по ',n,' элемента в строке:',
              sep = '')
    else:
        print('Введите матрицу ', n,'*',n,' по ',n,' элементов в строке:',
              sep = '')
    Y = []
    for i in range(n):
        Y.append([float(j) for j in input().split()])

    #формирование массива X
    X = []
    for i in range(n):
        for j in range(n):
            if i+j > n-1 and Y[i][j] > 0:
                X.append(Y[i][j])
                
    m = len(X)
    if m == 0:
        print('Под побочной диагональю матрицы нет положительных элементов.')
    else:
        #смена первого и максимального элемента
        nmel = 0
        mel = X[0]
        for i in range(1, m):
            if X[i] > mel:
                mel = X[i]
                nmel = i
        X[0], X[nmel] = X[nmel], X[0]
        
        print('Исходная матрица:')
        for i in range(n):
            for j in range(n):
                if abs(Y[i][j]) < 10000:
                    print('{:11.3f}'.format(Y[i][j]), end = ' ')
                else:
                    print('{:11.2e}'.format(Y[i][j]), end = ' ')
            print()
        print('Преобразованный (первый элемент на месте максимального'
              ', максимальный на месте первого)\nмассив положительных'
              ' элементов под побочной диагональю:')
        for i in range(m):
            if abs(X[i]) < 10000:
                print('{:11.3f}'.format(X[i]))
            else:
                print('{:11.2e}'.format(X[i]))