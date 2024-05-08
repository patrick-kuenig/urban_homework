def print_params(*args):
    print(*args, *args)

print_params([1, 2, 3, 4], {'a': 2, 'b': 3}, (2, 3, 4, 5), 'hello')
print_params(1, 2, 3, 4, 'ferrari', (5, 6, 7, 8))
print_params(True)
