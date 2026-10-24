from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0; blocks=0; isolated=0
def ck(x):
    global assertions
    assertions+=1
    assert x
    if time.perf_counter()-start>55: raise RuntimeError('Frozen runtime boundary reached')
def add(*items):
    d={}
    for v,c in items:
        for k,a in v.items(): d[k]=d.get(k,Q(0))+c*a
    return {k:a for k,a in d.items() if a}
@lru_cache(None)
def factors(a):
    d={}; k=2
    while k*k<=a:
        while a%k==0: d[k]=d.get(k,0)+1; a//=k
        k+=1
    if a>1:d[a]=d.get(a,0)+1
    return d
def lv(q):
    d=dict(factors(q.numerator))
    for k,a in factors(q.denominator).items():d[k]=d.get(k,0)-a
    return {k:Q(a) for k,a in d.items() if a}
def ent(weights):
    d={}
    for q in weights:
        if q:d=add((d,1),(lv(q),-q))
    return d
@lru_cache(None)
def ln_interval(k):
    m=24; shift=k.bit_length()-1
    z=Q(k-2**shift,k+2**shift)
    lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(m)),Q(0))
    err=2*z**(2*m+1)/Q(2*m+1)/(1-z*z)
    if k==2:
        z=Q(1,3)
        lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(m)),Q(0))
        err=2*z**(2*m+1)/Q(2*m+1)/(1-z*z)
        return lo,lo+err
    l,u=ln_interval(2)
    return lo+shift*l,lo+err+shift*u
def interval(v):
    lo=hi=Q(0)
    for k,c in v.items():
        l,u=ln_interval(k)
        lo+=c*(l if c>=0 else u);hi+=c*(u if c>=0 else l)
    return lo,hi
def nonpositive(v,extra=Q(0)):
    if not v:ck(extra<=0)
    else: ck(interval(v)[1]+extra<=0)
@lru_cache(None)
def spectrum(h):
    a=list(h); N=len(a); width=1
    while width<N:
        for t in range(0,N,2*width):
            for j in range(width):u=a[t+j];v=a[t+j+width];a[t+j]=u+v;a[t+j+width]=u-v
        width*=2
    return tuple(Q(v,N)**2 for v in a)
def direct(h):
    N=len(h)
    return tuple(Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(h)),N)**2 for s in range(N))
@lru_cache(None)
def raw(h):return ent(spectrum(h))
def mass(h):return Q(sum(x*x for x in h),len(h))
def energy(h,A):
    return sum((q*(s&A).bit_count() for s,q in enumerate(spectrum(h))),Q(0))
def edge_energy(h,A):
    return Q(sum((h[x]-h[x^(1<<i)])**2 for i in range(len(h).bit_length()-1) if A>>i&1 for x in range(len(h))),4*len(h))
def children(h,A):
    n=len(h).bit_length()-1;ai=[i for i in range(n) if A>>i&1];ci=[i for i in range(n) if not A>>i&1]
    def scatter(z,ids):return sum((z>>j&1)<<i for j,i in enumerate(ids))
    return tuple(tuple(h[scatter(x,ai)|scatter(y,ci)] for y in range(1<<len(ci))) for x in range(1<<len(ai)))
def ledger(h,A):
    ch=children(h,A);N=len(ch); avg={}
    for v in ch:avg=add((avg,1),(raw(v),Q(1,N)))
    L=add((raw(h),1),(avg,-1))
    p=spectrum(h);marg={}
    for s,q in enumerate(p):marg[s&~A]=marg.get(s&~A,Q(0))+q
    B=add((ent(p),1),(ent(marg.values()),-1));J=add((L,1),(B,-1))
    # Independent partial-row entropy, including nonuniform child mass.
    chspec=[spectrum(v) for v in ch];q=[sum((s[t] for s in chspec),Q(0))/N for t in range(len(ch[0]))]
    directJ=add((ent(q),1),(avg,-1));ck(J==directJ)
    ck(energy(h,A)==edge_energy(h,A));ck(mass(h)==sum(p))
    nonpositive(add((J,-1)))
    nonpositive(J,-2*energy(h,A))
    nonpositive(add((B,1),({2:mass(h)*A.bit_count()},-1)))
    ck(energy(h,(len(h)-1)^A)==sum((energy(v,len(v)-1) for v in ch),Q(0))/N)
    return L,B,J,ch
def comps(h):
    n=len(h).bit_length()-1; rem={x for x,v in enumerate(h) if v};out=[]
    while rem:
        seed=min(rem); rem.remove(seed); seen={seed};todo=[seed]
        while todo:
            x=todo.pop()
            for i in range(n):
                y=x^(1<<i)
                if y in rem:rem.remove(y);seen.add(y);todo.append(y)
        out.append(tuple(int(x in seen) for x in range(len(h))))
    return out
def test(h,A):
    global blocks,isolated
    blocks+=1;L,B,J,ch=ledger(h,A);cs=comps(h)
    cchildren=[children(c,A) for c in cs]
    if any(sum(any(v[x]) for v in cchildren)>1 for x in range(len(ch))):return
    isolated+=1; credits={}
    for c in cs:credits=add((credits,1),(ledger(c,A)[0],1))
    gap=raw(h)
    for c in cs:gap=add((gap,1),(raw(c),-1))
    ck(gap==add((L,1),(credits,-1)))
    ck(energy(h,len(h)-1)==sum((energy(c,len(c)-1) for c in cs),Q(0)))
    nonpositive(add((gap,1),(B,-1),(credits,1)),-2*energy(h,A))
pilot='--pilot' in sys.argv
tables=0
for n in range(0,3 if pilot else 4):
    for mask in range(1<<(1<<n)):
        h=tuple(mask>>x&1 for x in range(1<<n));tables+=1
        ck(spectrum(h)==direct(h))
        for A in range(1,1<<n):test(h,A)
connected=[]
for mask in range(1,16):
    h=tuple(mask>>x&1 for x in range(4))
    if len(comps(h))==1:connected.append(h)
thin=0
for r,d in ([(2,2)] if pilot else [(2,2),(3,2),(4,2)]):
    for va in connected[:1] if pilot else connected:
        for vb in connected[:1] if pilot else connected:
            n=r+2;A=(1<<r)-1
            c1=tuple(int((x&3)==0)*va[x>>r] for x in range(1<<n))
            c2=tuple(int((x&3)==3)*vb[x>>r] for x in range(1<<n))
            h=tuple(a+b for a,b in zip(c1,c2));thin+=1
            ck(len(comps(h))==2);ck(spectrum(h)==direct(h))
            L,B,J,ch=ledger(h,A);p=mass(h);E=energy(h,A)
            ck(E==Q(d,2)*p);ck(E>=Q(r,4)*p)
            for c in (c1,c2):ck(ledger(c,A)[0]=={2:2*d*mass(c)})
            nonpositive(add((B,1),({2:4*E},-1)))
controls=[]
if not pilot:
    for data,control in [(4,3),(5,4)]:
        n=data+control;N=1<<n;A=(1<<data)-1
        a=tuple(int((x&A).bit_count()<=1) for x in range(N))
        b=tuple(int(x==A) for x in range(N));g=tuple(x+y for x,y in zip(a,b))
        ck(len(comps(g))==2);ck(spectrum(g)==direct(g))
        test(g,A)
        gap=add((raw(g),1),(raw(a),-1),(raw(b),-1));lo,hi=interval(gap)
        ck(lo>0)
        if data==5:ck(lo>Q(1,5000))
        if data==4:
            ck(3**45*5**25>2**128)
            ck(2**23552>3**1620*23**2645*41**1681)
            ck(interval(add((raw(g),1),({2:4*energy(g,N-1)},-1)))[0]>0)
        controls.append(dict(n=n,component_sizes=[sum(a),sum(b)],excess_natural_interval=[str(lo),str(hi)],energy=str(energy(g,N-1))))
result=dict(status='PASS',pilot=pilot,tables=tables,block_cases=blocks,component_isolating_cases=isolated,thin_cylinder_cases=thin,assertions=assertions,controls=controls,seconds=time.perf_counter()-start)
(ROOT/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
