#Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
#вывести список размера 10, содержащий 10 первых членов данной прогрессии
A = float(input("Введите первый член прогрессии: "))
D = float(input("Введите знаменатель прогрессии: "))
prog = []
for i in range(10):
    num = A * (D ** i)
    prog.append(num)
print("Первые 10 членов геометрической прогрессии:")
print(prog)