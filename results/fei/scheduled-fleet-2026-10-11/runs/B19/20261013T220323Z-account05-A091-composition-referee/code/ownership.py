import check as c
from a091_math import Q
from pathlib import Path
import json,time
start=time.perf_counter();rows=[];count=0
def eq(a,b):
    global count
    assert a==b,(a,b);count+=1
def run(u,v,r,s,o):
    p=Q(1,1<<r);q=Q(1,1<<s);mu=Q(sum(u),len(u));mv=Q(sum(v),len(v));au=1-mu;av=1-mv
    t=c.shared(u,v,r,s,o);n=1+r+s+2
    ds=[Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
    if o==0:
        dx=(p*au+(1-p)*q*av)/2
        da=p*((1-q)*au+q*(1-mu*mv))/2;db=(1-p)*q*av/2
        correction=p*q*av*(r*mu-s-1)/2
    else:
        dx=(p*au+q*av-p*q*au*av)/2;da=p*au/2;db=q*av/2
        correction=-p*q*au*av/2
    eq(ds[0],dx)
    for z in ds[1:1+r]:eq(z,da)
    for z in ds[1+r:1+r+s]:eq(z,db)
    actual=sum(ds[:1+r+s]);nominal=(r+1)*p*au/2+(s+1)*q*av/2
    eq(actual,nominal+correction)
    P=c.S(t)
    eq(actual,sum(v for mask,v in enumerate(P) for i in range(1+r+s) if mask>>i&1))
    w1=p/2;w2=(1-p)*q/2 if o==0 else q/2
    eq(ds[-2],w1*c.m.inf(c.S(u)));eq(ds[-1],w2*c.m.inf(c.S(v)))
    rows.append({'u':u,'v':v,'widths':[r,s],'orientation':o,'exclusive_control_influence':str(actual),'nominal_independent_control_accounts':str(nominal),'signed_correction':str(correction),'per_coordinate_influences':[str(z) for z in ds],'terminal_weights':[str(w1),str(w2)]})
cores=[c.m.tab(mask,1) for mask in range(4)]
for u in cores:
    for v in cores:
        for r,s in [(1,1),(1,2),(2,1),(2,2)]:
            for o in [0,1]:run(u,v,r,s,o)
run((1,1),(-1,-1),4,1,0);run((-1,-1),(-1,-1),1,1,0)
output={'status':'PASS','cases':len(rows),'exact_assertions':count,'runtime_seconds':time.perf_counter()-start,'formula_scope':'All-dimension ownership identities proved in OVERLAP_INTERFACE.md; finite checks include both signs of correction. No overlapping-cap entropy payment is asserted.','rows':rows}
(c.ROOT/'out/OWNERSHIP.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({k:v for k,v in output.items() if k!='rows'}))
