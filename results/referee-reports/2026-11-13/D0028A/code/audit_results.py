#!/usr/bin/env python3
"""Independent hand-derived small cases plus artifact integrity checks."""
import hashlib
import json
import pathlib
from fractions import Fraction
R=pathlib.Path(__file__).resolve().parent.parent

def read(name): return json.loads((R/'data'/name).read_text())
# FA-2f on C4: the active fiber is exactly the seven independent occupied sets.
a=read('FA2_4_torus_q1-3.json')
e=next(e for e in a['extremal_stationary_measures'] if e['beta']==0)
assert e['states']==[0,1,2,4,5,8,10]
assert [Fraction(p) for p in e['probabilities']]==[Fraction(x,17) for x in [1,2,2,2,4,2,4]]
assert a['exact_kernel_dimension']==10 # nine blocked states plus this active class
assert a['nonproduct_examples'][0]['occupied_covariance']=='-36/289'
# East interval: choose the first vacancy; downstream occupations are arbitrary.
a=read('East_4_filled_q1-3.json')
assert a['exact_kernel_dimension']==5
assert sorted(len(e['states']) for e in a['extremal_stationary_measures'])==[1,1,2,4,8]
# FA-1f cycle: the only excluded active configuration is the all-occupied state.
a=read('FA1_4_torus_q1-3.json')
e=next(e for e in a['extremal_stationary_measures'] if e['beta']==0)
assert a['exact_kernel_dimension']==2 and len(e['states'])==15
assert sum(Fraction(p) for p in e['probabilities'])==1
# Source text integrity, independently recomputing every saved hash.
for p in (R/'sources').glob('*.metadata.json'):
    m=json.loads(p.read_text()); target=p.with_name(p.name.removesuffix('.metadata.json'))
    assert hashlib.sha256(target.read_bytes()).hexdigest()==m['text_sha256'],target
# Every archived extremal has exactly normalized nonnegative rational probabilities.
count=0
for p in (R/'data').glob('*_q*-*.json'):
    a=json.loads(p.read_text())
    for e in a['extremal_stationary_measures']:
        ps=list(map(Fraction,e['probabilities']))
        assert all(x>=0 for x in ps) and sum(ps)==1
    assert a['bp_fibers']==a['exact_kernel_dimension']==a['graph_components']
    assert a['exact_stationarity_residual']=='0'
    count+=1
assert (R/'REPORT.md').read_text().splitlines()[0]=='PARTIAL'
for p in R.rglob('*'):
    if p.is_file() and p.name not in {'codex.log'}:
        assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tiff','.tif','.gif','.webp'},p
        assert p.open('rb').read(4)!=b'%PDF',p
print(f'Independent audit passed: 3 hand-derived cases; {count} rational result artifacts; source hashes; PARTIAL first line; no PDF/image artifacts.')
