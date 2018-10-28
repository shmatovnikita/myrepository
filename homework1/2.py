n = int(input('целое число n '))
p = 0
for i in range(n):
    m = int(input("еще одно целое число: "))
    if m % 3 == 0:
        p = p + m
print(p)

