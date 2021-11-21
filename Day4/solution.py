from utils import utils
import re

def main():
    data = utils.read_file(__package__, "input.txt")
    data = process_input(data)
    print(data)
    print(process_pt1(data))
    print(process_pt2(data))

REQUIRED_ATTRIBUTES={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_ATTRIBUTES=set("cid")
KEY_FUNCTIONS={
    "byr": lambda year: int(year) >= 1920 and int(year) <= 2002,
    "iyr": lambda year: int(year) >= 2010 and int(year) <= 2020,
    "eyr": lambda year: int(year) >= 2020 and int(year) <= 2030,
    "hgt": lambda height: check_height(height),
    "hcl": lambda colour: len(re.compile("^(#[0-9a-f]{6})$").findall(colour)) == 1,
    "ecl": lambda colour: len({colour} & {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) == 1,
    "pid": lambda number: len(number) == 9,
}

def check_height(height):
    height = re.compile("^([\d]+)([a-z]+)$").match(height)
    if height == None:
        return False
    height = height.groups()
    if len(height) != 2:
        return False
    if height[1] == "cm":
        return int(height[0]) >= 150 and int(height[0]) <= 193
    elif height[1] == "in":
        return int(height[0]) >= 59 and int(height[0]) <= 76
    else:
        return False

def process_pt1(data):
    count = 0
    for d in data:
        if set(d.keys()) & REQUIRED_ATTRIBUTES == REQUIRED_ATTRIBUTES:
            count += 1
    return count

def process_pt2(data):
    count = 0
    for d in data:
        if validate_person(d):
            count += 1
    return count

def process_input(data):
    people = []
    person = ''
    for i in range(len(data)):
        if data[i] == '' and person != '':
            attributes = person.split(" ")
            # print(attributes)
            person_dict = dict()
            for attribute in attributes:
                if attribute != "":
                    person_dict[attribute.split(":")[0]] = attribute.split(":")[1]
            people.append(person_dict)
            # print(person_dict)
            person = ''
        else:
            person += data[i]+" "
    return people
    
def validate_person(person):
    print(person)
    if not set(person.keys()) & REQUIRED_ATTRIBUTES == REQUIRED_ATTRIBUTES:
        return False
    for key in REQUIRED_ATTRIBUTES:
        print(key, KEY_FUNCTIONS[key](person[key]))
        if not KEY_FUNCTIONS[key](person[key]):
            return False
    return True

if __name__ == "__main__":
    main()