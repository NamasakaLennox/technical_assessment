#!/usr/bin/python2
"""A module that parses a .json file. The file contains a json formatted text
"""
from datetime import datetime
from json import load
from sys import argv
from utils import flatten_dict


def encode_text(data):
    """Encodes given input to 'ascii' format
    Args:
        data: a dictionary object parsed by json module
    Returns:
        encoded data
    """
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, list):
        return [encode_text(item) for item in data]
    elif isinstance(data, dict):
        return {encode_text(key): encode_text(value)
                for key, value in data.iteritems()}
    else:
        return data


def parser(filename):
    """accepts a json input file and parses the content into a dictionary
    Args:
        filename: string representing name of the file to be parsed
    Returns:
        returns a dictionary of the parsed items
    """
    # open the file as read only
    with open(filename, "r") as f_open:
        f_json = load(f_open)

    output = encode_text(f_json)["user"]

    # convert date to datetime instance
    output["date_of_birth"] = datetime.strptime(output["date_of_birth"],
                                       "%Y-%m-%d")
    # convert age to integer
    output["age"] = int(output["age"])

    return flatten_dict(output)

# execute if module is run
if __name__ == "__main__":
    if len(argv) > 1:
        filename = argv[1]
        print(parser(filename))
    else:
        print("usage: {} [filename]".format(argv[0]))
