x = int(input('введите число: '))

xmin = x % 10
xmax = x % 10
x = x//10

while x >0:
    digit = x % 10
    if digit > xmax:
        xmax = digit
    if digit < xmin:
        xmin = digit
    x = x//10

print('максимальное число %d' % xmax)
print('минимальное число %d' % xmin)



