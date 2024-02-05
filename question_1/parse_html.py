#!/usr/bin/python2
"""
This module contains the `.html` parser functions and its utility functions
"""
from sys import argv
from bs4 import BeautifulSoup
from parse_txt import txt_to_dict


def parser(filename):
    """
    Parses `html` files using bs4's Beautiful soup to a uni-level dict

    filename: `str` name/path of file to be parsed
    """
    text = ""

    with open(filename, "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    for p in soup.find_all(class_="section"):
        text += p.text.encode("ascii", "ingnore").decode('utf-8')

    return txt_to_dict(text.replace("\r", ""))


# execute if module is run
if __name__ == "__main__":
    if len(argv) > 1:
        filename = argv[1]
        print(parser(filename))
    else:
        print("usage: {} [filename]".format(argv[0]))