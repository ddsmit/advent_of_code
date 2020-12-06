import re
def get_file_raw(file_path: str):
    if not file_path:
        raise Exception("Did not pass in a file or URL to access")
    with open(file=file_path) as file:
        return file.read()

data = get_file_raw('d6.txt')

groups = [
    line.replace('\n',' ').split(' ')
    for line in data.split('\n\n')
]

groups_comb = [
    ''.join(group)
    for group in groups
]

groups_comb_set = [
    ''.join(set(''.join(group)))
    for group in groups
]

num_q = [
    len(set(''.join(group)))
    for group in groups
]

print(groups)
print(groups_comb)
print(groups_comb_set)
print(num_q)
print(sum(num_q))

print('\n')
print(groups)

def collect_leters(group, letters):
    if len(group) == 0:
        return letters
    if len(group) != 0:
        current_letters = group[0]
        letters_remaining = set(letters).intersection(set(current_letters))
        if letters_remaining:
            letters = ''.join(letters_remaining)
        else:
            letters = ''
        new_group = group.copy()
        new_group.remove(current_letters)
        return collect_leters(new_group,letters)


print(sum(len(collect_leters(group, group[0])) for group in groups))