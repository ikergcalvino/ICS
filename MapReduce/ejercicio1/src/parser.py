#!/usr/bin/env python

results = []

with open('/MapReduce/ejercicio1/output/ejercicio1_output.txt') as file:
    for line in file:
        station, station_t_max, station_t_min = line.strip().split('\t')
        results.append((station, float(station_t_max), float(station_t_min)))

max_temp = max(results, key=lambda x: x[1])[1]
min_temp = min(results, key=lambda x: x[2])[2]

max_stations = [station for station, temp_max,
                _ in results if temp_max == max_temp]

min_stations = [station for station, _,
                temp_min in results if temp_min == min_temp]

print('Temperatura máxima: %s en %s' % (max_temp, max_stations))
print('Temperatura mínima: %s en %s' % (min_temp, min_stations))
