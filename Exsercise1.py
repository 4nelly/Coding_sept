print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))

x_diff = x1 - x2

y_diff = y1 - y2

if x_diff == 0:
    print('Уравнение прямой, проходящей через эти точки:\nx = ', x1)
elif y_diff == 0:
    print('Уравнение прямой, проходящей через эти точки:\ny = ', y1)
