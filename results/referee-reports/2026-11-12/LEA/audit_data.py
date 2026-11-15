"""Check every manuscript table row against stored data; compare fresh runs."""
from pathlib import Path
from decimal import Decimal as D
import re

paper = Path('PAPER.tex').read_text()
rows = re.findall(r'^\s*(\d+)\s*&\s*(\d+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\\\\', paper, re.M)
max_delta = D(0)
max_residual = D(0)
for ell, seed, *vals in rows:
    lines = Path(f'data/run_l{ell}_s{seed}.txt').read_text().splitlines()
    last = lines[-1].split()
    assert last[0] == '100000000' and last[-1] == 'ok'
    assert [D(x) for x in vals] == [D(x) for x in last[1:5]]
    max_delta = max(max_delta, abs(D(vals[0])-D(vals[1])))
    if int(ell) >= 2:
        max_residual = max(max_residual, abs(D(vals[2])-D(vals[3])))
print(f'Table rows matching data: {len(rows)}/{len(rows)}; max |a-c|={max_delta}; max ell>=2 |h-target|={max_residual}')
for ell in [1,2,3]:
    for suffix in ['', '_1e8']:
        fresh = Path(f'audit_run_l{ell}_s1{suffix}.out').read_text().splitlines()
        stored = Path(f'data/run_l{ell}_s1.txt').read_text().splitlines()
        assert fresh == stored[:len(fresh)]
        print(f'Fresh ell={ell} seed=1 to n={fresh[-1].split()[0]}: every output line matches supplied data')
assert Path('audit_author_check.out').read_text() == Path('data/check_path_law_out.txt').read_text()
freeze = Path('audit_freeze_l2.out').read_text()+Path('audit_freeze_l3.out').read_text()
assert freeze == Path('data/freeze_out.txt').read_text()
print('Author exact-check output and both freeze outputs reproduce supplied files exactly')
lines = Path('data/run_l2_s1.txt').read_text().splitlines()
resids = [D(row.split()[3])-D(row.split()[4]) for row in lines[3:]]
print('ell=2 seed=1 residuals at 1e4,...,1e8:', ', '.join(map(str,resids)))
print('consecutive decade residual ratios:', ', '.join(str(resids[i+1]/resids[i]) for i in range(4)))
lines = Path('data/run_l1_s1.txt').read_text().splitlines()[3:]
hs = [D(row.split()[3]) for row in lines]
print('ell=1 seed=1 reciprocal increments from rounded data:', ', '.join(str(1/hs[i+1]-1/hs[i]) for i in range(4)))
a,c,h = [D(v) for v in lines[-1].split()[1:4]]
Q=a*(1-a)+c*(1-c)+h
print('ell=1 seed=1 final log(10)/Q:', D(10).ln()/Q)
print('ALL DATA CHECKS PASS')
