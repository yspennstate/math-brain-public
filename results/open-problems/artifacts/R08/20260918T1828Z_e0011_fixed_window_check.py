#!/usr/bin/env python3
"""
Exact finite checker for R08 / E0011 fixed-window expander certificate.

This extends the 20260918T1727Z budgeted-prefix-DAG checker.  It proves a
uniform continuous-time expander bound in a deterministic time window by
summing every accepted protected-arrival history of lengths 0,...,8.

At p=1/2 the conservative protected block from the earlier R08 certificate
has total protected adsorption rate Lambda=301/2.  In an expander window of
length 4/301, Lambda*tau=2.  Every protected arrival not belonging to the
seven local expander labels is treated as failure.  The seven-label exact
transition law, including instantaneous reaction races, is summed by dynamic
programming.  The rational bound e^{-1}>32/87 is then used.

The checker also assembles the full two-child block using:
  * one six-arrival eraser window of Poisson mean 6,
  * twenty expander windows of Poisson mean 2,
  * two three-arrival planter windows of Poisson mean 3,
and compares the resulting exact lower bound b6 with the previous b5.
"""
from itertools import product
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction
from math import factorial, comb, log10

DIRS=((1,0),(-1,0),(0,1),(0,-1))
ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED={(-1,0),(-1,1),(0,0),(0,1)}

def patch_for(active):
    cells=set(active)
    for x,y in tuple(active):
        for dx,dy in DIRS:
            cells.add((x+dx,y+dy))
    cells=tuple(sorted(cells))
    return cells,{c:i for i,c in enumerate(cells)}

CELLS,FULLIDX=patch_for(ACTIVE)
LABELS=(
    ('CO',(0,0)),
    ('O2',((-1,1),(0,1))),
    ('CO',(0,1)),
    ('CO',(1,0)),
    ('O2',((-1,0),(-1,1))),
    ('O2',((0,0),(0,1))),
    ('CO',(-1,1)),
)

def support(label):
    kind,arg=label
    roots={arg} if kind=='CO' else set(arg)
    out=set(roots)
    for x,y in roots:
        for dx,dy in DIRS:
            out.add((x+dx,y+dy))
    return out

READ=set()
for lab in LABELS:
    READ |= support(lab)
RELEVANT=tuple(sorted((READ & set(CELLS))-FIXED))
IRRELEVANT=tuple(sorted(set(CELLS)-FIXED-set(RELEVANT)))
STATECELLS=tuple(sorted(FIXED|set(RELEVANT)))
IDX={c:i for i,c in enumerate(STATECELLS)}
assert IRRELEVANT==((1,2),(2,1))

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
for vals in product((0,1,2), repeat=len(VAR)):
    sf=[0]*len(CELLS)
    for c,v in zip(VAR,vals):
        sf[FULLIDX[c]]=v
    sf=tuple(sf)
    if not stable_full(sf):
        continue
    full_stable += 1
    inits.add(tuple(sf[FULLIDX[c]] for c in STATECELLS))
assert full_stable==50785
assert len(inits)==12201
INITS=tuple(sorted(inits))

TARGET_IDX=tuple(IDX[c] for c in ACTIVE)
def is_target(s):
    return all(s[i]==0 for i in TARGET_IDX)

# Conditional on one protected arrival in the conservative 144-site /
# 314-edge block: specified CO site = 1/301, specified O2 edge = 1/602.
# Multiplying by 36 clears every reaction-choice denominator.
H=602*36

@lru_cache(None)
def trans_int(s,li):
    kind,arg=LABELS[li]
    out=defaultdict(int)
    if kind=='CO':
        c=arg; a=list(s); i=IDX[c]
        if a[i]!=0:
            out[s]+=72                       # (1/301)*H
            return tuple(out.items())
        a[i]=1; x,y=c
        os=[(x+dx,y+dy) for dx,dy in DIRS
            if (x+dx,y+dy) in IDX and a[IDX[(x+dx,y+dy)]]==2]
        if not os:
            out[tuple(a)]+=72
            return tuple(out.items())
        k=len(os); assert 72%k==0
        w=72//k
        for q in os:
            t=a.copy(); t[i]=0; t[IDX[q]]=0
            out[tuple(t)]+=w
        return tuple(out.items())

    a,b=arg; arr=list(s); ia,ib=IDX[a],IDX[b]
    if arr[ia]!=0 or arr[ib]!=0:
        out[s]+=36                           # (1/602)*H
        return tuple(out.items())
    arr[ia]=arr[ib]=2
    choices=[]
    for c in (a,b):
        x,y=c
        cs=[(x+dx,y+dy) for dx,dy in DIRS
            if (x+dx,y+dy) in IDX and arr[IDX[(x+dx,y+dy)]]==1]
        choices.append(cs if cs else [None])
    den=len(choices[0])*len(choices[1]); assert 36%den==0
    w=36//den
    for qa in choices[0]:
        for qb in choices[1]:
            t=arr.copy()
            if qa is not None:
                t[ia]=0; t[IDX[qa]]=0
            if qb is not None:
                t[ib]=0; t[IDX[qb]]=0
            out[tuple(t)]+=w
    return tuple(out.items())

@lru_cache(None)
def A(n,s):
    if n==0:
        return int(is_target(s))
    z=0
    for li in range(7):
        for t,w in trans_int(s,li):
            z += w*A(n-1,t)
    return z

# Fixed deterministic expander window: mean protected-arrival count lambda=2.
# Sum all accepted histories with n=0,...,N protected arrivals; histories
# containing any other protected label are absent and therefore treated as
# failure.  Use one common integer denominator N!*H^N.
N=8
lam=2
factN=factorial(N)
DEN=factN*H**N
coeff=[
    lam**n*(factN//factorial(n))*H**(N-n)
    for n in range(N+1)
]
mn=None; worst=None
for s in INITS:
    z=sum(coeff[n]*A(n,s) for n in range(N+1))
    if mn is None or z<mn:
        mn=z; worst=s
poly=Fraction(mn,DEN)
assert poly == Fraction(27341216961274435267,3667636251235942483331232)

# Since e^{-1} > 32/87, e^{-2} > (32/87)^2.
c_exp = Fraction(32,87)**2 * poly
assert c_exp == Fraction(874918942760781928544,867510587050151520510440469)
assert c_exp > 0

# B6 parameter scan: among integer Poisson means 1,...,8, using the same
# N=8 truncation and the same rational e^{-1}>32/87 bound, lambda=2 is
# exactly optimal.
scan={}
for LAM in range(1,9):
    coeff_l=[
        LAM**n*(factN//factorial(n))*H**(N-n)
        for n in range(N+1)
    ]
    mn_l=None
    for s in INITS:
        z=sum(coeff_l[n]*A(n,s) for n in range(N+1))
        if mn_l is None or z<mn_l:
            mn_l=z
    poly_l=Fraction(mn_l,DEN)
    scan[LAM]=Fraction(32,87)**LAM * poly_l
assert max(scan,key=scan.get)==2
assert scan[2]==c_exp

# Full fixed-window two-child block.
# Eraser: exactly 6 protected arrivals, one of 4 disjoint robust variants;
# each uses 4 CO labels and 2 O2 labels and has reaction success >=35/486.
eraser = (
    Fraction(32,87)**6
    * Fraction(6**6,factorial(6))
    * Fraction(4*35,486)
    * Fraction(1,301)**4
    * Fraction(1,602)**2
)

# Planter: exactly 3 protected arrivals, one of 4 disjoint robust variants;
# each uses 2 CO labels and 1 O2 label and its reaction outcome is forced.
planter = (
    Fraction(32,87)**3
    * Fraction(3**3,factorial(3))
    * 4
    * Fraction(1,301)**2
    * Fraction(1,602)
)

# Previous exact b5, for comparison.
b5 = (
    Fraction(comb(20,10)*128*35,486)
    * Fraction(1,301)**8
    * Fraction(1,602)**4
    * Fraction(19,32834164804)**20
    * Fraction(32,87)**92
    * Fraction(92**92,factorial(92))
)

# New block uses a fixed order of the 20 expander windows; no interleaving
# multiplicity is counted.  The windows are disjoint time intervals, so the
# strong Markov/independent-increment product gives this lower bound.
b6 = eraser * c_exp**20 * planter**2
ratio=b6/b5
assert ratio > 1

# Deterministic total horizon:
# Lambda=301/2; means are 6, twenty copies of 2, and two copies of 3.
Lambda=Fraction(301,2)
mean_total=6+20*2+2*3
assert mean_total==52
T=Fraction(mean_total,1)/Lambda
assert T==Fraction(104,301)

print("PASS exact R08/E0011 fixed-window all-history certificate")
print("full_stable_states=",full_stable)
print("projected_initial_states=",len(INITS))
print("ignored_cells=",IRRELEVANT)
print("one_step_common_denominator=",H)
print("expander_window_poisson_mean=",lam)
print("expander_truncation_N=",N)
print("expander_poly_exact=",f"{poly.numerator}/{poly.denominator}")
print("expander_worst_state=",worst)
print("expander_fixed_window_lower_exact=",f"{c_exp.numerator}/{c_exp.denominator}")
print("expander_fixed_window_lower_float=",float(c_exp))
print("lambda_scan_float=",{k:float(v) for k,v in scan.items()})
print("lambda_scan_exact_argmax=",max(scan,key=scan.get))
print("eraser_window_lower_float=",float(eraser))
print("planter_window_lower_float=",float(planter))
print("total_block_time=",f"{T.numerator}/{T.denominator}")
print("b6_gt_b5_exact=",b6>b5)
print("ratio_num=",ratio.numerator)
print("ratio_den=",ratio.denominator)
print("log10_b5_for_scale=",log10(b5.numerator)-log10(b5.denominator))
print("log10_b6_for_scale=",log10(b6.numerator)-log10(b6.denominator))
print("log10_gain_over_b5=",log10(ratio.numerator)-log10(ratio.denominator))
print("A_cache=",A.cache_info())
print("transition_cache=",trans_int.cache_info())
