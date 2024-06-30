def password_game(key):
        keys = []
        for numbers in range(1, key + 1):
            keys.append(numbers)

        result_list = []
        for i in keys[:-1]:
            for j in keys[1:]:
                if key % (i + j) == 0:
                    result_list.extend([i, j])
            keys.remove(i)
        result = ''.join(str(x) for x in result_list)
        return result

if __name__ == "__main__":
    try:
        input_ = int(input("Which number do you need the password for?\n"))
        while input_ < 3 or input_ > 20:
            input_ = int(input("We're interested in a number between 3 and 20, try again.\n"))
        print(f"Password for {input_}:", password_game(input_))

    except ValueError:
        print("You entered an invalid value.")
        input_ = int(input("Please try again using a valid number between 3 and 20...\n"))
        print(f"Password for {input_}:", password_game(input_))
