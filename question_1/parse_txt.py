#!/usr/bin/python2
"""
This module contains the `.txt` parser functions and its utility functions
"""
import re
import copy
from datetime import datetime
from sys import argv
from utils import reg_dict, flatten_dict


def txt_to_dict(text):
    """
    Uses regex matching to parse text to a `dict` object
    Args:
        `text`: `str` - text to be parsed
    """

    # text should have content
    if not text or not len(text) > 0:
        raise ValueError("`text` argument cannot be empty for" +
                         "`def txt_to_dict(text)`")

    output = copy.deepcopy(reg_dict)

    for key, val in reg_dict.items():
        # match patterns using regex
        if not isinstance(val, dict):
            output[key] = re.search(val, text).group(1).strip()\
                if re.search(val, text) else ""

        else:
            for sub_key, sub_val in val.items():
                output[key][sub_key] = re.search(sub_val, text)\
                    .group(1).strip() if re.search(sub_val, text) else ""

        # convert date to datetime
        if key == "date_of_birth":
            output[key] = ", ".join(output[key].split(","))
            output[key] = datetime.strptime(output[key], "%B %d, %Y")
        # convert age to integer
        elif key == "age":
            output[key] = int(output[key])
        # listify
        elif key in ["hobbies", "hobbies", "favorite_music", "favorite_movies",
                     "languages_spoken"]:
            output[key] = [w.strip() for w in output[key].split(",")]

    return flatten_dict(output)


def parser(filename):
    """Parses `.txt` files to a uni-level dict object
    filename: name/path of .txt file to be parsed
    """
    with open(filename, "r") as f:
        text = f.read()

    return txt_to_dict(text.replace("\r", ""))


# execute if module is run
if __name__ == "__main__":
    if len(argv) > 1:
        filename = argv[1]
        print(parser(filename))
    else:
        print("usage: {} [filename]".format(argv[0]))
