import math

def f(x):
    """Основная функция: x^3 - 2x - 5 = 0"""
    return x**3 - 2*x - 5

def df(x):
    """Производная основной функции f(x)"""
    return 3*x**2 - 2

def bisection_method(f, a, b, eps=1e-6, max_iter=100):
    """
    Метод деления отрезка пополам (бисекции)
    
    Параметры:
    f - функция
    a, b - границы отрезка [a, b], где f(a)*f(b) < 0
    eps - точность
    max_iter - максимальное число итераций
    
    Возвращает:
    корень, число итераций, историю приближений
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка")
    history = []
    for i in range(max_iter):
        c = (a + b) / 2
        history.append(c)
        if abs(f(c)) < eps or (b - a) / 2 < eps:
            return c, i + 1, history
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, max_iter, history

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    """
    Метод Ньютона (касательных)
    
    Параметры:
    f - функция
    df - производная функции
    x0 - начальное приближение
    eps - точность
    max_iter - максимальное число итераций
    
    Возвращает:
    корень, число итераций, историю приближений
    """
    x = x0
    history = [x]
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < eps:
            raise ValueError("Производная близка к нулю")
        x_new = x - fx / dfx
        history.append(x_new)
        if abs(x_new - x) < eps and abs(f(x_new)) < eps:
            return x_new, i + 1, history
        x = x_new
    return x, max_iter, history

def print_results(method_name, root, iterations, history, current_f):
    """Вывод результатов"""
    print(f"\n{method_name}:")
    print(f"  Найденный корень: {root:.10f}")
    print(f"  Значение функции: {current_f(root):.2e}")
    print(f"  Количество итераций: {iterations}")
    if len(history) > 5:
        print(f"  Последние 5 приближений:")
        for i, val in enumerate(history[-5:]):
            print(f"    Итерация {len(history)-5+i+1}: {val:.10f}")
    else:
        print(f"  Все приближения:")
        for i, val in enumerate(history):
            print(f"    Итерация {i+1}: {val:.10f}")

def solve_equation(equation_name, equation_f, equation_df, 
                   bisection_interval, newton_x0):
    """Решение выбранного уравнения"""
    print(f"\n{'='*60}")
    print(f"Решение уравнения: {equation_name}")
    print(f"{'='*60}")
    print("\n1. Метод деления отрезка пополам:")
    try:
        a, b = bisection_interval
        print(f"  Отрезок: [{a}, {b}]")
        print(f"  f({a}) = {equation_f(a):.2f}, f({b}) = {equation_f(b):.2f}")
        root_bis, iter_bis, hist_bis = bisection_method(equation_f, a, b)
        print_results("Метод бисекции", root_bis, iter_bis, hist_bis, equation_f)
    except ValueError as e:
        print(f"  Ошибка: {e}")
        root_bis = None
    
    print("\n2. Метод Ньютона (касательных):")
    try:
        x0 = newton_x0
        print(f"  Начальное приближение: x0 = {x0}")
        root_newt, iter_newt, hist_newt = newton_method(equation_f, equation_df, x0)
        print_results("Метод Ньютона", root_newt, iter_newt, hist_newt, equation_f)
    except ValueError as e:
        print(f"  Ошибка: {e}")
        root_newt = None
    
    if root_bis is not None and root_newt is not None:
        print("\n" + "=" * 50)
        print("Сравнение методов:")
        print(f"  Разница между решениями: {abs(root_bis - root_newt):.2e}")
        if iter_newt > 0:
            print(f"  Метод Ньютона быстрее в {iter_bis/iter_newt:.1f} раз")

def main_menu():
    """Интерактивное меню выбора уравнения"""
    while True:
        print("\n" + "="*60)
        print("РЕШЕНИЕ НЕЛИНЕЙНЫХ УРАВНЕНИЙ")
        print("="*60)
        print("\nВыберите уравнение для решения:")
        print("1. x³ - 2x - 5 = 0")
        print("2. cos(x) - x = 0")
        print("3. x² - 2 = 0 (нахождение √2)")
        print("4. e^x - 3x = 0")
        print("5. ln(x) + x² - 3 = 0")
        print("6. sin(x) - 0.5 = 0")
        print("7. x³ + 4x² - 10 = 0")
        print("0. Выход из программы")
        
        choice = input("\nВведите номер выбора: ")
        
        if choice == '0':
            print("\nВыход из программы. До свидания!")
            break
        
        elif choice == '1':
            # x³ - 2x - 5 = 0
            def f1(x):
                return x**3 - 2*x - 5
            def df1(x):
                return 3*x**2 - 2
            solve_equation("x³ - 2x - 5 = 0", f1, df1, [2, 3], 2.5)
        
        elif choice == '2':
            # cos(x) - x = 0
            def f2(x):
                return math.cos(x) - x
            def df2(x):
                return -math.sin(x) - 1
            solve_equation("cos(x) - x = 0", f2, df2, [0, 1], 0.5)
        
        elif choice == '3':
            # x² - 2 = 0
            def f3(x):
                return x**2 - 2
            def df3(x):
                return 2*x
            solve_equation("x² - 2 = 0 (нахождение √2)", f3, df3, [1, 2], 1.5)
        
        elif choice == '4':
            # e^x - 3x = 0
            def f4(x):
                return math.exp(x) - 3*x
            def df4(x):
                return math.exp(x) - 3
            solve_equation("e^x - 3x = 0", f4, df4, [0, 1], 0.5)
        
        elif choice == '5':
            # ln(x) + x² - 3 = 0
            def f5(x):
                return math.log(x) + x**2 - 3
            def df5(x):
                return 1/x + 2*x
            solve_equation("ln(x) + x² - 3 = 0", f5, df5, [1, 2], 1.5)
        
        elif choice == '6':
            # sin(x) - 0.5 = 0
            def f6(x):
                return math.sin(x) - 0.5
            def df6(x):
                return math.cos(x)
            solve_equation("sin(x) - 0.5 = 0", f6, df6, [0, math.pi/2], 0.5)
        
        elif choice == '7':
            # x³ + 4x² - 10 = 0
            def f7(x):
                return x**3 + 4*x**2 - 10
            def df7(x):
                return 3*x**2 + 8*x
            solve_equation("x³ + 4x² - 10 = 0", f7, df7, [1, 2], 1.5)
        
        else:
            print("\nНеверный выбор. Пожалуйста, введите число от 0 до 7.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main_menu()