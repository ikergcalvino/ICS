#!/usr/bin/env python3
import sys

type_key = None
key_value = None
count = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    type, key = data[0], data[1]

    if key_value != key and key_value is not None:
        print(f'{type_key}\t{key_value}\t{count}')
        count = 0

    type_key = type
    key_value = key
    count += 1

if key_value is not None:
    print(f'{type_key}\t{key_value}\t{count}')
