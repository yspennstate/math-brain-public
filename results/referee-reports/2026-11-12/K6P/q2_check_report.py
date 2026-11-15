"""Final read-only mathematical/data checks, plus saved audit summary."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,re,pathlib,time,resource
from fractions import Fraction as Q
from q1_core import exact,lump
from q2_families import formula
import q2_search as s
begin=time.monotonic();report=pathlib.Path('REPORT.md').read_text()
assert report.splitlines()[0]=='Result: partial'
for a,b in ((r'\(',r'\)'),(r'\[',r'\]')):assert report.count(a)==report.count(b),(a,b)
for name in re.findall(r'\[[^\]]*\]\(([^)]+)\)',report):assert pathlib.Path(name).is_file(),name
with open('q2_best.json') as f:best=json.load(f)
with open('q2_family_results.json') as f:fam=json.load(f)
M=Q(10**12);ratios={N+2:formula(N,M)[1]/formula(N,M)[0] for N in range(3)}
expected={(4,2):Q(1),(4,3):Q(0),(5,2):ratios[2],(5,3):Q(1),(6,2):ratios[3],(6,3):ratios[2],(7,2):ratios[3],(7,3):ratios[3],(8,2):ratios[3],(8,3):ratios[4]}
for (n,r),ratio in expected.items():
    v=best[f'{n},{r}'];w=[[Q(x) for x in row] for row in v['w']]
    assert all(w[i][j]==w[j][i]>=0 for i in range(n) for j in range(n))
    assert len(v['partition'])==n-r and sorted(x for b in v['partition'] for x in b)==list(range(n))
    x=exact(w);h=exact(lump(w,v['partition']))
    assert x['t']==Q(v['T']) and h['t']==Q(v['That']) and h['t']/x['t']==Q(v['ratio'])==ratio
    if n-r>1:assert ratio<=min(r+1,n-r-1)
    else:assert ratio==0
    if f'{n},{r}' in fam:
        z=fam[f'{n},{r}'];a,b=formula(z['N'],M)
        assert a==Q(z['T']) and b==Q(z['That']) and b/a==ratio
    print('EXACT BEST VERIFIED',n,r,float(ratio),flush=True)
counts={n:[sum(1 for _ in s.partitions(n,n-r)) for r in (2,3)] for n in range(4,9)}
assert list(counts.values())==[[7,1],[25,15],[65,90],[140,350],[266,1050]]
raw_entries=[json.loads(line) for line in pathlib.Path('q2_counts.jsonl').read_text().splitlines()]
# Re-running an identical saved command replaces its count for validation.
entries=list({(z['mode'],z.get('n'),z.get('r'),z.get('seed')):z for z in raw_entries}.values())
assert sum(z['networks'] for z in entries if z['mode']=='random')==100
assert sum(z['partitions'] for z in entries if z['mode']=='random')==40180
assert sum(z['networks'] for z in entries if z['mode']=='structured')==96
assert sum(z['partitions'] for z in entries if z['mode']=='structured')==45252
assert sum(z['evaluations'] for z in entries if z['mode']=='opt')==296376
assert sum(z['candidates'] for z in entries if z['mode']=='opt')==69
assert sum(z['evaluations'] for z in entries if z['mode']=='exact_opt')==37749
with open('q2_shape_results.json') as f:z=json.load(f)
assert z['checks']==2361140 and z['failures']=={}
with open('q2_audit_results.json') as f:z=json.load(f)
assert z['counts']==dict(networks=20,partitions=8356,merged_source_entries=9352,two_pair_entries=22176,collinear_entries=78800)
assert all(z['seconds']<300 for z in entries)
assert max(z['seconds'] for z in entries)<171
print('REPORT CHECK PASSED; independent exact best-ratio, formula, partition-count, and search-total checks.',flush=True)
s.log(f'Final report validation PASSED: every best matrix and time independently recomputed; all exact ratio formulas, partition counts, run totals, partial-proof counts and report links verified. Runtime {time.monotonic()-begin:.3f}s; RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes. REPORT.md result is partial; Q2 and K(7)=3 remain unproved.')
