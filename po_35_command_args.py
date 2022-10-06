import sys
from po_34_logging import logger

# print(sys.argv)

if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
else:
    logger.warning("Не заданы необходимые параметры")
    x = 0
    y = 0

z = x + y
print(f"{x}+{y}={z}")