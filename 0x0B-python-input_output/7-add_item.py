#!/usr/bin/python3
"""Scripts that adds all arguments and saves on a list
"""
import sys

save_to_json_file = __import__("5-save-to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = load_from_json_file("add_item.json")


for arg in argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
