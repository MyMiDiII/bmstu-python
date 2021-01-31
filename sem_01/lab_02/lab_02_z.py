from math import sqrt

print('Координаты вводятся через пробел.')
x1, y1 = map(int, input('Введите координаты первой вершины: ').split())
x2, y2 = map(int, input('Введите координаты второй вершины: ').split())
x3, y3 = map(int, input('Введите координаты третьей вершины: ').split())

difx12 = x1-x2
difx13 = x1-x3
difx23 = x2-x3
dify12 = y1-y2
dify13 = y1-y3
dify23 = y2-y3

side1 = sqrt(difx12*difx12 + dify12*dify12)
side2 = sqrt(difx13*difx13 + dify13*dify13)
side3 = sqrt(difx23*difx23 + dify23*dify23)

per = side1+side2+side3
max_side = max(side1, side2, side3)
min_side = min(side1, side2, side3)

if max_side == per - max_side:
    print('Точки лежат на одной прямой.')
else:
    side1 = max_side
    side3 = min_side
    side2 = per - max_side - min_side

    sum12 = side1+side2
    bis = sqrt(side1*side2*(sum12*sum12 - side3*side3))/sum12

    print('Биссектриса, проведённая из наименьшего угла: ',
          '{:6.4f}'.format(bis))

