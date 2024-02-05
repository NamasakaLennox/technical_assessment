#!/usr/bin/python2
"""
Question 2
"""
import json
from sys import argv
from bs4 import BeautifulSoup


def parser(filename):
    """Extract cases from the given html page
    filename: `str` name/path of file to be parsed
    """
    return_list = []

    with open(filename, "r") as f:
        html_file = f.read()

    # general clean up
    html_file = html_file.replace(" =20 ", "").replace("=20 =20", "")
    html_file = html_file.replace("<=", "<").replace("=20", "")

    # soupify
    soup = BeautifulSoup(html_file, "html.parser")

    for el in soup.find_all(class_='3D"group"'):
        try:
            case_dict = {"categories": None,
                         "title": None,
                         "summary": None,
                         "meta": None
                         }
            # categories
            proceedings = el.find(attrs={
                "field--name-field-legal-library-record-types": True})
            cats = [a.text.replace("\r\n", "") for a in proceedings
                    .find_all("a")]
            cats = [a.strip("</a>") for a in cats]
            case_dict["categories"] = [a.encode("ascii", "ignore")
                                       for a in cats]

            # title
            title = el.find(class_='3D"node-title"').text
            case_dict["title"] = title.encode("ascii", "ignore")\
                .replace("\r\n", "")

            # summary
            summary = el.find(attrs={"field--type-text-with-summary": True})
            if summary:
                summary = summary.text
                summary = summary.replace("\r\n", "").replace("=", "")\
                    .replace("\n\n", "")
                case_dict["summary"] = summary.encode("ascii", "ignore")\
                    .strip("\n")
            else:
                case_dict["summary"] = ""
            # metas
            fields = el.find_all(class_='3D"field')
            metas = fields[2:]
            metas = {meta.find(class_='3D"field__label"').text:
                     meta.find(class_='3D"field__item"').text
                     for meta in metas
                     }
            metas = {key.encode("ascii", "ignore").strip():
                     val.encode("ascii", "ignore").strip()
                     for key, val in metas.items()
                     }
            case_dict["meta"] = metas

            return_list.append(case_dict)
        except Exception as e:
            return_list.append(case_dict)
            continue

    return return_list


# execute if module is run
if __name__ == "__main__":
    if len(argv) > 1:
        filename = argv[1]
        print(parser(filename))
    else:
        print("usage: {} [filename]".format(argv[0]))

