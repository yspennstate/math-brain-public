import json, time, itertools, hashlib
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); cases=checks=0
def ck(t):
    global checks
    checks+=1
    assert t, (cases,checks)
def fw(a):
    a=list(a); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):
                x,y=a[i],a[i+h]; a[i],a[i+h]=x+y,x-y
        h*=2
    return a
def tree_cells(ids):
    if len(ids)<=1:return []
    z=len(ids)//2
    return [sum(1<<i for i in ids)]+tree_cells(ids[:z])+tree_cells(ids[z:])
def cells(r,s,t,k):
    C=list(range(r));U=list(range(r,r+s));V=list(range(r+s,r+s+t));Y=list(range(r+s+t,r+s+t+k))
    tc=[] if r==1 else [sum(1<<i for i in C)]+tree_cells(C[1:])
    n=r+s+t+k
    return [(1<<n)-1,(1<<(r+s+t))-1,sum(1<<i for i in U+V)]+tc+tree_cells(U)+tree_cells(V)+tree_cells(Y)
def stats(a,cs):
    n=(len(a)-1).bit_length(); N=len(a); z=fw(a)
    G=F(sum(v*v*(1+2*sum(bool(j&c) for c in cs)) for j,v in enumerate(z)),N*N)
    inf=tuple(F(sum(a[j]!=a[j^(1<<i)] for j in range(N)),N) for i in range(n))
    var=1-F(sum(a)**2,N*N)
    return G,inf,var
def tab(m,k):return [1 if (m>>j)&1 else -1 for j in range(1<<k)]
def fixture(r,s,t,k,event,hp=None,hm=None,shared=None):
    global cases
    n=r+s+t+k;N=1<<n; z=r+s+t
    cs=cells(r,s,t,k); dc=event&((1<<r)-1);du=(event>>r)&((1<<s)-1);dv=(event>>(r+s))&((1<<t)-1)
    q=[];g=[]
    for j in range(N):
        active=(j&((1<<r)-1))==dc
        pa=((j>>r)&((1<<s)-1))==du
        pb=((j>>(r+s))&((1<<t)-1))==dv
        q.append(-1 if active and (pa!=pb) else 1)
        yy=j>>z
        g.append(shared[(j&((1<<r)-1))|(yy<<r)] if shared is not None else (hp if j&1 else hm)[yy])
    f=[x*y for x,y in zip(g,q)]
    Gg,ig,vg=stats(g,cs);Gq,iq,_=stats(q,cs);Gf,iff,_=stats(f,cs)
    a,b=F(1,1<<s),F(1,1<<t);p=a+b-2*a*b
    ck(p<=F(1,2));ck(Gf<=Gg+Gq-1);ck(Gq-1<=12*sum(iq))
    ck(sum(iq)<=sum(iff[:z]));ck(ig[z:]==iff[z:])
    for K in (1,3,12):
        coeff=max(F(12),(K+12*p)/(1-p))
        ck(K*sum(ig)+12*sum(iq)<=coeff*sum(iff))
    if shared is None:
        TY=tree_cells(list(range(k)))
        gp,ip,_=stats(hp,TY);gm,im,_=stats(hm,TY)
        B=(gp+gm)/2;J=(sum(ip)+sum(im))/2
        D=F(sum(x!=y for x,y in zip(hp,hm)),1<<k);d=0 if r==1 else 1
        ck(Gg==B+2*vg+2*(d+1)*D)
        ck(sum(ig)==J+D)
        ck(Gf<=B+2*sum(iff[z:])+(4*d+20)*sum(iff[:z]))
        ck(Gf<=B+2*sum(iff[z:])+max(F(12),F(2*d+4+12*p,1-p))*sum(iff[:z]))
    cases+=1
    if time.perf_counter()-start>55:raise RuntimeError('frozen wall guard')
for r,s,t,k in ((1,1,1,2),(2,1,1,2),(1,2,1,2),(1,1,2,2)):
    for event in range(1<<(r+s+t)):
        for m1,m2 in itertools.product(range(16),repeat=2):
            fixture(r,s,t,k,event,tab(m1,k),tab(m2,k))
for event in range(16):
    for m in range(256):fixture(2,1,1,1,event,shared=tab(m,3))
# Outside the source-independence hypothesis: A070 witness.
q=[-1 if (j&1) and bool(j&2)!=bool(j&4) else 1 for j in range(16)]
y=[1 if j&8 else -1 for j in range(16)]
g=[x*z for x,z in zip(q,y)];cs=cells(1,1,1,1)
Gq,iq,_=stats(q,cs);Gg,ig,_=stats(g,cs);Gf,iff,_=stats(y,cs)
RI=sum(ig)+sum(iq)-sum(iff);RT=Gg+Gq-1-Gf
ck((Gq-1,Gg,Gf,RI,RT)==(F(4),F(11,2),F(3),F(3),F(13,2)))
ck(RT-12*RI==F(-59,2));cases+=1
# Unequal non-flat majority and dictator terminals, on one common Y tree.
hp=[1 if j.bit_count()>=2 else -1 for j in range(8)];hm=[1 if j&1 else -1 for j in range(8)]
fixture(1,1,1,3,7,hp,hm)
gp,ip,_=stats(hp,tree_cells([0,1,2]));gm,im,_=stats(hm,tree_cells([0,1,2]))
ck(gp==F(9,2) and gm==3 and sum(ip)==F(3,2) and sum(im)==1)
spec=json.loads((R/'FROZEN_SPEC.json').read_text())
ck(cases==spec['case_count'])
result={'status':'PASS','cases':cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh and Fraction','memory_estimate_mb':32,'counterexample_signed_bank':str(RT-12*RI),'unequal_core_K':3,'spec_sha256':hashlib.sha256((R/'FROZEN_SPEC.json').read_bytes()).hexdigest()}
(R/'out').mkdir(exist_ok=True);(R/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
