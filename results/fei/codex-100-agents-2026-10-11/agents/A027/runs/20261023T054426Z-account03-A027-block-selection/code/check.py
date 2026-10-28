import exact as x
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;C=Q(21,4);N={};ROWS=[]
def ck(v,k):
    assert v,k
    N[k]=N.get(k,0)+1
    assert time.monotonic()-START<(60 if PILOT else 240),'runtime'
def add(*v):return x.add(*v)
def num(q):return {2:Q(q)} if q else {}
def log(q):return add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
@lru_cache(None)
def point(s):return (-1,)+(1,)*((1<<s)-1)
@lru_cache(None)
def G(s,d):return {} if not s else add((d,x.Hplus(point(s))),(1,x.R(Q(1,1<<s),d)))
@lru_cache(None)
def slope(s,t):
    if not s:return {}
    p=Q(1,1<<s);V=4*p*(1-p)
    return add((1,x.Hplus(point(s))),(4*(1-2*t),x.eta(p*p)),(2*(1-2*t)*V,num(1)),(-4*V*t,log(t)),(8*p*(1-2*p*t),log(1-2*p*t)),(-8*p*(1-2*t),log(1-2*t)))
def T(s,t,d):return add((1,G(s,t)),(d-t,slope(s,t)))
def U(s,t,d):return add((1,G(s,d)),(-1,T(s,t,d)))
def D(s,t,d):return add((1,num(2*C*s*Q(1,1<<s)*d)),(-1,T(s,t,d)))
def nonneg(e,k):ck(x.bounds(e)[0]>=0,k)
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in x.bounds(e)]}
def static(r,k):
    data=list(range(6));ctrl=list(range(6,6+r))
    return [data,ctrl+data,data[:1]+ctrl+data[1:],[z for j in range(6) for z in ([j]+([6+j] if j<r else []))],data[:2]+ctrl+data[2:],list(reversed(data))+ctrl][k]
def choose(fix,r,k,u):
    if k<6:
        return next((j for j in static(r,k) if j not in fix),None)
    data=[j for j in range(6) if j not in fix];ctrl=[j for j in range(6,6+r) if j not in fix]
    if k==7 and len(data)==1 and sum(fix.get(j,0) for j in range(6))%2:return None
    d=x.neg(x.restrict(u,tuple(sorted((j,b) for j,b in fix.items() if j<6))))
    trigger=[d>Q(1,4),sum(fix.get(j,0) for j in range(6))%2==1,(6-len(data))%2==0 and len(data)<6,not data][k-6]
    if ctrl and trigger:return ctrl[0]
    return data[0] if data else (ctrl[0] if ctrl else None)
def case(u,r,k):
    t=x.neg(u);p0=Q(1,1<<r);F=x.activate(u,point(r));m=len(u).bit_length()-1
    # Every declared family core has six bits; guard uses its own dedicated calculation below.
    leaves=[];bill={};Qc=Qd=Q(0);negative=0;controlnegative=0
    def walk(fix,w):
        nonlocal bill,Qc,Qd,negative,controlnegative
        ff=tuple(sorted(fix.items()));f=x.restrict(F,ff)
        v=x.restrict(u,tuple(sorted((j,b) for j,b in fix.items() if j<m)))
        s=r-sum(j in fix for j in range(m,m+r));p=Q(1,1<<s);d=x.neg(v)
        failed=any(fix.get(j,0)==1 for j in range(m,m+r))
        if failed:
            ck(set(f)=={1},'failed full terminal retained');leaves.append((w,True,s,v,f));return
        ck(f==x.activate(v,point(s)),'actual full physical restriction')
        ck(x.I(f)==p*x.I(v)+2*s*p*d,'full physical influence')
        ck(not add((1,x.H(f)),(-p,x.H(v)),(-1,G(s,d))),'full Fourier activation identity')
        nonneg(D(s,t,d),'all-bias tangent reserve')
        j=None if len(set(f))==1 else choose(fix,r,k,u)
        if j is None:
            full=add((1,num(C*x.I(f))),(-1,x.H(f)));core=add((1,num(C*x.I(v))),(-1,x.H(v)))
            ck(add((1,full),(1,U(s,t,d)))==add((p,core),(1,D(s,t,d))),'same FULL terminal surplus plus signed refund')
            nonneg(core,'fixture core terminal actually certified')
            nonneg(add((1,full),(1,U(s,t,d))),'combined full terminal liability paid')
            if x.bounds(U(s,t,d))[1]<0:
                negative+=1;nonneg(full,'negative endpoint paid by OWN surplus')
            leaves.append((w,False,s,v,f));return
        idx=j-sum(i<j for i in fix);q=x.inf(f,idx)
        if j>=m:
            a=add((1,T(s,t,d)),(Q(-1,2),T(s-1,t,d)))
            nonneg(add((1,num(C*q)),(-1,a)),'all-bias control tangent payment')
            Qc+=w*q;bill=add((1,bill),(w,a))
            rel=add((1,U(s,t,d)),(Q(-1,2),U(s-1,t,d)))
            if x.bounds(rel)[1]<0:controlnegative+=1
        else:Qd+=w*q
        for b in (0,1):
            child=dict(fix);child[j]=b;walk(child,w/2)
    walk({},Q(1))
    Hleaf=Hcore=B=term={};Ileaf=Icore=mass=Q(0)
    for w,failed,s,v,f in leaves:
        Hleaf=add((1,Hleaf),(w,x.H(f)));Ileaf+=w*x.I(f)
        if failed:continue
        p=Q(1,1<<s);pv=w*p/p0;mass+=pv
        Hcore=add((1,Hcore),(pv,x.H(v)));Icore+=pv*x.I(v)
        B=add((1,B),(w,U(s,t,x.neg(v))))
        term=add((1,term),(w,num(C*x.I(f))),(-w,x.H(f)),(w,U(s,t,x.neg(v))))
    ck(mass==1,'original input projected reaches')
    ck(Qd==p0*(x.I(u)-Icore),'projected physical queried influence')
    ck(x.I(F)==Qd+Qc+Ileaf,'complete physical influence partition')
    coredebit=add((1,num(C*(x.I(u)-Icore))),(-1,x.H(u)),(1,Hcore))
    nonneg(coredebit,'fixture actual projected decrement certified')
    error=add((1,x.H(F)),(-1,Hleaf),(-p0,x.H(u)),(p0,Hcore))
    ck(error==add((1,bill),(-1,B)),'signed frontier identity without endpoint band')
    surplus=add((1,num(C*x.I(F))),(-1,x.H(F)))
    ck(surplus==add((p0,coredebit),(1,num(C*Qc)),(-1,bill),(1,term)),'root surplus exact SAME account decomposition')
    nonneg(surplus,'fixture full rate certified')
    ROWS.append({'r':r,'policy':k,'root_bias':str(t),'leaves':len(leaves),'negative_terminal_refunds':negative,'negative_control_releases':controlnegative})
    for fn in [x.spectrum,x.H,x.inf,x.I,x.restrict,x.identity]:fn.cache_clear()

price=add((1,slope(1,Q(1,8))),(Q(1,6),log(Q(9,7))))
nonneg(add((1,num(C)),(-1,price)),'exact scalar unchanged rate21/4')
if not PILOT:
    for t in [Q(1,64),Q(1,16),Q(1,8),Q(9,64)]:
        for s in range(1,9):
            nonneg(add((-1,T(s,t,Q(0)))),'original tangent nonpositive intercept')
            nonneg(add((1,num(2*C*s*Q(1,1<<s))),(-1,slope(s,t))),'original tangent slope price')
            for j in range(17):
                d=Q(j,16);nonneg(D(s,t,d),'scalar all-endpoint reserve')
                a=add((1,T(s,t,d)),(Q(-1,2),T(s-1,t,d)))
                nonneg(add((1,num(2*C*Q(1,1<<s)*d)),(-1,a)),'scalar all-endpoint control')
sets=[[0],[0,1,2],[0,1,2,4],list(range(7)),list(range(8)),list(range(9))]
for z,S in enumerate(sets[:1] if PILOT else sets):
    u=tuple(-1 if (j&3)==0 and (j>>2) in S else 1 for j in range(64))
    for r in ([1] if PILOT else [1,2,3]):
        for k in range(10):case(u,r,k)
guard=add((1,num(C)),(1,U(1,Q(1,16),Q(1))))
nonneg(guard,'actual point4 own full terminal reserve')
nonneg(add((-1,U(1,Q(1,16),Q(1)))),'point4 negative refund genuinely exits old band')
result={'status':'PASS','policies':len(ROWS),'assertions':sum(N.values()),'counts':N,'elapsed_seconds':time.monotonic()-START,'negative_terminal_occurrences':sum(z['negative_terminal_refunds'] for z in ROWS),'negative_control_release_occurrences':sum(z['negative_control_releases'] for z in ROWS),'price_certificate':enc(price),'point4_paid_reserve':enc(guard),'rows':ROWS}
(RUN/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(dict,list))}))
