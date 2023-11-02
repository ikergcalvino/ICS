#!/usr/bin/env python3
import sys

results = {}
for line in sys.stdin:
    line = line.strip()
    wine_type, attribute, value = line.split('\t')
    attribute = int(attribute)
    value = float(value)

    if wine_type in results:
        if attribute in results[wine_type]:
            results[wine_type][attribute].append(value)
        else:
            results[wine_type][attribute] = [value]
    else:
        results[wine_type] = {attribute: [value]}

for wine_type in results:
    for attribute in results[wine_type]:
        mean_value = sum(results[wine_type][attribute]) / \
            len(results[wine_type][attribute])
        print('%s\t%s\t%.4f' % (wine_type, attribute, mean_value))
