import numpy as np

def inverse_matrix_gauss(matrix):
    """
    Находит обратную матрицу методом Гаусса с выбором главного элемента
    
    Args:
        matrix (list or np.ndarray): Исходная квадратная матрица
        
    Returns:
        np.ndarray: Обратная матрица или None, если матрица вырожденная
    """
    # Преобразуем в numpy массив, если нужно
    A = np.array(matrix, dtype=float)
    n = A.shape[0]
    
    # Проверяем, что матрица квадратная
    if A.shape[0] != A.shape[1]:
        raise ValueError("Матрица должна быть квадратной")
    
    # Создаем расширенную матрицу [A|I]
    augmented = np.hstack((A, np.eye(n)))
    
    # Прямой ход метода Гаусса
    for i in range(n):
        # Выбор главного элемента (поиск максимального в столбце)
        max_row = i
        max_val = abs(augmented[i, i])
        for k in range(i + 1, n):
            if abs(augmented[k, i]) > max_val:
                max_val = abs(augmented[k, i])
                max_row = k
        
        # Если все элементы столбца нулевые - матрица вырожденная
        if max_val < 1e-12:
            print("Матрица вырожденная, обратной не существует")
            return None
        
        # Меняем строки местами, если нужно
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Нормализуем текущую строку
        pivot = augmented[i, i]
        augmented[i] = augmented[i] / pivot
        
        # Вычитаем текущую строку из остальных строк
        for k in range(n):
            if k != i:
                factor = augmented[k, i]
                augmented[k] -= factor * augmented[i]
    
    # Обратная матрица находится в правой части расширенной матрицы
    inverse = augmented[:, n:]
    
    return inverse

def inverse_matrix_gauss_classic(matrix):
    """
    Классическая реализация метода Гаусса для нахождения обратной матрицы
    Более наглядная версия
    """
    A = np.array(matrix, dtype=float)
    n = len(A)
    
    # Создаем расширенную матрицу [A|I]
    augmented = np.zeros((n, 2 * n))
    augmented[:, :n] = A
    augmented[:, n:] = np.eye(n)
    
    # Прямой ход
    for i in range(n):
        # Если диагональный элемент близок к нулю, ищем ненулевой элемент ниже
        if abs(augmented[i, i]) < 1e-10:
            for j in range(i + 1, n):
                if abs(augmented[j, i]) > 1e-10:
                    augmented[[i, j]] = augmented[[j, i]]
                    break
        
        # Делим строку на диагональный элемент
        diag_element = augmented[i, i]
        if abs(diag_element) < 1e-10:
            print("Матрица вырожденная, обратной не существует")
            return None
        
        augmented[i] = augmented[i] / diag_element
        
        # Обнуляем элементы в текущем столбце для других строк
        for j in range(n):
            if j != i:
                factor = augmented[j, i]
                augmented[j] -= factor * augmented[i]
    
    # Обратная матрица
    inverse = augmented[:, n:]
    return inverse

# Пример использования
if __name__ == "__main__":
    # Пример матрицы 3x3
    matrix = [
        [4, 2, 1],
        [3, 5, 2],
        [1, 1, 3]
    ]
    
    print("Исходная матрица:")
    print(np.array(matrix))
    
    try:
        # Находим обратную матрицу
        inverse = inverse_matrix_gauss(matrix)
        
        if inverse is not None:
            print("\nОбратная матрица (метод Гаусса):")
            print(inverse)
            
            # Проверка: A * A^(-1) = I
            print("\nПроверка (A * A^(-1)):")
            check = np.dot(matrix, inverse)
            print(check)
            
            # Проверка с использованием numpy для сравнения
            print("\nОбратная матрица (numpy.linalg.inv для проверки):")
            print(np.linalg.inv(matrix))
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Тест с вырожденной матрицей
    print("\n" + "="*50)
    print("Тест с вырожденной матрицей:")
    singular_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]  # Эта строка = строка1 * 2 + строка2 (линейно зависимая)
    ]
    
    inverse_singular = inverse_matrix_gauss(singular_matrix)
    if inverse_singular is None:
        print("Для вырожденной матрицы обратной не существует - корректно!")
    
    # Тест с матрицей 2x2
    print("\n" + "="*50)
    print("Тест с матрицей 2x2:")
    matrix_2x2 = [
        [2, 1],
        [1, 3]
    ]
    
    print("Исходная матрица 2x2:")
    print(np.array(matrix_2x2))
    
    inverse_2x2 = inverse_matrix_gauss(matrix_2x2)
    if inverse_2x2 is not None:
        print("\nОбратная матрица 2x2:")
        print(inverse_2x2)

# Дополнительная функция с проверкой точности
def inverse_with_checks(matrix, method='gauss'):
    """
    Нахождение обратной матрицы с дополнительными проверками
    
    Args:
        matrix: Исходная матрица
        method: Метод ('gauss' или 'classic')
        
    Returns:
        Обратная матрица и информация о точности
    """
    A = np.array(matrix, dtype=float)
    
    if method == 'gauss':
        inv = inverse_matrix_gauss(A)
    else:
        inv = inverse_matrix_gauss_classic(A)
    
    if inv is not None:
        # Проверка точности
        identity = np.dot(A, inv)
        identity_ideal = np.eye(A.shape[0])
        error = np.max(np.abs(identity - identity_ideal))
        
        print(f"Максимальная ошибка: {error:.2e}")
        
        if error < 1e-10:
            print("Точность вычисления: отличная")
        elif error < 1e-6:
            print("Точность вычисления: хорошая")
        else:
            print("Точность вычисления: удовлетворительная")
    
    return inv

# Пример использования функции с проверками
print("\n" + "="*50)
print("Тест с проверкой точности:")
test_matrix = [
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
]

print("Тестовая матрица (трехдиагональная):")
print(np.array(test_matrix))

inv_check = inverse_with_checks(test_matrix)