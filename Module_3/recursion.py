def test(*args, **kwargs):
    print(*args)
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


test(1, 2, "hello", *(True, False), kwargs_1 = 'booboo', kwargs_2 = None)

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(6)) # 720
