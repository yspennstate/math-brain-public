"""Independent audit from the saved CSVs, without calling the solvers."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[k]='1'
import json,pathlib
import numpy as np
root=pathlib.Path(__file__).resolve().parents[1]
summary=json.loads((root/'data/grid_results.json').read_text())
logs=[json.loads(s) for s in (root/'data/grid_run.log').read_text().splitlines()]
assert logs==summary['results']
checks=[]
for res in (32,64,128):
 previous=None
 for n in (4,8,12,16):
  sites=np.loadtxt(root/'data'/f'grid_n{n}_r{res}.csv',delimiter=',',skiprows=1)
  c=np.loadtxt(root/'data'/f'centres_n{n}.csv',delimiter=',',skiprows=1)
  x=sites[:,0]; a=sites[:,1].astype(int); b=sites[:,2].astype(int)
  assert len(c)==n*(n+1)*(2*n+1)//3
  assert len(x)==2*(n+2)*res
  assert np.array_equal(a,b)
  assert np.all((a>=-1)&(a<len(c)))
  count=np.bincount(a[a>=0],minlength=len(c)); assert max(count)<=res
  # Independently recompute worst assigned distances and every blocking pair.
  capradius=[]
  for j in range(len(c)):
   assigned=x[a==j]
   capradius.append(np.inf if len(assigned)<res else max(abs(assigned-c[j])))
  capradius=np.array(capradius)
  current=np.where(a>=0,abs(x-c[np.maximum(a,0)]),np.inf)
  blockers=0
  for start in range(0,len(x),64):
   dist=abs(x[start:start+64,None]-c)
   blockers+=int(np.count_nonzero((dist<current[start:start+64,None])&(dist<capradius)))
  assert blockers==0
  core=a[abs(x)<=2]
  change=None if previous is None else int(np.count_nonzero(core!=previous)); previous=core.copy()
  row=dict(n=n,resolution=res,centres=len(c),sites=len(x),difference_cells=int(sum(a!=b)),
           blockers=blockers,core_change=change,sated=int(sum(count==res)),unclaimed=int(sum(a<0)))
  orig=next(z for z in summary['results'] if z['n']==n and z['h']==1/res)
  assert row['sated']==orig['sated_centres'] and row['unclaimed']==orig['unclaimed_cells']
  assert change==orig['core_change_from_previous_window']
  checks.append(row)
out={'passed':True,'method':'independent CSV reload, capacities and exhaustive blocking check','runs':checks}
(root/'data/audit_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'passed':True,'runs':len(checks),'max_centres':max(q['centres'] for q in checks),'max_sites':max(q['sites'] for q in checks)}))
