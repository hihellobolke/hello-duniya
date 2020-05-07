#!/usr/bin/env python
import os
import re
import coloredlogs, logging
import argparse
import fileinput
import json

def get_count(fp, search_string, logger):
    c = 0
    for line in fp:
        if re.search(search_string, line):
            c += 1
            logger.debug("{} => {}".format(c, line.strip()))
    return c


if __name__ == "__main__":

    # setup logging
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
    parser.add_argument("--json", action="store_true", default=False, help="output as json")
    args = parser.parse_args()

    # args
    input_file = args.input
    search_string = args.string

    # set loglevels
    logger.setLevel(logging.ERROR)
    if args.verbosity == 1:
        logger.setLevel(logging.INFO)
    if args.verbosity >= 2:
        print("setting to debug")
        logger.setLevel(logging.DEBUG)
        logger.debug("enabled debug")

    logger.info("Input file: {}".format(input_file))
    logger.info("Search string: {}".format(search_string))

    c = 0

    if input_file == "-":
        input_file = "stdin"
        with fileinput.input(files="-") as f:
            c = get_count(f, search_string, logger)
    else: 
        if os.path.exists(input_file) and os.path.isfile(input_file):
            with open(input_file) as f:
                c = get_count(f, search_string, logger)
        else:
            logger.error("file {} does not exist".format(input_file))
            exit(1)

    logger.info("searched for '{}' in file {}".format(search_string, input_file))  
    logger.info("🎉 total lines found: {}".format(c))
    result = {
        "filename": input_file,
        "search": search_string,
        "count": c
    }
    if args.json:
        print(json.dumps(result, indent=4, sort_keys=True))
    else:
        print(result["count"])
