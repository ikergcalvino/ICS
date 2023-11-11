#!/usr/bin/env python3
import sys

results = {}

for line in sys.stdin:
    data = line.strip().split('\t')

    wine, attribute, value = data[0], data[1], float(data[2])

    if wine not in results:
        results[wine] = {}

    if attribute not in results[wine]:
        results[wine][attribute] = []

    results[wine][attribute].append(value)

for wine, attributes in results.items():
    for attribute, values in attributes.items():
        mean_value = sum(values) / len(values)
        print(f'{wine}\t{attribute}\t{mean_value:.4f}')
