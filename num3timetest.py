#Ввод координат векторов
import timeit
code_to_test = """
a=54981145980059
x = [a, a, a]
y = [a, a, a]
z=[]
zx = x[0] * y[0] * a
zy = x[1] * y[1] * a
zz = x[2] * y[2] * a

z.append(zx)
z.append(zy)
z.append(zz)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)
print(elapsed_time)
