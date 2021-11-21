import os
import re

def read_file(path, filename):
    with open(os.path.join(path, filename), 'r') as file:
        return str(file.read()).split("\n")

def remove_empty_lines(data: list):
    return list(filter(lambda line: len(line) != 0, data))