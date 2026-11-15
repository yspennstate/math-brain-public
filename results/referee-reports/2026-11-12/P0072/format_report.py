"""Restore Markdown math delimiters in the referee report; preserve prose/code.

Run: python3 format_report.py > format_report.out
Idempotent: existing dollar-delimited mathematics is left alone.
"""
from pathlib import Path
import re

path = Path("REPORT.md")
text = path.read_text().replace(r"(r^*\)", "(r^*)")
count = 0
in_code = False
in_display = False
lines = []
for line in text.splitlines(keepends=True):
    if line.startswith("```"):
        in_code = not in_code
        lines.append(line)
        continue
    if line.strip() == r"\[":
        in_display = True
    if in_code or in_display or line.startswith("#"):
        lines.append(line)
        if line.strip() == r"\]":
            in_display = False
        continue
    parts = re.split(r"(`[^`]*`|\$[^$]*\$)", line)
    for j in range(0, len(parts), 2):
        source = parts[j]
        out = []
        i = 0
        while i < len(source):
            if source[i] != "(":
                out.append(source[i])
                i += 1
                continue
            depth = 1
            k = i+1
            while k < len(source) and depth:
                depth += (source[k] == "(") - (source[k] == ")")
                k += 1
            if depth:
                out.append(source[i:])
                break
            content = source[i+1:k-1]
            out.append("$" + content + "$")
            count += 1
            i = k
        parts[j] = "".join(out)
    lines.append("".join(parts))
result = "".join(lines).replace(chr(92) + "$", "$")
assert result.startswith("Overall verdict: SOUND\n")
assert result.count(r"\[") == result.count(r"\]")
assert result.count("```") % 2 == 0
assert r"\)" not in result
for line in result.splitlines():
    assert line.count("$") % 2 == 0, line
path.write_text(result)
print(f"Converted {count} inline mathematical expressions to dollar delimiters.")
print("Report structure and math delimiter checks PASS.")
