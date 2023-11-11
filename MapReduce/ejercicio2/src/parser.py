#!/usr/bin/env python3

users, urls = [], []

with open('ejercicio2_output.txt') as file:
    for line in file:
        type, key, count = line.strip().split('\t')

        if type == 'user':
            users.append((key, int(count)))
        elif type == 'url':
            urls.append((key, int(count)))

user_count = max(users, key=lambda x: x[1])[0]
top_users = [key for key, count in users if count == user_count]

url_count = max(urls, key=lambda x: x[1])[0]
top_urls = [key for key, count in urls if count == url_count]

print(f'Usuarios que accedieron a más ficheros en formato .ps [{user_count}]: {top_users}')
print(f'URLs más visitadas [{url_count}]: {top_urls}')
