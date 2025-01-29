def generate_code(template, **kwargs):
    try:
        code = template.format(**kwargs)
        return code
    except KeyError as e:
        raise ValueError(f"Missing placeholder in template: {e}")
    
def validate_code(code):
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError as e:
        raise ValueError(f"Syntax error in generated code: {e}")
    
def execute_code(code):
    try:
        exec(code, globals())
    except Exception as e:
        raise RuntimeError(f"Error executing code: {e}")
    
def dynamic_code_generation(template, **kwargs):
    try:
        code = generate_code(template, **kwargs)
        validate_code(code)
        execute_code(code)
        return "Code executed successfully."
    except Exception as e:
        return str(e)

# Przykładowe użycie
template = """
def dynamic_function(x):
    return x + {increment}
"""

data = {
    "increment": 2
}

result = dynamic_code_generation(template, **data)
print(result)

# Wywołanie wygenerowanej funkcji
try:
    print(dynamic_function(5))  # Oczekiwany wynik: 7
except NameError as e:
    print(f"Function not defined: {e}")