import os
from timeit import timeit
import random

with open("digits.txt", "w") as file:
    while os.path.getsize("digits.txt") < 52_428_800:
        file.write(str(random.randint(1_000_000, 9_000_000)) + '\n')

func = """
with open("digits.txt", "r") as file:
    s = 0
    lines = file.readlines()
    for line in lines:
        if line.strip().isdigit():
            s += int(line.strip())
"""
print(timeit(func, number = 20) / 20)

func = """
with open("digits.txt", "r") as file:
    s = 0
    for line in file:
        if line.strip().isdigit():
            s += int(line.strip())
"""
print(timeit(func, number = 20) / 20)

func = """
with open("digits.txt", "r") as file:
    s = 0
    arr = (int(i.strip()) for i in file if i.strip().isdigit())
    s = sum(arr)
"""
print(timeit(func, number = 20) / 20)

# 3.7028363
# 3.2551579999999993
# 3.366413

