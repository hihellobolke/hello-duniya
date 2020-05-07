#!/bin/bash

set -x
exec curl 'http://127.0.0.1:5000/' \
    -X 'POST' \
    -F "search=${1:-Othello}" \
    -F "log=@${2:-/path/to/log.txt}"
