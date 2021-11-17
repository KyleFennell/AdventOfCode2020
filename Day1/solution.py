from utils.utils import read_file

def run():
    data = read_file(__package__, "input.txt")

    for i in range(len(data)):
        for j in range(i, len(data)):
            if int(data[i]) + int(data[j]) == 2020:
                return int(data[i]) * int(data[j])

if __name__ == "__main__":
    print(run())