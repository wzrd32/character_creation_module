from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Останавливает при нулевом или отрицательном."""
    result = CalculateSquareRoot(your_number)
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {result}')


print(message)
calc(25.5)
