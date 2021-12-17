from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    return len([y for x in data for y in x["code"] if len(y) in [2, 3, 4, 7]])

def process_pt2(data):
    cumsum = 0
    for x in data:
        d = x["all_numbers"]
        certain_segments = {}
        certain_numbers = [set()]*10
        certain_numbers[1] = set(list(filter(lambda x: len(x) == 2, d))[0])
        certain_numbers[4] = set(list(filter(lambda x: len(x) == 4, d))[0])
        certain_numbers[7] = set(list(filter(lambda x: len(x) == 3, d))[0])
        certain_numbers[8] = set(list(filter(lambda x: len(x) == 7, d))[0])
        certain_segments["a"] = certain_numbers[7].difference(certain_numbers[1])
        # find 0, 6, 9
        for len_6 in [set(x) for x in filter(lambda x: len(x) == 6, d)]:
            potential_e = certain_numbers[8].difference(certain_numbers[4]).difference(len_6)
            potential_c = certain_numbers[8].difference(len_6).intersection(certain_numbers[1])
            if len(potential_e) == 1: 
                certain_numbers[9] = len_6
                certain_segments["e"] = potential_e
            elif len(potential_c) == 1:
                certain_numbers[6] = len_6
                certain_segments["c"] = potential_c
            else:
                certain_numbers[0] = len_6
        # find 2, 3, 5
        for len_5 in [set(x) for x in filter(lambda x: len(x) == 5, d)]:
            potential_5 = len_5.union(certain_segments["e"]) == certain_numbers[6]
            potential_3 = certain_numbers[8].difference(len_5).difference(certain_numbers[4])
            if potential_5:
                certain_numbers[5] = len_5
            elif len(potential_3) == 1:
                certain_numbers[3] = len_5
            else:
                certain_numbers[2] = len_5
        # decode
        num = ""
        for code_num in [set(x) for x in x["code"]]:
            for i in range(10):
                if certain_numbers[i] == code_num:
                    num += str(i)
        cumsum += int(num)
    return cumsum



def process_input(data):
    temp = [d.split(" | ") for d in data if len(d) != 0]
    new_data = []
    for i in range(len(temp)):
        entry = {
            "all_numbers": [d for d in temp[i][0].split(" ") if len(d) != 0],
            "code": [d for d in temp[i][1].split(" ") if len(d) != 0]
        }
        sorted_numbers = []
        for n in entry["all_numbers"]:
            sorted_number = [x for x in n]
            sorted_number.sort()
            sorted_numbers.append(sorted_number)
        entry["all_numbers"] = sorted_numbers
        entry["all_numbers"].sort(key=(len))
        new_data.append(entry)
    return new_data

if __name__ == "__main__":
    run()
