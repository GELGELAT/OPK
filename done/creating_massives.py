import random
import string


def make_random_mass(a):  # случайный массив
    mass = []
    for i in range(a):
        mass.append(random.randint(-100, 100))
    return mass


def make_sorted_random_mass(a, b):  # сортированый с случайным максимальным шагом b от заданого значения
    mass = [-100]
    for i in range(a):
        mass.append(random.randint(mass[i], mass[i] + b))
    return mass


def make_random_text_with_pattern(n, pattern):
    arr = [random.choice(string.ascii_lowercase) for _ in range(n)]
    arr[random.randint(0, n - 1)] = str(pattern)
    text = ''.join(arr)
    return text

