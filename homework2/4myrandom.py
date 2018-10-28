import random
b = random.randint(0, 10)
a = int(input('первая попытка отгадать число компа: '))
c = b-a
print('хитрый компьютер загадал число %d ;)' % b)
while c != 0 or -c != 0:
    a = int(input('неправильно,давай другое число: '))
    c = b-a
print('ю гад дэм райт ит ис %d=' % a)


