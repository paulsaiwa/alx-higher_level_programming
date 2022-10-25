#!/usr/bin/python3
"""
Load from JSON
"""
import json
"""import JSON Module"""


def load_from_json_file(filename):
    """
    Load from Json and write to a file
    """

    with open(filename, 'r', encoding='utf8') as file:
        return json.load(file)
