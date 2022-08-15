# Add values in a multivalue dictionary
import re
import sys

def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def count_values_for_key(sample_dict):
    for key in sample_dict:
        print(key + " : ", len(sample_dict[key]))


input_file_name = sys.argv[1]
dict = {}

with open(input_file_name, "rt") as input_file:
     for line in input_file:
         values = line.split
         add_values_in_dict(dict, values[0], {values[1]})

count_values_for_key(dict)