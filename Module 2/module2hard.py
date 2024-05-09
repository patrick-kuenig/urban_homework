def password_game(key):
    if 2 < key < 21:
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
    else:
        return "A number between 3 and 20 has to be used."


if __name__ == "__main__":
    try:
        input_ = int(input("Which number do you need the password for?\n"))
        print(f"Password for {input_}:", password_game(input_))
        if input('Would you like to know all the passwords? (y/n)') == 'y':
            for all in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
                print(f"{all}:", password_game(all))
        else:
            print('Goodbye')

    except ValueError:
        print("You entered an invalid value.")
        input_ = int(input("Please try again using a valid number between 3 and 20...\n"))
        print(f"Password for {input_}:", password_game(input_))
