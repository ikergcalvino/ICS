#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        print('%s\t%s\t%.4f' % (wine, attribute, mean_value))
