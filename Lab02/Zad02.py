def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices dimensions do not match for addition.")
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices dimensions do not match for multiplication.")
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def validate_operation(operation, matrix1, matrix2=None):
    if operation == "add":
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices dimensions do not match for addition.")
    elif operation == "multiply":
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Matrices dimensions do not match for multiplication.")
    elif operation == "transpose":
        pass  # Transpose operation is always valid
    else:
        raise ValueError("Invalid operation.")
    
def execute_operation(operation, matrix1, matrix2=None):
    if operation == "add":
        return add_matrices(matrix1, matrix2)
    elif operation == "multiply":
        return multiply_matrices(matrix1, matrix2)
    elif operation == "transpose":
        return transpose_matrix(matrix1)
    else:
        raise ValueError("Invalid operation.")
    
def matrix_operations(operation_str, matrix1, matrix2=None):
    try:
        operation = eval(operation_str)
        validate_operation(operation, matrix1, matrix2)
        result = execute_operation(operation, matrix1, matrix2)
        return result
    except Exception as e:
        return str(e)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

operation_str = "'add'"
result = matrix_operations(operation_str, matrix1, matrix2)
print("Wynik dodawania:", result)

operation_str = "'multiply'"
result = matrix_operations(operation_str, matrix1, matrix2)
print("Wynik mnożenia:", result)

operation_str = "'transpose'"
result = matrix_operations(operation_str, matrix1)
print("Wynik transponowania:", result)