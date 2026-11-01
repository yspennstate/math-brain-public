#!/usr/bin/env python3
from itertools import product
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction
from math import factorial, log10

DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c
    return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0):
    return {(x+dx,y+dy) for x,y in S}
def support(label):
    kind,arg=label
    roots={arg} if kind=="CO" else set(arg)
    out=set(roots)
    for c in roots: out |= neigh(c)
    return out
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    edges=set()
    for u in co:
        for v in neigh(u):
            edges.add(tuple(sorted((u,v))))
    return co,edges
def d_units(S):
    co,edges=interference(S)
    return 2*len(co)+len(edges),len(co),len(edges)

# expander exact local chain
ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED={(-1,0),(-1,1),(0,0),(0,1)}
LABELS=(
 ('CO',(0,0)),
 ('O2',((-1,1),(0,1))),
 ('CO',(0,1)),
 ('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),
 ('O2',((0,0),(0,1))),
 ('CO',(-1,1)),
)
def patch_for(active):
    cells=set(active)
    for c in tuple(active): cells |= neigh(c)
    cells=tuple(sorted(cells)); return cells,{c:i for i,c in enumerate(cells)}
CELLS,FULLIDX=patch_for(ACTIVE)
READ=set()
for lab in LABELS: READ |= support(lab)
assert len(READ)==14 and READ <= set(CELLS)
STATECELLS=tuple(sorted(READ))
IDX={c:i for i,c in enumerate(STATECELLS)}
VAR=tuple(c for c in CELLS if c not in FIXED)
def stable_full(s):
    for x,y in CELLS:
        a=s[FULLIDX[(x,y)]]
        for dx,dy in ((1,0),(0,1)):
            q=(x+dx,y+dy)
            if q in FULLIDX and (a,s[FULLIDX[q]]) in ((1,2),(2,1)):
                return False
    return True
inits=set(); full_stable=0
for vals in product((0,1,2),repeat=len(VAR)):
    sf=[0]*len(CELLS)
    for c,v in zip(VAR,vals): sf[FULLIDX[c]]=v
    sf=tuple(sf)
    if stable_full(sf):
        full_stable += 1
        inits.add(tuple(sf[FULLIDX[c]] for c in STATECELLS))
assert full_stable==50785 and len(inits)==12201
INITS=tuple(sorted(inits))
TARGET_IDX=tuple(IDX[c] for c in ACTIVE)
def is_target(s): return all(s[i]==0 for i in TARGET_IDX)

@lru_cache(None)
def trans_int(s,li):
    kind,arg=LABELS[li]; out=defaultdict(int)
    if kind=="CO":
        c=arg; a=list(s); i=IDX[c]
        if a[i]!=0:
            out[s]+=72; return tuple(out.items())
        a[i]=1
        os=[q for q in neigh(c) if q in IDX and a[IDX[q]]==2]
        if not os:
            out[tuple(a)]+=72; return tuple(out.items())
        assert 72%len(os)==0; w=72//len(os)
        for q in os:
            t=a.copy(); t[i]=0; t[IDX[q]]=0; out[tuple(t)]+=w
        return tuple(out.items())
    a,b=arg; arr=list(s); ia,ib=IDX[a],IDX[b]
    if arr[ia]!=0 or arr[ib]!=0:
        out[s]+=36; return tuple(out.items())
    arr[ia]=arr[ib]=2
    choices=[]
    for c in (a,b):
        cs=[q for q in neigh(c) if q in IDX and arr[IDX[q]]==1]
        choices.append(cs if cs else [None])
    den=len(choices[0])*len(choices[1]); assert 36%den==0
    w=36//den
    for qa in choices[0]:
        for qb in choices[1]:
            t=arr.copy()
            if qa is not None: t[ia]=0; t[IDX[qa]]=0
            if qb is not None: t[ib]=0; t[IDX[qb]]=0
            out[tuple(t)]+=w
    return tuple(out.items())

@lru_cache(None)
def A(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A(n-1,t) for li in range(7) for t,w in trans_int(s,li))

N=8; FACT=factorial(N)
def expander_lower(D):
    H=36*D
    den=FACT*H**N
    vals={}
    for lam in range(1,9):
        coeff=[lam**n*(FACT//factorial(n))*H**(N-n) for n in range(N+1)]
        mn=min(sum(coeff[n]*A(n,s) for n in range(N+1)) for s in INITS)
        vals[lam]=Fraction(32,87)**lam*Fraction(mn,den)
    best=max(vals,key=vals.get)
    assert best==2
    return vals[best]

# macro geometry
Q0={(x,y) for x in range(4) for y in range(4)}
Q1={(x,y) for x in range(10,14) for y in range(4)}
ERASE_LABELS=(("CO",(0,1)),("O2",((-1,0),(-1,1))),("CO",(0,0)))
ERASE_READ=set()
for lab in ERASE_LABELS: ERASE_READ |= support(lab)
ERASE_READ=shift(ERASE_READ,2,1)
assert ERASE_READ <= Q0
PLANT_LABELS=(("O2",((1,1),(1,2))),("CO",(2,1)))
PLANT_READ=set()
for lab in PLANT_LABELS: PLANT_READ |= support(lab)
assert PLANT_READ <= Q0

D_erase,ce,ee=d_units(Q0)
D_plant,cp,ep=d_units(Q0|Q1)
assert (D_erase,ce,ee)==(140,32,76)
assert (D_plant,cp,ep)==(280,64,152)

def cursor(cols,rows):
    return {(x,y) for x in cols for y in rows}
def stored_right(last):
    if last<10: return set()
    return {(x,y) for x in range(10,last+1) for y in range(4)}

Bsites={(x,y) for x in range(-2,16) for y in range(-2,6)}
stage_sets=[]; stage_D=[]; stage_counts=[]
for c in range(4,14):
    S_top=Q0|stored_right(c-1)|cursor([c-2,c-1],{2,3})|shift(READ,c-1,0)
    S_bot=Q0|stored_right(c-1)|{(c,0),(c,1)}|cursor([c-1,c],{0,1})|shift(READ,c-1,2)
    for kind,S in (("top",S_top),("bot",S_bot)):
        D,nc,ne=d_units(S)
        stage_sets.append((c,kind,S))
        stage_D.append(D); stage_counts.append((nc,ne))
        co,edges=interference(S)
        assert co <= Bsites
        assert all((a in Bsites) or (b in Bsites) for a,b in edges)
EXPECTED=[175,179,200,204,225,226,247,247,265,262,276,272,278,274,278,274,278,282,290,294]
assert stage_D==EXPECTED

# Accepted labels adsorb only inside ACTIVE; shell/parked vacancies can only be removed, not newly occupied.
ROOTS=set()
for kind,arg in LABELS:
    ROOTS |= ({arg} if kind=="CO" else set(arg))
assert ROOTS <= ACTIVE

c_stage=[expander_lower(D) for D in stage_D]

# Previous b6
c_global=expander_lower(602)
assert c_global==Fraction(874918942760781928544,867510587050151520510440469)
eraser_global=(Fraction(32,87)**6*Fraction(6**6,factorial(6))*Fraction(4*35,486)
               *Fraction(1,301)**4*Fraction(1,602)**2)
planter_global=(Fraction(32,87)**3*Fraction(3**3,factorial(3))*4
                *Fraction(1,301)**2*Fraction(1,602))
b6=eraser_global*c_global**20*planter_global**2

# Localized cone certificate
eraser=(Fraction(32,87)**6*Fraction(6**6,factorial(6))*Fraction(4*35,486)
        *Fraction(2,D_erase)**4*Fraction(1,D_erase)**2)
planter=(Fraction(32,87)**3*Fraction(3**3,factorial(3))*4
         *Fraction(2,D_plant)**2*Fraction(1,D_plant))
b7=eraser
for c in c_stage: b7*=c
b7*=planter**2
assert b7>b6
ratio=b7/b6

T7=Fraction(6,1)/Fraction(D_erase,4)
for D in stage_D: T7 += Fraction(2,1)/Fraction(D,4)
T7 += 2*Fraction(3,1)/Fraction(D_plant,4)
assert T7==Fraction(7059902017557060049739597,7762331170048708744504650)

def log10frac(x): return log10(x.numerator)-log10(x.denominator)

print("PASS exact R08/E0011 localized interference-cone certificate")
print("full_stable_states=",full_stable)
print("projected_initial_states=",len(INITS))
print("eraser_interference=(D,COsites,O2edges)=", (D_erase,ce,ee))
print("planter_pair_interference=(D,COsites,O2edges)=", (D_plant,cp,ep))
print("stage_D_units=",stage_D)
print("stage_clock_counts=",stage_counts)
print("stage_poisson_mean_argmax_all=", [2]*20)
print("stage_expander_lower_exact=")
for D,c in zip(stage_D,c_stage):
    print(D, f"{c.numerator}/{c.denominator}")
print("b7_gt_b6_exact=",b7>b6)
print("log10_b6_diagnostic=",log10frac(b6))
print("log10_b7_diagnostic=",log10frac(b7))
print("log10_gain_diagnostic=",log10frac(ratio))
print("T7_exact=",f"{T7.numerator}/{T7.denominator}")
print("T7_float=",float(T7))
print("ratio_num_digits=",len(str(ratio.numerator)),"ratio_den_digits=",len(str(ratio.denominator)))
