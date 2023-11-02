#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    if current_key == key:
        current_count += 1
    else:
        if current_key:
            print('%s\t%s' % (current_key, current_count))
        current_key = key
        current_count = 1

if current_key:
    print('%s\t%s' % (current_key, current_count))
