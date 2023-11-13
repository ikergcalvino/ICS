#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

type_key = None
key_value = None
count = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    type, key = data[0], data[1]

    if key_value != key and key_value is not None:
        print('%s\t%s\t%s' % (type_key, key_value, count))
        count = 0

    type_key = type
    key_value = key
    count += 1

if key_value is not None:
    print('%s\t%s\t%s' % (type_key, key_value, count))
