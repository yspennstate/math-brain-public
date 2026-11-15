"""Bounded cubic-lattice slices; successes are exact, failures only periodic."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import json,time,itertools,resource
from fractions import Fraction as F
from periodic import search_phases,verify
ROOT=Path(__file__).resolve().parents[1]


def run():
 start=time.monotonic();rows=[];certs=[]
 outpath=ROOT/'data'/'exploration_3d.jsonl'
 outpath.write_text('')
 def test(family,label,A):
  r=search_phases(A,max_rounds=5000,max_phases=1024,max_sites=150000)
  cert=r.pop('certificate',None)
  if cert:
   r['independent_check']=verify(cert)
   certs.append({'family':family,'parameters':label,'certificate':cert})
  row={'family':family,'parameters':label,'A':[[str(v) for v in line] for line in A],**r}
  rows.append(row)
  with outpath.open('a') as f:f.write(json.dumps(row)+'\n')
  return row
 # Full diagonal lattice in [-1,1]^3, modulo coordinate permutations.
 for a,b,c in itertools.combinations_with_replacement([F(i,4) for i in range(-4,5)],3):
  A=[[a,0,0],[0,b,0],[0,0,c]]
  test('diagonal',[str(a),str(b),str(c)],A)
 print('diagonal completed',len(rows),flush=True)
 # A(t,s) = t I + s(e1 e2^T + e2 e1^T), including irrational-looking slopes only through rational samples.
 for t in [F(i,8) for i in range(-4,5)]:
  for s in [F(i,8) for i in range(9)]:
   test('isotropic_shear',[str(t),str(s)],[[t,s,0],[s,t,0],[0,0,t]])
 print('isotropic shear completed',len(rows),flush=True)
 # Lifted Ford matrix; vary a scalar identity direction in its 2x2 block and the third curvature.
 for delta in [F(i,8) for i in range(-2,3)]:
  for c in [F(i,8) for i in range(-4,5)]:
   test('ford_block',[str(delta),str(c)],[[F(1,4)+delta,F(1,2),0],[F(1,2),delta,0],[0,0,c]])
 print('Ford block completed',len(rows),flush=True)
 # Positive rank-one perturbations of the lifted Ford point.
 base=[[F(1,4),F(1,2),0],[F(1,2),F(0),0],[0,0,F(0)]]
 dirs=[v for v in itertools.product((-1,0,1),repeat=3) if any(v) and next(x for x in v if x)!=-1]
 for v in dirs:
  for eps in (F(1,4),F(1,8)):
   A=[[base[i][j]+eps*v[i]*v[j] for j in range(3)] for i in range(3)]
   test('ford_rank_one',{'direction':v,'epsilon':str(eps)},A)
 print('rank-one probes completed',len(rows),flush=True)
 (ROOT/'data'/'certificates_3d.json').write_text(json.dumps(certs))
 from collections import Counter
 summary={'tests':len(rows),'statuses':dict(Counter(r['status'] for r in rows)),
 'by_family':{family:dict(Counter(r['status'] for r in rows if r['family']==family)) for family in sorted({r['family'] for r in rows})},
 'seconds':time.monotonic()-start,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'largest_tested_period':max(r.get('N',0) for r in rows),'max_sites':max(r.get('sites',0) for r in rows),
 'note':'All positive certificates independently verified. Negative periodic results do not prove nonmembership in Gamma.'}
 (ROOT/'data'/'exploration_3d_summary.json').write_text(json.dumps(summary,indent=2));print(summary,flush=True)

if __name__=='__main__':run()
