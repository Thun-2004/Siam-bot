
n = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 7]

b = 1 if len(n)//5 < 5 else 0
a = (len(n) % 5)+b


# print(n[0:5])
# print(n[5:10])
# print(n[10:12])

h = len(n)
j = 0
for i in range(a):
    if h > 5:
        print(n[j:j+5])
        h -= 5
        j += 5
    elif h < 5:
        print(n[j:j+h])
