import os
import re

def read_file(path, filename):
    with open(os.path.join(path.replace(".", "/"), filename), 'r') as file:
        return str(file.read()).split("\n")

def remove_empty_lines(data: list):
    return [d for d in data if len(d) != 0]