"""Independent exact phase/reference ledger. No campaign helper imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib
RUN=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
@lru_cache(None)
def factors(n):
    d=2; out=[]
    while d*d<=n:
        k=0
        while n%d==0: n//=d; k+=1
        if k: out.append((d,k))
        d+=1
    if n>1: out.append((n,1))
    return tuple(out)
def add(*terms):
    out={}
    for a,v in terms:
        for p,b in v.items(): out[p]=out.get(p,F(0))+a*b
    return {p:a for p,a in out.items() if a}
def logq(q):
    q=F(q); assert q>0
    return add((1,dict(factors(q.numerator))),(-1,dict(factors(q.denominator))))
def H(p): return add(*[(-q,logq(q)) for q in p if q])
def CE(p,r):
    assert len(p)==len(r) and sum(r)==1
    return add(*[(-q,logq(s)) for q,s in zip(p,r) if q])
def KL(p,r): return add((1,CE(p,r)),(-1,H(p)))
def const(q): return {2:F(q)} if q else {}
def lnunit(x):
    z=(x-1)/(x+1); total=F(0)
    for k in range(32): total+=2*z**(2*k+1)/(2*k+1)
    err=2*z**65/(65*(1-z*z))
    return total,total+err
LN2=lnunit(F(2)); GRID=1<<72
@lru_cache(None)
def logbounds(p):
    if p==2:return F(1),F(1)
    k=p.bit_length()-1; a,b=lnunit(F(p,1<<k))
    lo=F(k)+a/LN2[1]; hi=F(k)+b/LN2[0]
    return F((lo*GRID).__floor__(),GRID), F((hi*GRID).__ceil__(),GRID)
def bounds(v):
    lo=hi=F(0)
    for p,a in v.items():
        l,h=logbounds(p)
        lo+=a*(l if a>=0 else h); hi+=a*(h if a>=0 else l)
    return lo,hi
def rec(v):
    l,h=bounds(v)
    return {'prime_log_form':{str(p):str(a) for p,a in sorted(v.items())},'lower':str(l),'upper':str(h),'display_only':float((l+h)/2)}
def fw(v):
    w=list(v); step=1
    while step<len(w):
        for a in range(0,len(w),2*step):
            for b in range(a,a+step):
                x,y=w[b],w[b+step]; w[b],w[b+step]=x+y,x-y
        step*=2
    return tuple(F(x,len(v)) for x in w)
@lru_cache(None)
def spec(v): return tuple(a*a for a in fw(v))
def restrict(v,j,s): return tuple(x for t,x in enumerate(v) if ((t>>j)&1)==s)
def insert(t,j): return (t&((1<<j)-1))|((t>>j)<<(j+1))
def marginal(p,j): return tuple(p[insert(t,j)]+p[insert(t,j)|(1<<j)] for t in range(len(p)//2))
def B(p,j): return add((1,H(p)),(-1,H(marginal(p,j))))
def inf(v):
    return sum((F(sum(v[t]!=v[t^(1<<j)] for t in range(len(v))),len(v)) for j in range(len(v).bit_length()-1)),F(0))
def mix(r,t=F(1,8)): return tuple((1-t)*a+t/len(r) for a in r)
def node(v,r,j):
    p=spec(v); m=marginal(p,j); rm=marginal(r,j)
    vv=[restrict(v,j,s) for s in (0,1)]; pp=[spec(x) for x in vv]
    ck(all((pp[0][t]+pp[1][t])/2==m[t] for t in range(len(m))))
    for s in (0,1):
        a=fw(v); c=fw(vv[s])
        ck(all(c[t]==a[insert(t,j)]+(-1)**s*a[insert(t,j)|(1<<j)] for t in range(len(c))))
    conditional=add((1,KL(p,r)),(-1,KL(m,rm)))
    left=add((1,B(p,j)),*[(F(1,2),CE(q,rm)) for q in pp])
    ck(left==add((1,CE(p,r)),(-1,conditional)))
    ck(not conditional or bounds(conditional)[0]>=0)
    return vv,rm,conditional
def root_table():
    b=tuple(1 if y&7==0 else -1 for y in range(64)); c=list(b); c[0]=-1
    # Encoder occupies low three bits, data high six bits.
    f=tuple(b[y] if (3-2*x.bit_count())>0 else c[y] for y in range(64) for x in range(8))
    return b,tuple(c),f
def run(pilot):
    start=time.perf_counter(); b,c,v=root_table(); p=spec(v)
    ck(inf(b)==inf(c)==F(3,4)); ck(sum(p)==1)
    # Independent character-sum reconstruction, not a second FWHT call.
    direct=tuple(F(sum(z*(-1)**((s&t).bit_count()) for t,z in enumerate(v)),512) for s in range(512))
    ck(direct==fw(v)); ck(sum(F(s.bit_count())*q for s,q in enumerate(p))==inf(v))
    rootmargin=add((1,const(3)),(-1,H(p)))
    price=add((1,logq(F(8,7))))
    after=add((1,rootmargin),(-1,price))
    ck(bounds(rootmargin)[0]>F(555796,10**6)); ck(bounds(after)[0]>F(363150,10**6))
    # One actual weak dummy-data exposure: both full children are nonconstant.
    vv,rm,cost=node(v,p,6)
    q=mix(rm); ck(sum(q)==1 and min(q)>0 and len(set(q))>1)
    ck(all(len(set(w))==2 for w in vv))
    ck(all(qt>=F(7,8)*rt for qt,rt in zip(q,rm)))
    ratios=[(rt/qt,s) for s,(rt,qt) in enumerate(zip(rm,q)) if rt]
    maxratio,extreme=max(ratios)
    ck(maxratio<=F(8,7))
    for ratio,s in ratios:
        ck(ratio<=maxratio)
        atom=tuple(F(int(t==s)) for t in range(len(rm)))
        ck(add((1,CE(atom,q)),(-1,CE(atom,rm)))==logq(ratio))
    character=tuple((-1)**((extreme&t).bit_count()) for t in range(len(rm)))
    ck(spec(character)==tuple(F(int(t==extreme)) for t in range(len(rm))))
    reset=add(*[(F(1,2),add((1,CE(spec(w),q)),(-1,CE(spec(w),rm)))) for w in vv])
    ck(bounds(add((1,price),(-1,reset)))[0]>0)
    firstbill=add((1,B(p,6)),*[(F(1,2),CE(spec(w),q)) for w in vv])
    ck(firstbill==add((1,H(p)),(1,reset)))
    ck(bounds(add((1,const(3)),(-1,firstbill)))[0]>0)
    fixtures=[]
    for n in range(0,2 if pilot else 4):
        for mask in range(1<<(1<<n)):
            w=tuple(1 if mask>>t&1 else -1 for t in range(1<<n)); pw=spec(w)
            r=mix(pw); ck(sum(pw)==sum(r)==1)
            for j in range(n):
                children,rchild,cond=node(w,r,j)
                ck(inf(w)==sum(pw[t] for t in range(len(w)) if t>>j&1)+(inf(children[0])+inf(children[1]))/2)
                rn=mix(rchild)
                e=add(*[(F(1,2),add((1,CE(spec(a),rn)),(-1,CE(spec(a),rchild)))) for a in children])
                upper=add((1,price),(-1,e))
                ck(bounds(upper)[0]>0)
                fixtures.append((n,mask,j))
            ck(time.perf_counter()-start<55)
    # Reverse dominance is not enough: an actual dictator spectrum and a
    # normalized reference with half of its unique occupied atom removed.
    dictator=(1,-1); pd=spec(dictator); bad=(F(1,2),F(1,2))
    ck(bounds(KL(pd,bad))[0]==1)
    ck(bounds(price)[1]<1)
    out={'status':'PASS','pilot':pilot,'assertions':COUNT,'seconds':time.perf_counter()-start,'local_query_cases':len(fixtures),'fixture_hash':hashlib.sha256(bytes(1 if a==1 else 0 for a in v)).hexdigest(),'H_root':rec(H(p)),'original_quota':3,'original_margin':rec(rootmargin),'reset_upper_price':rec(price),'universal_one_frontier_margin':rec(after),'actual_reset_net_cost':rec(reset),'actual_post_reset_margin':rec(add((1,const(3)),(-1,firstbill))),'actual_full_terminal_cross_entropy':rec(add(*[(F(1,2),CE(spec(w),q)) for w in vv])),'root_conditional_KL':rec(cost),'sharp_fixed_reference_reset_price':rec(logq(maxratio)),'sharp_price_attained_by_character':extreme,'query':'data y3 (physical bit 6); both outcomes retained','independence':'No imported campaign helper; root coefficients also checked by direct character sum.','scope':'Finite checks plus analytic all-tree reference telescope; not arbitrary-core admission.'}
    (RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','pilot','assertions','seconds','local_query_cases')}))
if __name__=='__main__': run('--pilot' in sys.argv)
