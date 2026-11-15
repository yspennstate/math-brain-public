"""Check the report and its recorded evidence, without repeating computations."""
from pathlib import Path
import json

report=Path('REPORT.md').read_text()
assert report.splitlines()[0]=='Overall verdict: SOUND'
assert not any(ord(c)<32 and c not in '\n\t' for c in report)
assert sum(line=='$$' for line in report.splitlines())%2==0
for name in ('Theorem 2.1','Lemma 2.2','Lemma 2.3','Lemma 2.4','Lemma 2.5',
             'Lemma 4.1','Theorem 4.2','Proposition 4.3','Theorem 5.1',
             'Proposition 6.1','Theorem 6.2','Proposition 7.1','Corollary 7.3'):
    assert '## '+name+' — SOUND' in report or '## '+name+' (' in report,name

numeric=json.load(open('referee_numeric.json'))
all_rows=[]
for n in (1000,10000,20000):
    rows=json.load(open(f'referee_sim_{n}.json'))
    assert len(rows)==6
    assert {r['r'] for r in rows}=={0,1,2,5}
    for row in rows:
        assert f"{row['n']},{row['k']}" in numeric
        assert row['reps']==(100000 if row['r'] else 20000)
        assert row['omission_bound']<6e-12
    all_rows+=rows
    assert Path(f'referee_samples_{n}.npz').is_file()
assert len(all_rows)==18

for n,total in ((4,720),(5,3628800)):
    s=Path(f'referee_enumerate_{n}.txt').read_text()
    assert f'total={total}' in s
    assert 'FAIL' not in s
    assert s.count('PASS')==n-2
for filename in ('referee_constants.txt','referee_exact.txt','referee_check_lemmas.txt',
                 'referee_numeric.txt','referee_validate.txt','referee_lean_audit.txt',
                 'referee_summary.txt'):
    assert Path(filename).stat().st_size>0
print('Report first line, result coverage, math delimiters, and control characters: PASS')
print('18 simulation rows, requested budgets, sample files, and omission bounds: PASS')
print('Both exhaustive enumerations and all supporting output files: PASS')
print('All checks use locally saved referee programs; no author code was imported.')
