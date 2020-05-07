#!/usr/bin/env python


input_file="/path/to/log.txt"
search_string="Othello"


counter = 0 
with open(input_file) as fp:
    for line in fp:
        if search_string in line:
            counter += 1
            print("{} => {}".format(counter, line.strip()))

print("searched for '{}' in file {}".format(search_string, input_file))  
print("🎉 total lines found: {}".format(counter))  
print(counter)