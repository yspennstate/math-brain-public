from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def fw(v):
    v=list(v);h=1
    while h<len(v):
        for j in range(0,len(v),2*h):
            for i in range(j,j+h):
                a,b=v[i],v[i+h];v[i]=a+b;v[i+h]=a-b
        h*=2
    return v
def facts(f):
    N=len(f);n=N.bit_length()-1;den=N*N;ws=fw(f)
    corr=fw([x*x for x in ws])
    raw=[(den-x)//2 for x in corr];costs=[min(x,den-x) for x in raw]
    pn=[raw[1<<i] for i in range(n)]
    basis=[];sp={0}
    for v in sorted(range(1,N),key=lambda x:(costs[x],x)):
        if v not in sp:basis.append(v);sp|={s^v for s in list(sp)}
    ck(len(sp)==N)
    amin=sum(costs[v] for v in basis)
    # Reconstruct the actual Boolean affine transform, not just its law.
    new=[0]*N
    for s,a in enumerate(ws):
        lab=sum((((s&v).bit_count()%2)^(raw[v]*2>den))<<j for j,v in enumerate(basis))
        new[lab]=a
    vals=fw(new);ck(all(abs(x)==N for x in vals))
    ck(sorted(x*x for x in new)==sorted(x*x for x in ws))
    ck(sum(s.bit_count()*a*a for s,a in enumerate(new))==amin)
    return {'n':n,'den':den,'I':sum(pn),'pn':pn,'char':sum(min(x,den-x) for x in pn),'aff':amin,'basis':basis,'raw':raw,'costs':costs,'ws':ws}
# A052's fixed m=3 path address code, then two point-activation controls.
C=[0,1,3,6,12,24,48,32]
f=[]
for x in range(2048):
    data=x&63;addr=(x>>6)&7;controls=x>>9
    f.append((-1 if (data&C[addr]).bit_count()%2 else 1) if controls==0 else 1)
p=facts(f);N=len(f);n=11;den=p['den']
ck(Q(sum(f),N)==Q(25,32))
ck(all(4*x<=den for x in p['pn']))
for v in range(1,N):
    physical=sum(f[x]!=f[x^v] for x in range(N))
    ck(p['raw'][v]==physical*N)
    ck(p['costs'][v]>=max(p['pn'][j] for j in range(n) if v>>j&1))
    assert time.perf_counter()-start<55
ck(p['aff']==p['I'])
rows=[];tr=Q(0);ar=Q(0)
for i in range(n):
    for b in [0,1]:
        child=[]
        for y in range(1024):
            x=(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i)
            child.append(f[x])
        c=facts(child);ck(c['char']==c['I'])
        if i in [2,3]:
            ck(sorted(Q(x*x,den) for x in p['ws'] if x)==sorted(Q(x*x,c['den']) for x in c['ws'] if x))
            ck(Q(c['I'],c['den'])==Q(p['I'],den)-Q(1,16))
        for j,v in enumerate(c['basis']):
            mismatch=sum(child[x]!=child[x^v] for x in range(1024))
            ck(c['raw'][v]==mismatch*1024)
        gain=Q(c['I']-c['aff'],2*c['den']);ar+=gain
        tr+=Q(c['I']-c['char'],2*c['den'])
        rows.append({'i':i,'b':b,'I':str(Q(c['I'],c['den'])),'D_char':str(Q(c['char'],c['den'])),'I_affine_min':str(Q(c['aff'],c['den'])),'weighted_release':str(gain),'basis':c['basis']})
ck(tr==0);ck(ar>0)
# Full affine spectral rank from nonzero labels; 0 occurs in the support.
ck(p['ws'][0]!=0);sp={0}
for s,a in enumerate(p['ws']):
    if a and s not in sp:sp|={x^s for x in list(sp)}
ck(len(sp)==2048)
out={'status':'PASS','n':11,'family':'fixed A052 m3 path code with k2 point activation; no dimension sweep','assertions':checks,'mean':'25/32','I':str(Q(p['I'],den)),'p':[str(Q(x,den)) for x in p['pn']],'affine_minimal':True,'full_affine_span':True,'character_child_release':str(tr),'full_affine_child_release':str(ar),'children':rows,'scope':'actual weak affine-minimal root; no criticality or FEI counterexample asserted','seconds':time.perf_counter()-start}
(R/'out/PATH_CHILD.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='children'}))
