"""Repair Markdown math delimiters and check saved report/artifact consistency."""
from pathlib import Path
import re

p = Path('REPORT.md')
txt = p.read_text()
txt = txt.replace('AM Section 2.4 at line 160', 'AM Section 2.5 at line 160')
assert not any(ord(c) < 32 and c not in '\n\t' for c in txt)

# The report's original inline delimiters were stripped by JavaScript string
# parsing. Identify their balanced outer parentheses, preserving prose ones.
plain_exceptions = {
    'the source the user supplied', 'distance two', 'theorem counter',
}


def is_math(s):
    if s in plain_exceptions:
        return False
    if '\\' in s or '_' in s:
        return True
    if any(z in s for z in ['=', '<', '>', '^']):
        return True
    if re.fullmatch(r'[A-Za-z0-9., +/()\-]+', s) and len(s.split()) <= 3:
        return (',' in s and any(c.isupper() for c in s)) or s in {'h>0', '1/h_n'}
    return False


def commands(s):
    for word in ['ell','sigma','chi','widehat','prod','log','sum','lambda','rho','pi',
                 'kappa','psi','delta','beta','eta','theta','epsilon']:
        s = re.sub(r'(?<![\\A-Za-z])'+word+r'(?![A-Za-z])', lambda m: '\\'+word, s)
    return s


lines, in_code, in_display = [], False, False
for line in txt.splitlines():
    if line.startswith('```'):
        in_code = not in_code
    if line.strip() == '\\[':
        in_display = True
    if not in_code and not in_display:
        spans, depth, start = [], 0, None
        for i,ch in enumerate(line):
            if ch == '(':
                if depth == 0:
                    start = i
                depth += 1
            elif ch == ')' and depth:
                depth -= 1
                if depth == 0 and is_math(line[start+1:i]):
                    spans.append((start,i))
        for start,end in reversed(spans):
            line = line[:start]+'$'+commands(line[start+1:end])+'$'+line[end+1:]
    lines.append(line)
    if line.strip() == '\\]':
        in_display = False
txt = '\n'.join(lines)+'\n'
p.write_text(txt)
assert txt.splitlines()[0] == 'Verdict: SOUND WITH GAPS'
assert 'AM Section 2.5 at line 160' in txt
for artifact in ['audit_exact.out','audit_symbolic.out','audit_data.out',
                 'audit_run_l1_s1_1e8.out','audit_run_l2_s1_1e8.out','audit_run_l3_s1_1e8.out']:
    assert Path(artifact).is_file()
for name in ['audit_exact','audit_symbolic','audit_data']:
    assert 'PASS' in Path(name+'.out').read_text()
print('Report first line, local artifacts, mathematical delimiters, AM section reference: checked')
