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
def support(label):
    kind,arg=label
    roots={arg} if kind=='CO' else set(arg)
    out=set(roots)
    for c in roots: out |= neigh(c)
    return out
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
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def log10frac(x): return log10(x.numerator)-log10(x.denominator)

ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED_BASE={(-1,0),(-1,1),(0,0),(0,1)}
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
STATECELLS=tuple(sorted(READ)); IDX={c:i for i,c in enumerate(STATECELLS)}
TARGET_IDX=tuple(IDX[c] for c in ACTIVE)

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
BEHIND_FIXED=FIXED_BASE|{(-2,0),(-2,1)}
INITS_BEH,FULL_BEH=enumerate_inits(BEHIND_FIXED)
assert FULL_BASE==50785 and len(INITS_BASE)==12201
assert FULL_BEH==7255 and len(INITS_BEH)==1743

def is_target(s): return all(s[i]==0 for i in TARGET_IDX)

@lru_cache(None)
def trans_int(s,li):
    kind,arg=LABELS[li]; out=defaultdict(int)
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
    return sum(w*A7(n-1,t) for li in range(7) for t,w in trans_int(s,li))

ALLOWED6=tuple(i for i in range(7) if i!=3)
READ6=set()
for li in ALLOWED6: READ6 |= support(LABELS[li])
assert READ-READ6=={(1,-1),(2,0)}
@lru_cache(None)
def A6(n,s):
    if n==0: return int(is_target(s))
    return sum(w*A6(n-1,t) for li in ALLOWED6 for t,w in trans_int(s,li))
assert min(A6(5,s) for s in INITS_BEH)>0
assert min(A6(4,s) for s in INITS_BEH)==0

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

OLD_D=[174,178,195,199,220,221,242,242,260,257,271,278,281,290,302,307,324,325]
PLAN8=Fraction(256,44876601)
b8=PLAN8
for D in OLD_D: b8*=expander_best(D,INITS_BASE,A7)

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
    if not pbuf <= corridor|guards: return None
    hreads=[]
    for c in range(2,L+2):
        R=shift(READ6 if c==L+1 else READ,c-1,0)
        hreads.append(R)
    if any(OCC & R for R in hreads): return None
    greads=[read_down(down_block[0]),read_up(up_block[0])]
    if any(OCC & R for R in greads): return None
    req=pbuf|child_cursor|guards
    stages=[]
    for c,R in zip(range(2,L+2),hreads):
        cleared_before={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared_before)
        stages.append(('h6' if c==L+1 else 'h',c,S,d_units(S)))
    cleared=corridor.copy()
    S=PARENT_CORE|greads[0]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gd',0,S,d_units(S)))
    cleared|={(x,-1) for x in down_block}
    S=PARENT_CORE|greads[1]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gu',1,S,d_units(S)))
    cleared|={(x,2) for x in up_block}
    finalS=PARENT_CORE|child_cursor|pbuf|guards
    Df=d_units(finalS)
    co=set(); edges=set()
    for _,_,S,_ in stages:
        a,b=interference(S); co|=a; edges|=b
    a,b=interference(finalS); co|=a; edges|=b
    disj=not(co&shift(co,2*L,0)) and not(edges&shifted_edges(edges,2*L))
    return {'stages':stages,'Df':Df,'co':co,'edges':edges,'disj':disj,
            'Ochild':Ochild,'Cchild':Cchild,'child_cursor':child_cursor,
            'pbuf':pbuf,'guards':guards,'corridor':corridor}

G={L:geometry(L) for L in range(6,10)}
assert all(G[L] is not None for L in G)
assert [G[L]['disj'] for L in range(6,10)]==[False,False,False,True]
assert len(G[8]['co']&shift(G[8]['co'],16,0))==0
assert G[8]['edges']&shifted_edges(G[8]['edges'],16)=={((10,1),(11,1))}

g=G[9]
assert g['Ochild']==((6,0),(7,0)) and g['Cchild']==(5,1)
assert g['Df']==(249,55,139)
Ds=[row[3][0] for row in g['stages']]
assert Ds==[157,167,184,201,212,221,231,248,252,269,273]
assert (min(x for x,y in g['co']),max(x for x,y in g['co']))==(-5,11)
assert g['disj']

Df=g['Df'][0]
PLANT9=Fraction(32,87)**2*Fraction(8,Df**2)
b9=PLANT9
stage_probs=[]
for kind,idx,S,counts in g['stages']:
    D=counts[0]
    if kind=='h':
        ins=INITS_BASE if idx==2 else INITS_BEH
        p=expander_best(D,ins,A7)
    elif kind=='h6':
        p=expander_best(D,INITS_BEH,A6)
    else:
        p=expander_best(D,INITS_BASE,A7)
    stage_probs.append((kind,idx,D,p))
    b9*=p
assert b9>b8

assert g['pbuf'] <= g['corridor']|g['guards']
assert all(o not in neigh(g['Cchild']) for o in g['Ochild'])
for kind,idx,S,counts in g['stages']:
    assert OCC <= S and CURSOR <= S
assert g['Ochild']==tuple(sorted((x+9,y) for x,y in OPARENT))
assert g['Cchild']==(CPARENT[0]+9,CPARENT[1])
assert g['child_cursor']==shift(CURSOR,9,0)

print('PASS exact R08/E0011 thin-corridor shield certificate')
print('full_stable_base=',FULL_BASE,'projected_base=',len(INITS_BASE))
print('full_stable_behind=',FULL_BEH,'projected_behind=',len(INITS_BEH))
print('terminal_removed_labels=CO(1,0)')
print('terminal_removed_read_cells=',sorted(READ-READ6))
print('terminal_sixlabel_min_A4=',min(A6(4,s) for s in INITS_BEH))
print('terminal_sixlabel_min_A5=',min(A6(5,s) for s in INITS_BEH))
print('spacing_disjoint_L6_L9=',{L:G[L]['disj'] for L in G})
print('L8_unique_shared_edge=',sorted(G[8]['edges']&shifted_edges(G[8]['edges'],16)))
print('selected_L=9')
print('selected_parent_Oedge=',tuple(sorted(OPARENT)))
print('selected_parent_CO=',CPARENT)
print('selected_child_Oedge=',g['Ochild'])
print('selected_child_CO=',g['Cchild'])
print('selected_child_cursor=',sorted(g['child_cursor']))
print('selected_guard_cells=',sorted(g['guards']))
print('selected_stage_D_units=',Ds)
print('selected_final_D_counts=',g['Df'])
print('full_clock_union_CO_x_span=',(min(x for x,y in g['co']),max(x for x,y in g['co'])))
print('distance_two_shift=18 disjoint=',g['disj'])
print('planter_two_orders_exact=',f'{PLANT9.numerator}/{PLANT9.denominator}')
print('b9_gt_b8_exact=',b9>b8)
print('log10_b8_diagnostic=',repr(log10frac(b8)))
print('log10_b9_diagnostic=',repr(log10frac(b9)))
print('log10_gain_diagnostic=',repr(log10frac(b9/b8)))
print('b9_num_digits=',len(str(b9.numerator)),'b9_den_digits=',len(str(b9.denominator)))
for kind,idx,D,p in stage_probs:
    print('stage',kind,idx,'D=',D,'log10p=',repr(log10frac(p)))
print('b9_exact=',f'{b9.numerator}/{b9.denominator}')
print('gain_exact=',f'{(b9/b8).numerator}/{(b9/b8).denominator}')
