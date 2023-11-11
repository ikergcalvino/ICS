#!/usr/bin/env python3
import json

results = {}

with open('ejercicio3_output.txt') as file:

    for line in file:
        data = line.strip().split('\t')

        wine, attribute, mean_value = data[0], data[1], float(data[2])

        if wine not in results:
            results[wine] = {}

        results[wine][attribute] = mean_value

    print(json.dumps(results, sort_keys=True, indent=4))
