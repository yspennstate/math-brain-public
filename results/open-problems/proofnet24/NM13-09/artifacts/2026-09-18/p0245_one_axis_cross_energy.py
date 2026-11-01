"""Exact self-check for NM13-09 / P0245 one-axis opposite-edge imbalance theorem.

This is a self-check, not an independent audit.  It verifies:
1. the exact symbolic formula for the remaining cross-energy E_* on
   b=e=B/2, c=d=C/2, a=(A+x)/2, f=(A-x)/2;
2. one exact rational spot value;
3. two bounded exact rational-grid searches used only as route diagnostics.
"""
from fractions import Fraction
from itertools import combinations, product
from math import gcd
import sympy as sp

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

# ---------- symbolic one-axis identity ----------
A,B,C,x = sp.symbols("A B C x")
a=(A+x)/2
f=(A-x)/2
b=e=B/2
c=d=C/2
vals=[a,b,c,d,e,f]
w=dict(zip(EDGES,vals))

def W(i,j):
    if i==j:
        return sp.Integer(0)
    return w[tuple(sorted((i,j)))]

deg=[sum(W(i,j) for j in range(4) if j!=i) for i in range(4)]
L=sp.Matrix([[deg[i] if i==j else -W(i,j) for j in range(4)] for i in range(4)])
tau=sp.expand(L[:3,:3].det())

def forest_poly(i,j):
    ans=0
    for es in combinations(EDGES,2):
        parent=list(range(4))
        def find(q):
            while parent[q]!=q:
                parent[q]=parent[parent[q]]
                q=parent[q]
            return q
        ok=True
        for u,v in es:
            ru,rv=find(u),find(v)
            if ru==rv:
                ok=False
                break
            parent[rv]=ru
        if not ok or len({find(t) for t in range(4)})!=2 or find(i)==find(j):
            continue
        wt=1
        for ed in es:
            wt*=W(*ed)
        ans+=wt
    return sp.expand(ans)

F={ed:forest_poly(*ed) for ed in EDGES}

def rdel(i):
    vv=[q for q in range(4) if q!=i]
    p,q,r=vv
    return sp.expand(W(p,q)*W(p,r)+W(p,q)*W(q,r)+W(p,r)*W(q,r))

r=[rdel(i) for i in range(4)]

# psi_i = (1/(2 tau)) sum_z d_z F_iz, up to the exact resistance identity.
psi_num=[]
for i in range(4):
    psi_num.append(sp.expand(sum(deg[z]*F[tuple(sorted((i,z)))]
                                 for z in range(4) if z!=i)))

Estar=0
for k,l in EDGES:
    u,v=[q for q in range(4) if q not in (k,l)]
    Estar += W(u,v)/F[(k,l)]*(r[l]-r[k])*(psi_num[l]-psi_num[k])/(2*tau)
Estar=sp.cancel(Estar)

T=A+B+C
U=T**2-x**2
V=A**2+A*(B+C)+B*C-x**2
closed=2*(B+C)*x**2*(U**2-B**2*C**2)/((U-B**2)*(U-C**2)*V)

assert sp.expand(sp.together(Estar-closed).as_numer_denom()[0])==0
spot=sp.cancel(Estar.subs({A:5,B:3,C:2,x:1}))
assert spot==sp.Rational(217,1045)
assert spot>0

# ---------- bounded exact grids, route diagnostics only ----------
OPP={}
for i,j in EDGES:
    rest=[q for q in range(4) if q not in (i,j)]
    OPP[(i,j)]=tuple(sorted(rest))

def connected(vals):
    adj=[[] for _ in range(4)]
    for (u,v),wt in zip(EDGES,vals):
        if wt>0:
            adj[u].append(v)
            adj[v].append(u)
    seen={0}
    stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen)==4

def primitive(vals):
    g=0
    for q in vals:
        g=gcd(g,int(q))
    return g==1

def estar_fraction(vals):
    wf=dict(zip(EDGES,[Fraction(v) for v in vals]))
    def Q(i,j):
        if i==j:
            return Fraction(0)
        return wf[tuple(sorted((i,j)))]
    dg=[sum((Q(i,j) for j in range(4) if j!=i),Fraction(0)) for i in range(4)]

    tree=Fraction(0)
    for es in combinations(EDGES,3):
        parent=list(range(4))
        def find(q):
            while parent[q]!=q:
                parent[q]=parent[parent[q]]
                q=parent[q]
            return q
        ok=True
        for u,v in es:
            ru,rv=find(u),find(v)
            if ru==rv:
                ok=False
                break
            parent[rv]=ru
        if ok and len({find(t) for t in range(4)})==1:
            wt=Fraction(1)
            for ed in es:
                wt*=Q(*ed)
            tree+=wt
    assert tree>0

    FF={}
    for ij in EDGES:
        i,j=ij
        ans=Fraction(0)
        for es in combinations(EDGES,2):
            parent=list(range(4))
            def find2(q):
                while parent[q]!=q:
                    parent[q]=parent[parent[q]]
                    q=parent[q]
                return q
            ok=True
            for u,v in es:
                ru,rv=find2(u),find2(v)
                if ru==rv:
                    ok=False
                    break
                parent[rv]=ru
            if not ok or len({find2(t) for t in range(4)})!=2 or find2(i)==find2(j):
                continue
            wt=Fraction(1)
            for ed in es:
                wt*=Q(*ed)
            ans+=wt
        assert ans>0
        FF[ij]=ans

    rd=[]
    for i in range(4):
        vv=[q for q in range(4) if q!=i]
        p,q,s=vv
        rd.append(Q(p,q)*Q(p,s)+Q(p,q)*Q(q,s)+Q(p,s)*Q(q,s))

    psi=[]
    for i in range(4):
        num=sum((dg[z]*FF[tuple(sorted((i,z)))] for z in range(4) if z!=i),Fraction(0))
        psi.append(num/(2*tree))

    val=Fraction(0)
    for k,l in EDGES:
        val += Q(*OPP[(k,l)])/FF[(k,l)]*(rd[l]-rd[k])*(psi[l]-psi[k])
    return val

def scan(values):
    checked=0
    negatives=0
    minimum=None
    minimizer=None
    for vals in product(values, repeat=6):
        if not any(vals) or not primitive(vals) or not connected(vals):
            continue
        checked+=1
        z=estar_fraction(vals)
        if z<0:
            negatives+=1
        if minimum is None or z<minimum:
            minimum=z
            minimizer=vals
    return checked, negatives, minimum, minimizer

pos=scan(range(1,5))
bdy=scan(range(0,4))
assert pos==(4031,0,Fraction(0),(1,1,1,1,1,1))
assert bdy[0]==3758 and bdy[1]==0 and bdy[2]==0

print("P0245 one-axis cross-energy exact self-check")
print("symbolic_identity = PASS")
print("E_star = 2(B+C)x^2(U^2-B^2 C^2)/((U-B^2)(U-C^2)V)")
print("U=(A+B+C)^2-x^2")
print("V=A^2+A(B+C)+BC-x^2")
print("spot_A5_B3_C2_x1 =", spot)
print("spot_positive = PASS")
print("positive_grid_1_to_4_primitive_connected =", pos[0], "negative =", pos[1], "minimum =", pos[2])
print("boundary_grid_0_to_3_primitive_connected =", bdy[0], "negative =", bdy[1], "minimum =", bdy[2])
print("GRID_RESULTS_ARE_ROUTE_DIAGNOSTICS_NOT_CONTINUOUS_CERTIFICATES")
print("ALL_EXACT_CHECKS_PASS")
