def validate_coefficients(a, b, c):
    """
    Проверяет корректность коэффициентов квадратного уравнения.

    Возвращает (True, None) если всё в порядке,
    или (False, сообщение_об_ошибке) если есть проблема.
    """
    for name, val in [("a", a), ("b", b), ("c", c)]:
        if not isinstance(val, (int, float)):
            return False, f"Коэффициент {name} должен быть числом, получено: {type(val).__name__}"

    if a == 0:
        return False, "Коэффициент a не может быть равен 0 (иначе уравнение не квадратное)"

    return True, None


def parse_coefficient(prompt: str) -> float:
    """
    Запрашивает у пользователя число с повторным вводом при ошибке.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  Ошибка: '{raw}' не является числом. Попробуйте ещё раз.")
