#!/usr/bin/env python3
import os
import sys

for line in sys.stdin:
    line = line.strip()
    if not line.startswith('"fixed acidity"'):
        attributes = line.split(';')
        wine_type = "white" if "winequality-white.csv" in os.environ['mapreduce_map_input_file'] else "red"
        for i, value in enumerate(attributes):
            print('%s\t%s\t%s' % (wine_type, i, value))
