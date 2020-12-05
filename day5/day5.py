from file.data import get_file


def get_number(id, high, num_range):
    current_range = num_range.copy()
    for letter in id:
        if letter == high:
            current_range = current_range[len(current_range)//2:]
        else:
            current_range = current_range[:len(current_range)//2]
    return current_range[0]


def get_row_set(line):
    return line[:7]


def get_column_set(line):
    return line[7:]


def get_seat_id(line):
    row = get_number(get_row_set(line), high='B', num_range=list(range(0,128)))
    column = get_number(get_column_set(line), high='R', num_range=list(range(0,8)))
    return row*8+column


data = get_file('d5.txt')

all_filled_seats = sorted([get_seat_id(line) for line in data])
print(max(all_filled_seats))

all_possible_seats = list(range(min(all_filled_seats), max(all_filled_seats)+1))
print(set(all_possible_seats)-set(all_filled_seats))