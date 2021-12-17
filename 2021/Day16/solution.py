from utils import utils

def run():
    data = utils.remove_empty_lines(utils.read_file(__package__, "test2.txt"))
    data = process_input(data)
    print(data)
    print("part1: ", process_pt1(data))
    print("part2: ", process_pt2(data))
                
def process_pt1(data):
    _, packets = process_to_packets(data)
    print(packets)
    return calculate_version_total([packets])

def process_pt2(data):
    pass

def process_to_packets(data):
    bits_left = data
    children = []
    while (len(bits_left) > 0 and "1" in bits_left):
        packet = {} 
        print("bits left:", bits_left)
        packet["version"] = int(bits_left[:3], 2)
        packet["type_id"] = int(bits_left[3:6], 2)
        bits_left = bits_left[6:]
        print(packet)
        if (packet["type_id"] == 4):
            print("literal")
            literal = ""
            next_literal_packet = bits_left[:5]
            bits_left = bits_left[5:]
            print("literal packet:", next_literal_packet)
            while(next_literal_packet[0] == "1"):
                literal += next_literal_packet[1:]
                next_literal_packet = bits_left[:5]
                bits_left = bits_left[5:]
                print(next_literal_packet)
            literal += next_literal_packet[1:]
            print("final literal:", literal)
            packet["data"] = int(literal, 2)
            children.append(packet)
            packet = None
        else:
            length = 0
            if (bits_left[0] == "0"):
                length = int(bits_left[1:16], 2)
                bits_left = bits_left[16:]
                sub_bits_left = bits_left[:length]
                bits_left = bits_left[length:]
                print("bits length:", length)
                while(len(sub_bits_left) > 0 and "1" in sub_bits_left):
                    sub_bits_left, child = process_to_packets(sub_bits_left)
                    if child:
                        children.append(child)
            else:
                length = int(bits_left[1:12], 2)
                bits_left = bits_left[12:]
                print("children length:", length)
                for i in range(length):
                    bits_left, child = process_to_packets(bits_left)
                    if child:
                        children.append(child)
    return bits_left, packet

def calculate_version_total(packets):
    total = 0
    for p in packets:
        print(p)
        total += p["version"]
        if isinstance(p["data"], list):
            total += calculate_version_total(p["data"]) 
    return total

def process_input(data):
    d_size = len(data[0]) * 4
    return bin(int(data[0], 16))[2:].zfill(d_size)

if __name__ == "__main__":
    run()
