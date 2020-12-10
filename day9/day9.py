import itertools

def get_file(file_path: str):
    if not file_path:
        raise Exception("Did not pass in a file or URL to access")
    with open(file=file_path) as file:
        inputs = file.readlines()
    return [line.strip('\n') for line in inputs if line]


def find_invalid_number(data, preamble_length, ):
    for index, number_to_check in enumerate(data[preamble_length:]):
        range_to_check = data[index:preamble_length+index]
        if not any(
                [
                    number_to_check
                    for value1, value2 in itertools.combinations(range_to_check, 2)
                    if value1+value2 == number_to_check
                ]
        ):
            return number_to_check


def get_sequence_summed(data, match_value):
    indices = list(range(len(data)+1))
    for start, end in itertools.combinations(indices, 2):
        cont_range = data[start:end]
        if sum(cont_range) == match_value:
            return min(cont_range) + max(cont_range)


data = [int(number) for number in get_file('d9.txt')]

part_1_answer = find_invalid_number(data, 25)

print(part_1_answer)

print(get_sequence_summed(data, part_1_answer))