#!/usr/bin/env python3
import sys

current_key = None
current_count = 0
max_user = None
max_url = None
max_user_count = 0
max_url_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    if current_key == key:
        current_count += 1
    else:
        if current_key:
            if key == 'user':
                if current_count > max_user_count:
                    max_user_count = current_count
                    max_user = current_key
            else:
                if current_count > max_url_count:
                    max_url_count = current_count
                    max_url = current_key
        current_key = key
        current_count = 1

if current_key:
    if current_key == 'user' and current_count > max_user_count:
        max_user_count = current_count
        max_user = current_key
    elif current_key == 'url' and current_count > max_url_count:
        max_url_count = current_count
        max_url = current_key

print("El usuario que accedió a más ficheros .ps es:",
      max_user, "Número de ficheros accedidos:", max_user_count)
print("La URL más visitada es:", max_url,
      "Número total de visitas:", max_url_count)
