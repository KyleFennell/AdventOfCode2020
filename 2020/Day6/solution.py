from utils import utils

def main():
    data = utils.read_file(__package__, "input.txt")
    data = process_input(data)
    print(process_pt1(data))
    print(process_pt2(data))

def process_pt1(data):
    total = 0
    for group in data:
        answers = set()
        for answer in group:
            if answer == "":
                break
            for letter in answer:
               answers.add(letter)
            # print(answer, answers)   
        total += len(answers)
    return total

def process_pt2(data):
    total = 0
    for group in data:
        answers = None
        for answer in group:
            answer_set = set()
            if answer == "":
                break
            for letter in answer:
               answer_set.add(letter)
            if answers == None:
                answers = answer_set
            else :
                answers = answers & answer_set
        total += len(answers)
    return total
    pass

def process_input(data):
    groups = []
    group = ''
    for i in range(len(data)):
        if data[i] == '' and group != '':
            groups.append(group.split(" "))
            group = ''
        else:
            group += data[i]+" "
    return groups

if __name__ == "__main__":
    main()