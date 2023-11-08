#!/usr/bin/env python3
import sys

current_key = None
count = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    key, value = data[0], data[1]

    if current_key != key and current_key is not None:
        print(f'{current_key}\t{count}')
        count = 0

    count += 1

if current_key is not None:
    print(f'{current_key}\t{count}')
