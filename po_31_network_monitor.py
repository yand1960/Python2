# Выдать список плохих хостов

import os


def host_is_valid(host: str) -> bool:
    command = f"ping {host}"
    result = os.popen(command).read().encode("windows-1251").decode("866")
    return result.find("TTL") > 0


def progress_bar(counter: int, max: int, scale=50):
    message = f"{counter} of {max} " + ("=" * int(scale * counter / max))
    print(f"\r{message}", end="")


if __name__ == "__main__" :

    hosts = ["127.0.0.1", "127.0.0.1","127.0.0.1","127.0.0.1",
             "127.0.0.1","127.0.0.1","127.0.0.1",
             "192.168.1.250", "ya.ru", "tpr.tpr"]
    print("Checking hosts...")
    counter = 1
    for host in hosts:
        # print(f"\r{counter} of {len(hosts)}", end="")
        progress_bar(counter, len(hosts), scale=len(hosts))
        counter += 1
        if not host_is_valid(host):
            print(f"\nHOST {host} IS BAD")

