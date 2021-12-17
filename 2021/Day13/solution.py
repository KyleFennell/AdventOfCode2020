from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    points, instructions = process_input(data)
    print("part1: ", process_pt1(points, instructions))
    print("part2: ", process_pt2(points, instructions))
                
def process_pt1(points, instructions):
    instruction = instructions[0]
    axis = 0 if instruction[0] == "x" else 1
    value = int(instruction[1])
    print('value', value)
    new_points = set()
    for p in points:
        num = p.split(",")[axis]
        if int(num) > value:
            p = p.replace(num, str(value-(int(num)-value)))
        new_points.add(p)
    return len(new_points)

def process_pt2(points, instructions):
    for i in instructions:
        points = process_fold(points, i)
    print_points(points)

def process_fold(points, instruction):
    axis = 0 if instruction[0] == "x" else 1
    value = int(instruction[1])
    new_points = set()
    for p in points:
        num = p.split(",")[axis]
        if int(num) >= value:
            p = p.replace(num, str(value-(int(num)-value)))
        new_points.add(p)
    print_points(new_points)
    return new_points

def print_points(points):
    max_x = 0
    max_y = 0
    for p in points:
        [x, y] = p.split(',')
        x = int(x)
        y = int(y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    arr = [[' ']*(max_x+1) for y in range(max_y+1)]
    for p in points:
        [x, y] = p.split(',')
        arr[int(y)][int(x)] = "#"
    for a in arr:
        print("".join(a))

def process_input(data):
    points = set()
    instructions = []
    for d in data:
        if "," in d:
            points.add(d)
        else:
            instructions.append(d[11:].split("="))
    return points, instructions

if __name__ == "__main__":
    run()