#!/usr/bin/env python3
from itertools import product
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction
from math import factorial

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
def canon(label):
    k,a=label
    return (k,tuple(sorted(a))) if k=='O2' else label

ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED_BASE={(-1,0),(-1,1),(0,0),(0,1)}
LABELS7=(
 ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),
)
EXTRA9=(('O2',((-1,0),(0,0))),('CO',(-1,0)))
LABELS9=tuple(map(canon,LABELS7+EXTRA9))
READ=set()
for lab in LABELS7: READ |= support(lab)
CO_SAFE={('CO',c) for c in READ if support(('CO',c))<=READ}
edges0=set()
for c in READ:
    for q in neigh(c):
        if q in READ: edges0.add(tuple(sorted((c,q))))
O2_SAFE={('O2',e) for e in edges0 if support(('O2',e))<=READ}
MAX_SAFE=CO_SAFE|O2_SAFE
MISSING=tuple(sorted(MAX_SAFE-set(LABELS9),key=str))
assert MISSING==( ('O2',((0,0),(1,0))), )
LABELS10=LABELS9+MISSING
assert len(LABELS10)==10

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
assert (FULL_BASE,len(INITS_BASE))==(50785,12201)
assert (FULL_BEH,len(INITS_BEH))==(7255,1743)

def is_target(s): return all(s[i]==0 for i in TARGET_IDX)

@lru_cache(None)
def trans10(s,li):
    kind,arg=LABELS10[li]; out=defaultdict(int)
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

ALL10=tuple(range(10))
TERM8=tuple(i for i in range(9) if i!=3)
assert sum(72 if LABELS10[i][0]=='CO' else 36 for i in ALL10)==540
assert sum(72 if LABELS10[i][0]=='CO' else 36 for i in TERM8)==432

# Exact first-hit-before-cemetery recursion. G_m/H^m is the probability
# of reaching the six-vacancy target in at most m total protected arrivals,
# before any protected arrival outside the allowed alphabet.
def hit_min(D,inits,allowed,M=8):
    H=36*D
    memo=[{} for _ in range(M+1)]
    def G(n,s):
        if s in memo[n]: return memo[n][s]
        if is_target(s): z=H**n
        elif n==0: z=0
        else:
            z=0
            for li in allowed:
                for t,w in trans10(s,li): z += w*G(n-1,t)
        memo[n][s]=z
        return z
    vals=[]; args=[]
    for m in range(M+1):
        mn=None; arg=None
        for s in inits:
            z=G(m,s)
            if mn is None or z<mn: mn=z; arg=s
        vals.append(Fraction(mn,H**m)); args.append(arg)
    return vals,args

# Existing separately timed endpoint-window factor used by the current corridor.
# It sums accepted histories through n=8 and uses the certified e^{-2}>(32/87)^2.
def fixed_window(D,inits,allowed):
    N=8; H=36*D; FACT=factorial(N); memo=[{} for _ in range(N+1)]
    def A(n,s):
        if s in memo[n]: return memo[n][s]
        if n==0: z=int(is_target(s))
        else:
            z=0
            for li in allowed:
                for t,w in trans10(s,li): z += w*A(n-1,t)
        memo[n][s]=z
        return z
    coeff=[2**n*(FACT//factorial(n))*H**(N-n) for n in range(N+1)]
    mn=min(sum(coeff[n]*A(n,s) for n in range(N+1)) for s in inits)
    return Fraction(32,87)**2*Fraction(mn,FACT*H**N)

SPECS=(
 ('h3',150,INITS_BEH,ALL10),('h4',167,INITS_BEH,ALL10),
 ('h5',178,INITS_BEH,ALL10),('h6',187,INITS_BEH,ALL10),
 ('h7',197,INITS_BEH,ALL10),('h8_terminal',201,INITS_BEH,TERM8),
 ('gdown',218,INITS_BASE,ALL10),('gup',222,INITS_BASE,ALL10),
)
EXPECTED={
 'h3': Fraction(16074639051680369,124556484375000000000),
 'h4': Fraction(30344586508740575,294014018843111629926),
 'h5': Fraction(44282206001815193,489774632850230109696),
 'h6': Fraction(59326158916448255,726723361761569191206),
 'h7': Fraction(80812237507711895,1102468218239207857446),
 'h8_terminal': Fraction(11115007398201754,215801012628378849681),
 'gdown': Fraction(335516236200631,5685932881388232576),
 'gup': Fraction(40748997767361727,716803427892952381824),
}
qprod=Fraction(1,1); fprod=Fraction(1,1); ratios=[]
for name,D,inits,allowed in SPECS:
    vals,args=hit_min(D,inits,allowed,8)
    q=vals[8]; f=fixed_window(D,inits,allowed); r=q/f
    assert q==EXPECTED[name]
    assert all(vals[i+1]>=vals[i] for i in range(8))
    assert r>3
    qprod*=q; fprod*=f; ratios.append(r)
    print(name,'D=',D,'entrances=',len(inits),'labels=',len(allowed))
    print('  hit8=',f'{q.numerator}/{q.denominator}')
    print('  fixed=',f'{f.numerator}/{f.denominator}')
    print('  ratio=',float(r))
    print('  worst_state=',args[8])

R=qprod/fprod
assert R>36000
# Conditional on all eight stagewise first-hit events, each stage consumes <=8 arrivals.
# Waiting times are independent of mark identities; using 8/(D/4)=32/D per stage,
# the conditional expected traversal time is at most EUP. Markov therefore gives
# P(time <= 2 EUP | successful mark histories) >= 1/2.
EUP=sum(Fraction(32,D) for _,D,_,_ in SPECS)
assert EUP==Fraction(15184435759212032,11096310444002025)
print('PASS exact R08/E0011 stopping-frontier local theorem')
print('q_product=',f'{qprod.numerator}/{qprod.denominator}')
print('q_product_decimal=',float(qprod))
print('fixed_product_decimal=',float(fprod))
print('diagnostic_product_ratio=',float(R))
print('conditional_expected_time_upper=',f'{EUP.numerator}/{EUP.denominator}',float(EUP))
print('Markov_time_cutoff_2E=',float(2*EUP),'conditional_finish_probability_at_least=1/2')
print('NOTE: product ratio and time bound are route diagnostics only; no B_cat movement is asserted without deterministic-top stitching.')
