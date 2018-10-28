import math
a = int(input('введите первую сторону: '))
b = int(input('введите вторую сторону: '))
c = int(input('введите третью сторону: '))
if a+b > c and a+c > b and c+b > a:
    print('такой трейгольнрик существует')
    x = ((b**2+c**2-a**2)/(2*b*c))
    y = ((a**2+c**2-b**2)/(2*a*c))
    z = ((b**2+a**2-c**2)/(2*b*a))
    x = math.acos(x)
    y = math.acos(y)
    z = math.acos(z)
    print(math.degrees(x))
    print(math.degrees(y))
    print(math.degrees(z))
else:
    print('такой  треугольник не существует')




