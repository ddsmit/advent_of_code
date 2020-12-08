def get_file(file_path: str):
    if not file_path:
        raise Exception("Did not pass in a file or URL to access")
    with open(file=file_path) as file:
        inputs = file.readlines()
    return [line.strip('\n') for line in inputs if line]

data = get_file('d8.txt')

commands = [
    (
        line.split(' ')[0],
        int(line.split(' ')[1]),
    )
    for line in data
]

def run_sequence(commands):
    commands_ran = set()
    command_new = True
    index = 0
    acc = 0
    while command_new:
        commands_ran.add(index)
        if index <= 0:
            index = 0
        current_command_action = commands[index][0]
        current_command_value = commands[index][1]
        if current_command_action == 'acc':
            acc += current_command_value
            index += 1
        elif current_command_action == 'jmp':
            index += current_command_value
        else:
            index += 1

        command_new = not index in commands_ran and index < len(commands)

    return acc, commands[-1] in commands_ran or index >= len(commands)

print(run_sequence(commands))

nops = [
    index
    for index, command in enumerate(commands)
    if command[0] == 'nop'
]

jmps = [
    index
    for index, command in enumerate(commands)
    if command[0] == 'jmp'
]
for index in nops:
    new_commands = commands.copy()
    new_commands[index] = ('jmp',new_commands[index][1])
    acc, finished = run_sequence(new_commands)
    if finished:
        print(acc)

for index in jmps:
    new_commands = commands.copy()
    new_commands[index] = ('nop',new_commands[index][1])
    acc, finished = run_sequence(new_commands)
    print(acc, finished)
    if finished:
        print(acc)

