from math import sin

print('График функции y = sin(x).')
fn, ln = map(float,
             input('Введите начальное и конечное значение аргумента: ').split())
step = float(input('Введите шаг аргумента: '))

if -1000 <= fn <= 1000 and -1000 <= ln <= 1000 and fn != ln:

    x = fn
    fe = True
    while x < ln + step/2:
        y = sin(x)
        
        if fe:
            fe = False
            y_max = y
            y_min = y
        else:
            if y > y_max:
                y_max = y
            if y < y_min:
                y_min = y

        x += step

    print(18*' ', end = '')
    print('{:5.2f}'.format(y_min), end = '')
    print(69*' ', end = '')
    print('{:5.2f}'.format(y_max))
    print('    №         x     ', '├', 73*'─', '┤', sep = '')
    
    m0 = int((-y_min)/(y_max-y_min)*74) + 1

    i = 1
    x = fn
    while x < ln + step/2:
        y = sin(x)

        m = int((y-y_min)/(y_max-y_min)*74)+1
        
        print(' {:7d}  {:8.2f}  '.format(i, x), end = '')
        if 0 < m0 < 76:
            if m < m0:
                print(' '*(m-1),'*',' '*(m0-m-1),'│',' '*(75-m0), sep = '')
            elif m > m0:
                print(' '*(m0-1),'│',' '*(m-m0-1),'*',' '*(75-m), sep = '')
            else:
                print(' '*(m-1), '*', ' '*(75-m), sep = '')
        else:
            print(' '*(m-1), '*', ' '*(75-m), sep = '')
        x += step
        i += 1
else:
    print('Недопустимые значения аргумента.')
