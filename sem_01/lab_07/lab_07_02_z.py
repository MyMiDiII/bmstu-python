N = int(input('Введите количество строк в матрице (N<=7,N-натуральное): '))
L = int(input('Введите количество столбцов в матрице (2<=L<=9,L-натуральное): '))
print('Введите матрицу ', N, '*', L, ' по ', L, ' элементов(целых) в строке:',
      sep = '')
T = []
s = False
for i in range(N):
    T.append([int(j) for j in input().split()])
    if len(T[i]) < L:
        print('Неверное количество элементов в строке!')
        s = True
        break

if s:
    print('Неверные входные данные!')
else:
    k = int(input('Введите по сколько элементов строке необходимо выводить'
              '(2<=k<=6, k<=L, k-натуральное): '))
    if N > 7 or L > 9 or L < 2 or k < 2 or k > 6 or k > L:
        print('Неверные входные данные!')
    else:
        st = 0
        while st < L:
            print(end = '  ')
            x = st
            while x < st+k and x < L:
                print('{:5d}'.format(x+1), end = ' ')
                x += 1
            print()
            for i in range(N):
                print(i+1, end = ' ')
                j = st
                while j < st+k and j < L:
                    print('{:5d}'.format(T[i][j]), end = ' ')
                    j += 1
                print()
            st += k
            print()
            
                
