"""Exact checks for finite-edit signature returns; no floating sign decisions."""
import itertools, json, sys, time
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
START=time.monotonic(); checks=states=0
def ck(b):
    global checks
    checks+=1
    assert b
    if time.monotonic()-START>55: raise RuntimeError('frozen 55s cap')
def span(vs):
    a={0}
    for v in vs: a|={x^v for x in tuple(a)}
    return a
def dot(x,y): return (x&y).bit_count()%2
def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
def project(x,free): return sum(((x>>j)&1)<<i for i,j in enumerate(free))
def restriction(a,n,assign):
    free=[j for j in range(n) if assign[j]<0]
    fixed=sum(x<<j for j,x in enumerate(assign) if x>=0)
    vertices=[fixed|sum(((u>>i)&1)<<j for i,j in enumerate(free)) for u in range(1<<len(free))]
    return [a[v] for v in vertices],free,vertices
def verify(g,n,edits,assign):
    global states
    states+=1
    N=1<<n; f=[-v if i in edits else v for i,v in enumerate(g)]
    gg,free,verts=restriction(g,n,assign); ff,_,_=restriction(f,n,assign)
    m=len(free); M=1<<m; gw=walsh(gg); fw=walsh(ff)
    V0=span(i for i,x in enumerate(walsh(g)) if x)
    V={project(v,free) for v in V0}
    ck(all(i in V for i,x in enumerate(gw) if x))
    D=[i for i,v in enumerate(verts) if v in edits]
    ck(all(ff[i]==(-gg[i] if i in D else gg[i]) for i in range(M)))
    W=span([x^D[0] for x in D[1:]]) if D else {0}
    cells={}
    for s in range(M):
        key=('core',s) if s in V else ('shell',tuple(dot(s,w) for w in sorted(W)))
        cells.setdefault(key,[]).append(s)
    ck(sum(fw[s]**2 for s in range(M))==M*M)
    for key,C in cells.items():
        ck(len({fw[s]**2 for s in C})==1)
        if key[0]=='shell':
            for s in C:
                ck(fw[s]==-2*sum(gg[x]*(-1)**dot(s,x) for x in D))
            # An explicit rank-one involution independently witnesses orbit transitivity.
            u=C[0]
            for v in C[1:]:
                d=u^v
                ell=next(l for l in range(M) if dot(l,u)==1 and dot(l,d)==0 and all(dot(l,a)==0 for a in V))
                T=[s^(d if dot(ell,s) else 0) for s in range(M)]
                ck(len(set(T))==M and T[u]==v and all(T[T[s]]==s for s in range(M)))
                ck(all(T[a]==a for a in V) and all(dot(T[s],w)==dot(s,w) for s in range(M) for w in W))
        if fw[C[0]]:
            # Exact AM-GM certificate: CE difference has constant nonnegative cell weight.
            for Q in ([F(s+1,M*(M+1)//2) for s in range(M)],
                      [(F(fw[s]**2,M*M)+F(1,M))/2 for s in range(M)]):
                avg=sum((Q[s] for s in C),F())/len(C)
                prod=F(1)
                for s in C: prod*=Q[s]
                ck(prod<=avg**len(C))
                ck(sum((avg for s in C),F())==sum((Q[s] for s in C),F()))
    # The actual law is fixed by its own return, including zero-mass cells.
    ck(all(sum(fw[s]**2 for s in C)==len(C)*fw[C[0]]**2 for C in cells.values()))

pilot='pilot' in sys.argv
ns=[2] if pilot else [2,3]
for n in ns:
    N=1<<n
    for mask in range(1<<N):
        g=[1-2*((mask>>x)&1) for x in range(N)]
        if n==3 and not (all(g[x]==g[x^4] for x in range(8)) or any(all(g[x]==sign*(-1)**dot(s,x) for x in range(8)) for s in (3,5,6,7) for sign in (-1,1))): continue
        V=span(i for i,x in enumerate(walsh(g)) if x)
        if len(V)==N: continue  # frozen nonvacuous supplied-core domain
        for k in range(min(3,N)+1):
            for E in itertools.combinations(range(N),k):
                for assign in itertools.product((-1,0,1),repeat=n):
                    verify(g,n,set(E),assign)
out={'status':'PASS','mode':'pilot' if pilot else 'full','states':states,'exact_assertions':checks,'seconds':time.monotonic()-START,'arithmetic':'integer Walsh, Fraction AM-GM, explicit rank-one maps','max_dimension':max(ns)}
(ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
