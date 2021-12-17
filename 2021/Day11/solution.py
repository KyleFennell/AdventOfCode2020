from os import EX_TEMPFAIL
from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data.copy()))
    print("part2: ", process_pt2(data.copy()))
                
def process_pt1(data):
    total_flashes = 0
    step = data
    print_array(data)
    for i in range(100):
        step = process_step(step)
        total_flashes += len(list(filter(lambda i: i == 0, [x for y in step for x in y])))
    return total_flashes

def process_pt2(data):
    step = data
    print_array(data)
    i = 1
    flashes = 0
    while flashes != 100:
        step = process_step(step)
        flashes = len(list(filter(lambda i: i == 0, [x for y in step for x in y])))
        i += 1
    return i

def process_step(step):
    for x in range(len(step)):
        for y in range(len(step[x])):
            step[x][y] = step[x][y]+1
    flash = process_flash(step)
    next_flash = process_flash(flash)
    while flash != next_flash:
        flash = next_flash
        next_flash = process_flash(flash)
    return flash

def process_flash(step):
    light = [[0]*len(step[x]) for x in range(len(step))]
    for x in range(len(step)):
        for y in range(len(step[x])):
            if step[x][y] <= 9:
                continue
            if x > 0:
                if y > 0:
                    light[x-1][y-1] = light[x-1][y-1] + 1
                if y < len(step[x])-1:
                    light[x-1][y+1] += 1
                light[x-1][y] += 1
            if x < len(step)-1:
                if y > 0:
                    light[x+1][y-1] += 1
                if y < len(step[x])-1:
                    light[x+1][y+1] += 1
                light[x+1][y] += 1
            if y > 0:
                light[x][y-1] += 1
            if y < len(step[x])-1:
                light[x][y+1] += 1
            step[x][y] = 0
    next_step = [[0]*len(step[x]) for x in range(len(step))]
    for x in range(len(step)):
        for y in range(len(step[x])):
            next_step[x][y] = (step[x][y] + light[x][y]) if step[x][y] != 0 else 0
    return next_step

def print_array(arr):
    print()
    for a in arr:
        print(a)

def process_input(data):
    return [[int(l) for l in line] for line in data]

if __name__ == "__main__":
    run()
