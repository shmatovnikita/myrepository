палиндром = str(input('введите нежно строку '))
y = len(палиндром)
i =0
if y % 2 == 0:
    while y[i] == y[-(i+1)]:
        i += 1
        continue
    print('yes')
else:
    print('no')

