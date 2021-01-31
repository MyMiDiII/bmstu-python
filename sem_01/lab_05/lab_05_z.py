eps = float(input('Введите точность вычисления суммы: '))
x = float(input('Введите аргумент x: '))
n = int(input('Введите начальное значение для печати (натуральное): '))
step = int(input('Введите шаг для печати (натуральное): '))
m = int(input('Введите максимальное количество циклов (натуральное): '))

sm = 0
el = x
nn = 1
k = 0
sh = False
table = False

print()
while abs(el) > eps:
     sm += el
     nn += 1
     el = -el*x/nn/nn
     
     if nn-1 == step*k+n and abs(el) > eps:
          if nn-1 == n:
               print('┌─────────────┬─────────────┐')
               print('│    Число    │   Текущая   │')
               print('│    членов   │    сумма    │')
               print('├─────────────┼─────────────┤')
               table = True
          if abs(sm) < 10:
               print('│  {:9d}  │ {:11.6f} │'.format(nn-1,sm))
          elif abs(sm) < 1000:
               print('│  {:9d}  │ {:11.4f} │'.format(nn-1,sm))
          elif abs(sm) < 10000:
               print('│  {:9d}  │ {:11.2f} │'.format(nn-1,sm))
          else:
               print('│  {:9d}  │ {:11.2e} │'.format(nn-1,sm))

          k += 1
     
     #выход при превышении m
     if abs(el) > eps and nn-1 == m:
          sh = True
          break

if table:
     print('└─────────────┴─────────────┘')
else:
     print('Ряд сошёлся раньше заданного начального значения.')

if sh:
     print('За', m, 'циклов ряд не сошёлся')
else:
     if nn == 1:
          nn += 1
          sm = el
     print('Количество просуммированныx членов:', nn-1)
     print('Сумма ряда:', '{:9.6f}'.format(sm))
