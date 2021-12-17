from os import replace
from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "test.txt"))
    initial, replacements = process_input(data)
    print("part1: ", process_pt1(initial, replacements))
    print("part2: ", process_pt2(initial, replacements))
                
def process_pt1(initial, replacements):
    step = initial
    print(step)
    for i in range(20):
        next_step = slow_process_step(step, replacements)
        step = next_step
        letters = set([x for x in step])
        frequencies = { x: len(list(filter(lambda l: l == x, [s for s in step]))) for x in letters}
        print(frequencies)
    return max(frequencies.values()) - min(frequencies.values())

def process_pt2(initial, replacements):
    for r in replacements.keys():
        step = r
        print(step, replacements[r])
        for i in range(40):
            next_step = slow_process_step(step, replacements)
            step = next_step
            letters = set([x for x in step])
            frequencies = { x: len(list(filter(lambda l: l == x, [s for s in step]))) for x in letters}
            print(i, frequencies)
    pass

def slow_process_step(step, replacements):
    next_step = ""
    for s in zip(step[:-1], step[1:]):
        next_step += s[0] + replacements["".join(s)]
    return next_step + step[-1]

def process_input(data):
    initial = data[0]
    replacements = {}
    for d in data[1:]:
        key, value = d.split(" -> ")
        replacements[key] = value
    return initial, replacements

if __name__ == "__main__":
    run()
