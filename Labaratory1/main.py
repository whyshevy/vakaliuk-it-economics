import matplotlib.pyplot as plt  # імпорт модуля matplotlib для роботи з графіками
import numpy as np  # імпорт модуля numpy для роботи з математичними функціями та масивами


def main():
    fig = plt.figure()
    # створення фігури

    ax = fig.add_subplot(1, 1, 1)
    # додання осі до фігури як частину домовленості (позиціонування нашого графіку)

    ax.set_ylim([-100, 100])
    # обмеження по осі Оу

    plt.xlabel('x', fontsize=13, color='blue')
    # підпис під віссю Ох

    plt.ylabel('y', fontsize=13, color='blue')
    # підпис під віссю Оу

    plt.grid(True)
    # відображення сітки поза графіком

    plt.title("$y = x/cos(x)$", fontsize=13)
    # напис над графіком

    start = int(input("Enter start point: "))
    # початок проміжку табличних значень для y=x/cos(x)

    end = int(input("Enter end point: "))
    # кінець проміжку табличних значень для y=x/cos(x)

    step = int(input("Enter your step: "))
    # розмір кроку

    for pointX in range(start, end + 1, step):
        x = np.linspace(start, end, 150000)  # передання початку, кінця проміжку та вказання розриву

        y = x / np.cos(x)
        # наша функція

        plt.plot(x, y, '.r', markersize=1)
        # вхідні параметри для нашого графіка функції

        print("x =", pointX, "\t| y =",
              pointX / np.cos(pointX))
        # ітерація для того щоб знайти всі значення y на проміжку

    for pointX in range(start, end):
        if pointX == 0:
            print("Special point: ", "x =", pointX, "y =", pointX / np.cos(pointX))
            # вивід особливої точки

    plt.show()
    # відображення графіка функції


main()