"""Compare the saved challenge and solution definitions; no Lean build."""
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parent


def strip_comments(text):
    # Lean block comments nest. Preserve newlines for readable failure locations.
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            if text[i] == '\n':
                out.append('\n')
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end == -1 else end
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError('unclosed block comment')
    return ''.join(out)


def definition_block(text):
    text = strip_comments(text)
    start = text.index('abbrev Spin := Bool')
    end = text.index('\nend DilutedSpinGlass', start)
    block = text[start:end]
    # The challenge additionally contains the theorem stub.
    block = block.split('\ntheorem mezard_parisi', 1)[0]
    return re.sub(r'\s+', ' ', block).strip()


def main():
    sources = ROOT / 'sources'
    model = (sources / 'Model.lean').read_text()
    challenge = (sources / 'Comparator-DilutedSpin.lean').read_text()
    a, b = definition_block(model), definition_block(challenge)
    if a != b:
        raise AssertionError('challenge and solution definition blocks differ')
    declarations = re.findall(r'^(?:noncomputable )?(?:abbrev|def|structure) (\w+)',
                              strip_comments(model), flags=re.M)
    print('MATCH: challenge and solution definition blocks (comments/whitespace removed)')
    print('Declarations:', ', '.join(declarations))
    print('Normalized SHA256:', hashlib.sha256(a.encode()).hexdigest())
    theorem = re.compile(r'theorem mezard_parisi.*?:= by', re.S)
    main_source = (sources / 'Main.lean').read_text()
    t1 = theorem.search(strip_comments(challenge)).group()
    t2 = theorem.search(strip_comments(main_source)).group()
    if re.sub(r'\s+', ' ', t1) != re.sub(r'\s+', ' ', t2):
        raise AssertionError('theorem headers differ')
    print('MATCH: challenge and solution theorem headers')
    print('This is a text comparison, not parsing, elaboration, or a kernel check.')


if __name__ == '__main__':
    main()
