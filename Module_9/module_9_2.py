first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(name) for name in first_strings if len(name) > 5]
second_result = [(name, word) for name in first_strings for word in second_strings if len(name) == len(word)]
third_result = {key: len(key) for key in (first_strings + second_strings)}

print(first_result, second_result, third_result, sep='\n')
