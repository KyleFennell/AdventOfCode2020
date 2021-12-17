from utils import utils
from functools import reduce
import numpy as np

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    print(data)
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    return calculate_answer(data, calculate_fuel_pt1)

def process_pt2(data):
    return calculate_answer(data, calculate_fuel_pt2)

def calculate_answer(data, calculate_fuel):
    pos_min = min(data)
    pos_max = max(data)
    while pos_min != pos_max:
        midpoint = calculate_midpoint(pos_min, pos_max)
        midpoint_fuel = calculate_fuel(midpoint, data)
        min_pos_fuel = calculate_fuel(pos_min, data)
        max_pos_fuel = calculate_fuel(pos_max, data)
        if calculate_midpoint(midpoint_fuel,max_pos_fuel) > calculate_midpoint(midpoint_fuel, min_pos_fuel) :
            if (pos_max == midpoint):
                break
            pos_max = midpoint
        else :
            if (pos_min == midpoint):
                break
            pos_min = midpoint
    if (calculate_fuel(pos_max, data) < calculate_fuel(pos_min, data)):
        return calculate_fuel(pos_max, data)
    return calculate_fuel(pos_min, data)

def calculate_fuel_pt1(pos, data):
    return sum(list(map(lambda x: abs(pos-x), data)))

def calculate_fuel_pt2(pos, data):
    return sum(list(map(lambda x:sum(range(abs(x-pos)+1)), data)))

def calculate_midpoint(_min, _max):
    return int(np.floor((_max+_min)/2))

def process_input(data):
    return [int(d) for d in data[0].split(",") if len(d) != 0]

if __name__ == "__main__":
    run()
