"""Exact witnesses to proof shortcuts that cannot justify Q2."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,random
from fractions import Fraction as Q
from q1_core import exact,lump,serialize
from q2_families import k5
import q2_search as s
rng=random.Random(7112);bs=[[0,1],[2,3],[4],[5],[6]];out={}
for trial in range(100):
    w=[[Q(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):w[i][j]=w[j][i]=Q(rng.randint(1,9))
    x=exact(w);z=exact(lump(w,bs));F=x['F']
    for i in (4,5,6):
        for j in range(i+1,7):
            a=[F[i][1]-F[i][0],F[i][3]-F[i][2]];b=[F[j][1]-F[j][0],F[j][3]-F[j][2]]
            if a[0]*b[1]!=a[1]*b[0] and z['F'][i-2][j-2]>F[i][j]:
                out['nonparallel_singleton']=serialize(dict(w=w,partition=bs,i=i,j=j,beta_i=a,beta_j=b,F=F[i][j],Fhat=z['F'][i-2][j-2],T=x['t'],That=z['t']))
                break
        if out:break
    if out:break
assert out
w=k5(Q(10));x=exact(w);z=exact(lump(w,[[0],[1],[2,3]]))
kappa=-sum(p*x['F'][i][i] for i,p in enumerate(x['pi']));kh=-sum(p*z['F'][i][i] for i,p in enumerate(z['pi']))
assert z['t']>x['t']+kappa-kh
out['false_additive_trace_bound']=serialize(dict(t=10,T=x['t'],That=z['t'],trace_loss=kappa-kh,excess=z['t']-x['t']-(kappa-kh)))
with open('q2_obstacle_results.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
s.log('Exact obstacles saved: independent positive rank-two correction at two singleton states; and the tempting inequality T_hat <= T + (Kemeny(X)-Kemeny(quotient)) is false already for the supplied four-state family at t=10. These are not Q2 counterexamples.')
