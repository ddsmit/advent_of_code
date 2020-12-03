from collections import Counter
from data import get_file

def elfing_passwords(data, condition_func):
    return [
        line
        for line in data
        if line and condition_func(
            condition_value_1=int(line.split(' ')[0].split('-')[0]),
            condition_value_2=int(line.split(' ')[0].split('-')[1]),
            letter=line.split(' ')[1].strip().replace(':', ''),
            password=line.split(':')[-1].strip(),
        )
    ]

data = get_file('d2.txt')

meets_policy = elfing_passwords(
    data=data,
    condition_func=lambda condition_value_1, condition_value_2, letter, password: condition_value_1 <= Counter(password)[letter] <= condition_value_2
)

print(len(meets_policy))

meets_policy2 = elfing_passwords(
    data=data,
    condition_func=lambda condition_value_1, condition_value_2, letter, password: (len(password) >= condition_value_1 and password[condition_value_1-1] == letter) != (len(password) >= condition_value_2 and password[condition_value_2-1] == letter)
)

print(len(meets_policy2))