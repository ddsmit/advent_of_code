def get_file(file_path: str):
    if not file_path:
        raise Exception("Did not pass in a file or URL to access")
    with open(file=file_path) as file:
        inputs = file.readlines()
    return [line.strip('\n') for line in inputs if line]

def find_bag(rules, bag="shiny yellow", counter=0):
    rules = rules.copy()
    for key, bags in rules.items():
        print(key,bags)
        for temp_bag in bags:
            if bag.lower() in temp_bag.lower():
                counter += 1
            elif temp_bag in rules:
                print(temp_bag)
                counter += find_bag({temp_bag:rules[temp_bag]}, bag, counter)
        # return counter
    if counter != 0:
        x = 1
    return counter

def find_bag(rules_containing_bag, bag='shiny yellow', counter = 0):
    for containing_bag, rule in rules_containing_bag.items():
        print(bag, containing_bag)
        if bag == containing_bag:
            counter += 1
        if bag in rule:
            print('bag found')
            counter += 1
            return find_bag(rules, containing_bag, counter)
    return counter



data = get_file('d7.txt')

rules_raw = {
    line.split('contain')[0].replace(' bags','').strip():line.split('contain')[1]
    for line in data
}

rules = dict()
for key, value in rules_raw.items():
    contained_items = {
        item.strip()[item.strip().find(' ')+1:].replace(' bags','').replace(' bag',' ').replace('.','').strip():
            (item.strip()[:item.strip().find(' ')])
        for item in value.split(',')
    }
    rules.update(
        {
            key:contained_items
        }
    )

rules_containing_bag = {
    key:value
    for key, value in rules.items()
    if 'shiny yellow' in value
}
print(rules_containing_bag)

print('start')
print(find_bag(rules))