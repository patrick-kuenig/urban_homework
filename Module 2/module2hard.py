import random

def password_game(key):
    if 2 < key < 21:
        keys = []
        for numbers in range(1, key + 1):
            keys.append(numbers)

        result_list = []
        for i in keys[:-1]:
            for j in keys[1:]:
                if i + j == key:
                    result_list.extend([i, j])
            keys.remove(i)
        result = ''.join(str(x) for x in result_list)
        return result
    else:
        return "A number between 3 and 20 has to be used."

if __name__ == "__main__":
    input_ = randint(3, 20)
    print(password_game()
