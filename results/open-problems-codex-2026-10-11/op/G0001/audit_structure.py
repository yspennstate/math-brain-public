from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
tree = json.loads((root / 'pinned_actual_tree.txt').read_text())
groups = {}
for item in tree['tree']:
    parent, _, name = item['path'].rpartition('/')
    groups.setdefault(parent, []).append((name, item))
checked = []
for directory, children in groups.items():
    ordered = sorted(children, key=lambda pair: (pair[0] + ('/' if pair[1]['type'] == 'tree' else '')).encode())
    raw = b''.join(format(int(item['mode'], 8), 'o').encode() + b' ' + name.encode() + b'\0' + bytes.fromhex(item['sha'])
                   for name, item in ordered)
    actual = hashlib.sha1(b'tree ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    expected = tree['sha'] if not directory else next(item['sha'] for item in tree['tree'] if item['path'] == directory)
    checked.append({'directory': directory or '.', 'actual': actual, 'expected': expected, 'matches': actual == expected})
(root / 'pinned_git_tree_checks.json').write_text(json.dumps(checked, indent=2), encoding='utf8')
print('Git tree objects reconstructed:', len(checked), 'all match:', all(c['matches'] for c in checked), flush=True)

def without_comments(source):
    output = []
    i, depth = 0, 0
    while i < len(source):
        if depth:
            if source.startswith('/-', i): depth += 1; i += 2
            elif source.startswith('-/', i): depth -= 1; i += 2
            else: i += 1
        elif source.startswith('/-', i): depth = 1; i += 2
        elif source.startswith('--', i):
            j = source.find('\n', i)
            i = len(source) if j < 0 else j
        elif source[i] == '"':
            j = i + 1
            while j < len(source):
                if source[j] == '\\': j += 2
                elif source[j] == '"': j += 1; break
                else: j += 1
            output.append(source[i:j]); i = j
        else: output.append(source[i]); i += 1
    if depth: raise ValueError('Unterminated Lean comment')
    return ''.join(output)

def vocabulary(source):
    return source.split('-- VOCABULARY-BEGIN', 1)[1].split('-- VOCABULARY-END', 1)[0]

challenge = (root / 'pinned_audit_challenge.txt').read_text()
basic = (root / 'pinned_audit_solution_basic.txt').read_text()
norm = lambda s: re.findall(r'\w+|[^\w\s]', without_comments(s), flags=re.UNICODE)
report = {}
try:
    report['vocabulary_byte_identical'] = vocabulary(challenge) == vocabulary(basic)
    report['vocabulary_token_identical'] = norm(vocabulary(challenge)) == norm(vocabulary(basic))
except Exception as exc:
    report['vocabulary_error'] = str(exc)
for key in ['pinned_audit_challenge', 'pinned_audit_solution_basic', 'pinned_audit_solution', 'pinned_final', 'pinned_assembly']:
    code = without_comments((root / (key + '.txt')).read_text())
    report[key] = {'sorry_tokens': len(re.findall(r'\bsorry\b', code)),
                   'axiom_declarations': len(re.findall(r'^\s*axiom\s+', code, re.M)),
                   'native_decide_tokens': len(re.findall(r'\bnative_decide\b', code))}
(root / 'pinned_structural_checks.json').write_text(json.dumps(report, indent=2), encoding='utf8')
print('STRUCTURAL REPORT', json.dumps(report, indent=2), flush=True)
for file in ['pinned_principal_receipt.txt', 'pinned_acceptance_receipt.txt', 'pinned_build_receipt.txt']:
    print('\nEXTERNAL RECEIPT', file, '\n', (root / file).read_text(), flush=True)
print('\nLOCAL LEAN LOG\n', (root / 'lean_check.log').read_text() if (root / 'lean_check.log').exists() else 'absent', flush=True)
