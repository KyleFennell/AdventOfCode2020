from utils import utils
def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    open_paths = [["start"]]
    finished_paths = []
    while len(open_paths) > 0:
        working_path = open_paths.pop()
        for con in data[working_path[-1]]:
            if con == "end":
                new_path = working_path.copy()
                new_path.append(con)
                finished_paths.append(new_path)
            elif con.upper() == con:
                new_path = working_path.copy()
                new_path.append(con)
                open_paths.append(new_path)
            elif not con in working_path:
                new_path = working_path.copy()
                new_path.append(con)
                open_paths.append(new_path)
    return len(finished_paths)

def process_pt2(data):
    open_paths = [[False, "start"]]
    finished_paths = []
    while len(open_paths) > 0:
        working_path = open_paths.pop()
        for con in data[working_path[-1]]:
            if con == "end":
                new_path = working_path.copy()
                new_path.append(con)
                finished_paths.append(new_path)
            elif con.upper() == con:
                new_path = working_path.copy()
                new_path.append(con)
                open_paths.append(new_path)
            elif con in working_path and not working_path[0] and con != "start":
                new_path = working_path.copy()
                new_path[0] = True
                new_path.append(con)
                open_paths.append(new_path)
            elif not con in working_path:
                new_path = working_path.copy()
                new_path.append(con)
                open_paths.append(new_path)
    return len(finished_paths)
def process_input(data):
    data = [x.split("-") for x in data if len(x) > 0]
    connections = {}
    for d in data:
        if not d[0] in connections.keys():
            connections[d[0]] = []
        if not d[1] in connections.keys():
            connections[d[1]] = []
        connections[d[0]].append(d[1])
        connections[d[1]].append(d[0])
    return connections

if __name__ == "__main__":
    run()
