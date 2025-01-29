from functools import reduce

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices dimensions do not match for addition.")
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices dimensions do not match for multiplication.")
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def apply_operation(matrices, operation):
    if not matrices:
        raise ValueError("No matrices provided.")
    
    if operation == "add":
        return reduce(add_matrices, matrices)
    elif operation == "multiply":
        return reduce(multiply_matrices, matrices)
    else:
        raise ValueError("Unsupported operation.")
    
def custom_operation(matrix1, matrix2, operation_code):
    operation = eval(operation_code)
    return operation(matrix1, matrix2)

def apply_custom_operation(matrices, operation_code):
    if not matrices:
        raise ValueError("No matrices provided.")
    
    return reduce(lambda x, y: custom_operation(x, y, operation_code), matrices)

def matrix_operations(matrices, operation_str, custom=False):
    try:
        if custom:
            result = apply_custom_operation(matrices, operation_str)
        else:
            result = apply_operation(matrices, operation_str)
        return result
    except Exception as e:
        return str(e)

matrices = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

operation_str = "add"
result = matrix_operations(matrices, operation_str)
print("Wynik sumowania:", result)

operation_str = "multiply"
result = matrix_operations(matrices, operation_str)
print("Wynik mnożenia:", result)

operation_code = "lambda x, y: [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]"
result = matrix_operations(matrices, operation_code, custom=True)
print("Wynik niestandardowej operacji:", result)