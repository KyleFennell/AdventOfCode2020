from utils import utils

def main():
    data = utils.remove_empty_lines(utils.read_file(__package__, "input.txt"))
    data = process_input(data)
    print(process_pt1(data))
    print(process_pt2(data))

def process_pt1(data):
    visited = set()
    accumulator = 0
    pointer = 0
    while visited.isdisjoint({pointer}):
        [instruction, value] = data[pointer]
        visited.add(pointer)
        pointer, accumulator = process_instruction(pointer, accumulator, instruction, value)
    return accumulator

def process_pt2(data):
    jump_to = calculate_jump_to_array(data)
    print(jump_to)
    has_access_to_terminals = calculate_access_to_terminals_array(data, jump_to)
    print(has_access_to_terminals)
    visited = set()
    pointer = 0
    accumulator = 0
    found_error = False
    while visited.isdisjoint({pointer}) and pointer >= 0 and pointer < len(data):
        visited.add(pointer)
        instruction, value = data[pointer]
        print(pointer, accumulator, instruction, value)
        temp_pointer = temp_accumulator = None
        if not found_error:
            if instruction == "nop":
                temp_pointer, temp_accumulator = process_instruction(pointer, accumulator, "jmp", value)
            elif instruction == "jmp":
                temp_pointer, temp_accumulator = process_instruction(pointer, accumulator, "nop", value)
        if has_access_to_terminals.issuperset({temp_pointer}):
            print("found", temp_pointer)
            found_error = True
            pointer = temp_pointer
            accumulator = temp_accumulator
        else:
            pointer, accumulator = process_instruction(pointer, accumulator, instruction, value)

    return accumulator


def process_instruction(pointer, accumulator, instruction, value):
    if instruction == "acc":
        accumulator += value
        pointer += 1
    elif instruction == "nop":
        pointer += 1
    elif instruction == "jmp":
        pointer += value
    else:
        print("unknown instruction", instruction)
    return pointer, accumulator

def calculate_jump_to_array(data):
    jump_to = []
    for i in range(len(data)):
        [instruction, value] = data[i]
        if instruction == "acc":
            jump_to.append(i+1)
        elif instruction == "nop":
            jump_to.append(i+1)
        elif instruction == "jmp":
            jump_to.append(i+int(value))
    return jump_to

def calculate_access_to_terminals_array(data, jump_to):
    has_access_to_terminals = {i for i in range(len(jump_to)) if jump_to[i] >= len(data)}  
    print(has_access_to_terminals)      
    done = False
    while(not done):
        done = True
        for d in range(len(data)):
            if has_access_to_terminals.issuperset({jump_to[d]}) and has_access_to_terminals.isdisjoint({d}):
                done = False
                has_access_to_terminals.add(d)
    return has_access_to_terminals

def process_input(data):
    processed = []
    for d in data:
        processed.append([
            d.split(" ")[0], 
            int(d.split(" ")[1])
        ])
    return processed

if __name__ == "__main__":
    main()