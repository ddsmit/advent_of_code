import functools
import collections

from file import get_file


def sonnys_ultimate_question(
        data,
        move_x,
        move_y,
        initial_y=0,
        initial_x=0,
        tree='#'
):
    return collections.Counter(
        [
            (((index*move_x + initial_x // len(row)) + 1)*row)[index*move_x+initial_x]
            for index, row in enumerate(data[initial_y::move_y])
        ]
    )[tree]


data = get_file('d3.txt')

print(sonnys_ultimate_question(
    data,
    move_x=3,
    move_y=1,
))

moves = [
    {'move_x':1, 'move_y':1},
    {'move_x':3, 'move_y':1},
    {'move_x':5, 'move_y':1},
    {'move_x':7, 'move_y':1},
    {'move_x':1, 'move_y':2},
]

print(functools.reduce(lambda a, b: a*b, [sonnys_ultimate_question(data,**move) for move in moves],))
