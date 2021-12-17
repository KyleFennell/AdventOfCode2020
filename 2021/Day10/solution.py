from os import sched_rr_get_interval
from utils import utils

matches = { "{": "}", "[": "]", "(": ")", "<": ">"}
opens = [x for x in matches.keys()]
closes = [x for x in matches.values()]
def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    score, open_strings = process_pt1(data)
    print("part1: ", score)
    print("part2: ", process_pt2(open_strings))
                
def process_pt1(data):
    open_strings = []
    error = ""
    for d in data:
        string = d
        only_open = False
        error_found = False
        while(string != "" and not only_open and not error_found):
            only_open = True
            error_found = False
            string = string.replace("<>", "").replace("[]", "").replace("()", "").replace("{}", "")
            for s in range(len(string)-1):
                if string[s] in opens and string[s+1] in closes and matches[string[s]] != string[s+1]:
                    error += string[s+1]
                    error_found = True
                    break
                if string[s] in closes:
                    only_open = False
                    break
            if not error_found and only_open and string[-1] in opens:
                open_strings.append(string)

    score = 0   
    for e in error:
        if e == ")":
            score += 3
        elif e == "]":
            score += 57
        elif e == "}":
            score += 1197
        elif e == ">":
            score += 25137
        else:
            print("unknown", e)
    return score, open_strings

def process_pt2(data):
    scores = []
    for d in data:
        score = 0
        for s in range(len(d)-1, -1, -1):
            key = matches[d[s]]
            score *= 5
            if key == ")":
                score += 1
            elif key == "]":
                score += 2
            elif key == "}":
                score += 3
            elif key == ">":
                score += 4
            else:
                print("unknown", s)
        scores.append(score)
    scores.sort()
    print(scores)
    return scores[int((len(scores)-1)/2 - 0.5)]

def process_input(data):
    return data

if __name__ == "__main__":
    run()
