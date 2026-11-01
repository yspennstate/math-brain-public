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
def shift(S,dx=0,dy=0): return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def support(label):
    kind,arg=label
    roots={arg} if kind=='CO' else set(arg)
    out=set(roots)
    for c in roots: out |= neigh(c)
    return out
def canon(label):
    k,a=label
    return (k,tuple(sorted(a))) if k=='O2' else label
def log10frac(x): return log10(x.numerator)-log10(x.denominator)
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    edges=set()
    for u in co:
        for v in neigh(u): edges.add(tuple(sorted((u,v))))
    return co,edges
def d_units(S):
    co,edges=interference(S)
    return 2*len(co)+len(edges),len(co),len(edges)

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
EXTRA9=(('O2',((-1,0),(0,0))),('CO',(-1,0)))
LABELS9=tuple(map(canon,LABELS7+EXTRA9))
READ=set()
for lab in LABELS7: READ |= support(lab)

# B14: target-rectangle Klein four orbit, then retain only support-preserving labels.
def f_id(c): return c
def f_x(c): return (-c[0],c[1])
def f_y(c): return (c[0],1-c[1])
def f_xy(c): return (-c[0],1-c[1])
GROUP=(f_id,f_x,f_y,f_xy)
def transform_label(lab,f):
    k,a=lab
    if k=='CO': return (k,f(a))
    u,v=a
    return canon((k,(f(u),f(v))))
ORBIT={canon(transform_label(lab,f)) for lab in LABELS7 for f in GROUP}
SAFE_ORBIT={lab for lab in ORBIT if support(lab)<=READ}

# B24: enumerate the entire maximal support-preserving square-lattice alphabet.
CO_SAFE={('CO',c) for c in READ if support(('CO',c))<=READ}
edges0=set()
for c in READ:
    for q in neigh(c):
        if q in READ: edges0.add(tuple(sorted((c,q))))
O2_SAFE={('O2',e) for e in edges0 if support(('O2',e))<=READ}
MAX_SAFE=CO_SAFE|O2_SAFE
assert SAFE_ORBIT==MAX_SAFE and len(ORBIT)==13 and len(MAX_SAFE)==10
MISSING=tuple(sorted(MAX_SAFE-set(LABELS9),key=str))
assert MISSING==( ('O2',((0,0),(1,0))), )
LABELS10=LABELS9+MISSING

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

@lru_cache(None)
def A9(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A9(n-1,t) for li in range(9) for t,w in trans10(s,li))
@lru_cache(None)
def A10(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A10(n-1,t) for li in range(10) for t,w in trans10(s,li))

# Terminal support: previous CO(1,0) deletion. Its 8-label language is already maximal.
ALLOWED8=tuple(i for i in range(9) if i!=3)
READ_TERM=set()
for i in ALLOWED8: READ_TERM |= support(LABELS10[i])
CO_TERM={('CO',c) for c in READ_TERM if support(('CO',c))<=READ_TERM}
edges_term=set()
for c in READ_TERM:
    for q in neigh(c):
        if q in READ_TERM: edges_term.add(tuple(sorted((c,q))))
O2_TERM={('O2',e) for e in edges_term if support(('O2',e))<=READ_TERM}
MAX_TERM=CO_TERM|O2_TERM
assert len(MAX_TERM)==8 and MAX_TERM=={LABELS10[i] for i in ALLOWED8}
@lru_cache(None)
def A8(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A8(n-1,t) for li in ALLOWED8 for t,w in trans10(s,li))

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

# Reconstruct entering b10 exactly.
DS_B10=[157,167,184,201,212,221,231,248,252,269,273]
PLAN_B10=Fraction(8192,469285569)
b10=PLAN_B10
for j,D in enumerate(DS_B10):
    if j==0:
        p=expander_best(D,INITS_BASE,A9)
    elif 1<=j<=7:
        p=expander_best(D,INITS_BEH,A9)
    elif j==8:
        p=expander_best(D,INITS_BEH,A8)
    else:
        p=expander_best(D,INITS_BASE,A9)
    b10*=p
assert abs(log10frac(b10)-(-57.57813815284567))<1e-12

CURSOR={(x,y) for x in (0,1) for y in (0,1)}
OPARENT={(-3,0),(-2,0)}
CPARENT=(-4,1)
OCC=OPARENT|{CPARENT}
PARENT_CORE=OCC|CURSOR

def read_down(a): return {(a+y,-x) for x,y in READ}
def read_up(a): return {(a+y,x+1) for x,y in READ}

def geometry(L):
    Ochild=tuple(sorted(((L-3,0),(L-2,0))))
    Cchild=(L-4,1)
    child_cursor={(x,y) for x in (L,L+1) for y in (0,1)}
    pbuf=support(('O2',Ochild))|support(('CO',Cchild))
    down_block=(L-3,L-2)
    up_block=(L-4,L-3)
    guards={(x,-1) for x in down_block}|{(x,2) for x in up_block}
    corridor={(x,y) for x in range(0,L+2) for y in (0,1)}
    hreads=[]
    for c in range(2,L+2):
        R=shift(READ_TERM if c==L+1 else READ,c-1,0)
        hreads.append(R)
    req=pbuf|child_cursor|guards
    stages=[]
    for c,R in zip(range(2,L+2),hreads):
        cleared_before={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared_before)
        stages.append(('h6' if c==L+1 else 'h',c,S,d_units(S),R))
    greads=[read_down(down_block[0]),read_up(up_block[0])]
    cleared=corridor.copy()
    S=PARENT_CORE|greads[0]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gd',0,S,d_units(S),greads[0]))
    cleared|={(x,-1) for x in down_block}
    S=PARENT_CORE|greads[1]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gu',1,S,d_units(S),greads[1]))
    finalS=PARENT_CORE|child_cursor|pbuf|guards
    return stages,finalS,d_units(finalS),Ochild,Cchild,child_cursor,pbuf,guards

def full_union(L):
    stages,finalS,Df,*rest=geometry(L)
    co=set(); edges=set()
    for _,_,S,_,_ in stages:
        a,b=interference(S); co|=a; edges|=b
    a,b=interference(finalS); co|=a; edges|=b
    return stages,finalS,Df,co,edges,rest

# Refined spacing: L=8 has one coarse shared edge, irrelevant to the left block.
st8,final8,Df8,co8,ed8,rest8=full_union(8)
shared_co8=co8 & shift(co8,16,0)
shared_ed8=ed8 & shifted_edges(ed8,16)
E8=((10,1),(11,1))
assert shared_co8==set() and shared_ed8=={E8}
seen=[]
for j,(_,_,S,_,_) in enumerate(st8):
    if E8 in interference(S)[1]:
        seen.append(j)
        assert support(('O2',E8)) & S == {(9,1)}
assert seen==[7,8,9]
assert support(('O2',E8)) & final8 == {(9,1)}
assert (9,1) in rest8[2]
ed8_refined=set(ed8); ed8_refined.remove(E8)
assert not (co8 & shift(co8,16,0))
assert not (ed8_refined & shifted_edges(ed8_refined,16))

# L=7 obstruction in the frozen seed/cursor family.
st7,final7,Df7,co7,ed7,rest7=full_union(7)
E7=((8,1),(9,1))
assert E7 in (ed7 & shifted_edges(ed7,14))
assert (8,1) in rest7[2]
assert (10,1)==(CPARENT[0]+14,CPARENT[1]) and (10,1) in neigh((9,1))

# Parent seed occupations make 3 CO clocks and 11 O2-edge clocks identically blocked.
blocked_co=set(OCC)
blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK_UNITS=2*len(blocked_co)+len(blocked_edges)
assert (len(blocked_co),len(blocked_edges),BLOCK_UNITS)==(3,11,17)
for kind,idx,S,d,R in st8:
    assert not (R & OCC)
Ochild8,Cchild8,child_cursor8,pbuf8,guards8=rest8
assert not (support(('O2',Ochild8)) & OCC)
assert not (support(('CO',Cchild8)) & OCC)

# L=8 certificate: 10 local stages instead of 11, maximal support-preserving local dynamics,
# 17 fixed blocked parent units removed everywhere, and E8 removed where irrelevant.
DS8_OLD=[]; DS8_NEW=[]; stage_probs=[]
b11=Fraction(1,1)
for j,(kind,idx,S,counts,R) in enumerate(st8):
    Dold=counts[0]
    e8_here=1 if E8 in interference(S)[1] else 0
    Dnew=Dold-BLOCK_UNITS-e8_here
    DS8_OLD.append(Dold); DS8_NEW.append(Dnew)
    if kind=='h':
        inits=INITS_BASE if idx==2 else INITS_BEH
        Afun=A10
    elif kind=='h6':
        inits=INITS_BEH
        Afun=A8
    else:
        inits=INITS_BASE
        Afun=A10
    p=expander_best(Dnew,inits,Afun)
    stage_probs.append((kind,idx,Dold,Dnew,p))
    b11*=p
DPLAN8_OLD=Df8[0]
DPLAN8_NEW=DPLAN8_OLD-BLOCK_UNITS-1
assert (DPLAN8_OLD,DPLAN8_NEW)==(243,225)
PLAN8=Fraction(32,87)**2*Fraction(8,DPLAN8_NEW**2)
b11*=PLAN8
assert b11>b10
assert DS8_OLD==[157,167,184,201,212,225,242,246,263,263]
assert DS8_NEW==[140,150,167,184,195,208,225,228,245,245]

print('PASS exact R08/E0011 L=8 refined-causal-spacing certificate')
print('symmetry_orbit_size=',len(ORBIT),'safe_orbit_size=',len(SAFE_ORBIT))
print('max_support_preserving_size=',len(MAX_SAFE),'new_safe_label=',MISSING)
print('terminal_max_support_preserving_size=',len(MAX_TERM))
print('base_min_A4_9_10=',min(A9(4,s) for s in INITS_BASE),min(A10(4,s) for s in INITS_BASE))
print('parent_blocked_CO_O2_Dunits=',len(blocked_co),len(blocked_edges),BLOCK_UNITS)
print('L8_coarse_shared_CO=',sorted(shared_co8))
print('L8_coarse_shared_edges=',sorted(shared_ed8))
print('L8_shared_edge_stage_indices=',seen)
print('L8_shared_edge_support_intersection_final=',sorted(support(('O2',E8)) & final8))
print('L8_refined_distance_two_disjoint=',not(ed8_refined & shifted_edges(ed8_refined,16)))
print('L7_unavoidable_shared_edge=',E7,'child_root=',(8,1),'shifted_parent_CO=',(10,1))
print('L8_stage_D_old=',DS8_OLD)
print('L8_stage_D_new=',DS8_NEW)
print('L8_planter_D_old_new=',DPLAN8_OLD,DPLAN8_NEW)
for kind,idx,Do,Dn,p in stage_probs:
    print('stage',kind,idx,'D_old_new=',Do,Dn,'log10p=',repr(log10frac(p)))
print('b11_gt_b10_exact=',b11>b10)
print('log10_b10_diagnostic=',repr(log10frac(b10)))
print('log10_b11_diagnostic=',repr(log10frac(b11)))
print('log10_gain_diagnostic=',repr(log10frac(b11/b10)))
print('gain_exact=',f'{(b11/b10).numerator}/{(b11/b10).denominator}')
print('b11_exact=',f'{b11.numerator}/{b11.denominator}')
