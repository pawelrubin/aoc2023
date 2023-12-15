import re
import sys


def parse_line(line: str) -> int:
    pattern = re.compile(r"(\d)\w*(\d)|(\d)")

    if match := pattern.findall(line):
        d1, d2, d0 = match[0]
        return int(d0 + d0 if d0 else d1 + d2)

    raise ValueError(f"line {line} does not match regex {pattern}")


with open(sys.argv[1]) as f:
    print(sum(map(parse_line, f.readlines())))
