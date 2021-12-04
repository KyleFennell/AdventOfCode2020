from typing import List
from functools import reduce
from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data: List):
    return sum([d[1] if d[0][0] == "d" else -d[1] if d[0][0] == "u" else 0 for d in data]) * sum(d[1] for d in data if d[0][0] == "f")

def process_pt2(data):
    # x = [aim, horizontal, vertical]
    return (lambda x: x[1] * x[2])(reduce(lambda x, y: [x[0] + (y[1] if y[0][0] == "d" else -y[1] if y[0][0] == "u" else 0), x[1] + (y[1] if y[0][0] == "f" else 0), x[2] + (x[0] * y[1] if y[0][0] == "f" else 0)], data, [0]*3))

def process_input(data):
    new_data = list(map(lambda x: [x[0], int(x[1])],  [d.split(" ") for d in data]))
    return new_data

if __name__ == "__main__":
    run()
