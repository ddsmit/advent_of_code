import itertools
import functools
from file.data import get_file

def elfing_around(dataset, number_of_numbers, sum_target=2020):
    for num_set in itertools.product(*[dataset]*number_of_numbers):
        if sum(num_set) == sum_target:
            product = functools.reduce(lambda a, b: a * b, num_set)
            return num_set, product

data = get_file('d1.txt')

numbers = [int(number) for number in data if number]

print(*elfing_around(numbers, number_of_numbers=2))
print(*elfing_around(numbers, number_of_numbers=3))
