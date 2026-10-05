import math


def solve_quadratic(a: float, b: float, c: float):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.

    Args:
        a: коэффициент при x^2, должен быть ненулевым.
        b: коэффициент при x.
        c: свободный член.

    Returns:
        Список корней: два элемента (D > 0), один (D = 0) или пустой (D < 0).

    Raises:
        ValueError: если a == 0.
    """
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен 0.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []


def main():
    print("Решение квадратного уравнения ax^2 + bx + c = 0")
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        roots = solve_quadratic(a, b, c)
        if len(roots) == 2:
            print(f"Два вещественных корня: x1 = {roots[0]:.4f}, x2 = {roots[1]:.4f}")
        elif len(roots) == 1:
            print(f"Один корень (кратный): x = {roots[0]:.4f}")
        else:
            print("Вещественных корней нет.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
