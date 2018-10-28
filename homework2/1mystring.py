f = open("grin.txt")
x = 0
y = 0
s = f.read()
k = []
k1 = 0

for i in range(len(s)):
    if s[i] != ' ' and x == 0:
        y += 1
        x = 1
    else:
        if s[i] == ' ':
            x = 0

print(y)



