#!/usr/bin/env python
# -*- coding: utf-8 -*-

users, urls = [], []

with open('/MapReduce/ejercicio2/output/ejercicio2_output.txt') as file:
    for line in file:
        type, key, count = line.strip().split('\t')

        if type == 'user':
            users.append((key, int(count)))
        elif type == 'url':
            urls.append((key, int(count)))

user_count = max(users, key=lambda x: x[1])[1]
top_users = [key for key, count in users if count == user_count]

url_count = max(urls, key=lambda x: x[1])[1]
top_urls = [key for key, count in urls if count == url_count]

print('Usuarios que accedieron a más ficheros en formato .ps [%s veces]: %s' %
      (user_count, top_users))
print('URLs más visitadas [%s veces]: %s' % (url_count, top_urls))
