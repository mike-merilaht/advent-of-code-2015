# Day 4: The Ideal Stocking Stuffer

import hashlib

input = """yzbqklnj"""


def run(key, leading):
    num = 0

    hash = ''

    while not hash.startswith('0'*leading):
        num += 1
        hash = hashlib.md5(f'{key}{num}'.encode()).hexdigest()

    return num


def run_part_2(key):
    pass


def tests_part_1():
    assert run("abcdef", 5) == 609043
    assert run("pqrstuv", 5) == 1048970


def tests_part_2():
    pass


if __name__ == "__main__":
    tests_part_1()
    print(f"Part 1: {run(input, 5)}")
    tests_part_2()
    print(f"Part 2: {run(input, 6)}")

