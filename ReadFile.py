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

def find_probe_id_entity_id(str, probe_id_index):
    if (str[probe_id_index] != "{"):
        next_space_index = str.find(" ", probe_id_index);
        pid = str[probe_id_index:next_space_index]
        entity_start_index = str.find(entity_pattern)
        if (entity_start_index > 0):
            entity_id_index = entity_start_index + len(entity_pattern) + 1;
            if (str[entity_id_index] != "{"):
                next_space_index = str.find(" " , entity_id_index);
                eid = str[entity_id_index:next_space_index]
            else: eid = "{}"
    else:
        pid = "{}"
        eid = "{}"
    return [pid, eid]

def get_probe_to_enty_map(input_file):
    for line in input_file:
        probe_start_index = line.find(probe_pattern)
        if (probe_start_index > 0):
            probe_id_index = probe_start_index + len(probe_pattern) + 1
            [probe_id, entity_id] = find_probe_id_entity_id(line, probe_id_index)
            output_file.write(probe_id + " " + entity_id + "\n");
            if probe_id != "{}":
                add_values_in_dict(probe_entity_map, probe_id, {entity_id})
    return probe_entity_map

def extract_hourly_rollups(input_file):
    for line in input_file:
        rollups_index = line.find(rollups_pattern)
        if (rollups_index > 0):
            output_file.write(line[rollups_index:]);


input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
pattern = sys.argv[3]

probe_entity_map = {}
probe_pattern = "Could not find the probe metadata for probe"
entity_pattern = "needed by the following entity"
rollups_pattern = "Running hourly rollups for snapshot time"

with open(input_file_name, "rt") as input_file, open(output_file_name, "w") as output_file:
    #contents = input_file.read()
    #print(contents)
    if (pattern == "probe"):
        probe_entity_map = get_probe_to_enty_map(input_file)
    if (pattern == "rollups"):
        extract_hourly_rollups(input_file)
    
            


print(probe_entity_map.keys())
print(len(probe_entity_map.keys()))
count_values_for_key(probe_entity_map)

