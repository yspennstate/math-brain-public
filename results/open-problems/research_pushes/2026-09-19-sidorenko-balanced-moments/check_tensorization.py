"""Exact test of tensor amplification with fixed one-copy parameters."""
from fractions import Fraction as F
from pathlib import Path
import json
from check_balanced_moments import value_bound, from_flow, traces
from itertools import product
W,p=from_flow([[0,1,1],[1,0,1],[1,1,0]])
n=3;pairs=list(product(range(n),repeat=2))
C={(i,j,k):sum(p[u]*W[u][i]*W[u][j]*W[u][k] for u in range(n)) for i,j,k in product(range(n),repeat=3)}
T=[[p[k]*C[i,j,k] if j==v else F(0) for v,k in pairs] for i,j in pairs]
ts=traces(T);beta=F(9,8);q=F(3,2)
assert ts=={2:F(81,32),3:F(567,256),4:F(4617,2048),5:F(37179,16384)}
records=[]
L1=value_bound(ts,beta,q/2)[0]
for m in range(1,7):
    tsm={j:t**m for j,t in ts.items()}
    L,b=value_bound(tsm,beta**m,q**m/2)
    assert L<=ts[5]**m
    records.append({'tensor_power':m,'bound_on_density_power':str(L),'b':str(b),'positive':L>0,'improves_on_single_copy':L>L1**m})
assert records[0]['positive'] and not records[4]['positive']
assert all(not r['improves_on_single_copy'] for r in records)
out={'status':'ALL_EXACT_CHECKS_PASS','fixed_beta':str(beta),'fixed_q':str(q),'records':records,'full_Sidorenko_proof':False,
     'scope':'Failure of monotone improvement for this fixed-parameter tensor test; adaptive choices not ruled out.'}
s=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('tensorization_checks.json').write_text(s);print(s,end='')
