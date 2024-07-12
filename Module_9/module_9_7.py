def is_prime(func):
    def checker(*args):
        result = func(*args)
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result

    return checker


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
    result1 = sum_three(3, 3, 3)
    print(result1)
