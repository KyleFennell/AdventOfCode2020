import os

def read_file(path, filename):
    with open(os.path.join(path, filename), 'r') as file:
        return str(file.read()).split("\n")