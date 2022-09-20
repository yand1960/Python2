# 1. Импорт модулей по отношению к текущей
from module1.module11.po_28a_modules import foo, foo1
from module1.module12.po_28b_modules import Arith

import sys

# 2. Добавление PYTHONPATH в run-time
import sys
# sys.path.append("C:\\temp\\module01")

# 3. Добавить PYTHONPATH в качестве переменной окружения на уровне OS

# 4. File -> Setting -> Python Interpreter -> cog -> Show All -> Пятая кнопка -> +

# from module011.po_28a_modules import foo, foo1
# from module012.po_28b_modules import Arith

# 5. Относительный импорт
# Но это катит только в том случае, если написано внутри пакета:
# from  ..Python2.module1.module11.po_28a_modules import foo, foo1
# from  ..Python2.module1.module12.po_28b_modules import Arith
# так что работающий относительный импорт
# см. в файле module1/module11/po_28a_modules.py

print(foo, foo1(), Arith().plus(1, 2))

