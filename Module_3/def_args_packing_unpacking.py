def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2)
print_params(b='bad')
print_params(4, 5, False)
print_params(b=25)
print_params(c=[1, 2, 3])
# all works fine

values_list = [20, 'yo', ('hello', 'bye')]
values_dict = {'a': False, 'b': 2024, 'c': ['I', 'don\'t', 'know']}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [2, 'Batman']
print_params(*values_list2, 42)
# works fine because three parameters
