from exact import *
from v import V,GV
from functools import lru_cache
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1];checks=0
def eq(a,b):
    global checks
    checks+=1;assert not plus(a,mul(b,-1)),(a,b)
def tails(p):
    q=list(p)
    for i in range(len(p).bit_length()-1):
        for S in range(len(p)):
            if not S>>i&1:q[S]+=q[S|1<<i]
    return q
def table(mask,m=2):return tuple(1 if mask>>x&1 else -1 for x in range(1<<m))
@lru_cache(None)
def R(a,c):
    h=tuple(a[z] if y==0 else c[z] for z in range(len(a)) for y in (0,1))
    p=spectrum(h);q=tails(p);j=mul(lg(q[1]/p[1]),p[1]) if p[1] else {}
    return plus(V(h),mul(j,-1),mul(plus(V(a),V(c)),-Q(1,2)))
def GR(a,c):
    return plus(*(plus(R(a,c),mul(plus(*(R(tuple(restrict(a,j,b)),tuple(restrict(c,j,b))) for b in (0,1))),-Q(1,2))) for j in range(len(a).bit_length()-1)))
def enc(x):return {str(p):str(c) for p,c in sorted(x.items())}
def signed(x):
    if not x:return 'zero'
    lo,hi=bounds(x)
    assert lo>0 or hi<0,('UNRESOLVED',x)
    return 'positive' if lo>0 else 'negative'
def witness(am,cm,r,g):
    return {'a_mask':am,'c_mask':cm,'R':enc(r),'GR':enc(g),'R_sign':signed(r),'GR_sign':signed(g),'R_interval':[str(x) for x in bounds(r)],'GR_interval':[str(x) for x in bounds(g)]}
def E(f,k):
    p=spectrum(f);q=tails(p)
    return plus(*(mul(lg(q[S]/p[S]),p[S]) for S in range(1,1<<k) if p[S]))
def adjacent():
    global checks
    cases=0;d=Q(1,64);k=6;seed=tuple(g(x&7)*g(x>>3) for x in range(64))
    for v,w in ((0,1),(1,3)):
        eps=seed[v]*seed[w]
        for am,cm in ((1,6),(3,5),(7,1),(0,15)):
            a=table(am);rawc=table(cm);c=tuple(eps*x for x in rawc)
            f=tuple(seed[x]*(a[z] if x==v else rawc[z] if x==w else 1) for z in range(4) for x in range(64))
            vars=2-Q(sum(a),4)**2-Q(sum(c),4)**2
            qpart=plus(V(f),mul(E(f,k),-1))
            eq(qpart,plus(mul(plus(V(a),V(c)),d),mul(R(a,c),2*d),const(d*Q(k-1,2)*vars)))
            edrift=plus(*(plus(E(f,k),mul(plus(*(E(tuple(restrict(f,k+j,b)),k) for b in (0,1))),-Q(1,2))) for j in range(2)))
            wa=sum(Q(sum(a[z]*(-1 if z>>j&1 else 1) for z in range(4)),4)**2 for j in range(2))
            wc=sum(Q(sum(c[z]*(-1 if z>>j&1 else 1) for z in range(4)),4)**2 for j in range(2))
            rhs=plus(mul(plus(GV(a,range(2)),GV(c,range(2))),d),mul(GR(a,c),2*d),const(d*Q(k-1,2)*(wa+wc)),edrift)
            eq(GV(f,range(k,k+2)),rhs);cases+=1
    return cases
mode=sys.argv[1];start=time.monotonic();classes={'R':dict(positive=0,negative=0,zero=0),'GR':dict(positive=0,negative=0,zero=0)};witnesses={};cases=0
if mode=='adjacent':cases=adjacent()
else:
    pairs=((1,6),(3,5),(7,1),(0,15)) if mode=='pilot' else ((a,c) for a in range(16) for c in range(16))
    assert mode in ('pilot','main')
    for am,cm in pairs:
        a,c=table(am),table(cm);r,gr=R(a,c),GR(a,c)
        for name,x in (('R',r),('GR',gr)):
            sign=signed(x);classes[name][sign]+=1;checks+=1
            key=name+'_'+sign
            if key not in witnesses:witnesses[key]=witness(am,cm,r,gr)
        # Exact commutation identity, retaining BOTH physical outcomes.
        h=tuple(a[z] if y==0 else c[z] for z in range(4) for y in (0,1));p=spectrum(h);q=tails(p)
        jy=mul(lg(q[1]/p[1]),p[1]) if p[1] else {}
        sumjy={}
        for j in range(2):
            children=[]
            for b in (0,1):
                child=tuple(restrict(h,j+1,b));pp=spectrum(child);qq=tails(pp)
                children.append(mul(lg(qq[1]/pp[1]),pp[1]) if pp[1] else {})
            sumjy=plus(sumjy,jy,mul(plus(*children),-Q(1,2)))
        eq(GV(h,range(1,3)),plus(mul(plus(GV(a,range(2)),GV(c,range(2))),Q(1,2)),gr,sumjy))
        cases+=1;assert time.monotonic()-start<60
out={'status':'PASS','mode':mode,'cases':cases,'assertions':checks,'sign_counts':classes,'witnesses':witnesses,'elapsed_seconds':time.monotonic()-start,'peak_memory':'unmeasured','scope':'finite signs and exact all-coordinate identity; no universal upper bound inferred'}
(ROOT/'out'/('selector_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}));print(json.dumps(witnesses)[:4000])
