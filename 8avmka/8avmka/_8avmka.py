import numpy as np

def inverse_matrix_gauss(matrix):
    """
    Нахождение обратной матрицы методом Гаусса
    (классический метод с отдельными прямым и обратным ходом)
    Аргументы:
    matrix - квадратная матрица (список списков или numpy array)
    Возвращает:
    Обратная матрица или None, если матрица вырожденная
    """
    
    if len(matrix) != len(matrix[0]):
        print("Ошибка: Матрица должна быть квадратной!")
        return None

    n = len(matrix)

    augmented = []
    for i in range(n):
        row = []
        row.extend(matrix[i].copy() if hasattr(matrix[i], 'copy') else matrix[i][:])
        row.extend([1.0 if j == i else 0.0 for j in range(n)])
        augmented.append(row)

    for i in range(n):
        max_row = i
        max_val = abs(augmented[i][i])
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > max_val:
                max_val = abs(augmented[k][i])
                max_row = k
        if max_val < 1e-12:
            print("Ошибка: Матрица вырожденная, обратной матрицы не существует!")
            return None
        
        if max_row != i:
            augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        divisor = augmented[i][i]
        for j in range(i, 2 * n):
            augmented[i][j] /= divisor
        for k in range(i + 1, n):
            factor = augmented[k][i]
            for j in range(i, 2 * n):
                augmented[k][j] -= factor * augmented[i][j]
    

    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = augmented[k][i]
            for j in range(i, 2 * n):
                augmented[k][j] -= factor * augmented[i][j]
    inverse = []
    for i in range(n):
        inverse.append(augmented[i][n:])
    return inverse

def print_matrix(matrix, title="Матрица"):
    """Функция для красивого вывода матрицы с очисткой численного шума"""
    print(f"\n{title}:")
    for row in matrix:
        print("[", end="")
        for i, val in enumerate(row):
            if i > 0:
                print(" ", end="")
            if abs(val) < 1e-10:
                val = 0.0
            print(f"{val:8.4f}", end="")
        print("]")

def main():
    print("=" * 50)
    print("ПРИМЕР 1: Матрица 3x3 (классический метод Гаусса)")
    print("=" * 50)
    A1 = [
        [4, 7, 2],
        [3, 6, 1],
        [2, 5, 3]
    ]
    
    print_matrix(A1, "Исходная матрица A")
    A1_inv = inverse_matrix_gauss(A1)
    
    if A1_inv:
        print_matrix(A1_inv, "Обратная матрица A⁻¹")
        A_np = np.array(A1)
        A_inv_np = np.array(A1_inv)
        identity_check = np.dot(A_np, A_inv_np)
        
        print_matrix(identity_check, "Проверка: A * A⁻¹ (должна быть единичной матрицей)")

    print("\n" + "=" * 50)
    print("ПРИМЕР 2: Матрица 2x2 (классический метод Гаусса)")
    print("=" * 50)
    A2 = [
        [2, 5],
        [1, 3]
    ]
    
    print_matrix(A2, "Исходная матрица A")
    A2_inv = inverse_matrix_gauss(A2)
    if A2_inv:
        print_matrix(A2_inv, "Обратная матрица A⁻¹")
        A2_np = np.array(A2)
        A2_inv_np = np.array(A2_inv)
        identity_check2 = np.dot(A2_np, A2_inv_np)
        
        print_matrix(identity_check2, "Проверка: A * A⁻¹")

    print("\n" + "=" * 50)
    print("ПРИМЕР 3: Случайная матрица 4x4 (классический метод Гаусса)")
    print("=" * 50)
    np.random.seed(42) 
    A3 = np.random.rand(4, 4).tolist()
    print_matrix(A3, "Исходная матрица A")
    A3_inv = inverse_matrix_gauss(A3)
    if A3_inv:
        print_matrix(A3_inv, "Обратная матрица A⁻¹")
        A3_np = np.array(A3)
        A3_inv_np = np.array(A3_inv)
        identity_check3 = np.dot(A3_np, A3_inv_np)
        print_matrix(identity_check3, "Проверка: A * A⁻¹")
        numpy_inv = np.linalg.inv(A3_np)
        print_matrix(numpy_inv, "Обратная матрица (numpy.linalg.inv для сравнения)")

    print("\n" + "=" * 50)
    print("ПРИМЕР 4: Вырожденная матрица (классический метод Гаусса)")
    print("=" * 50)
    A4 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix(A4, "Исходная матрица A")
    A4_inv = inverse_matrix_gauss(A4)
    if not A4_inv:
        print("(Ожидаемо) Матрица вырожденная, обратной не существует!")

if __name__ == "__main__":
    main()