#!/usr/bin/env python3
import os
import sys

filename = os.environ['mapreduce_map_input_file'].split('/')[-1]
user = filename.split('.')[0]

for line in sys.stdin:
    data = line.strip().split()

    url = data[3].strip('\"')

    if url.endswith('.ps'):
        print(f'user\t{user}')

    print(f'url\t{url}')
