from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "test.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    pass

def process_pt2(data):
    pass

def process_input(data):
    new_data = data
    return new_data

if __name__ == "__main__":
    run()
