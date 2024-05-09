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
    try:
        input_ = int(input("Which number do you need the password for?\n"))
        print(f"Password for {input_}:", password_game(input_))

    except ValueError:
        print("You entered an invalid value.")
        input_ = int(input("Please try again using a valid number between 3 and 20...\n"))
        print(f"Password for {input_}:", password_game(input_))
