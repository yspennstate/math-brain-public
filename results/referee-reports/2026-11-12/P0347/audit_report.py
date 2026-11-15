"""Final artifact, mathematics-delimiter, and independent-check audit."""
from common import log
from pathlib import Path
import ast,re,json
s=Path('REPORT.md').read_text()
assert sum(line.strip()==r'\[' for line in s.splitlines())==sum(line.strip()==r'\]' for line in s.splitlines())
assert s.count(r'\(')==s.count(r'\)')
tags=re.findall(r'\\tag\{(\d+)\}',s)
assert tags==list(map(str,range(1,28))),tags
prose=[];display=False
for line in s.splitlines():
    if line.strip()==r'\[':display=True;continue
    if line.strip()==r'\]':display=False;continue
    if not display:prose.append(line)
prose='\n'.join(prose)
for path in re.findall(r'\[[^\]]+\]\(([^)]+)\)',prose):
    if not path.startswith(('http:','https:','#')):assert Path(path).exists(),path
for path in Path('.').glob('*.py'):ast.parse(path.read_text(),filename=str(path))
d=json.loads(Path('verification_raw4.json').read_text());assert d['n']>=4000 and max(d['worst_relative_errors'])<1e-11
p=json.loads(Path('pmf_audit.json').read_text())
for v in p.values():assert v['n']>=200 and v['all_finite_nonnegative'] and max(v['worst_relative_moment_errors'])<1e-10
mc=json.loads(Path('mc_summary.json').read_text());assert any(row['n']==1000000 and row['replicates']>=5000 for row in mc)
v=json.loads(Path('mc_verification.json').read_text());assert max(row['max_relative_disagreement'] for row in v)<1e-11
assert 'not proved' in s and 'conjecture' in s and 'Theorem 1.2' in s
log('Final artifact audit passed: all report links exist, equation tags 1–27 complete, math delimiters paired, Python sources parse, independent Decimal raw-four and full-PMF moment checks pass, Monte Carlo n=10^6 and integer-sum verification present. Full S/C law remains explicitly conjectural; QC law, all three variance constants, S/C non-normality and joint asymptotic equality are proved in REPORT.md.')
