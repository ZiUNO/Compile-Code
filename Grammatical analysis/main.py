# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Contact: github.com/ZiUNO/Compile-Code
* @Software: PyCharm
* @Time: 2018/10/14 14:30
"""

from lib.FFSet import FFSet
from lib.LL1 import LL1

# fileName = input("Grammar file name:")
from lib.LR1 import LR1

fileName = 'test.txt'
f = open("../src/" + fileName)
size = int(f.readline())  # 非终结符个数
ff_set = FFSet(size)
terminator = f.readline().strip().split(" ")  # 所有的终结符
ff_set.set_terminator(terminator)
for i in range(size):
    grammarLine = f.readline().strip()
    e = grammarLine.split("->")[0]
    expression = grammarLine.split("->")[1]
    ff_set.input_grammar(e, expression)
    if i == 0:
        ff_set.set_first_non_terminator(e)
    elif i == size - 1:
        ff_set.set_last_non_terminator(e)
f.close()
print("终结符：", ff_set.get_terminator_of_first())
print("文法:", ff_set.get_grammar())
print("First集:", ff_set.get_first())
print("Follow集:", ff_set.get_follow())
# grammarAnalysis = LL1(ff_set)
# print(grammarAnalysis.get_chart())
# # toCheck = input("输入语句（以$结尾）：")
# toCheck = '(d**d+(dd+*dd*d+dd($'
# process, message = grammarAnalysis.check(toCheck)
# print(process)
# print(message)
lr1 = LR1(ff_set)
print('items###################')
for item_index in range(len(lr1.get_items())):
    print(item_index, lr1.get_items()[item_index])
lr_map = lr1.get_lr_map()
print('lr map ~~~~~~~~~~~~~~~~')
for row_index in range(len(lr_map)):
    print(row_index, lr_map[row_index])
process, message = lr1.check('(d**d+(dd+*dd*d+dd($')
print(process)
print(message)
process, message = lr1.check('(d*d+(d+d)+d*d+d)$')
print(process)
print(message)
