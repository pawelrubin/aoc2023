import re
import sys

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

digit = "|".join(digits.keys())


def parse_line(line: str) -> int:
    pattern = re.compile(rf"(\d|{digit})\w*(\d|{digit})|(\d|{digit})")

    if match := pattern.findall(line):
        d1, d2, d0 = map(lambda d: digits.get(d, d), match[0])
        return int(d0 + d0 if d0 else d1 + d2)

    raise ValueError(f"line {line} does not match regex {pattern}")


with open(sys.argv[1]) as input_file:
    print(sum(map(parse_line, input_file.readlines())))
