"""Restore inline TeX delimiters and audit the finished report/artifacts.

The initial write lost the backslashes of inline delimiters in its JS
string. This pass recognizes balanced outer parentheses in prose, while
preserving equation references, code, display math, and ordinary output
parentheticals. It is idempotent on the corrected document.
"""
from pathlib import Path
from fractions import Fraction as Q
import json, re

p=Path('REPORT.md'); src=p.read_text(); out=[]; display=False; code=False
for line in src.splitlines(keepends=True):
    if line.lstrip().startswith('```'):
        code=not code; out.append(line); continue
    if code: out.append(line); continue
    if line.strip()==r'\[': display=True
    if display:
        out.append(line)
        if line.strip()==r'\]': display=False
        continue
    dest=''; i=0
    while i<len(line):
        if line.startswith(r'\(',i):
            j=line.index(r'\)',i)+2; dest+=line[i:j]; i=j; continue
        if line[i]!='(':
            dest+=line[i]; i+=1; continue
        depth=1; j=i+1
        while j<len(line) and depth:
            if line[j]=='(': depth+=1
            elif line[j]==')': depth-=1
            j+=1
        assert depth==0, line
        content=line[i+1:j-1]
        if content.isdigit() or content.startswith('output '): dest+=line[i:j]
        else: dest+=r'\('+content+r'\)'
        i=j
    out.append(dest)
dst=''.join(out)
if dst!=src: p.write_text(dst)

assert dst.splitlines()[0]=='Result: proved'
assert dst.count(r'\[')==dst.count(r'\]')
assert dst.count(r'\(')==dst.count(r'\)')
assert r'\\)' not in dst and r'\\(' not in dst
for name in re.findall(r'`([A-Za-z0-9_]+\.(?:py|txt|json))`',dst):
    assert Path(name).is_file(), name
audit=json.loads(Path('audit_proof_results.json').read_text())
assert audit['counts']=={'networks':101,'merges':846,'entries':22392,'minimum_lemmas':12822}
for a in audit['family']:
    t=a['t']; T=Q(a['original']); Th=Q(a['quotient'])
    assert Q(a['ratio'])==Th/T<2
    W=t**6+2*t*t+2*t+2
    assert T==Q(t**7+t**6+2*t**5+2*t**4+2*t**3+t*t+4*t+2,W)
    assert Th==Q(2*t**7+4*t**3+2*t*t+4*t,W)
    assert format(float(Th/T),'.15g') in dst
assert Q(audit['family'][-1]['ratio'])>Q(1999997,1000000)
search=json.loads(Path('search_q1_results.json').read_text())
assert [x['n'] for x in search]==[3,4,5,6]
for a in search: assert Q(a['all_exact_merges'][0][0])<=2
structured=json.loads(Path('exact_and_structured_results.json').read_text())
assert structured['networks']==466 and structured['identity_entries']==9130
assert all(Q(x['ratio'])<=2 for x in structured['random_best']+structured['families'])
assert 'ALL CHECKS PASSED' in Path('audit_proof_output.txt').read_text()
print('REPORT CHECK PASSED: result line, TeX delimiters, artifact links, exact family, counts, search records.')
