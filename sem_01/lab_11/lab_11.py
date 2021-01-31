'''Лабораторна работа №11
   "Редактирование текста"

   Назначение:
   1)выравнивание текста по ширине;
   2)выравнивание по левому краю;
   3)выравнивание по правому краю;
   4)замена во всем тексте одного слова другим;
   5)удаление заданного слова из текста;
   6)замена арифметических выражений, состоящих
     из сложения и вычитания на результат их вычисления;
   7)смена местами самого длинного и самого короткаого по
     количеству слов предложения,
   8)предложения в порядке возрастания количества слов.

   Переменные, используемые в программе:
   text, t, new_text -- исходный и полученный в результате
   обработки текст;
   lor, number_of_spaces -- массив длин строк и количества
   пробелов в каждой строке;
   choice -- выбор пункта меню;
   x, c, y -- символы в текущей строке;
   new_row, replaced_word, removable_word, add_word --
   слова, соответствующие названиям;
   prev -- предыдущий символ в тексте;
   i, k, num_rep, now_index, num_spaces, numnum, numsign --
   счетчики.
   
   Тестовый пример:
   Входные данные:
   1
   
   Выходные данные:
       10+6-15 октября. Проснувшись поутру, я увидел, что наш корабль сняло
   с  мели  приливом  и  пригнало  гораздо  ближе  к берегу. Это подало мне
   надежду,   что,   когда   ветер   стихнет,   мне  удастся  добраться  до
   корабля  и  запастись  едой  и  другими  необходимыми  вещами. Я немного
   приободрился,   хотя   печаль   о   погибших   товарищах   не   покидала
   меня.  Мне  все  думалось,  что,  останься  мы на корабле, мы непременно
   спаслись   бы.   Теперь   из   его   обломков   мы  могли  бы  построить
   баркас,   на   котором   и   выбрались   бы   из  этого  гиблого  места.
'''

#длина и количество пробелов в каждой строке
def len_of_rows_and_spaces(t):
    kolst = 1
    for x in t:
        if x == '\n':
            kolst += 1
    lens = [0]*kolst
    num_of_spaces = [0]*kolst
    k = 0
    i = 0
    num_spaces = -4
    for x in t:
        if x == '\n':
            lens[k] = i
            num_of_spaces[k] = num_spaces
            i = 0
            k += 1
            num_spaces = 0
        else:
            i += 1
            if x == ' ':
                num_spaces += 1
    lens[k] = i
    num_of_spaces[k] = num_spaces
    return lens, num_of_spaces

#длина самой длинной строки
def max_len_row(sp):
    max_r = 0
    for x in sp:
        if x > max_r:
            max_r = x
    return max_r

#перевод в нижний регистр
def lower(c):
    if 'А' < c < 'Я':
        return chr(ord('а') + ord(c) - ord('А'))
    if 'A' < c < 'Z':
        return chr(ord('a') + ord(c) - ord('A'))
    return c

#перевод в верхний регистр
def upper(c):
    if 'а' < c < 'я':
        return chr(ord('А') + ord(c) - ord('а'))
    if 'a' < c < 'z':
        return chr(ord('A') + ord(c) - ord('a'))
    return c

#перевод в нижний регистр строки
def low_row(row):
    new_row = ''
    for x in row:
        new_row += lower(x)
    return new_row

#проверка на букву
def not_letter(c):
    return ((c>'я' or c<'а') and (c>'Я' or c<'А')
               and (c>'z' or c<'a') and (c>'Z' or c<'A'))

#проверка на слово
def check(word):
    for x in word:
        if not_letter(x):
            return False
    return True

#выравнивание по ширине
def width(t):
    new_text = ''
    k = 0
    num_spaces = (max_len - lor[k])//number_of_spaces[k]
    last_big = (max_len - lor[k])%number_of_spaces[k]
    space_is = -3
    for x in t:
        new_text += x
        if x == ' ':
            if space_is > 0:
                if space_is <= last_big:
                    new_text += ' ' * (num_spaces + 1)
                else:
                    new_text += ' ' * num_spaces
            space_is += 1
        else:
            if x == '\n':
                space_is = 1
                k += 1
                num_spaces = (max_len - lor[k])//number_of_spaces[k]
                last_big = (max_len - lor[k])%number_of_spaces[k]
    print('Текст, выровненный по ширине:')
    print()
    print(new_text)

#выравнивание по левому краю
def prepare_text(t):
    new_text = '    '
    spaces = False
    enter = True
    for x in t:
        if x == '\n':
            new_text += '\n'
            enter = True
        elif x == ' ':
            spaces = True
        elif x != ' ':
            if spaces and not enter:
                new_text += ' ' + x
                spaces = False
            else:
                new_text += x
                spaces = False
                enter = False
    return new_text

#выравнивание по правому краю  
def right(t):
    new_text = ''
    number_of_row = 0
    spaces = False
    for x in t:
        if spaces:
            new_text += x
            if x == '\n':
                spaces = False
                number_of_row += 1
        else:
            number_of_spaces= max_len - lor[number_of_row]
            new_text += ' '*number_of_spaces + x
            spaces = True
    print('Текст, выровненный по правому краю:')
    print()
    print(new_text)

#замена одного слова другим
def replacement_of_word(t):
    while True:
        replaced_word = input('Введите слово, которое хотите заменить: ')
        if check(replaced_word) and replaced_word != '':
            break
        else:
            print()
            print('Словом считается последовательность из русских или латинских букв.')
            print()
    replaced_word = low_row(replaced_word)
    needed_word = input('Введите слово, на  которое хотите заменить предыдущее: ')
    add_word = ''
    new_text = ''
    num_rep = 0
    now_index = 0
    
    #формирование добавляемого слово с большой буквы
    first_letter = True
    new_needed_word = ''
    for y in needed_word:
        if first_letter:
            y = upper(y)
            first_letter = False
        new_needed_word += y
        
    big = False
    prev = ' '
    for x in t:
        if now_index == 0 and 'A'<x<'Я' or 'A'<x<'Z':
            big = True
        if (now_index < len(replaced_word) and lower(x) == replaced_word[now_index]
            and (now_index !=  0 or not_letter(prev))):
            add_word += x
            now_index += 1
        else:
            if low_row(add_word) == replaced_word and not_letter(x):
                if big:
                    new_text += new_needed_word
                else:
                    new_text += needed_word
                num_rep += 1
            else:
                new_text += add_word
            new_text += x
            add_word = ''
            now_index = 0
            big = False
        prev = x
    print(add_word)
    
    #если в конце не стоит знак препинания
    if add_word != '':
        if low_row(add_word) == replaced_word:
            if big:
                new_text += new_needed_word
            else:
                new_text += needed_word
                num_rep += 1
        else:
            new_text += add_word

    print()
    if num_rep == 0:
        print('Слова', replaced_word, 'нет в тексте.')
    else:
        print('Текст с заменой: ')
        print()
        print(new_text)
        		
#удаление слова
def removal(t):
    while True:
        removable_word = input('Введите слово, которое хотите удалить: ')
        if check(removable_word) and removable_word != '':
            break
        else:
            print()
            print('Словом считается последовательность из русских или латинских букв.')
            print()
    removable_word = low_row(removable_word)
    add_word = ''
    new_text = ''
    now_index = 0
    num_rem = 0
    prev = ' '
    for x in t:
        if (now_index < len(removable_word) and lower(x) == removable_word[now_index]
            and (now_index !=  0 or not_letter(prev))):
            add_word += x
            now_index += 1
        else:
            if low_row(add_word) == removable_word and not_letter(x):
                num_rem += 1
                if x != ' ':
                    new_text += x
            else:
                new_text += add_word
                new_text += x
            add_word = ''
            now_index = 0
    print()
    if num_rem == 0:
        print('Слова', removable_word, 'нет в тексте.')
    else:
        print('Текст без заданного слова: ')
        print()
        print(new_text)

#подсчет выражения, заданного строкой        
def result(row):
    pred = ''
    summ = 0
    sign = ['+', '-']
    for x in row:
        if x in sign and pred != '':
            summ += int(pred)
            pred = ''
        pred += x
    summ += int(pred)
    return str(summ)+ ' '
        
        

def replacement_of_sum(t):
    num = ['0','1','2','3','4','5','6','7','8','9'] #'.'
    sign = ['+', '-']
    new_text = ''
    expr = ''
    add_word = ''
    last = 0
    numnum = 0
    numsign = 0
    prev = ''
    not_exp = True
    end_expr = False
    for x in t:
        #формирование выражения
        if expr != '' and x == ' ':
            add_word += x
        elif x in num or x in sign:
            if last == 0:
                expr += x
                add_word += x
            elif prev != ' ':
                expr += x
                add_word += x
            elif (expr[last-1] in sign and x in num or
                expr[last-1] in num and x in sign):
                expr += x
                add_word += x
            else:
                end_expr = True
            if not end_expr:
                if x in num and (last == 0 or expr[last-1] not in num):
                    numnum += 1
                if x in sign:
                    numsign += 1
            last += 1
            not_exp = False
        elif expr != '':
            not_exp = True
            end_expr = True
        prev = x
        
        #подсчет выражения
        if end_expr:
            if numsign > numnum or numsign == numnum == 1: #or expr == "." 
                new_text += add_word
            else:
                new_text += result(expr)
            expr = ''
            add_word = ''
            if x in num or x in sign:
                add_word += x
                expr += x
                if x in num:
                    numsign = 0
                    numnum = 1
                else:
                    numsign = 1
                    numnum = 0
                last = 1
            else:
                numnum = 0
                numsign = 0
                last = 0
            end_expr = False
            not_exp = True
        if not_exp:
            new_text += x
    print(new_text)

#смена местами самого длинного и самого короткого
#по количеству слов предложения
def change(t):
    ends = ['.', '!', '?']
    min_len = -1
    ind_min = -1
    max_len = -1
    ind_max = -1
    now_pred = ''
    now_len = 0
    spaces = 0
    pred_bet = ''
    sp_of_sen = [''] * 7
    last_sen = 0
    #поиск минимального и максимального
    for x in t:
        if x == '\n':
            now_pred += ' '
        elif spaces >= 3:
            now_pred += x
        if x in ends:
            sp_of_sen[last_sen] = now_pred
            if min_len > now_len or min_len == -1:
                min_len = now_len
                ind_min = last_sen
            if max_len <= now_len:
                max_len = now_len
                ind_max = last_sen
            last_sen += 1
            now_pred = ''
            now_len = 0
        if not_letter(x):
            if spaces < 4:
                spaces += 1
            else:
                now_len += 1
    sp_of_sen[ind_min], sp_of_sen[ind_max] =(
        sp_of_sen[ind_max], sp_of_sen[ind_min])
    new_text = '   '
    sym = 3
    #формирование нового текста
    for x in sp_of_sen:
        for y in x:
            if y == ' ' and sym > 68:
                new_text += '\n'
                sym = 0
            else:
                new_text += y
                sym += 1
    print(new_text)

#вывод предложений в порядке возрастания количества слов
def sort_sen(t):
    ends = ['.', '!', '?']
    now_pred = ''
    now_len = 0
    spaces = 0
    sp_of_sen = [''] * 7
    sp_of_len = [0] * 7
    last_sen = 0
    pred = '\n'
    for x in t:
        if x == '\n':
            now_pred += ' '
        elif spaces >= 3:
            now_pred += x
        if x in ends:
            sp_of_sen[last_sen] = now_pred
            sp_of_len[last_sen] = now_len
            last_sen += 1
            now_pred = ''
            now_len = 0
        if x == ' ' and spaces < 4:
            spaces += 1
        if not_letter(x) and not not_letter(pred):
            now_len += 1
        pred = x
    sp_of_len[0] += 1
    i = 0
    while i < last_sen:
        min_len = sp_of_len[i]
        ind_min = i
        j = i
        while j < last_sen:
            if sp_of_len[j] < min_len:
                min_len = sp_of_len[j]
                ind_min = j
            j += 1
        sp_of_sen[i], sp_of_sen[ind_min] = sp_of_sen[ind_min], sp_of_sen[i]
        sp_of_len[i], sp_of_len[ind_min] = sp_of_len[ind_min], sp_of_len[i]
        i += 1
    for x in sp_of_sen:
        sym = 0
        for y in x:
            if y == ' ' and sym > 50:
                print('\n', end = '')
                sym = 0
            else:
                print(y, end = '')
                sym += 1
        print()
        print()

text = ('  1-ое октября. Проснувшись поутру, я увидел, что наш корабль сняло\n'+
       'с мели приливом и пригнало   гораздо ближе к берегу. Это подало мне\n'+
       '   надежду, что, когда ветер стихнет, мне   удастся добраться до\n'+
       'корабля и запастись едой и другими необходимыми вещами. Я немного\n'+
       '       приободрился, хотя   печаль о погибших товарищах не покидала\n'+
       'меня. Мне все думалось, что, останься мы на корабле, мы непременно\n'+
       '  спаслись  бы. Теперь  из его обломков мы могли бы построить    \n'+
       '      баркас, на котором и выбрались бы из этого гиблого места.')


#подготовка
text = prepare_text(text)
lor, number_of_spaces = len_of_rows_and_spaces(text)
max_len = max_len_row(lor)

print('             Редактирование текста')
while True:
    print('                   Меню')
    print('   1 - Выравнивание по ширине')
    print('   2 - Выравнивание по левому краю')
    print('   3 - Выравнивание по правому краю')
    print('   4 - Замена во всём тексте одного слова другим')
    print('   5 - Удаление заданного слова из текста')
    print('   6 - Замена арифметических выражений, ')
    print('       состоящих из сложения и вычитания')
    print('       на результат их вычисления')
    print('   7 - Смена местами самого длинного и')
    print('       самого короткого по количеству ')
    print('       слов предложения')
    print('   8 - Вывод предложений в порядке возрастания')
    print('       количества слов')
    print()
    print('   0 - Выход')
    print()
    choice = input('Выберете пункт меню: ')
    print()
    if choice == '1':
        width(text)
    elif choice == '2':
        print('Текст, выровненный по левому краю:')
        print()
        print(text)
    elif choice == '3':
        right(text)
    elif choice == '4':
        replacement_of_word(text)
    elif choice == '5':
        removal(text)
    elif choice == '6':
        replacement_of_sum(text)
    elif choice == '7':
        change(text)
    elif choice == '8':
        sort_sen(text)
    elif choice == '0':
        print('Спасибо за использование программы!')
        break
    else:
        print('В меню нет указанного пункта.')
    print()
