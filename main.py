#Вариант 15. Последовательности натуральных чисел, расположенных в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
import re

def number_to_words(number):
    words = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(words[digit] for digit in str(number))

with open("input.txt", "r") as file:
    for line in file:
        numbers = re.findall(r'\b\d+\b', line)
        sequence = []
        
        for number in map(int, numbers):
            sequence.append(number)
        
        if len(sequence) > 1 and sequence == sorted(sequence):
            min_number = sequence[0]
            min_number_words = number_to_words(min_number)
            
            print(' '.join(map(str, sequence)) + f': {min_number_words} - минимальное число')

