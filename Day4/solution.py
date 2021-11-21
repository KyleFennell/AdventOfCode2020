from utils import utils

def main():
    data = utils.read_file(__package__, "input.txt")
    data = process_input(data)
    print(data)
    print(process_pt1(data))
    print(process_pt2(data))


def process_pt1(data):
    pass

def process_pt2(data):
    pass

def process_input(data):
    people = []
    person = ''
    for i in range(len(data)):
        if data[i] == '' and person != '':
            print(person)
            print(person.split(" "))
            print(map(lambda attribute: attribute.split(":"), person.split(" ")))
            person_dict = dict()
            people.append(person_dict)
            print(person_dict)
            person = ''
        else:
            person += data[i]+" "
    return people
    
if __name__ == "__main__":
    main()