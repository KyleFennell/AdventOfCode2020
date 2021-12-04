import re
import numpy as np
from utils import utils

def main():
    input = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    process = re.compile("^([\d]*)-([\d]*) ([\w]): ([\w]*)$")
    hits1 = 0
    hits2 = 0
    for password in input:
        if re.match("([\w])", password):
            code = process.match(password).groups()
            if process_pt1(np.asarray(code)):
                hits1 += 1
            if process_pt2(np.asarray(code)):
                hits2 += 1
    print("part1: ", hits1, "\npart2: ", hits2)

def process_pt1(code):
    pattern = "(["+code[2]+"])"
    string = code[3]
    instances = len(re.compile(pattern).findall(string))
    return instances >= int(code[0]) and instances <= int(code[1])

def process_pt2(code):
    inc = 0
    if code[3][int(code[0])-1] == code[2]:
        inc += 1
    if code[3][int(code[1])-1] == code[2]:
        inc += 1
    return inc == 1

if __name__ == "__main__":
    main()
