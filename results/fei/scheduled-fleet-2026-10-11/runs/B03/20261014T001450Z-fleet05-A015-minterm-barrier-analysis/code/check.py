"""A015 v3: independent determinant / chronological-event review.
No author implementation imported. All mathematical comparisons exact.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import factorial
import json, time, sys

BASE=Path(__file__).resolve().parents[1]
CHECKS=0
def ck(v):
    global CHECKS
    CHECKS+=1
    assert v, CHECKS
def add(a,b):
    c=a.copy()
    for m,v in b.items():
        c[m]=c.get(m,F(0))+v
        if not c[m]: del c[m]
    return c
def mul(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            m=tuple(p+q for p,q in zip(x,y)); c[m]=c.get(m,F(0))+u*v
    return {m:v for m,v in c.items() if v}
def scale(a,v): return {m:t*v for m,t in a.items() if t*v}
def determinant(a,zero):
    out={}; n=len(a)
    for p in permutations(range(n)):
        term={zero:F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))}
        for i in range(n): term=mul(term,a[i][p[i]])
        out=add(out,term)
    return out
def sources(adj):
    n=len(adj); reach=[{i}|set(adj[i]) for i in range(n)]
    for k in range(n):
        for i in range(n):
            if k in reach[i]: reach[i]|=reach[k]
    comps=[]; todo=set(range(n))
    while todo:
        i=min(todo); c={j for j in todo if j in reach[i] and i in reach[j]}; comps.append(c); todo-=c
    return [sorted(c) for c in comps if not any(v in c for u in range(n) if u not in c for v in adj[u])]

def review(supports,owned,pi):
    used=[i for i,b in enumerate(owned) if b]
    supports=[supports[i] for i in used]; owned=[owned[i] for i in used]; pi=[pi[i] for i in used]
    n=len(used); groups=[(u,j) for u,b in enumerate(owned) for j in sorted(b)]; idx={g:i for i,g in enumerate(groups)}
    z=(0,)*len(groups)
    adj=[{v for v in range(n) if v!=u and owned[u]&supports[v]} for u in range(n)]
    src=sources(adj); roots=list(product(*src)); e=n-len(src)
    w={}
    for u in range(n):
        for v in adj[u]:
            t={}
            for j in owned[u]&supports[v]:
                m=list(z); m[idx[u,j]]=1; t[tuple(m)]=F(1)
            w[u,v]=t
    lap=[[{} for _ in range(n)] for _ in range(n)]
    for (u,v),t in w.items(): lap[v][v]=add(lap[v][v],t); lap[v][u]=scale(t,-1)
    poly={}
    for rt in roots:
        rem=[i for i in range(n) if i not in rt]
        minor=determinant([[lap[i][j] for j in rem] for i in rem],z)
        weight=F(1)
        for u in rt: weight*=pi[u]
        poly=add(poly,scale(minor,weight))
    # Independently execute chronological BFS events, deciding each gate's
    # selected child list when it is popped. Queue entries are distinct IDs.
    events={}; tracecount=0
    def visit(queue,seen,m,weight):
        nonlocal tracecount
        if not queue:
            if len(seen)==n:
                events[m]=events.get(m,F(0))+weight; tracecount+=1
            return
        u=queue[0]; tail=queue[1:]; avail=sorted(adj[u]-seen)
        for mask in range(1<<len(avail)):
            children=[v for k,v in enumerate(avail) if mask>>k&1]
            opts=[sorted(owned[u]&supports[v]) for v in children]
            for attaches in product(*opts):
                buckets={j:[] for j in sorted(owned[u])}
                for v,j in zip(children,attaches): buckets[j].append(v)
                keys=[j for j in buckets if buckets[j]]
                for seqs in product(*(list(permutations(buckets[j])) for j in keys)):
                    new=list(m); ordered=[]
                    for j,seq in zip(keys,seqs): new[idx[u,j]]+=len(seq); ordered.extend(seq)
                    visit(tail+ordered,seen|set(children),tuple(new),weight)
    for rt in roots:
        weight=F(1)
        for u in rt: weight*=pi[u]
        visit(sorted(rt),set(rt),z,weight)
    moments={m:v*product_factorials(m) for m,v in poly.items()}
    ck(events==moments)
    ck(all(v>0 for v in poly.values()))
    can=sum(poly.values(),F(0)); moment=sum(events.values(),F(0))
    d=[sum(v!=u and j in supports[v] for v in range(n)) for u,j in groups]
    up=F(0)
    for m,v in poly.items():
        t=v
        for h,D in zip(m,d): t*=F(D+1,2)**h if D else 1
        up+=t
    ck(can<=moment<=min(factorial(e)*can,up))
    if all(D<=1 for D in d): ck(can==moment==up)
    return tracecount, can,moment
def product_factorials(m):
    v=1
    for h in m: v*=factorial(h)
    return v
def fwht(a):
    a=a.copy(); s=1
    while s<len(a):
        for k in range(0,len(a),2*s):
            for j in range(k,k+s): a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
        s*=2
    return a
def rare(r):
    n=r+2; y=r; zz=r+1
    vals=[(1 if x>>zz&1 else -1) if x&((1<<r)-1)==(1<<r)-1 else (1 if x>>y&1 else -1) for x in range(1<<n)]
    expected=[frozenset([(y,1),(zz,1)])]+[frozenset([(y,1),(j,0)]) for j in range(r)]+[frozenset([(zz,1)]+[(j,1) for j in range(r)])]
    implicants=[]
    for term in product((-1,0,1),repeat=n):
        lits=frozenset((j,t) for j,t in enumerate(term) if t>=0)
        if all(vals[x]==1 for x in range(1<<n) if all((x>>j&1)==t for j,t in lits)): implicants.append(lits)
    primes={t for t in implicants if not any(u<t for u in implicants)}
    ck(primes==set(expected))
    a=fwht(vals); p=F(1,1<<r)
    ck(sum(t*t for t in a)==(1<<n)**2)
    infl=[F(sum(vals[x]!=vals[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n)]
    ck(infl==[p]*r+[1-p,p]); ck(sum(infl)==1+r*p)
    ck(F(a[1<<y]**2,1<<(2*n))==(1-p)**2)
    supports=[{j for j,t in term} for term in expected]
    pi=[F(1,4)]*(r+1)+[p/2]
    cases=traces=0
    # Absent coordinate or one eligible gate: generates all A and ownerships.
    choices=[[-1]+[i for i,b in enumerate(supports) if j in b] for j in range(n)]
    for assignment in product(*choices):
        if all(i<0 for i in assignment): continue
        owned=[set() for b in supports]
        for j,i in enumerate(assignment):
            if i>=0: owned[i].add(j)
        count,can,moment=review(supports,owned,pi); cases+=1; traces+=count
    ck(cases==3*(r+2)*3**r-1)
    # Singleton y, all y-containing primes have y first, exactly one root.
    lam=[F(1,4)]+[F(3,4*r)]*r+[F(1,4)]
    ck(all(sum(lam[i] for i,b in enumerate(supports) if j in b)<=1 for j in range(n)))
    D=F(1)
    for l,q in zip(lam,pi): D*=1+l*q
    D-=1
    t=sum(l*q for l,q in zip(lam,pi)); ck(t==F(1,4)+p/8)
    ck(D<=t/(1-t)<=F(5,11))
    # alpha=2^-6/5 has alpha^5=1/64; enclose by dyadic bisection.
    lo,hi=F(0),F(1)
    for _ in range(80):
        mid=(lo+hi)/2
        if mid**5<F(1,64): lo=mid
        else: hi=mid
    ck(lo**5<=F(1,64)<=hi**5); ck(hi<F(1,2))
    qlo=1/(16*D*(1+hi)); qhi=1/(16*D*(1+lo))
    ck(qlo>F(11,120)); ck(F(1,4)==sum(lam[i]*pi[i] for i in range(r+1)))
    # S({y})=sum lambda*pi=1/4; posterior-surrogate residual D/S<20/11.
    ck(4*D<=F(20,11))
    return {'r':r,'n':n,'ownership_cases':cases,'actual_traces':traces,'D':str(D),'q_y_interval':[str(qlo),str(qhi)],'surrogate_singleton_mass':'1/4'}

def main():
    begin=time.perf_counter(); pilot='--pilot' in sys.argv
    rows=[]
    for r in ([1,2] if pilot else [1,2,3,4]):
        rows.append(rare(r))
        (BASE/'out'/('PILOT_CHECKPOINT.json' if pilot else 'CHECKPOINT.json')).write_text(json.dumps(rows,indent=2),encoding='utf-8')
    # Forced actual prime sunflowers check sharp factorial chronology directly.
    stars=[]
    for e in range(1,6):
        supports=[{0,j} for j in range(1,e+2)]
        owned=[{0}]+[{j} for j in range(2,e+2)]
        c,can,m=review(supports,owned,[F(1,4)]*(e+1))
        ck(c==factorial(e)); ck(m==factorial(e)*can)
        stars.append({'edges':e,'traces':c,'canonical':str(can),'moment':str(m)})
    ck(stars[1]['canonical']=='1/4' and stars[1]['moment']=='1/2')
    result={'helper_version':'A015-v3-independent-bfs','mode':'pilot' if pilot else 'full','assertions':CHECKS,'seconds':time.perf_counter()-begin,'rare_switch':rows,'sunflower':stars,'status':'PASS'}
    target=BASE/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json'); target.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['mode','assertions','seconds','status']}))
if __name__=='__main__': main()
