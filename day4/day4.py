import data
import re

def height_check(value):
    if 'in' in value.lower():
        value = int(value.replace('in',''))
        return 59 <= value <= 76
    elif 'cm' in value.lower():
        value = int(value.replace('cm', ''))
        return 150 <= value <= 193
    else:
        return False

validation = {
    'byr': lambda val: 1920 <= int(val) <= 2002 and len(val) == 4,
    'iyr': lambda val: 2010 <= int(val) <= 2020 and len(val) == 4,
    'eyr': lambda val: 2020 <= int(val) <= 2030 and len(val) == 4,
    'hgt': height_check,
    'hcl': lambda val: bool(re.findall("^#[0-9a-f]{6}$", val)),
    'ecl': lambda val: val in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda val: bool(re.findall("^\d{9}$", val)),
    'cid': lambda val: True,
}

required_cred = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

def validate_credentials(person):
    return required_cred.issubset(
        {
            feature.split(':')[0]
            for feature in person
        }
    )

def validate_format(person):
    return all(
        validation[feature.split(':')[0]](feature.split(':')[1])
        for feature in person
    )


data = data.get_file_raw('d4.txt')


people = [
    line.replace('\n',' ').split(' ')
    for line in data.split('\n\n')
]

print(
    'Valid Credentials',
    sum(validate_credentials(person) for person in people)
)
print(
    'Valid Credentials and Format',
    sum(validate_credentials(person) and validate_format(person) for person in people)
)
