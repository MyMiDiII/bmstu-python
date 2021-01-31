'''Лабораторная работа №0

   Поиск номера подъезда и номер этажа по номеру квартиры.
   В доме 9 этажей, на каждом этаже 4 квартиры.
'''

room = input('Введите номер квартиры: ')

let = 0
i = 0
while let == 0 and i < len(room):
    if room[i] < '0' or room[i] > '9':
        let += 1
    i += 1

if let != 0 or room == '' or room == '0':
    print('Неверно введен номер квартиры.')
else:
    room = int(room)
    floor = (room-1)//4%9+1
    pod = (room-1)//36+1
    print('Подъезд:', pod)
    print('Этаж:', floor)

