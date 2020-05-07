#!/usr/bin/env python
import os
import re
import coloredlogs, logging


# Create a logger object.
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt='%(asctime)s,%(msecs)03d %(levelname)s %(message)s')


input_file = os.environ.get('ARG_INPUT_FILE', "/path/to/log.txt")
search_string = os.environ.get(r'ARG_SEARCH_STRING', r'Othello')

logger.info("Input file: {}".format(input_file))
logger.info("Search string: {}".format(search_string))

counter = 0 
with open(input_file) as fp:
    for line in fp:
        if re.search(search_string, line):
            counter += 1
            logger.debug("{} => {}".format(counter, line.strip()))

logger.info("searched for '{}' in file {}".format(search_string, input_file))  
logger.info("🎉 total lines found: {}".format(counter))  
print(counter)