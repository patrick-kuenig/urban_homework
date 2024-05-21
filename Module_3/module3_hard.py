def calculate_structure_sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, dict) and arg is not None:
            for key, value in arg.items():
                result += calculate_structure_sum(key)
                result += calculate_structure_sum(value)
        elif isinstance(arg, (list, tuple, set)) and len(arg) != 0:
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, int):
            result += arg
        elif isinstance(arg, str):
            result += len(arg)

    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # 99
