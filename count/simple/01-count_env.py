#!/usr/bin/env python
import os
import re

input_file = os.environ.get('ARG_INPUT_FILE', "/path/to/log.txt")
search_string = os.environ.get('ARG_SEARCH_STRING', 'Othello')


counter = 0 
with open(input_file) as fp:
    for line in fp:
        if re.search(search_string, line):
            counter += 1
            print("{} => {}".format(counter, line.strip()))

print("searched for '{}' in file {}".format(search_string, input_file))  
print("🎉 total lines found: {}".format(counter))  
print(counter)
