from utils import utils
from functools import reduce 

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    return process_sequence(data, 80)

def process_pt2(data):
    return process_sequence(data, 256)

def process_sequence(data, iterations):
    frequency = reduce(lambda x, y: [(x[i] + (1 if i == y else 0)) for i in range(9)], data, [0]*9)
    for _ in range(iterations):
        next_frequency = [0]*9
        for i in range(9):
            if i == 6:
                next_frequency[i] = frequency[i+1] + frequency[0]
            elif i == 8:
                next_frequency[i] = frequency[0]
            else:
                next_frequency[i] = frequency[i+1]
        frequency = next_frequency
    return sum(frequency)

def process_input(data):
    return [int(d) for d in data[0].split(',') if len(d) != 0]

if __name__ == "__main__":
    run()
