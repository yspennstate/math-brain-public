#!/usr/bin/env python3
# Exact symbolic checker for T07 triangle-seeded matched-right theorem.
# Graph family H_{k,r}=K_3 vee (M_k disjoint_union I_r).
from itertools import combinations
from collections import defaultdict
import math
import sympy as sp

class DSU:
    def __init__(self,n):
        self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b: return False
        self.p[b]=a
        return True

def canon(blocks):
    blocks=[tuple(sorted(b)) for b in blocks]
    return tuple(sorted(blocks,key=lambda b:(b[0],len(b),b)))

PARTS=[
    canon(((0,),(1,),(2,))),
    canon(((0,),(1,2))),
    canon(((0,1),(2,))),
    canon(((0,2),(1,))),
    canon(((0,1,2),)),
]
PINDEX={p:i for i,p in enumerate(PARTS)}

def transfer(nv, edges, forced=()):
    forced=set(forced)
    M=[[0]*5 for _ in range(5)]
    for pi,p in enumerate(PARTS):
        for mask in range(1<<len(edges)):
            if any(((mask>>j)&1)==0 for j in forced):
                continue
            d=DSU(nv)
            for block in p:
                for z in block[1:]:
                    assert d.union(block[0],z)
            ok=True
            for j,(a,b) in enumerate(edges):
                if (mask>>j)&1 and not d.union(a,b):
                    ok=False
                    break
            if not ok: continue
            groups=defaultdict(list)
            for t in (0,1,2):
                groups[d.find(t)].append(t)
            M[pi][PINDEX[canon(groups.values())]] += 1
    return sp.Matrix(M)

STAR=[(0,3),(1,3),(2,3)]
PAIR=[(0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(3,4)]
CORE=[(0,1),(0,2),(1,2)]

S=transfer(4,STAR)
P=transfer(5,PAIR)
I=sp.eye(5)
N=S-4*I
assert N**3==sp.zeros(5)
assert N**2!=sp.zeros(5)
assert P == 23*I + 12*N + sp.Rational(5,3)*(N**2)

def core_vector(forced=()):
    forced=set(forced)
    out=[0]*5
    for mask in range(1<<3):
        if any(((mask>>j)&1)==0 for j in forced):
            continue
        d=DSU(3)
        ok=True
        for j,(a,b) in enumerate(CORE):
            if (mask>>j)&1 and not d.union(a,b):
                ok=False
                break
        if not ok: continue
        groups=defaultdict(list)
        for t in (0,1,2):
            groups[d.find(t)].append(t)
        out[PINDEX[canon(groups.values())]] += 1
    return sp.Matrix([out])

c0=core_vector()
ce=[core_vector((j,)) for j in range(3)]
cef={(i,j):core_vector((i,j)) for i in range(3) for j in range(i+1,3)}
assert list(c0)==[1,1,1,1,3]

O=[transfer(4,STAR,(j,)) for j in range(3)]
OO={(i,j):transfer(4,STAR,(i,j)) for i in range(3) for j in range(i+1,3)}
M=[transfer(5,PAIR,(j,)) for j in range(6)]
Mh=transfer(5,PAIR,(6,))
MM={(i,j):transfer(5,PAIR,(i,j)) for i in range(7) for j in range(i+1,7)}

x,y=sp.symbols("x y", integer=True, nonnegative=True)
u=sp.Rational(12,23)*x + sp.Rational(1,4)*y
v=(sp.Rational(5,69)*x + sp.Rational(72,529)*x*(x-1)
   +sp.Rational(1,32)*y*(y-1) + sp.Rational(3,23)*x*y)
U=I+u*N+v*(N**2)
one=sp.Matrix([1]*5)

def mp(ms):
    R=I
    for A in ms:
        R=R*A
    return R

def count(row,ms):
    return sp.expand((row*mp(ms)*U*one)[0])

def gap(z,ze,zf,zef):
    return sp.expand(ze*zf-z*zef)

T={}
T["CC"]=gap(count(c0,[]),count(ce[0],[]),count(ce[1],[]),count(cef[(0,1)],[]))
for nm,Oj in (("CO_inc",O[0]),("CO_opp",O[2])):
    T[nm]=gap(count(c0,[S]),count(ce[0],[S]),count(c0,[Oj]),count(ce[0],[Oj]))
T["Ch"]=gap(count(c0,[P]),count(ce[0],[P]),count(c0,[Mh]),count(ce[0],[Mh]))
for nm,Mj in (("CM_inc",M[0]),("CM_opp",M[2])):
    T[nm]=gap(count(c0,[P]),count(ce[0],[P]),count(c0,[Mj]),count(ce[0],[Mj]))
T["OO_same"]=gap(count(c0,[S]),count(c0,[O[0]]),count(c0,[O[1]]),count(c0,[OO[(0,1)]]))
for nm,A,B in (("OO_diff_same",O[0],O[0]),("OO_diff_diff",O[0],O[1])):
    T[nm]=gap(count(c0,[S,S]),count(c0,[A,S]),count(c0,[S,B]),count(c0,[A,B]))
T["Oh"]=gap(count(c0,[S,P]),count(c0,[O[0],P]),count(c0,[S,Mh]),count(c0,[O[0],Mh]))
for nm,Mj in (("OM_same",M[0]),("OM_diff",M[1])):
    T[nm]=gap(count(c0,[S,P]),count(c0,[O[0],P]),count(c0,[S,Mj]),count(c0,[O[0],Mj]))
for nm,i,j in (("hM",6,0),("MM_sameendpoint",0,1),("MM_opp_sameT",0,3),("MM_opp_diffT",0,4)):
    A=Mh if i==6 else M[i]
    B=Mh if j==6 else M[j]
    T[nm]=gap(count(c0,[P]),count(c0,[A]),count(c0,[B]),count(c0,[MM[tuple(sorted((i,j)))]]))
for nm,A,B in (("hh_diff",Mh,Mh),("hM_diff",Mh,M[0]),("MM_diff_sameT",M[0],M[0]),("MM_diff_diffT",M[0],M[1])):
    T[nm]=gap(count(c0,[P,P]),count(c0,[A,P]),count(c0,[P,B]),count(c0,[A,B]))

CONSUME={
"CC":(0,0),
"CO_inc":(0,1),"CO_opp":(0,1),
"Ch":(1,0),"CM_inc":(1,0),"CM_opp":(1,0),
"OO_same":(0,1),"OO_diff_same":(0,2),"OO_diff_diff":(0,2),
"Oh":(1,1),"OM_same":(1,1),"OM_diff":(1,1),
"hM":(1,0),"MM_sameendpoint":(1,0),"MM_opp_sameT":(1,0),"MM_opp_diffT":(1,0),
"hh_diff":(2,0),"hM_diff":(2,0),"MM_diff_sameT":(2,0),"MM_diff_diffT":(2,0)
}
assert len(T)==20 and set(T)==set(CONSUME)

def primitive_integer_form(expr):
    poly=sp.Poly(expr,x,y,domain=sp.QQ)
    den=1
    for c in poly.coeffs():
        den=sp.ilcm(den,sp.denom(c))
    ip=sp.Poly(sp.expand(poly.as_expr()*den),x,y,domain=sp.ZZ)
    g=int(den)
    for c in ip.coeffs():
        g=math.gcd(g,abs(int(c)))
    if g>1:
        den=int(den)//g
        ip=sp.Poly(ip.as_expr()/g,x,y,domain=sp.ZZ)
    return int(den),ip

print("S=",S.tolist())
print("P=",P.tolist())
print("N3_ZERO=",N**3==sp.zeros(5),"N2_NONZERO=",N**2!=sp.zeros(5))
print("P_POLY_IDENTITY=",P == 23*I+12*N+sp.Rational(5,3)*(N**2))
print("CORE_VECTOR=",list(c0))

Znorm=sp.expand((c0*U*one)[0])
print("FOREST_COUNT_NORMALIZED=",Znorm)
print("FOREST_COUNT_EXACT: Z(k,r)=23^k 4^r * normalized")

for nm in T:
    den,poly=primitive_integer_form(T[nm])
    coeffs=poly.coeffs()
    assert all(c>0 for c in coeffs)
    a,b=CONSUME[nm]
    print(f"ORBIT {nm} consume_matched={a} consume_ordinary={b} degree={poly.total_degree()} denominator={den}")
    print("  numerator=",sp.expand(poly.as_expr()))
    print("  all_coefficients_strictly_positive=True")

def build_graph(k,r):
    edges=list(CORE)
    cur=3
    for _ in range(k):
        a,b=cur,cur+1
        cur+=2
        for t in (0,1,2):
            edges.append((t,a)); edges.append((t,b))
        edges.append((a,b))
    for _ in range(r):
        a=cur; cur+=1
        for t in (0,1,2):
            edges.append((t,a))
    return cur,edges

def brute(k,r):
    nv,edges=build_graph(k,r)
    m=len(edges)
    Z=0; Ze=[0]*m; Zef=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        d=DSU(nv); chosen=[]; ok=True
        for j,(a,b) in enumerate(edges):
            if (mask>>j)&1:
                if not d.union(a,b):
                    ok=False; break
                chosen.append(j)
        if not ok: continue
        Z+=1
        for j in chosen: Ze[j]+=1
        for aa in range(len(chosen)):
            for bb in range(aa+1,len(chosen)):
                i,j=chosen[aa],chosen[bb]
                Zef[i][j]+=1; Zef[j][i]+=1
    gaps=[(Ze[i]*Ze[j]-Z*Zef[i][j],i,j) for i in range(m) for j in range(i+1,m)]
    assert all(g>0 for g,_,_ in gaps)
    Zn=23**k * 4**r * Znorm.subs({x:k,y:r})
    assert sp.Integer(Z)==sp.simplify(Zn)
    return nv,m,Z,min(g for g,_,_ in gaps)

for kr in ((1,0),(1,1),(2,0)):
    print("BRUTE",kr,brute(*kr))

print("ALL_EXACT_CHECKS_PASS")
