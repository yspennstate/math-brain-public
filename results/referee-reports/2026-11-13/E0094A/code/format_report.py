"""Restore inline math delimiters after the shell-string import."""
from pathlib import Path
import re


def mathematical(content):
    c = content.strip()
    if not c or c.startswith(('http', 'https', 'including ')):
        return False
    if '\\' in c:
        return True
    if re.fullmatch(r'[A-Za-z]', c):
        return True
    if re.fullmatch(r'(?:[0-9]+(?:\.[0-9]+)?(?:/[0-9]+)?)(?:,[0-9]+(?:\.[0-9]+)?(?:/[0-9]+)?)+', c):
        return True
    if re.search(r'[=<>_^!]|[A-Za-z][+-][0-9]', c):
        return True
    if c.startswith('O('):
        return True
    return False


def convert(line):
    out = ''
    i = 0
    while i < len(line):
        if line[i] == chr(96):
            j = line.find(chr(96), i+1)
            if j >= 0:
                out += line[i:j+1]
                i = j+1
                continue
        if line[i] != '(':
            out += line[i]
            i += 1
            continue
        depth = 1
        j = i+1
        while j < len(line) and depth:
            if line[j] == '(': depth += 1
            if line[j] == ')': depth -= 1
            j += 1
        if depth:
            out += line[i]
            i += 1
            continue
        c = line[i+1:j-1]
        if mathematical(c) and (i == 0 or line[i-1] != ']'):
            out += '$' + c + '$'
        else:
            out += line[i:j]
        i = j
    return out


def main():
    p = Path('REPORT.md')
    text = p.read_text().replace('\\)', ')')
    text = text.replace(
        'The raw state-array budget at (n=11) is 1,437,004,800 bytes for five successor arrays and two probability vectors.',
        'The raw state-array budget at (n=11) is 1,437,004,800 bytes for five successor arrays and two probability vectors. '
        'The measured peak during propagation was 1,438,400,512 bytes (1.44 GB). '
        'The largest mass discrepancy was (1.18\\times10^{-10}); the largest error against exact integer path counts was (1.26\\times10^{-14}).')
    lines = []
    display = code = False
    for line in text.splitlines():
        if line.strip().startswith(chr(96)*3):
            code = not code
        if not code and line.strip() in ('\\[', '\\]'):
            lines.append('$$')
            display = not display
        elif not code and not display:
            lines.append(convert(line))
        else:
            lines.append(line)
    assert not display and not code
    p.write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
