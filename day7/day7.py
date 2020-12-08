def get_file(file_path: str):
    if not file_path:
        raise Exception("Did not pass in a file or URL to access")
    with open(file=file_path) as file:
        inputs = file.readlines()
    return [line.strip('\n') for line in inputs if line]


def find_bag(rules, bag='shiny gold', collection = None):
    if not collection:
        collection = set()
    for containing_bag, rule in rules.items():
        if bag in rule:
            collection.add(containing_bag)
            collection = find_bag(rules, containing_bag, collection)
    return collection

data = get_file('d7.txt')

rules_raw = {
    line.split('contain')[0].replace(' bags','').strip():line.split('contain')[1]
    for line in data
}

rules = dict()
for key, value in rules_raw.items():
    contained_items = {
        item.strip()[item.strip().find(' ')+1:].replace(' bags','').replace(' bag',' ').replace('.','').strip():
            int((item.strip()[:item.strip().find(' ')]))
        for item in value.split(',')
        if not 'no' in item
    }
    rules.update(
        {
            key:contained_items
        }
    )

print(rules)
print(len(find_bag(rules)))

def get_num_bags(rules, start_bag='shiny gold', total=0):
    new_amount=0
    for containing_bag, rule in rules.items():


        if containing_bag == start_bag:
            print(containing_bag, rule)
            if len(rule) == 0:
                return 1

            for bag, qty in rule.items():
                new_amount += qty*get_num_bags(rules, start_bag=bag, total=total)+qty
                print(new_amount)
                # total += new_amount
    total += new_amount
    return new_amount

# print(sum([get_num_bags(rules, start_bag=bag,)*qty for bag, qty in rules['shiny gold'].items()]))
print(get_num_bags(rules))
print(sum(rules['shiny gold'].values()))
print(get_num_bags(rules)+sum(rules['shiny gold'].values()))
