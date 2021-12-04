from utils import utils
from functools import reduce

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "test.txt"))
    data = process_input(data)
    
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    return (lambda x: int(x[0], 2) * int(x[1], 2))(get_important_values(data))
    #return (lambda x: int(x[0], 2) * int(x[1], 2))(reduce(lambda x, y: [x[0] + str(round(y/len(data)+1e-15)), x[1] + str(pow(round(y/len(data)+1e-15)-1, 2))], reduce(lambda x, y: [x[i] + int(y[i]) for i in range(len(x))], data, [0]*len(data[0])), ["", ""]))

def process_pt2(data):
    co2_data = oxy_data = data.copy()
    for i in range(len(data[0])):
        [gamma, _] = get_important_values(oxy_data)
        oxy_data = list(filter(lambda x: x[i] == gamma[i], oxy_data))
        [_, epsilon] = get_important_values(co2_data)
        co2_data = list(filter(lambda x: x[i] == epsilon[i], co2_data))
        if len(co2_data) == 1 and len(oxy_data) == 1:
            return int(co2_data[0], 2) * int(oxy_data[0], 2)

def get_important_values(data):
    frequency = reduce(lambda x, y: [x[i] + int(y[i]) for i in range(len(x))], data, [0]*len(data[0]))
    gamma = epsilon = ""
    for f in frequency:
        gamma += str(f) if len(data) == 1 else str(round( f/len(data) +1e-15))
        epsilon += str(f) if len(data) == 1 else str(pow(round( f/len(data) +1e-15) -1, 2))
    return [gamma, epsilon]
    #return reduce(lambda x, y: [x[0] + (str(y) if len(data) == 1 else str(round(y/len(data)+1e-15))), x[1] + (str(y) if len(data) == 1 else str(pow(round(y/len(data)+1e-15)-1, 2)))], reduce(lambda x, y: [x[i] + int(y[i]) for i in range(len(x))], data, [0]*len(data[0])), ["", ""])

def process_input(data):
    return data 

if __name__ == "__main__":
    run()

#    reduce(lambda x, y: [x[i] + int(y[i]) for i in range(len(x))], data, [0]*len(data[0]))
# reduce(lambda x, y: [x[0] + (str(y) if len(data) == 1 else str(round(y/len(data)+1e-15))), x[1] + (str(y) if len(data) == 1 else str(pow(round(y/len(data)+1e-15)-1, 2)))], freq, ["", ""])
# reduce(lambda x, y: [x[0] + str(round(y/len(data)+1e-15)), x[1] + str(pow(round(y/len(data)+1e-15)-1, 2))], reduce(lambda x, y: [x[i] + int(y[i]) for i in range(len(x))], data, [0]*len(data[0])), ["", ""])