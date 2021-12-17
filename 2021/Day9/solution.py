from utils import utils
import numpy as np

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            val = data[x][y]
            if x > 0 and val >= data[x-1][y]:
                continue
            if x < len(data)-1 and val >= data[x+1][y]:
                continue
            if y > 0 and val >= data[x][y-1]:
                continue
            if y < len(data[x])-1 and val >= data[x][y+1]:
                continue
            count += data[x][y]+1
    return count

def process_pt2(data):
    basins = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            in_basins = []
            if data[x][y] == 9:
                continue
            if x > 0:
                for b in basins:
                    if b.issuperset({"{},{}".format(x-1, y)}):
                        in_basins.append(b)
            if x < len(data):
                for b in basins:
                    if b.issuperset({"{},{}".format(x+1, y)}) and not b in in_basins:
                        in_basins.append(b)
            if y > 0:
                for b in basins:
                    if b.issuperset({"{},{}".format(x, y-1)}) and not b in in_basins:
                        in_basins.append(b)
            if y < len(data[x]):
                for b in basins:
                    if b.issuperset({"{},{}".format(x, y+1)}) and not b in in_basins:
                        in_basins.append(b)

            if len(in_basins) == 0:
                basins.append({"{},{}".format(x, y)})
            elif len(in_basins) == 1:
                list(in_basins)[0].add("{},{}".format(x, y))
            else:
                new_basin = {"{},{}".format(x, y)}
                for b in in_basins:
                    new_basin = new_basin.union(b)
                    basins.remove(b)
                basins.append(new_basin)
    basin_lens = [len(x) for x in basins]
    basin_lens.sort(reverse=True)
    return np.prod(basin_lens[:3])

def process_input(data):
    return [[int(x) for x in y] for y in data if len(data) != 0]

if __name__ == "__main__":
    run()
