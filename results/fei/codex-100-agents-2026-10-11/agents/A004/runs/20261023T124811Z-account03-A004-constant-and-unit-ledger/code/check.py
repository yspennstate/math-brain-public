from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time,sys
import exact as e
RUN=Path(__file__).resolve().parents[1]
# Pure immutable rational/logarithmic computations; cache does not change any law.
for name in ('fw','logq','H','B'):
    setattr(e,name,lru_cache(None)(getattr(e,name)))
@lru_cache(None)
def loginterval(key):return e.bounds(dict(key))
def ck(x):e.ck(x)
def save(n,x):(RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def CE(p,q):
    ck(0<sum(q)<=1 and len(p)==len(q))
    ck(all(y>0 for x,y in zip(p,q) if x))
    return e.add(*[(-x,e.logq(y)) for x,y in zip(p,q) if x])
@lru_cache(None)
def KL(p,q):return e.add((1,CE(p,q)),(-1,e.H(p)))
def neg(v):return not v or loginterval(tuple(sorted(v.items())))[1]<=0
def nonneg(v):return not v or loginterval(tuple(sorted(v.items())))[0]>=0
def avg(a,b):return e.add((F(1,2),a),(F(1,2),b))
def refs(p,s):
    if len(p)==1 or p[0]==1:return [(tuple(s*x for x in p),)*2]*2
    a=1-p[0];N=len(p)-1
    uniform=tuple(F(1,N) for _ in range(N));shape=tuple(F(k,N*(N+1)//2) for k in range(1,N+1))
    tar=(s*p[0],)+tuple(s*a*x for x in shape)
    old=(s*p[0],)+tuple(s*(p[t]+a*uniform[t-1])/2 for t in range(1,len(p)))
    return [(tuple(s*x for x in p),tar),(old,tar)]
def inherit(v,q,j):
    p=e.spec(v);s=sum(q);m=e.marginal(p,j);r=e.marginal(q,j)
    vv=[e.restrict(v,j,b) for b in (0,1)];pp=[e.spec(w) for w in vv];raw=[];zz=[];qq=[]
    ck(all((pp[0][t]+pp[1][t])/2==m[t] for t in range(len(m))))
    for pb in pp:
        zraw=tuple(r[t]*pb[t]/m[t] if m[t] else r[t] for t in range(len(m)))
        z=sum(zraw);ck(z>0);raw.append(zraw);zz.append(z);qq.append(tuple(s*x/z for x in zraw))
        ck(sum(qq[-1])==s)
    ck(sum(zz)==2*s)
    rho=e.add((1,KL(p,q)),(-1,KL(m,r)))
    delta=e.add((1,e.H(p)),(-1,avg(e.H(pp[0]),e.H(pp[1]))))
    js=e.add((1,e.H(m)),(-1,avg(e.H(pp[0]),e.H(pp[1]))))
    ck(delta==e.add((1,e.B(p,j)),(1,js)))
    ck(nonneg(rho) and nonneg(js) and nonneg(delta))
    inc=e.add((1,delta),(1,avg(CE(pp[0],qq[0]),CE(pp[1],qq[1]))),(-1,CE(p,q)))
    predict=e.add((-1,rho),(F(1,2),e.logq(zz[0]/s)),(F(1,2),e.logq(zz[1]/s)))
    ck(inc==predict and neg(inc))
    return vv,pp,raw,zz,qq,inc

def querycheck(v,q0,q1,j,lam=F(1,4),deep=False):
    s=sum(q0);ck(sum(q1)==s and q0[0]==q1[0])
    q=tuple((1-lam)*x+lam*y for x,y in zip(q0,q1))
    aa=inherit(v,q0,j);bb=inherit(v,q1,j);mm=inherit(v,q,j)
    for b in (0,1):
        z0,z1,zm=aa[3][b],bb[3][b],mm[3][b]
        lp=lam*z1/zm
        ck(zm==(1-lam)*z0+lam*z1)
        ck(mm[2][b]==tuple((1-lam)*x+lam*y for x,y in zip(aa[2][b],bb[2][b])))
        ck(mm[4][b]==tuple((1-lp)*x+lp*y for x,y in zip(aa[4][b],bb[4][b])))
        ck((lp>=lam)==(z1>=z0))
        ck(all(x>=lp*y for x,y in zip(mm[4][b],bb[4][b])))
        if deep and len(aa[0][b])>1:
            # Second query: differing child vacuum masses are allowed by formula(2).
            cc0=inherit(aa[0][b],aa[4][b],0);cc1=inherit(bb[0][b],bb[4][b],0);ccm=inherit(mm[0][b],mm[4][b],0)
            for t in (0,1):
                L0=z0/s*cc0[3][t]/s;L1=z1/s*cc1[3][t]/s
                lhist=lam*L1/((1-lam)*L0+lam*L1)
                ck(lhist==lp*cc1[3][t]/ccm[3][t])
                ck(ccm[4][t]==tuple((1-lhist)*x+lhist*y for x,y in zip(cc0[4][t],cc1[4][t])))
    return aa,bb,mm

def tariff(v,q):
    p=e.spec(v);s=sum(q);tail=s-q[0];var=1-p[0];N=len(q)-1
    if not N or not tail:
        ck(var==0);return 0
    targets=[(F(1),)+(F(0),)*(N-1),tuple(F(k,N*(N+1)//2) for k in range(1,N+1))]
    for T in targets:
        fresh=(q[0],)+tuple(F(3,4)*q[t]+tail*T[t-1]/4 for t in range(1,len(q)))
        ck(sum(fresh)==s and fresh[0]==q[0])
        ck(all(x>=F(3,4)*y for x,y in zip(fresh[1:],q[1:])))
        ck(all(fresh[t]>=tail*T[t-1]/4 for t in range(1,len(q))))
        cost=e.add((1,CE(p,fresh)),(-1,CE(p,q)))
        bound=e.add((var,e.logq(F(4,3))),(-1,cost))
        ck(nonneg(bound))
        if not var:ck(cost=={})
    return len(targets)

@lru_cache(None)
def lift(g,state):
    ell=[2 if x==0 else 1 for x in state];out=[]
    for x in range(1<<sum(ell)):
        shift=idx=0
        for j,L in enumerate(ell):
            parity=((x>>shift)&((1<<L)-1)).bit_count()%2
            idx|=(parity^(state[j]==2))<<j;shift+=L
        out.append(g[idx])
    return tuple(out)
def blockcheck(g):
    n=len(g).bit_length()-1;p=e.spec(g);H=e.H(p)
    alpha=[sum(q for t,q in enumerate(p) if t>>j&1) for j in range(n)];J=sum(alpha,F(0));states=queries=0
    for state in product(range(3),repeat=n):
        v=lift(g,state);pv=e.spec(v);ell=[2 if s==0 else 1 for s in state];offset=[];pos=0;expect=[F(0)]*len(v)
        for L in ell:offset.append(pos);pos+=L
        for S,coef in enumerate(e.fw(g)):
            T=sgn=0
            for j,L in enumerate(ell):
                if S>>j&1:T|=((1<<L)-1)<<offset[j];sgn+=int(state[j]==2)
            expect[T]=coef*(-1)**sgn
        ck(e.fw(v)==tuple(expect));ck(e.H(pv)==H)
        current=sum(F(L)*a for L,a in zip(ell,alpha));ck(e.inf(v)==current)
        ck(current>=J)
        for j,L in enumerate(ell):
            if L!=2:continue
            for k in range(2):
                i=offset[j]+k;pm=e.marginal(pv,i);ck(e.B(pv,i)=={})
                for b in (0,1):
                    ns=list(state);ns[j]=1 if b==0 else 2;w=lift(g,tuple(ns))
                    ck(e.restrict(v,i,b)==w and e.spec(w)==pm)
                    ck(e.H(e.spec(w))==H and current-e.inf(w)==alpha[j])
                queries+=1
        states+=1
    return states,queries

def run(pilot):
    start=time.perf_counter();limit=55 if pilot else 180;maxn=2 if pilot else 3;tables=[];sourcequeries=tariffs=states=blocks=edits=0
    for n in range(maxn+1):
        for mask in range(1<<(1<<n)):
            v=tuple(1 if mask>>t&1 else -1 for t in range(1<<n));tables.append(v);p=e.spec(v)
            direct=tuple(F(sum(x*(-1)**((t&S).bit_count()) for t,x in enumerate(v)),len(v)) for S in range(len(v)))
            ck(e.fw(v)==direct);ck(e.inf(v)==sum(F(t.bit_count())*a for t,a in enumerate(p)))
            st,bq=blockcheck(v);states+=st;blocks+=bq
            for s in (F(1),F(1,2)):
                for q0,q1 in refs(p,s):
                    ck(CE(p,tuple(s*a for a in p))==e.add((1,e.H(p)),(-1,e.logq(s))))
                    ck(nonneg(e.add((1,CE(p,q0)),(-1,e.H(p)))))
                    tariffs+=tariff(v,q0)
                    for j in range(n):
                        querycheck(v,q0,q1,j,deep=(s==1 and q0==p));sourcequeries+=1
                        child=[e.restrict(v,j,b) for b in (0,1)]
                        ck(sum(1-e.spec(w)[0] for w in child)/2<=1-p[0])
            if n and e.inf(v):
                ff=list(v[t&((1<<n)-1)] for t in range(1<<(n+3)));ff[0]*=-1;ff=tuple(ff)
                ck(1-e.spec(ff)[0]<=F(9,8)*e.inf(v));ck(e.inf(v)>=F(2*n,1<<n));edits+=1
            ck(time.perf_counter()-start<limit)
    # Actual Boolean floor failure, BOTH children kept and complete ledger checked.
    v=tuple(1 if t==0 else -1 for t in range(8));q0=tuple(F(t,256) for t in (144,1,1,1,106,1,1,1));q1=tuple(F(t,256) for t in (144,80,15,13,1,1,1,1))
    aa,bb,mm=querycheck(v,q0,q1,0,deep=True)
    ck((aa[3][0],bb[3][0],mm[3][0])==(F(35,32),F(3,5),F(621,640)))
    lam=F(1,4)*bb[3][0]/mm[3][0];ratio=mm[4][0][1]/bb[4][0][1]
    ck(lam==F(32,207) and mm[4][0][1]==F(85,1242) and bb[4][0][1]/4==F(35,384))
    ck(ratio==F(272,1449) and ratio<F(1,4));ck(e.spec(mm[0][0])[1]==F(1,4))
    # Explicit entropy bank != remaining-influence bank endpoint.
    maj=tuple(1 if t.bit_count()<=1 else -1 for t in range(8));ck(e.H(e.spec(maj))==e.const(2) and e.inf(maj)==F(3,2))
    ck(2*e.inf(maj)-2==1 and e.inf(maj)-2==F(-1,2))
    ck(4**12<2**5*3**12)
    out={'status':'PASS','pilot':pilot,'seconds':time.perf_counter()-start,'assertions':e.COUNT,'boolean_tables':len(tables),'parity_block_states':states,'physical_deferral_queries':blocks,'source_query_cases':sourcequeries,'quarter_tariff_cases':tariffs,'point_edit_variance_cases':edits,'counterexample':{'truth':'1 only at index0; three bits, queried bit0','old_ref_numerators':[144,1,1,1,106,1,1,1],'target_ref_numerators':[144,80,15,13,1,1,1,1],'denominator':256,'parent_lambda':'1/4','active_child_lambda':str(lam),'actual_occupied_child_frequency':1,'child_actual_mass':'1/4','mixture_child_mass':'85/1242','quarter_target_child_mass':'35/384','ratio':str(ratio),'complete_full_entropy_ledger_increment':e.rec(mm[5]),'normalized_old_child':[str(t) for t in aa[4][0]],'normalized_target_child':[str(t) for t in bb[4][0]],'normalized_mixture_child':[str(t) for t in mm[4][0]]},'scope':'Exact finite checks plus written all-dimensional proof. No FEI proof and no source-price premise removed.'}
    save('PILOT.json' if pilot else 'CHECK.json',out)
    print(json.dumps({k:v for k,v in out.items() if k!='counterexample'}))
if __name__=='__main__':run('--pilot' in sys.argv)
