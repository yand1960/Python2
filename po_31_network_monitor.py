# Выдать список плохих хостов

import os

hosts = ["127.0.0.1", "192.168.1.250", "ya.ru", "tpr.tpr"]

os.system("CHCP 65001")

for host in hosts:
    command = f"ping {host}"
    os.system(command)
