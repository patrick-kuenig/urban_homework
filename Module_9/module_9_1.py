def apply_all_func(int_list: list[int], *functions):
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    # {'max': 20, 'min': 6}
    # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}