#!/usr/bin/env python3
import os
import sys

filename = os.environ['mapreduce_map_input_file'].split('/')[-1]
wine = filename[filename.find('-') + 1: filename.find('.')]

attributes = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
              "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]

for line in sys.stdin:
    data = line.strip().split(';')

    if not data[0].startswith('"fixed acidity"'):
        for i, value in enumerate(data):
            print(f'{wine}\t{attributes[i]}\t{value}')
