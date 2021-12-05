from utils import utils

def main():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    print(process_pt1(data))
    print(process_pt2(data))

def process_pt1(data):
    highest = 0
    for d in data:
        if process_seat(d) > highest:
            highest = process_seat(d)
    return highest

def process_pt2(data):
    seats = list(map(lambda d: process_seat(d), data))
    seats.sort()
    for s in range(len(seats)):
        if seats[s+1] - seats[s] != 1:
            return seats[s]+1

def process_seat(seat_id):
    seat_id = seat_id.replace('F', "0").replace('L', "0").replace('B', "1").replace('R', "1")
    return int(seat_id[:7], 2) * 8 + int(seat_id[7:], 2)

if __name__ == "__main__":
    main()