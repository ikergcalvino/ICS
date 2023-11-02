#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    user = line.split()[2]  # User is at index 2 in the log format
    url = line.split()[6]  # URL is at index 6 in the log format
    if url.endswith('.ps'):
        # Emit key-value pairs for Problem 1
        print('user\t%s' % user)
        # Emit key-value pairs for Problem 2
        print('url\t%s' % url)
