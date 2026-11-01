from pathlib import Path
from fractions import Fraction as F
import json,time
RUN=Path(__file__).resolve().parents[1];spec=json.loads((RUN/'FORMULA_SPEC.json').read_text())
start=time.perf_counter();checks=0
def ck(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen formula limit')
def core(q):
    z=(q-1)/(q+1);p=z;r=F(0)
    for k in range(36):r+=2*p/(2*k+1);p*=z*z
    return r,r+2*p/(73*(1-z*z))
ln2lo,ln2hi=core(F(2));cache={}
def lg(q):
    if q in cache:return cache[q]
    original=q;k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    lo,hi=core(q);D=1<<90
    out=F(((k+lo/ln2hi)*D).__floor__(),D),F(((k+hi/ln2lo)*D).__ceil__(),D)
    cache[original]=out;return out
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,y):return x[0]*y,x[1]*y
def entropy(atoms):
    out=(F(0),F(0))
    for p,count in atoms:
        if p:out=add(out,mul(lg(1/p),p*count))
    return out
def conditional(groups):
    out=(F(0),F(0))
    for ps,count in groups:
        q=sum(ps,F(0))
        for p in ps:
            if p:out=add(out,mul(lg(q/p),p*count))
    return out
def display(x):return {'lower':str(x[0]),'upper':str(x[1]),'approx':float((x[0]+x[1])/2) if x[1]-x[0]<F(1,100000) else None,'wide_interval_only_sign_certified':x[1]-x[0]>=F(1,100000)}
records=[]
for m in spec['domain']:
    delta=F(1,1<<m);u=F(1,1<<(m//2));N={1:((1<<m)+(1<<(m//2)))//2,-1:((1<<m)-(1<<(m//2)))//2}
    atoms=[];zrows=[];private=[];zgroups=[];privategroups=[]
    for e1 in [1,-1]:
        for e2 in [1,-1]:
            count=N[e1]*N[e2]
            v0=delta*e1*e2-F(3,2)*delta*u*e1-F(1,2)*delta*u*e2+delta**2
            vz=delta*u*(e1+e2)/2-delta**2
            vw=vz;vzw=delta*u*(e1-e2)/2+delta**2
            coeff=[v0,vz,vw,vzw];ps=[v*v for v in coeff]
            atoms.extend((p,count) for p in ps)
            zrows.extend([(ps[0]+ps[1],count),(ps[2]+ps[3],count)])
            private.append((sum(ps,F(0)),count))
            zgroups.extend([(ps[:2],count),(ps[2:],count)])
            privategroups.append((ps,count))
    ck(sum(p*c for p,c in atoms)==1,'closed Parseval')
    dz=sum(p*c for k,(p,c) in enumerate(atoms) if k%4 in [1,3])
    dw=sum(p*c for k,(p,c) in enumerate(atoms) if k%4 in [2,3])
    E=sum(p*c for k,(p,c) in enumerate(atoms) if k%4==3)
    ck(dz==dw==delta,'two weak physical pivots')
    ck(E==delta*(1+delta)/2,'shared cross energy')
    hz=entropy(atoms);Bz=conditional(zgroups);Bblock=conditional(privategroups)
    childatoms=[];childrows=[];childgroups=[]
    for e in [1,-1]:
        p0=(u*e-delta)**2;p1=delta**2
        childatoms.extend([(p0,N[e]),(p1,N[e])]);childrows.append((p0+p1,N[e]))
        childgroups.append(([p0,p1],N[e]))
    Bw=conditional(childgroups)
    # Analytic bounds verified separately; no rounded sign is used.
    root_lower=delta*(1-delta)**2*(m-1)/2
    child_lower=delta*(m-1)
    ck(Bz[0]>=root_lower,'root linear-m lower bound')
    ck(Bw[0]>=child_lower,'descendant linear-m lower bound')
    if m>=12:
        ck(root_lower>4*delta,'K4 root analytically bad')
        ck(child_lower>4*delta,'K4 descendants analytically bad')
    I=m+(2*m+2)*delta;T=(4*m+1)*delta*(1+delta)
    CE=add((F(2*m),F(2*m)),Bblock)
    ck(T<=2*I,'complete boundary bill')
    ck(CE[1]<=3*I,'complete normalized reference')
    rec={'m':m,'delta':str(delta),'n':2+2*m,'truth_table_constructed':False,'I':str(I),'B_root_over_Inf':display(mul(Bz,1/delta)),'B_child_over_Inf':display(mul(Bw,1/delta)),'root_analytic_B_over_Inf_lower':str(root_lower/delta),'child_analytic_B_over_Inf_lower':str(child_lower/delta),'all_three_nodes_K4_bad':m>=12,'raw_bill':str(T),'raw_bill_over_I':str(T/I),'complete_reference_CE_over_I':display(mul(CE,1/I)),'H':display(hz)}
    records.append(rec)
    (RUN/'out/FORMULA_PARTIAL.json').write_text(json.dumps({'records':records},indent=2)+'\n')
result={'helper_version':spec['helper_version'],'cases':len(records),'assertions':checks,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'asymptotics_proved_in_REPORT':{'both_shared_Inf':'2^-m -> 0','root_B_over_Inf_lower':'(1-2^-m)^2(m-1)/2 -> infinity','child_B_over_Inf_lower':'m-1 -> infinity','raw_bill_over_I':'(4+1/m)2^-m(1+2^-m)/(1+(2+2/m)2^-m) -> 0','complete_reference_CE_over_I':'2 + O(1/m) -> 2'},'full_FEI':'OPEN'}
(RUN/'out/FORMULA_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['helper_version','cases','assertions','failures','elapsed_seconds']}))
