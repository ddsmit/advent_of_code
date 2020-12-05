import functools

from file.data import get_file


def sonnys_ultimate_question(
        data,
        move_x,
        move_y,
        initial_y=0,
        initial_x=0,
        tree='#'
):
    counter = 0
    current_x = initial_x
    for row in data[initial_y::move_y]:
        row = ((current_x//len(row))+1)*row
        if row[current_x] == tree:
            counter += 1
        current_x += move_x
    return counter



data = get_file('d3.txt')

move_x = 3
move_y = 1

print(sonnys_ultimate_question(
    data,
    move_x,
    move_y,
))

moves = [
    {'move_x':1, 'move_y':1},
    {'move_x':3, 'move_y':1},
    {'move_x':5, 'move_y':1},
    {'move_x':7, 'move_y':1},
    {'move_x':1, 'move_y':2},
]

print(functools.reduce(lambda a, b: a*b, [sonnys_ultimate_question(data,**move) for move in moves],))
