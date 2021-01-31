s = input('Введите строку(только русские, латинские буквы и пробелы): ')
mas = list(s.split())
n = len(mas)
s1 = ''
for i in range(n):
    if (mas[i][0] < 'А' or mas[i][0] > 'Я'
        ) and (mas[i][0] < 'A'or mas[i][0] > 'Z') and mas[i][0] != 'Ё':
            s1 += mas[i] + ' '
if s1 == '':
    print('Все слова из строки удалены.')
else:
    if s1[len(s1) - 1] == ' ':
        s1 = s1[:len(s1)-1]
    print('Строка без слов с большой буквы и без лишних пробелов:')
    print(s1)
