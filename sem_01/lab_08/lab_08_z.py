from math import pi, sin

def leftp(n):
    Il = 0
    h = (b-a)/n
    x0 = a
    while x0 < b - h/2:
        y = sin(x0)
        Il += y
        x0 += h
    Il = Il * h
    return Il

a = float(input('Введите нижний предел интегрирования: '))
b = float(input('Введите верхний предел интегрирования: '))
eps = float(input('Введите степень точности вычисления интеграла: '))
ku = 1
men = leftp(ku)
bol = leftp(2*ku)
while abs(bol - men) > eps:
    ku *= 2
    men = bol
    bol = leftp(2*ku)
print('Интеграл, вычесленный с заданной степенью точности:', '{:11.6f}'.format(men))
print('Заданная точность достигается при', ku, 'участках разбиения.')
