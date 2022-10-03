import time
from threading import Thread, Lock

lock = Lock()
results = []


def measure(n):
    time.sleep(3) # симуляция задрежки
    result = 10 * n # симуляция реального измерения
    return n, result

def measure_wrapper(n):
    result = measure(n)
    # В этот блок кода не должно одновременно заходить нескольким рльлкам одновременно
    lock.acquire()
    # print(result)
    results.append(result)
    lock.release()

# Синхронный плох при заметной задержке
# for n in range(1, 10):
#     print(measure(n))


for n in range(1, 10):
    # thread = Thread(target=measure, args=(n, ))
    thread = Thread(target=measure_wrapper, args=(n,))
    thread.start()

counter = 0
while counter < 9:
    time.sleep(0.05)
    lock.acquire()
    counter = len(results)
    lock.release()

results.sort()
print(results)


