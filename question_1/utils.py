#!/usr/bin/python2
"""Contains all the utilities for question 1
"""
import copy


reg_dict = {
    "name": r"Name:(.+)",
    "date_of_birth": r"Date\s?of\s?Birth:(.+)",
    "age": r"Age:(.+)",
    "gender": r"Gender:(.+)",
    "occupation": r"Job:(.+)",
    "place_of_work": r"Place\s?of\s?Work:(.+)",
    "education": r"Education\n(.+)",
    "location": {
        "country": r"Country:(.+)",
        "state": r"State:(.+)",
        "city": r"City:(.+)",
        "zip_code": r"Zip Code:(.+)"
    },
    "hobbies": r"Hobbies:(.+)",
    "favorite_music": r"Favorite Music:(.+)",
    "favorite_movies": r"Favorite Movies: (.+)",
    "languages_spoken": r"Languages\s+Spoken\n(.+)",
    "pet": {
        "type": r"Pet Type:(.+)",
        "name": r"Pet Type:[^\n]+\n+Name:\s*(.+)",
        "breed": r"Breed:(.+)",
    },
    "social_media": {
        "Facebook": r"Facebook:(.+)",
        "Instagram": r"Instagram:(.+)",
        "Twitter": r"Twitter:(.+)"
        }
}


def flatten_dict(return_dict):
    """
    Converts a dict to a one-level dict
    return_dict: `dict` to flatten
    """
    dict_copy = copy.deepcopy(return_dict)

    for key, val in return_dict.items():
        if not isinstance(val, dict):
            continue
        sub_dict = dict_copy.pop(key)
        for sub_key, sub_val in sub_dict.items():
            dict_copy["{}_{}".format(key, sub_key)] = sub_val

    return dict_copy
