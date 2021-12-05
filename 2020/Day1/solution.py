from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))

    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if int(data[i]) + int(data[j]) == 2020:
                return int(data[i]) * int(data[j])

def process_pt2(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                    return int(data[i]) * int(data[j]) * int(data[k])

if __name__ == "__main__":
    run()
