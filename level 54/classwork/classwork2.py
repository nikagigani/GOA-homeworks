def square(x):
    return x * x

def apply_to_list(func, values):
    results = []
    for value in values:
        results.append(func(value))
    return results