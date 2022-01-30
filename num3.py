#Ввод координат векторов
x = []
y = []
z = []
print('Введите координаты вектора x')
for i in range(3):
    x_var = int(input())
    x.append(x_var)
print('Введите координаты вектора y')
for i in range(3):
    y_var = int(input())
    y.append(y_var)
a = int(input('Введите скаляр a'))
zx = x[0] * y[0] * a
zy = x[1] * y[1] * a
zz = x[2] * y[2] * a
z.append(zx)
z.append(zy)
z.append(zz)
print('Вектор z - ', z)
