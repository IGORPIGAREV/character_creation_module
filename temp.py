from math import sqrt

message = ("Добро пожаловать в самую лучшую программу для вычисления "
           "квадратного корня из заданного числа")
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет квадратный корень, если число больше 0."""
    if your_number <= 0:
        return 0
    else:
        square_root = CalculateSquareRoot(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа."
          f"Это будет: {square_root}")


print(message)
calc(25.5)
