def find_max_number(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    return max(numbers) if numbers else None

def find_longest_string(data):
    strings = list(filter(lambda x: isinstance(x, str), data))
    return max(strings, key=len) if strings else None

def find_largest_tuple(data):
    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    return max(tuples, key=len) if tuples else None

def analyze_data(data):
    max_number = find_max_number(data)
    longest_string = find_longest_string(data)
    largest_tuple = find_largest_tuple(data)
    
    return {
        "max_number": max_number,
        "longest_string": longest_string,
        "largest_tuple": largest_tuple
    }

data = [123, "hello", (1, 2, 3), 45.67, "world", (4, 5), {"key": "value"}, [1, 2, 3, 4], "Python", (1, 2, 3, 4, 5)]
results = analyze_data(data)

print("Największa liczba:", results["max_number"])
print("Najdłuższy napis:", results["longest_string"])
print("Krotka o największej liczbie elementów:", results["largest_tuple"])