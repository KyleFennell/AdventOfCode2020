from utils import utils

PREAMBLE_LENGTH = 25

def main():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    print(process_pt1(data))
    print(process_pt2(data))

def process_pt1(data):
    preamble = data[:PREAMBLE_LENGTH]
    to_calculate = data[PREAMBLE_LENGTH:]
    for num in data:
        solution_found = True
        
        for i in range(PREAMBLE_LENGTH):
            for j in range(i, j):
                
    pass

def process_pt2(data):
    pass

def process_input(data):
    return [int(num) for num in data]

if __name__ == "__main__":
    main()