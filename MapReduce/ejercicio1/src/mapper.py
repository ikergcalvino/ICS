#!/usr/bin/env python3
import os
import sys

HOT_THRESHOLD = 27.0
COLD_THRESHOLD = -1.0
UNKNOWN_DATA = -99.0

filename = os.environ['mapreduce_map_input_file'].split('/')[-1]
station = filename.split('-')[-1].split('.')[0]

for line in sys.stdin:
    data = line.strip().split()

    t_daily_max, t_daily_min = float(data[5]), float(data[6])

    if t_daily_max > HOT_THRESHOLD:
        print(f'{station}\t{t_daily_max}')

    if UNKNOWN_DATA < t_daily_min < COLD_THRESHOLD:
        print(f'{station}\t{t_daily_min}')
