#!/usr/bin/python2
"""
This module contains the `.pdf` parser function and its utility functions
"""
from sys import argv
from pypdf import PdfReader
from parse_txt import txt_to_dict


def parser(filename):
    """
    Parses pdf files to a uni-level dict object
    """
    with open(filename, "rb") as f:
        reader = PdfReader(f)
        text = ""
        for page_num in range(reader._get_num_pages()):
            page = reader.pages[page_num]
            text += page.extract_text(extraction_mode="layout",
                                      layout_mode_space_vertically=False)

        return txt_to_dict(text.replace("\r", ""))


# execute if module is run
if __name__ == "__main__":
    if len(argv) > 1:
        filename = argv[1]
        print(parser(filename))
    else:
        print("usage: {} [filename]".format(argv[0]))
