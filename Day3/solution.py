from utils import utils

def main():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    print(process_pt1(data))
    print(process_pt2(data))

def process_pt1(data):
    return run_down_slope(data, 1, 3)

def run_down_slope(data, down, right):
    count = 0
    print(range(0, len(data), down))
    for i in range(0, int(len(data)/down),):
        if data[i*down][i*right%len(data[i*down])] == '#':
            count += 1
    print(count)
    return count

def process_pt2(data):
    product = 1
    product *= run_down_slope(data, 1, 1)
    product *= run_down_slope(data, 1, 3)
    product *= run_down_slope(data, 1, 5)
    product *= run_down_slope(data, 1, 7)
    product *= run_down_slope(data, 2, 1)
    return product

if __name__ == "__main__":
    main()