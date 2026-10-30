import json,time
from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path
import check as c
BASE=Path(__file__).resolve().parents[1];start=time.monotonic()
tab=c.function(254)
@lru_cache(None)
def record(state):
    free,mask=c.restricted(tab,state)
    return c.rec(len(free),mask)
@lru_cache(None)
def solve(state,depth):
    lo,hi,inf,*_=record(state)
    best=(2*inf*c.PREC-hi,2*inf*c.PREC-lo,-1,R(inf))
    if depth:
        for i,v in enumerate(state):
            if v!=-1:continue
            t=list(state);t[i]=0;a=solve(tuple(t),depth-1);t[i]=1;b=solve(tuple(t),depth-1)
            cand=((a[0]+b[0])//2,(a[1]+b[1])//2,i,(a[3]+b[3])/2)
            if cand[1]<best[1] or (cand[1]==best[1] and cand[3]>best[3]):best=cand
    return best
leaves=[];nodes=[]
def walk(state,depth):
    i=solve(state,depth)[2]
    if i==-1:leaves.append(state);return
    nodes.append({'state':state,'coordinate':i})
    for b in range(2):
        s=list(state);s[i]=b;walk(tuple(s),depth-1)
walk((-1,)*6,4)
Hlo=R(0);Hhi=R(0);I=R(0)
for state in leaves:
    lo,hi,inf,*_=record(state);weight=R(1,2**sum(v!=-1 for v in state))
    Hlo+=weight*lo;Hhi+=weight*hi;I+=weight*inf
piI=3*c.DEN-I
ratio_lo=(6*c.UNIT-Hhi)/(piI*c.PREC);ratio_hi=(6*c.UNIT-Hlo)/(piI*c.PREC)
assert ratio_hi<2
result={'status':'PASS','max_depth':4,'internal_nodes':nodes,'leaves':leaves,
 'leaf_I_exact':str(I/c.DEN),'Pi_I_exact':str(piI/c.DEN),
 'ratio_interval':[str(ratio_lo),str(ratio_hi)],'display_only_ratio':float((ratio_lo+ratio_hi)/2),
 'strict_gain_lower':str(4-ratio_hi),'display_only_gain_lower':float(4-ratio_hi),
 'elapsed_seconds':time.monotonic()-start,
 'warning':'DP min-D2 certificate is not a certificate of optimum tree ratio; selected tree ratio is an attained upper bound'}
if (BASE/'out'/'depth4.json').exists() and not (BASE/'out'/'depth4_first.json').exists():
    (BASE/'out'/'depth4_first.json').write_bytes((BASE/'out'/'depth4.json').read_bytes())
(BASE/'out'/'depth4.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
