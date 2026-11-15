"""Restore inline math delimiters in the report; leave prose parentheses alone."""
import re
from pathlib import Path

path = Path(__file__).with_name("REPORT.md")
lines = path.read_text().splitlines(keepends=True)
output = []
code = False
display = False
changes = 0
for line in lines:
    if line.startswith(chr(96)*3):
        code = not code
    if line.strip() == r"\[":
        display = True
    if code or display:
        output.append(line)
    else:
        result = []
        i = 0
        while i < len(line):
            if line[i] == "$":
                end_math = line.find("$", i+1)
                if end_math != -1:
                    result.append(line[i:end_math+1])
                    i = end_math+1
                    continue
            if line[i] != "(":
                result.append(line[i])
                i += 1
                continue
            end = i+1
            depth = 1
            while end < len(line) and depth:
                if line[end] == "(":
                    depth += 1
                if line[end] == ")":
                    depth -= 1
                end += 1
            if depth:
                result.append(line[i:])
                break
            content = line[i+1:end-1]
            mathematical = (
                "\\" in content or
                len(content) == 1 or
                (re.fullmatch(r"[A-Za-z0-9_+\-*/=^.,<>{}()\[\]]+", content) is not None
                 and re.search(r"[_+\-*/=^.,<>{}0-9]", content) is not None)
            )
            if mathematical:
                result.append("$"+content+"$")
                changes += 1
            else:
                result.append(line[i:end])
            i = end
        output.append("".join(result))
    if line.strip() == r"\]":
        display = False
path.write_text("".join(output))
print(f"Restored {changes} inline math delimiters in REPORT.md")
