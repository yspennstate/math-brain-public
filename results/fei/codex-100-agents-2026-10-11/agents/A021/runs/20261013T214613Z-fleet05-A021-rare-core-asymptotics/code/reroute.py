"""Small-cube reproduction via rational h2 atoms, separate from prime-log helper."""
from check import Q,erasure,activate,restrict,union_table,influence
from itertools import permutations
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def ln(x):
    x=Q(x)
    if x<1:
        lo,hi=ln(1/x);return -hi,-lo
    e=0
    while x>=2:x/=2;e+=1
    def series(y):
        a=(y-1)/(y+1)
        lo=sum((2*a**(2*k+1)/(2*k+1) for k in range(16)),Q(0))
        return lo,lo+2*a**33/(33*(1-a*a))
    lo,hi=series(x);l2,u2=series(Q(2))
    return lo+e*l2,hi+e*u2

def classify(a,j):
    ap,am=restrict(a,j,1),restrict(a,j,0)
    fp,fm=activate(ap,(-1,1)),activate(am,(-1,1))
    ledger=erasure(fp,fm);lo=hi=Q(0)
    for r,mass in ledger.items():
        lr,ur=ln(r);ls,us=ln(1-r)
        lo+=mass*(-r*ur-(1-r)*us)
        hi+=mass*(-r*lr-(1-r)*ls)
    d=Q(sum(x!=y for x,y in zip(fp,fm)),len(fp))
    l2,u2=ln(Q(2));lo-=4*d*u2;hi-=4*d*l2
    assert lo>0 or hi<0 or not ledger
    sign=1 if lo>0 else -1 if hi<0 else 0
    return sign,d,lo,hi

def tree(a,order):
    if len(set(a))==1:return []
    j=order[0];sign,d,lo,hi=classify(a,j)
    new=tuple(x-(x>j) for x in order[1:])
    return [(sign,d)]+tree(tuple(restrict(a,j,0)),new)+tree(tuple(restrict(a,j,1)),new)

start=time.perf_counter();out=[]
for events in ((6,10,13),(6,11,12),(7,10,12)):
    a=union_table(events,4);roots=[];good=[]
    for j in range(4):
        sign,d,lo,hi=classify(a,j)
        roots.append({'coordinate':j,'sign_B_minus_4d':sign,'d':str(d),'ln2_scaled_gap_lower':str(lo),'ln2_scaled_gap_upper':str(hi)})
    for order in permutations(range(4)):
        nodes=tree(a,order)
        if all(s<=0 for s,d in nodes):good.append(order)
    assert roots[0]['sign_B_minus_4d']==1
    assert good
    p=Q(sum(a),16);J=influence([1-2*x for x in a])/2
    out.append({'events':events,'roots':roots,'all_24_orders_checked':True,'zero_bad_orders':good,'density':str(p),'controller_boundary':str(J),'F_influence_for_dictator_core':str(p+J)})
(ROOT/'out'/'reroute_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','critical_controllers':3,'orders_checked':72,'root_nodes_reproduced':12,'zero_bad_order_counts':[len(x['zero_bad_orders']) for x in out],'seconds':time.perf_counter()-start},indent=2))
