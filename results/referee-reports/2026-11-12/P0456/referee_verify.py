"""Final report consistency check against saved independent outputs."""
from pathlib import Path
import re

report=Path('REPORT.md').read_text()
assert report.splitlines()[0]=='Overall verdict: SOUND WITH GAPS'
results=['Theorem 1.1','Corollary 1.2','Lemma 2.1','Lemma 2.2','Lemma 2.3',
         'Proposition 3.1','Corollary 3.2','Proposition 3.3','Lemma 4.1','Lemma 4.2']
for name in results:
    assert f'## {name} — ' in report,name
print('All ten numbered results have verdict sections.')

def rows(text):
    answer={}
    for line in text.splitlines():
        if not line.startswith('| '):continue
        fields=[x.strip() for x in line.split('|')[1:-1]]
        if len(fields)==10 and fields[0].isdigit():
            answer[tuple(map(int,fields[:2]))]=fields
    return answer
a=rows(report);b=rows(Path('referee_tables.md').read_text())
assert a.keys()==b.keys() and len(a)==20
for key in a:
    for j,(x,y) in enumerate(zip(a[key],b[key])):
        if key==(50000,9) and j==6:
            assert x=='0/2500 successes';continue
        assert x==y,(key,j,x,y)
print('All 20 simulation rows match saved analysis (zero-success display corrected).')

lines=Path('referee_numeric.out').read_text().splitlines()
checked=0
for line in lines:
    if not line.startswith(('limiting ','finite ')):continue
    x=float(re.search(r'ratio=([0-9.]+)',line)[1])
    y=float(re.search(r'independent_scipy=([0-9.]+)',line)[1])
    assert abs(x-y)<2e-12,(line,x-y)
    checked+=1
assert checked==16
print('All 16 high-precision/scaled-SciPy integral pairs agree within 2e-12.')
for name in ['referee_numeric.py','referee_exact.py','referee_sim.c','referee_analyze.py',
             'referee_numeric.out','referee_exact.out','referee_analyze.out']:
    assert Path(name).is_file(),name
print('Programs and primary outputs exist. Final consistency checks passed.')
