from utils import utils
from functools import reduce
import re
def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    [numbers, boards] = process_input(data)
    print("part1: ", process_pt1(numbers, boards))
    print("part2: ", process_pt2(numbers, boards))
                
def process_pt1(numbers, boards):
    for n in numbers:
        boards = [board.replace(" {} ".format(n), " x ") for board in boards]
        answer = list(filter(lambda board: check_board(board), boards))
        if len(answer) > 0:
            return(int(n) * sum([int(x) for x in answer[0].split(" ") if len(x) != 0 and x != "x"]))

def process_pt2(numbers, boards):
    for n in numbers:
        boards = [board.replace(" {} ".format(n), " x ") for board in boards]
        losing_boards = list(filter(lambda board: not check_board(board), boards))
        if len(losing_boards) == 1:
            return process_pt1(numbers, losing_boards)  
    pass

def process_input(data):
    numbers = [n for n in data[0].split(",")]
    boards = []
    for b in range(round(len(data[1:])/5)):
        board = reduce(lambda x, y: x + y+" ", [data[1:][5*b + row] for row in range(5)], " ")
        boards.append(re.sub(r"[\s]+", " ", board))
    return [numbers, boards]

def check_board(board):
    valid_rows = [True]*5
    valid_cols = [True]*5
    board_as_numbers = [b for b in board.split(" ") if len(b) > 0]
    for row in range(5):
        for col in range(5):
            if board_as_numbers[col*5+row] != "x":
                valid_rows[row] = False
                valid_cols[col] = False
    return any(valid_rows) or any(valid_cols)

if __name__ == "__main__":
    run()
