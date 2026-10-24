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
def support(label):
    kind,arg=label
    roots={arg} if kind=='CO' else set(arg)
    out=set(roots)
    for c in roots: out |= neigh(c)
    return out

def log10frac(x): return log10(x.numerator)-log10(x.denominator)

ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED_BASE={(-1,0),(-1,1),(0,0),(0,1)}
LABELS7=(
 ('CO',(0,0)),
 ('O2',((-1,1),(0,1))),
 ('CO',(0,1)),
 ('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),
 ('O2',((0,0),(0,1))),
 ('CO',(-1,1)),
)
# B27/B19 augmentation: add the two vertically-reflected labels whose supports
# are already contained in the old read set. This changes no protected geometry.
EXTRA=(('O2',((-1,0),(0,0))),('CO',(-1,0)))
LABELS9=LABELS7+EXTRA
READ=set()
for lab in LABELS7: READ |= support(lab)
assert all(support(lab) <= READ for lab in EXTRA)
STATECELLS=tuple(sorted(READ)); IDX={c:i for i,c in enumerate(STATECELLS)}
TARGET_IDX=tuple(IDX[c] for c in ACTIVE)

CELLS=set(ACTIVE)
for c in tuple(ACTIVE): CELLS |= neigh(c)
CELLS=tuple(sorted(CELLS)); FULLIDX={c:i for i,c in enumerate(CELLS)}

def stable_full(s):
    for x,y in CELLS:
        a=s[FULLIDX[(x,y)]]
        for dx,dy in ((1,0),(0,1)):
            q=(x+dx,y+dy)
            if q in FULLIDX and (a,s[FULLIDX[q]]) in ((1,2),(2,1)):
                return False
    return True

def enumerate_inits(fixed_zero):
    var=tuple(c for c in CELLS if c not in fixed_zero)
    inits=set(); full=0
    for vals in product((0,1,2),repeat=len(var)):
        sf=[0]*len(CELLS)
        for c,v in zip(var,vals): sf[FULLIDX[c]]=v
        sf=tuple(sf)
        if stable_full(sf):
            full+=1
            inits.add(tuple(sf[FULLIDX[c]] for c in STATECELLS))
    return tuple(sorted(inits)),full

INITS_BASE,FULL_BASE=enumerate_inits(FIXED_BASE)
INITS_BEH,FULL_BEH=enumerate_inits(FIXED_BASE|{(-2,0),(-2,1)})
assert FULL_BASE==50785 and len(INITS_BASE)==12201
assert FULL_BEH==7255 and len(INITS_BEH)==1743

def is_target(s): return all(s[i]==0 for i in TARGET_IDX)

@lru_cache(None)
def trans9(s,li):
    kind,arg=LABELS9[li]; out=defaultdict(int)
    if kind=='CO':
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
def A7(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A7(n-1,t) for li in range(7) for t,w in trans9(s,li))
@lru_cache(None)
def A9(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A9(n-1,t) for li in range(9) for t,w in trans9(s,li))

ALLOWED6=tuple(i for i in range(7) if i!=3)
ALLOWED8=tuple(i for i in range(9) if i!=3)
READ6=set()
for li in ALLOWED6: READ6 |= support(LABELS9[li])
READ8=set()
for li in ALLOWED8: READ8 |= support(LABELS9[li])
assert READ8==READ6
@lru_cache(None)
def A6(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A6(n-1,t) for li in ALLOWED6 for t,w in trans9(s,li))
@lru_cache(None)
def A8(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A8(n-1,t) for li in ALLOWED8 for t,w in trans9(s,li))

N=8; FACT=factorial(N)
def expander_best(D,inits,Afun):
    H=36*D; den=FACT*H**N; vals={}
    for lam in range(1,9):
        coeff=[lam**n*(FACT//factorial(n))*H**(N-n) for n in range(N+1)]
        mn=min(sum(coeff[n]*Afun(n,s) for n in range(N+1)) for s in inits)
        vals[lam]=Fraction(32,87)**lam*Fraction(mn,den)
    best=max(vals,key=vals.get)
    assert best==2
    return vals[best]

Ds=[157,167,184,201,212,221,231,248,252,269,273]
PLAN=Fraction(8192,469285569)

old=[]; new=[]
for j,D in enumerate(Ds):
    if j==0:
        po=expander_best(D,INITS_BASE,A7); pn=expander_best(D,INITS_BASE,A9)
    elif 1<=j<=7:
        po=expander_best(D,INITS_BEH,A7); pn=expander_best(D,INITS_BEH,A9)
    elif j==8:
        po=expander_best(D,INITS_BEH,A6); pn=expander_best(D,INITS_BEH,A8)
    else:
        po=expander_best(D,INITS_BASE,A7); pn=expander_best(D,INITS_BASE,A9)
    assert pn>po
    old.append(po); new.append(pn)

b9=PLAN
b10=PLAN
for p in old: b9*=p
for p in new: b10*=p
assert b10>b9

assert min(A9(4,s) for s in INITS_BASE)==134369280
assert min(A7(4,s) for s in INITS_BASE)==127650816
assert min(A8(5,s) for s in INITS_BEH)==48399814656
assert min(A6(5,s) for s in INITS_BEH)==5724131328

print('PASS exact R08/E0011 reflected-label augmentation certificate')
print('full_stable_base=',FULL_BASE,'projected_base=',len(INITS_BASE))
print('full_stable_behind=',FULL_BEH,'projected_behind=',len(INITS_BEH))
print('extra_labels=',EXTRA)
print('read_set_unchanged=',all(support(l)<=READ for l in EXTRA))
print('terminal_read_set_unchanged=',READ8==READ6)
print('base_min_A4_old_new=',min(A7(4,s) for s in INITS_BASE),min(A9(4,s) for s in INITS_BASE))
print('terminal_min_A5_old_new=',min(A6(5,s) for s in INITS_BEH),min(A8(5,s) for s in INITS_BEH))
print('stage_D_units=',Ds)
for i,(D,po,pn) in enumerate(zip(Ds,old,new)):
    print('stage',i,'D=',D,'log10_old=',repr(log10frac(po)),'log10_new=',repr(log10frac(pn)),'gain=',repr(log10frac(pn/po)))
print('b10_gt_b9_exact=',b10>b9)
print('log10_b9_diagnostic=',repr(log10frac(b9)))
print('log10_b10_diagnostic=',repr(log10frac(b10)))
print('log10_gain_diagnostic=',repr(log10frac(b10/b9)))
print('gain_exact=',f'{(b10/b9).numerator}/{(b10/b9).denominator}')
print('b10_exact=',f'{b10.numerator}/{b10.denominator}')
