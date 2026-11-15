"""Normalize inline math delimiters in the report; preserve equation references."""
from pathlib import Path


def main():
    path = Path('REPORT.md')
    bs = chr(92)
    rows = []
    code = False
    display = False
    for line in path.read_text().splitlines(keepends=True):
        if line.startswith('```'):
            code = not code
            rows.append(line)
            continue
        if line.strip() == bs+'[':
            display = True
            rows.append(line)
            continue
        if line.strip() == bs+']':
            display = False
            rows.append(line)
            continue
        if code or display or line.startswith('Task:'):
            rows.append(line)
            continue
        line = line.replace(bs+')',')').replace(bs+'(','(')
        out = []
        i = 0
        dollar = False
        backtick = False
        while i < len(line):
            char = line[i]
            if char == '`' and not dollar:
                backtick = not backtick
            if char == '$' and not backtick:
                dollar = not dollar
            if char != '(' or dollar or backtick:
                out.append(char)
                i += 1
                continue
            j = i+1
            depth = 1
            while j < len(line) and depth:
                depth += (line[j]=='(')-(line[j]==')')
                j += 1
            assert depth == 0, line
            body = line[i+1:j-1]
            if body.isdigit():
                out.append(line[i:j])
            else:
                for raw in ('{3,4}','{0,3}','{z_k,y_k}','{z_N,c}'):
                    body = body.replace(raw,bs+'{'+raw[1:-1]+bs+'}')
                out.append('$'+body+'$')
            i = j
        rows.append(''.join(out))
    path.write_text(''.join(rows))


if __name__ == '__main__':
    main()
