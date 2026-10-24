#!/usr/bin/env python3
from itertools import product
from functools import lru_cache
from fractions import Fraction
from math import factorial, log10

DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c
    return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0):
    return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def support(label):
    k,a=label
    roots={a} if k=="CO" else set(a)
    out=set(roots)
    for r in roots: out |= neigh(r)
    return out
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u): ed.add(tuple(sorted((u,v))))
    return co,ed
def lg(x):
    return log10(x.numerator)-log10(x.denominator)

# Incoming ten-label terminal alphabet.
LABELS10=(
 ("CO",(0,0)),
 ("O2",((-1,1),(0,1))),
 ("CO",(0,1)),
 ("CO",(1,0)),
 ("O2",((-1,0),(-1,1))),
 ("O2",((0,0),(0,1))),
 ("CO",(-1,1)),
 ("O2",((-1,0),(0,0))),
 ("CO",(-1,0)),
 ("O2",((0,0),(1,0))),
)

# B12/B20/B28 enlargement: two clocks requiring one new lower halo cell,
# plus the three clocks whose two support cells were already present in the
# old full stable-descriptor patch but not promoted to the dynamic projection.
ADDED=(
 ("CO",(0,-1)),
 ("O2",((0,-1),(0,0))),
 ("CO",(1,1)),
 ("O2",((0,1),(1,1))),
 ("O2",((1,0),(1,1))),
)
LABELS15=LABELS10+ADDED

# Old full stable-descriptor patch (16 cells) plus one genuinely new halo cell.
CEL=(( -2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),
     (0,-2),(0,-1),(0,0),(0,1),(0,2),
     (1,-1),(1,0),(1,1),(1,2),(2,0),(2,1))
PATCH=set(CEL)
READ=set()
for lab in LABELS15: READ |= support(lab)
assert READ==PATCH

# Exhaustively verify that LABELS15 is exactly the maximal lattice adsorption
# alphabet whose full reaction support is contained in PATCH.
xmin,xmax=min(x for x,y in PATCH)-1,max(x for x,y in PATCH)+1
ymin,ymax=min(y for x,y in PATCH)-1,max(y for x,y in PATCH)+1
ALL=[]
for x in range(xmin,xmax+1):
    for y in range(ymin,ymax+1):
        lab=("CO",(x,y))
        if support(lab)<=PATCH: ALL.append(lab)
EDGES=set()
for x in range(xmin,xmax+1):
    for y in range(ymin,ymax+1):
        u=(x,y)
        for v in neigh(u):
            e=tuple(sorted((u,v)))
            if e in EDGES: continue
            EDGES.add(e)
            lab=("O2",e)
            if support(lab)<=PATCH: ALL.append(lab)
assert set(ALL)==set(LABELS15)
assert len(ALL)==15

# Recheck the L=8 terminal owned-clock geometry from the incoming certificate.
READ7=set()
for lab in LABELS10[:7]: READ7 |= support(lab)
READ10=set()
for lab in LABELS10: READ10 |= support(lab)
OPARENT={(-3,0),(-2,0)}
CPARENT=(-4,1)
OCC=OPARENT|{CPARENT}
CURSOR1={(0,0),(0,1)}
PARENT_CORE=OCC|CURSOR1
def geometry(L,Rterm):
    Ochild=tuple(sorted(((L-3,0),(L-2,0))))
    Cchild=(L-4,1)
    child_cursor={(L,0),(L,1)}
    pbuf=support(("O2",Ochild))|support(("CO",Cchild))
    down=(L-3,L-2); up=(L-4,L-3)
    guards={(x,-1) for x in down}|{(x,2) for x in up}
    req=pbuf|child_cursor|guards
    stages=[]
    for c in range(2,L+1):
        R=shift(Rterm if c==L else READ7,c-1,0)
        cleared={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared)
        stages.append(("h_term" if c==L else "h",c,S,R))
    final=PARENT_CORE|child_cursor|pbuf|guards
    return stages,final
def deps(L,Rterm):
    stages,final=geometry(L,Rterm)
    co=set(); ed=set()
    for _,_,S,_ in stages:
        a,b=interference(S); co|=a; ed|=b
    a,b=interference(final); co|=a; ed|=b
    return co,ed,stages,final
co8,ed8,st8,final8=deps(8,READ10)
assert not (co8 & shift(co8,16,0))
assert not (ed8 & shifted_edges(ed8,16))
terminal_S=[S for kind,c,S,R in st8 if kind=="h_term"][0]
blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(blocked_edges)
DCOARSE=2*len(interference(terminal_S)[0])+len(interference(terminal_S)[1])
D=DCOARSE-BLOCK
assert (DCOARSE,BLOCK,D)==(231,17,214)

# Every added clock was already inside the old D=214 owned family; hence the
# dependency geometry and hazard are unchanged.  The event only reclassifies
# five previously-killed marks as accepted state-dependent transitions.
co_owned,ed_owned=interference(terminal_S)
for k,a in ADDED:
    if k=="CO":
        assert (a[0]+7,a[1]) in co_owned
    else:
        e=tuple(sorted(((a[0][0]+7,a[0][1]),(a[1][0]+7,a[1][1]))))
        assert e in ed_owned

# Exact 15-label projected Markov chain.
SC=tuple(sorted(PATCH))
IDX={c:i for i,c in enumerate(SC)}
P3=[1]
for _ in range(24): P3.append(P3[-1]*3)
def gettr(s,i): return (s//P3[i])%3
def settr(s,i,v): return s+(v-gettr(s,i))*P3[i]
def nidx(c): return [IDX[q] for q in neigh(c) if q in IDX]
@lru_cache(None)
def trans(s,li):
    kind,arg=LABELS15[li]
    out={}
    if kind=="CO":
        i=IDX[arg]
        if gettr(s,i)!=0: return ((s,72),)
        a=settr(s,i,1)
        os=[q for q in nidx(arg) if gettr(a,q)==2]
        if not os: return ((a,72),)
        assert 72%len(os)==0
        w=72//len(os)
        for q in os:
            t=settr(settr(a,i,0),q,0)
            out[t]=out.get(t,0)+w
    else:
        u,v=arg; iu,iv=IDX[u],IDX[v]
        if gettr(s,iu)!=0 or gettr(s,iv)!=0: return ((s,36),)
        a=settr(settr(s,iu,2),iv,2)
        cu=[q for q in nidx(u) if gettr(a,q)==1] or [-1]
        cv=[q for q in nidx(v) if gettr(a,q)==1] or [-1]
        den=len(cu)*len(cv); assert 36%den==0
        w=36//den
        for qu in cu:
            for qv in cv:
                t=a
                if qu!=-1: t=settr(settr(t,iu,0),qu,0)
                if qv!=-1: t=settr(settr(t,iv,0),qv,0)
                out[t]=out.get(t,0)+w
    return tuple(sorted(out.items()))

TARGET=((-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1))
TIDX=tuple(IDX[c] for c in TARGET)
def target(s): return all(gettr(s,i)==0 for i in TIDX)
FIXED={(-2,0),(-2,1),(-1,0),(-1,1),(0,0),(0,1)}
VAR=[c for c in SC if c not in FIXED]
def enum_inits():
    out=[]
    for vals in product((0,1,2),repeat=len(VAR)):
        d={c:0 for c in FIXED}; d.update(zip(VAR,vals))
        ok=True
        for c in SC:
            a=d[c]
            for q in ((c[0]+1,c[1]),(c[0],c[1]+1)):
                if q in d and (a,d[q]) in ((1,2),(2,1)):
                    ok=False; break
            if not ok: break
        if not ok: continue
        s=sum(d[c]*P3[i] for i,c in enumerate(SC))
        out.append(s)
    return out
INITS=enum_inits()
assert len(INITS)==18257
assert len(set(INITS))==18257

@lru_cache(None)
def A(n,s):
    if n==0: return int(target(s))
    z=0
    for li in range(15):
        for t,w in trans(s,li): z += w*A(n-1,t)
    return z

MINS=[]
for n in range(9):
    MINS.append(min(A(n,s) for s in INITS))
assert MINS==[
 0,0,4320,4611168,3306432960,2501526571776,
 1895247087386112,1437917402423817216,1091797427731911413760
]

def stage_poly(lam):
    H=36*D
    mn=None; arg=None
    for s in INITS:
        z=Fraction(0)
        for n in range(9):
            z += Fraction(A(n,s),factorial(n)*H**n)*lam**n
        if mn is None or z<mn:
            mn=z; arg=s
    return mn,arg

# Certified rational time window.  For r=121/1000, the degree-7 alternating
# Taylor truncation is a lower bound on exp(-r).
lam=Fraction(2121,1000)
r=lam-2
emr=sum(((-1)**k)*r**k/Fraction(factorial(k)) for k in range(8))
assert emr>0
elow=Fraction(32,87)**2*emr
poly,arg=stage_poly(lam)
p15=elow*poly
P15=Fraction(
229764455366845618711724942545032040908678194195997576585319159,
10371549862797001958400000000000000000000000000000000000000000000000)
assert p15==P15
assert arg==129086946

# Incoming b14 terminal factor.
p10=Fraction(
103936503566984629647143194039811221052609,
6221649932703678742303190625000000000000000000)
assert p15>p10
ratio=p15/p10

# Reconstruct incoming b14 and the updated b15.
pboot=Fraction(6183007688263727208881325190913,1204952248442880000000000000000000000000)
p150=Fraction(20193231009117236036,580023299851226806640625)
p167=Fraction(9763107163899290190848,350499257108203128488308305)
p178=Fraction(11133436709205330292,456147586622526713121501)
p187=Fraction(22544728691405487104,1022833101788426753598015)
p197=Fraction(26015322500884764075008,1314271656156778872998881905)
pold=Fraction(7168864776621912190976,514520327344022846669179035)
p218=Fraction(1672277727444803056,105910938933255255436245)
p222=Fraction(40628945155674655856,2670355970159927065747101)
plan198=Fraction(2048,74183769)
b13=pboot*p150*p167*p178*p187*p197*pold*p218*p222*plan198
b14=b13/pold*p10
b15=b14/p10*p15
assert b15>b14

print("PASS exact R08/E0011 maximal-17-cell terminal patch certificate")
print("maximal_support_preserving_labels=",len(ALL))
print("added_labels=",ADDED)
print("stable_initial_states=",len(INITS))
print("L8_shared_CO=",len(co8 & shift(co8,16,0)))
print("L8_shared_O2=",len(ed8 & shifted_edges(ed8,16)))
print("terminal_coarse_D=",DCOARSE,"blocked_units=",BLOCK,"owned_D=",D)
print("min_weighted_counts_n0_to_n8=",MINS)
print("lambda=",f"{lam.numerator}/{lam.denominator}")
print("worst_initial_state_code=",arg)
print("p15_exact=",f"{p15.numerator}/{p15.denominator}")
print("p15_over_p10=",repr(float(ratio)))
print("log10_gain=",repr(lg(ratio)))
print("log10_b14=",repr(lg(b14)))
print("log10_b15=",repr(lg(b15)))
print("b15_gt_b14_exact=",b15>b14)
import sys,os
sys.stdout.flush()
os._exit(0)
