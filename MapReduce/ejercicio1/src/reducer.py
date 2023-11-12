#!/usr/bin/env python
import sys

current_station = None
station_t_max = -float('inf')
station_t_min = float('inf')

for line in sys.stdin:
    data = line.strip().split('\t')

    station, temp = data[0], float(data[1])

    if current_station != station and current_station is not None:
        print('%s\t%s\t%s' % (current_station, station_t_max, station_t_min))
        station_t_max = -float('inf')
        station_t_min = float('inf')

    current_station = station
    station_t_max = max(station_t_max, temp)
    station_t_min = min(station_t_min, temp)

if current_station is not None:
    print('%s\t%s\t%s' % (current_station, station_t_max, station_t_min))
