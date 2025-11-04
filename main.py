#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

resp = urllib.request.urlopen('https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt')
with open('servers.txt', 'w') as fout:
    for line in resp:
        line = line.decode('utf-8').strip()
        if not line.startswith('vless'):
            continue 
        fout.write(line + '\n')
