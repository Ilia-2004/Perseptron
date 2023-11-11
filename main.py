import numpy as np
import matplotlib.pyplot as plt

N = 5                                                       # колличество образов
b = 3

x1 = np.random.random(N)                                    # моделирование случайные величины по оси x1
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] + b  # моделирование х1 + случайное отклонение
C1 = [x1, x2]                                               # формирование двумерного списка из точек,
                                                            # которые будут лежать выше прямой
# тоже самое делаем для второго класса:
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1 + b    # ставим - после x1 и ставим - 0.1,
C2 = [x1, x2]                                                       # чтобы эта точка была точно ниже прямой

f = [0 + b, 1 + b]                                                  # формируем прямую под 45 градусов

w2 = 0.5
w3 = -b * w2
w = np.array([-w2, w2, w3])                                   # задаём веса для нейронки
for i in range(N):                                          # (веса были специально подобраны)
    x = np.array([C1[0][i], C1[1][i], 1])
    y = np.dot(w, x)
    if y >= 0:                                              # если входной параметр больше или равен 0,
        print("Класс С1")                                   # то это класс C1
    else:                                                   # иначе класс C2
        print("Класс С2")

plt.scatter(C1[0][:], C1[1][:], s = 10, c = 'red')
plt.scatter(C2[0][:], C2[1][:], s = 10, c = 'blue')
plt.plot(f)
plt.grid(True)
plt.show()