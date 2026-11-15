#!/usr/bin/env python3
"""Final cross-checks of data, saved examples, sample regeneration, and folder contents."""
import csv,json,hashlib,os,resource,sys
from pathlib import Path
from collections import Counter
from matching import solve,SCALE,np
root=Path.cwd()
expected={(d,n):count for n,count in [(32,500),(64,500),(128,400),(256,400),(512,320),(1024,240),(2048,200)] for d in [2,3,4]}
with Path('data/samples.csv').open() as f:rows=list(csv.DictReader(f))
counts=Counter((int(r['d']),int(r['n'])) for r in rows)
assert counts==Counter(expected),dict(counts)
keys=[(int(r['d']),int(r['n']),int(r['sample'])) for r in rows]
assert len(keys)==len(set(keys))==sum(expected.values())
assert len({r['seed'] for r in rows})==len(rows)
assert all(int(r['certificate'])==0 and int(r['nice'])==10 and int(r['scale'])==SCALE for r in rows)
assert max(int(r['max_rss_bytes']) for r in rows)<4_000_000_000
example_checks=[]
for d,n in sorted(expected):
 r=next(r for r in rows if int(r['d'])==d and int(r['n'])==n and int(r['sample'])==0)
 x=np.random.default_rng(int(r['seed'])).random((n,d))
 assert hashlib.sha256(x.tobytes()).hexdigest()==r['point_sha256']
 c,q,p=solve(x)
 assert q==int(r['integer_cost']) and c==float(r['length'])
 z=np.load(f'data/example_d{d}_n{n}.npz')
 assert np.array_equal(x,z['points']) and np.array_equal(p,z['partners'])
 # Independently re-sum the actual matching edge lengths.
 j=np.arange(n);sel=j<p
 resummed=float(np.linalg.norm(x[sel]-x[p[sel]],axis=1).sum())
 assert abs(resummed-c)<1e-11
 example_checks.append({'d':d,'n':n,'integer_cost':q,'resummed_difference':abs(resummed-c)})
# Independent two-pass, plain-Python variance check against NumPy output.
with Path('data/summary.csv').open() as f:summaries=list(csv.DictReader(f))
for s in summaries:
 d,n=int(s['d']),int(s['n']);xs=[float(r['length']) for r in rows if int(r['d'])==d and int(r['n'])==n]
 mean=sum(xs)/len(xs);v=sum((x-mean)**2 for x in xs)/(len(xs)-1)
 assert abs(v-float(s['variance']))<1e-12
 assert int(s['samples'])==len(xs)
for p in root.rglob('*'):
 if p.is_file():
  assert p.suffix.lower() not in ['.pdf','.png','.jpg','.jpeg','.gif','.webp','.tif','.tiff','.ps','.eps'],p
  if p.parent.name=='sources':
   assert p.suffix=='.txt'
   b=p.read_bytes();b.decode('utf-8');assert b'\x00' not in b
  if p.suffix.lower() in ['.txt','.md','.py','.cpp','.h','.json','.csv','.log']:
   assert not p.read_bytes().startswith(b'%PDF'),p
assert Path('REPORT.md').read_text().splitlines()[0]=='PARTIAL'
checks={'samples':len(rows),'groups':len(counts),'all_counts_as_planned':True,'all_integer_certificates_zero':True,'all_sample_priorities':sorted({int(r['nice']) for r in rows}),'max_sample_rss_bytes':max(int(r['max_rss_bytes']) for r in rows),'example_checks':example_checks,'variance_cross_checks':len(summaries),'source_text_count':len(list(Path('sources').glob('*.txt'))),'no_pdfs_or_raster_images_in_workspace':True,'symbolic_exactness':'integer optimum certified; real distance rounding explicitly bounded and disclosed'}
Path('data/final_audit.json').write_text(json.dumps(checks,indent=2)+'\n')
manifest={}
for folder in ['sources','code','data']:
 for p in sorted(Path(folder).rglob('*')):
  if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts:
   manifest[str(p)]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
manifest['REPORT.md']={'sha256':hashlib.sha256(Path('REPORT.md').read_bytes()).hexdigest(),'bytes':Path('REPORT.md').stat().st_size}
Path('data/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(checks,indent=2))
