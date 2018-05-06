import json
from fake_addresses import list_fake_dict
from pprint import pprint

file_name = "fake_adds.json"


def write_json(lfd):
    with open(file_name, "w") as out_file:
        json.dump(lfd, out_file)

def read_json():
    with open(file_name, "r") as in_file:
        data = json.load(in_file)
    for person in data:
        pprint(person)
        print()

def modify_json_file():
    with open(file_name) as in_file:
        data = json.load(in_file)
    for person in data:
        del person["phone"]
    with open(file_name, "w") as new_file:
        json.dump(data, new_file, indent=2)


if __name__ == '__main__':

    write_json(list_fake_dict)
    modify_json_file()
    read_json()

