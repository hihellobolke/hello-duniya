#!/usr/bin/env python
import os
import re
import coloredlogs, logging
import argparse

# Create a logger object.
if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger, fmt='%(asctime)s,%(msecs)03d %(levelname)s %(message)s')


    # get defaults from env
    input_file_env = os.environ.get('ARG_INPUT_FILE', "/path/to/log.txt")
    search_string_env = os.environ.get(r'ARG_SEARCH_STRING', r'Othello')


    # parse cmd line args
    parser = argparse.ArgumentParser(description='count occurence of a string in a file')
    parser.add_argument("-i","--input", default=input_file_env, nargs='?', help="file to search")
    parser.add_argument("string", default=search_string_env, nargs='?', const=search_string_env, help="string to search")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    args = parser.parse_args()

    # args
    input_file = args.input
    search_string = args.string

    # set loglevels
    logger.setLevel(logging.ERROR)
    if args.verbosity == 1:
        logger.setLevel(logging.INFO)
    if args.verbosity >= 2:
        logger.setLevel(logging.DEBUG)

    logger.info("Input file: {}".format(input_file))
    logger.info("Search string: {}".format(search_string))

    counter = 0 

    if not os.path.exists(input_file) or not os.path.isfile(input_file):
        logger.error("file {} does not exist".format(input_file))
        exit(1)

    with open(input_file) as fp:
        for line in fp:
            if re.search(search_string, line):
                counter += 1
                logger.debug("{} => {}".format(counter, line.strip()))

    logger.info("searched for '{}' in file {}".format(search_string, input_file))  
    logger.info("🎉 total lines found: {}".format(counter))  
    print(counter)
