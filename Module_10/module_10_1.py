import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf8') as file:
        for count in range(1, word_count+1):
            file.write(f'Какое-то слово №{count}\n')
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Прошло {end_time - start_time}с.")

thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = time.time()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end_time = time.time()

print(f"Прошло {end_time - start_time}с.")

#Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Прошло 34.167181730270386с.
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Прошло 20.099226474761963с.
