"""Exact algebra checks for X082; standard library, no LP solver."""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path

E = tuple(range(6))
P = tuple(combinations(E, 2))
T = tuple(combinations(E, 3))
ps = {a: set(a) for a in P}
ts = {a: set(a) for a in T}
edges = []
for j in P:
    for a in P:
        if ps[a].isdisjoint(ps[j]):
            b = tuple(sorted(set(E) - ps[a] - ps[j]))
            if a < b:
                edges.append((j, a, b))
atoms = [(a,j,b) for j,a,b in edges] + [(b,j,a) for j,a,b in edges]
assert len(edges) == 45 and len(atoms) == 90

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def matmul(a,b):
    return [[dot(row,col) for col in zip(*b)] for row in a]

def tr(a):
    return [list(x) for x in zip(*a)]

def det(a):
    n = len(a)
    ans = F(0)
    for q in permutations(range(n)):
        sign = (-1)**sum(q[i]>q[j] for i in range(n) for j in range(i+1,n))
        v = F(sign)
        for i in range(n): v *= a[i][q[i]]
        ans += v
    return ans

def vol(q,cols,rows):
    return det([[q[i][j] for j in cols] for i in rows])

def pi(a,b):
    z = len(ps[a] & ps[b])
    return {2:F(3,5),1:F(-3,20),0:F(1,10)}[z]

Pi = [[pi(a,b) for b in P] for a in P]
assert matmul(Pi,Pi) == Pi
assert sum(Pi[i][i] for i in range(15)) == 9
for j in range(15):
    for i in E:
        assert sum(Pi[k][j] for k,a in enumerate(P) if i in a) == 0

def repair(delta):
    return {(j,a,b):(3*delta[a]+3*delta[b]-delta[j])/20 for j,a,b in edges}

def image(m):
    return {a:sum(m[e] for e in edges if a in e[1:]) for a in P}

for col in range(15):
    d = {a:Pi[i][col] for i,a in enumerate(P)}
    z = repair(d)
    for j in P: assert sum(z[e] for e in edges if e[0] == j) == 0
    assert image(z) == d
    assert sum(v*v for v in z.values()) == F(3,20)*sum(v*v for v in d.values())
for j,a,b in edges:
    row = [(3*pi(a,d)+3*pi(b,d)-pi(j,d))/20 for d in P]
    assert dot(row,row) == F(3,100)

# A positive rational table checks the full reconstruction independently of DPPs.
den = sum(range(1,91))
x = {atom:F(i+1,den) for i,atom in enumerate(atoms)}
a = {p:sum(v for (aa,j,b),v in x.items() if aa == p) for p in P}
h = {p:sum(v for (aa,j,b),v in x.items() if j == p) for p in P}
c = {p:sum(v for (aa,j,b),v in x.items() if b == p) for p in P}
y = {(j,i):sum(v for (aa,jj,b),v in x.items() if jj==j and i in aa)
     for j in P for i in E if i not in j}
r = {m:sum(y[(j,next(iter(ts[m]-ps[j])))] for j in P if ps[j]<ts[m]) for m in T}
g = {m:sum(v for (aa,j,b),v in x.items() if ps[aa]<ts[m] and len(ts[m]&ps[j])==1) for m in T}
masses = {(j,aa,b):x[(aa,j,b)]+x[(b,j,aa)] for j,aa,b in edges}
L,rho,m0 = {},{},{}
for j in P:
    es = [e for e in edges if e[0]==j]
    for e in es:
        aa=e[1]
        d=sum(y[(j,i)] for i in aa)-h[j]
        L[e]=abs(d)
        assert (masses[e]+d)/2 == x[(aa,j,e[2])]
        assert masses[e]>=L[e]
    rho[j]=h[j]-sum(L[e] for e in es)
    assert rho[j] == 2*min(min(y[(j,i)],h[j]-y[(j,i)]) for i in E if i not in j)
    for e in es: m0[e]=L[e]+rho[j]/3
for mm in T:
    assert g[mm]+r[mm] == sum(c[b] for b in P if ps[b]<set(E)-ts[mm])

def check_difference(a,h,c,r):
    hi={i:sum(h[p] for p in P if i in p) for i in E}
    ri={i:sum(r[m] for m in T if i in m) for i in E}
    for p in P:
        i,j=p
        rp=sum(r[m] for m in T if ps[p]<ts[m])
        assert a[p]-c[p] == ri[i]+ri[j]-hi[i]-hi[j]-1+h[p]-rp

check_difference(a,h,c,r)
s0=image(m0)
delta={p:a[p]+c[p]-s0[p] for p in P}
z=repair(delta)
assert image(z)==delta
for i in E: assert sum(delta[p] for p in P if i in p)==0

# Check the support function at several exact pair potentials by direct
# evaluation of all three row vertices (not a numerical LP coupling).
for seed in range(1,6):
    v={p:F(((i+1)*seed)%11-5,3) for i,p in enumerate(P)}
    for j in P:
        es=[e for e in edges if e[0]==j]
        costs={e:v[e[1]]+v[e[2]] for e in es}
        top=max(costs.values())
        formula=h[j]*top-sum((top-costs[e])*L[e] for e in es)
        vertices=[sum(L[e]*costs[e] for e in es)+rho[j]*costs[t] for t in es]
        assert formula==max(vertices)

# Independent exact projection flag: three rational Householder factors.
I=[[F(i==j) for j in E] for i in E]
Q=I
for v in [(1,2,3,4,5,6),(2,-1,3,-2,1,4),(3,1,-2,4,2,-1)]:
    nn=sum(t*t for t in v)
    R=[[I[i][j]-F(2*v[i]*v[j],nn) for j in E] for i in E]
    Q=matmul(Q,R)
assert matmul(tr(Q),Q)==I
a={p:vol(Q,(0,1),p)**2 for p in P}
h={p:vol(Q,(2,3),p)**2 for p in P}
c={p:vol(Q,(4,5),p)**2 for p in P}
g={m:sum(vol(Q,(0,1,k),m)**2 for k in (2,3)) for m in T}
r={m:sum(vol(Q,(2,3,k),m)**2 for k in (0,1)) for m in T}
assert sum(a.values())==sum(h.values())==sum(c.values())==1
assert sum(g.values())==sum(r.values())==2
for mm in T:
    assert g[mm]+r[mm]==sum(c[b] for b in P if ps[b]<set(E)-ts[mm])
check_difference(a,h,c,r)

out={"status":"PASS", "arithmetic":"exact rational", "projector_rank":9,
     "right_inverse_columns_checked":15,"sharp_cell_norm_squared":"3/100",
     "minimum_norm_ratio_squared":"3/20", "local_row_fibers_checked":15,
     "row_support_vertex_comparisons":75,"determinantal_triple_identities":20,
     "determinantal_pair_difference_identities":15,
     "scope":"Exact reductions and conditional capacity certificate; no universal coupling claimed."}
Path(__file__).with_name("verified_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
