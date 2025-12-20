import numpy as np

def newton_method_system(functions, jacobian, initial_guess, tol=1e-10, max_iter=100):
    x = np.array(initial_guess, dtype=float)
    history = [x.copy()]
    convergence = False
    for i in range(max_iter):
        F = functions(x)
        J = jacobian(x)
        det = np.linalg.det(J)
        if abs(det) < 1e-15:
            print(f"Предупреждение: матрица Якоби вырождена (det = {det:.2e})")
            break
        try:
            dx = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Ошибка при решении линейной системы")
            break
        x = x + dx
        history.append(x.copy())
        norm_dx = np.linalg.norm(dx)
        norm_F = np.linalg.norm(F)
        if norm_dx < tol and norm_F < tol:
            print(f"Решение найдено за {i+1} итераций")
            convergence = True
            return x, i+1, history, convergence
    print(f"Достигнуто максимальное количество итераций ({max_iter})")
    return x, max_iter, history, convergence

def numerical_jacobian(f, x, h=1e-6):
    n = len(x)
    J = np.zeros((n, n))
    
    for i in range(n):
        x_plus = x.copy()
        x_plus[i] += h
        x_minus = x.copy()
        x_minus[i] -= h
        J[:, i] = (f(x_plus) - f(x_minus)) / (2*h)
    return J

def solve_system_interactive():
    print("=" * 60)
    print("РЕШЕНИЕ СИСТЕМЫ 2-Х УРАВНЕНИЙ МЕТОДОМ НЬЮТОНА")
    print("=" * 60)
    
    print("\nВыберите систему уравнений:")
    print("1. Пример 1: x² + y² = 4, exp(x) + y = 1")
    print("2. Пример 2: x² - y = 1, x + y² = 2")
    print("3. Пример 3: sin(x) + cos(y) = 0.5, x² + y = 1")
    print("4. Своя система")
    choice = input("\nВыберите вариант (1-4): ")
    
    if choice == '1':
        def system1(x):
            f1 = x[0]**2 + x[1]**2 - 4
            f2 = np.exp(x[0]) + x[1] - 1
            return np.array([f1, f2])
        def jacobian1(x):
            df1_dx = 2*x[0]
            df1_dy = 2*x[1]
            df2_dx = np.exp(x[0])
            df2_dy = 1
            return np.array([[df1_dx, df1_dy],
                             [df2_dx, df2_dy]])
        system = system1
        jacobian_func = jacobian1
        print("\nСистема: x² + y² = 4, exp(x) + y = 1")
        
    elif choice == '2':
        def system2(x):
            f1 = x[0]**2 - x[1] - 1
            f2 = x[0] + x[1]**2 - 2
            return np.array([f1, f2])
        def jacobian2(x):
            df1_dx = 2*x[0]
            df1_dy = -1
            df2_dx = 1
            df2_dy = 2*x[1]
            return np.array([[df1_dx, df1_dy],
                             [df2_dx, df2_dy]])
        system = system2
        jacobian_func = jacobian2
        print("\nСистема: x² - y = 1, x + y² = 2")
        
    elif choice == '3':
        def system3(x):
            f1 = np.sin(x[0]) + np.cos(x[1]) - 0.5
            f2 = x[0]**2 + x[1] - 1
            return np.array([f1, f2])
        def jacobian3(x):
            df1_dx = np.cos(x[0])
            df1_dy = -np.sin(x[1])
            df2_dx = 2*x[0]
            df2_dy = 1
            return np.array([[df1_dx, df1_dy],
                             [df2_dx, df2_dy]])
        system = system3
        jacobian_func = jacobian3
        print("\nСистема: sin(x) + cos(y) = 0.5, x² + y = 1")
        
    elif choice == '4':
        print("\nВведите уравнения в формате Python:")
        print("Используйте x для первой переменной, y для второй")
        print("Пример: x**2 + y**2 - 4")
        f1_expr = input("Введите первое уравнение f1(x,y) = 0: ")
        f2_expr = input("Введите второе уравнение f2(x,y) = 0: ")
        def custom_system(x):
            x_val, y_val = x[0], x[1]
            allowed_names = {
                'x': x_val, 'y': y_val,
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                'pi': np.pi, 'e': np.e
            }
            f1 = eval(f1_expr, {"__builtins__": {}}, allowed_names)
            f2 = eval(f2_expr, {"__builtins__": {}}, allowed_names)
            return np.array([f1, f2])
        system = custom_system
        jacobian_func = lambda x: numerical_jacobian(custom_system, x)
        print(f"\nСистема: {f1_expr} = 0, {f2_expr} = 0")

    else:
        print("Неверный выбор. Используется пример 1.")
        return

    print("\nВведите начальное приближение:")
    try:
        x0 = float(input("x0 = "))
        y0 = float(input("y0 = "))
    except ValueError:
        print("Ошибка ввода. Используются значения по умолчанию x0=1, y0=1")
        x0, y0 = 1.0, 1.0
    initial_guess = [x0, y0]
    
    try:
        tol = float(input("Точность (по умолчанию 1e-10): ") or "1e-10")
        max_iter = int(input("Максимальное число итераций (по умолчанию 100): ") or "100")
    except ValueError:
        tol = 1e-10
        max_iter = 100
    
    print("\n" + "=" * 60)
    print("РЕШЕНИЕ:")
    print("=" * 60)
    solution, iterations, history, converged = newton_method_system(
        system, jacobian_func, initial_guess, tol, max_iter
    )
    print(f"\nНачальное приближение: ({x0}, {y0})")
    print(f"Решение: x = {solution[0]:.12f}, y = {solution[1]:.12f}")
    print(f"Количество итераций: {iterations}")
    print(f"Сходимость: {'да' if converged else 'нет'}")
    
    F = system(solution)
    print(f"\nПроверка (значения уравнений в найденной точке):")
    print(f"f1(x,y) = {F[0]:.2e}")
    print(f"f2(x,y) = {F[1]:.2e}")
    
    print(f"\nИстория итераций:")
    print("-" * 50)
    for i, point in enumerate(history[:10]):
        if i < len(history):
            F_val = system(point)
            print(f"Итерация {i:3d}: x = {point[0]:12.8f}, y = {point[1]:12.8f}, "
                  f"|F| = {np.linalg.norm(F_val):.2e}")
    if len(history) > 10:
        print(f"... и еще {len(history) - 10} итераций")
    return solution, history

def test_multiple_starting_points():
    def test_system(x):
        f1 = x[0]**2 + x[1]**2 - 4
        f2 = np.exp(x[0]) + x[1] - 1
        return np.array([f1, f2])
    def test_jacobian(x):
        df1_dx = 2*x[0]
        df1_dy = 2*x[1]
        df2_dx = np.exp(x[0])
        df2_dy = 1
        return np.array([[df1_dx, df1_dy],
                         [df2_dx, df2_dy]])
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ МЕТОДА С РАЗНЫМИ НАЧАЛЬНЫМИ ПРИБЛИЖЕНИЯМИ")
    print("=" * 70)
    print("Система: x² + y² = 4, exp(x) + y = 1")
    print("-" * 70)
    

    starting_points = [
        [1.0, 1.0],   
        [2.0, 0.0],   
        [-1.0, -1.0], 
        [0.0, 2.0],   
        [10.0, 10.0]  
    ]
    
    results = []
    
    for i, point in enumerate(starting_points):
        print(f"\nТест {i+1}: начальная точка ({point[0]}, {point[1]})")
        print("-" * 40)
        
        solution, iterations, history, converged = newton_method_system(
            test_system, test_jacobian, point, tol=1e-10, max_iter=50
        )
        
        results.append({
            'start': point,
            'solution': solution,
            'iterations': iterations,
            'converged': converged
        })
        
        if converged:
            print(f"Решение: x = {solution[0]:.10f}, y = {solution[1]:.10f}")
            print(f"Итераций: {iterations}")
        else:
            print(f"Метод не сошелся за {iterations} итераций")
    
    print("\n" + "=" * 70)
    print("СВОДКА РЕЗУЛЬТАТОВ:")
    print("=" * 70)
    
    for i, res in enumerate(results):
        status = "Сходимость" if res['converged'] else "Расходимость"
        print(f"Тест {i+1}: Начало ({res['start'][0]}, {res['start'][1]}) → "
              f"Решение ({res['solution'][0]:.6f}, {res['solution'][1]:.6f}), "
              f"Итераций: {res['iterations']}, {status}")
def main():
    """Главная функция программы"""
    print("МЕТОД НЬЮТОНА ДЛЯ РЕШЕНИЯ СИСТЕМЫ ДВУХ НЕЛИНЕЙНЫХ УРАВНЕНИЙ")
    print("=" * 70)
    
    while True:
        print("\nМЕНЮ:")
        print("1. Решить систему уравнений")
        print("2. Протестировать метод на разных начальных точках")
        print("3. Выход")
        
        choice = input("\nВыберите действие (1-3): ")
        
        if choice == '1':
            solve_system_interactive()
        elif choice == '2':
            test_multiple_starting_points()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    try:
        import numpy as np
        print("NumPy успешно импортирован")
    except ImportError:
        print("Ошибка: NumPy не установлен. Установите его командой:")
        print("pip install numpy")
        exit(1)
    
    main()