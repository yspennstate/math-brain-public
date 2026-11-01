from pathlib import Path
import json,numpy as np
p=Path(__file__).parent
rows=json.loads((p/'computations.json').read_text())
results=[]
# Each graph in this test is a Cayley graph of an abelian group or cube.
# Recover full K by translation of the computed fixed-start row.
for row in rows:
 name=row['graph'];n=row['n'];k=np.array(row['law'])
 if name.startswith('C') and not name.startswith('Circulant'):steps=[1];adj=[list({(x+1)%n,(x-1)%n}) for x in range(n)];K=np.array([np.roll(k,x) for x in range(n)])
 elif name.startswith('Circulant'):adj=[list({(x+s)%n for s in [1,-1,2,-2]}) for x in range(n)];K=np.array([np.roll(k,x) for x in range(n)])
 elif name=='cube3':adj=[[x^(1<<i) for i in range(3)] for x in range(n)];K=np.array([[k[x^y] for y in range(n)] for x in range(n)])
 else:continue
 P=np.zeros((n,n))
 for x,a in enumerate(adj):P[x,a]=1/len(a)
 Q=(np.eye(n)+P)/2;Qt=np.eye(n);bsum=0;tv=row['tv']
 for t in range(1,21):
  Qt=Qt@Q; b=np.sum(Qt*K.T,axis=1)
  invariant_error=float(np.ptp(b));bsum+=b[0]
  D=float(abs(Qt[0]-1/n).sum()/2)
  suffix=Qt[0]@K;suffixtv=float(abs(suffix-1/n).sum()/2)
  rec=dict(graph=name,t=t,b=float(b[0]),invariant_error=invariant_error,degree_bound=(1-2**(-t))/len(adj[0]),tv=tv,D=D,bsum=float(bsum),suffix_tv=suffixtv)
  assert invariant_error<1e-12
  assert b[0] <= rec['degree_bound']+1e-12
  assert tv <= D+bsum+1e-12
  assert suffixtv<=D+1e-12
  results.append(rec)
(p/'bound_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(len(results),'checks passed; max invariance error',max(r['invariant_error'] for r in results))
