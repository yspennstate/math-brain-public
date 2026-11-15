"""Audit saved results and compare to supplied data without running claim code."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import csv,json,math,hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np
from independent_integrals import noncollision

def rows(p):return list(csv.DictReader(open(p)))
ours=rows('data/independent_exact.csv'); claimed=rows('claim_files/data/exact_waiting.csv')
lookup={(int(r['n']),r['family'],float(r['alpha'])):r for r in ours}
gaps=[];rats=0
for r in claimed:
    key=(int(r['n']),r['family'],float(r['alpha']))
    if key not in lookup:continue
    s=lookup[key];gaps.append(abs(float(s['mean'])-float(r['matching_mean'])))
    if s['rational'] and r['exact_rational']:
        assert Fraction(s['rational'])==Fraction(r['exact_rational']);rats+=1
assert len(ours)==52 and max(gaps)<1e-9
raw_scaled=[]
rng=np.random.default_rng(192715)
for k in range(1,7):
    for rep in range(12):
        x=np.sort(rng.normal(size=k)); y=np.sort(rng.normal(size=k));t=.8
        a=np.exp(-.5*(y[None,:]-x[:,None])**2/t)/math.sqrt(2*math.pi*t)
        raw=np.linalg.det(a)/np.prod(np.diag(a))
        scaled=noncollision(x[None,:],y[None,:],np.array([t]))[0]
        raw_scaled.append(abs(raw-scaled))
assert max(raw_scaled)<1e-10
for r in rows('data/independent_constants.csv'):
    first=next(s for s in rows('data/independent_slabs.csv') if s['alpha']==r['alpha'] and s['m']=='0')
    assert abs(float(first['estimate'])-float(r['first_slab_reference']))<4*float(first['scramble_se'])
bounds=[]
for n in (100,200,500,1000,2000):
    a=math.floor(-math.sqrt(n));a+=(n-a)%2;a=-a
    bound=float(Fraction(n*(1<<n),a*math.comb(n,(n-a)//2)))
    bounds.append({'n':n,'drop':a,'exact_lower_bound_as_float':bound})
files=list(Path('sources').iterdir())
assert all(p.suffix=='.txt' for p in files)
for p in Path('.').rglob('*'):
    if p.is_file():
        assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tiff','.gif','.webp'},str(p)
        with p.open('rb') as f:assert f.read(5)!=b'%PDF-',str(p)
summary={
 'status':'PASS','nice':os.getpriority(os.PRIO_PROCESS,0),
 'exact_rows':len(ours),'rational_rows':sum(bool(r['rational']) for r in ours),
 'prefix_chain_checks':sum(bool(r['automaton_mean']) for r in ours),
 'max_matrix_residual':max(float(r['matrix_residual']) for r in ours),
 'max_prefix_matrix_difference':max(abs(float(r['mean'])-float(r['automaton_mean'])) for r in ours if r['automaton_mean']),
 'claim_common_rows':len(gaps),'claim_equal_rationals':rats,'max_claim_mean_difference':max(gaps),
 'max_scaled_raw_determinant_difference':max(raw_scaled),
 'source_table_exact_lower_bounds':bounds,'source_texts':len(files),
 'constants':rows('data/independent_constants.csv')}
Path('data/independent_validation.json').write_text(json.dumps(summary,indent=2)+'\n')
manifest={}
for folder in ('sources','code','data'):
 for p in sorted(Path(folder).rglob('*')):
  if p.is_file() and '__pycache__' not in str(p) and p.name!='independent_manifest.json':manifest[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
manifest['REPORT.md']=hashlib.sha256(Path('REPORT.md').read_bytes()).hexdigest()
Path('data/independent_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(summary,indent=2))
