from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    return len([x for x, y in zip(data[:-1], data[1:]) if x < y])

def process_pt2(data):
    return len([x for x, y in zip(data[:-3], data[3:]) if x < y])

def process_input(data):
    new_data = []
    for d in range(len(data)):
        new_data.append(int(data[d]))
    return new_data

if __name__ == "__main__":
    run()


# def process_pt1(data):
#     total = 0
#     prev = data[0]
#     for d in data:
#         if d > prev:
#             total += 1
#         prev = d
#     return total

# def process_pt2(data):
#     total = 0
#     prev_sum = 9001
#     for i in range(2, len(data)):
#         crnt_sum = data[i] + data[i-1] + data[i-2]
#         if crnt_sum > prev_sum:
#             total += 1
#         prev_sum = crnt_sum
#     return total


len([x for x, y in zip(data[:-1], data[1:]) if x < y]) # part 1
len([x for x, y in zip(data[:-3], data[3:]) if x < y]) # part 2
