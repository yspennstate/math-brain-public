#!/usr/bin/env python3
from itertools import product, combinations
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
        for v in neigh(u): edges.add(tuple(sorted((u,v))))
    return co,edges
def d_units(S):
    co,edges=interference(S)
    return 2*len(co)+len(edges),len(co),len(edges)
def log10frac(x):
    return log10(x.numerator)-log10(x.denominator)

# Exact seven-label local vacancy-expander chain from prior R08 certificates.
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
STATECELLS=tuple(sorted(READ)); IDX={c:i for i,c in enumerate(STATECELLS)}
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
        full_stable+=1
        inits.add(tuple(sf[FULLIDX[c]] for c in STATECELLS))
assert full_stable==50785 and len(inits)==12201
INITS=tuple(sorted(inits)); TARGET_IDX=tuple(IDX[c] for c in ACTIVE)
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
@lru_cache(None)
def expander_lower(D):
    H=36*D; den=FACT*H**N; vals={}
    for lam in range(1,9):
        coeff=[lam**n*(FACT//factorial(n))*H**(N-n) for n in range(N+1)]
        mn=min(sum(coeff[n]*A(n,s) for n in range(N+1)) for s in INITS)
        vals[lam]=Fraction(32,87)**lam*Fraction(mn,den)
    best=max(vals,key=vals.get)
    assert best==2
    return vals[best]

# Exact previous b7 baseline from the immediately preceding immutable R08 report.
OLD_D=[175,179,200,204,225,226,247,247,265,262,276,272,278,274,278,274,278,282,290,294]
eraser_old=(Fraction(32,87)**6*Fraction(6**6,factorial(6))*Fraction(4*35,486)
            *Fraction(2,140)**4*Fraction(1,140)**2)
planter_old=(Fraction(32,87)**3*Fraction(3**3,factorial(3))*4
             *Fraction(2,280)**2*Fraction(1,280))
b7=eraser_old
for D in OLD_D: b7*=expander_lower(D)
b7*=planter_old**2

# B3/B15 candidate family: an eight-vacancy 4x2 cursor, one O2 pair, and one CO site.
CURSOR={(x,y) for x in (0,1) for y in range(4)}

def candidate_geometry(L,Oedge_parent,C_parent):
    occ=set(Oedge_parent)|{C_parent}
    # Seed species must remain untouched by every accepted local expander label.
    for c in range(2,L+2):
        if occ & (shift(READ,c-1,0)|shift(READ,c-1,2)):
            return None
    parent_core=occ|CURSOR
    Ochild=tuple(sorted(((Oedge_parent[0][0]+L,Oedge_parent[0][1]),
                         (Oedge_parent[1][0]+L,Oedge_parent[1][1]))))
    Cchild=(C_parent[0]+L,C_parent[1])
    pbuf=support(('O2',Ochild))|support(('CO',Cchild))
    child_cursor={(x,y) for x in (L,L+1) for y in range(4)}
    corridor={(x,y) for x in range(0,L+2) for y in range(4)}
    if not pbuf <= corridor:
        return None
    req=pbuf|child_cursor
    stages=[]
    for c in range(2,L+2):
        cleared_before={(x,y) for x in range(0,c) for y in range(4)}
        other_bottom={(x,y) for x in (c-2,c-1) for y in (2,3)}
        S_top=parent_core|other_bottom|shift(READ,c-1,0)|(req&cleared_before)
        stages.append((c,'top',S_top,d_units(S_top)))
        cleared_after_top=cleared_before|{(c,0),(c,1)}
        other_top={(x,y) for x in (c-1,c) for y in (0,1)}
        S_bottom=parent_core|other_top|shift(READ,c-1,2)|(req&cleared_after_top)
        stages.append((c,'bottom',S_bottom,d_units(S_bottom)))
    final_state=parent_core|req
    Dfinal=d_units(final_state)
    co=set(); edges=set()
    for _,_,S,_ in stages:
        a,b=interference(S); co|=a; edges|=b
    a,b=interference(final_state); co|=a; edges|=b
    return {'occ':occ,'parent_core':parent_core,'Ochild':Ochild,'Cchild':Cchild,
            'pbuf':pbuf,'child_cursor':child_cursor,'stages':stages,
            'Dfinal':Dfinal,'co':co,'edges':edges}

def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def distance_two_disjoint(g,L):
    return not (g['co'] & shift(g['co'],2*L,0)) and not (g['edges'] & shifted_edges(g['edges'],2*L))

# Frozen finite extremal family: roots in rows 1,2 and parent x=-12,...,-1.
coords=[(x,y) for x in range(-12,0) for y in (1,2)]
oedges=[tuple(sorted((a,b))) for a,b in combinations(coords,2) if b in neigh(a)]
family={}
for L in range(5,11):
    arr=[]
    for oe in oedges:
        for cp in coords:
            if cp in oe: continue
            if any(cp in neigh(o) for o in oe): continue  # canonical seed must be stable
            g=candidate_geometry(L,oe,cp)
            if g is not None and distance_two_disjoint(g,L):
                arr.append((oe,cp,g))
    family[L]=arr
assert {L:len(v) for L,v in family.items()}=={5:0,6:0,7:0,8:0,9:3,10:16}

# Exact B24 optimization over the three first-admissible L=9 seeds.
scored=[]
for oe,cp,g in family[9]:
    Ds=[entry[3][0] for entry in g['stages']]
    Df=g['Dfinal'][0]
    # In one final window of Poisson mean 2, exactly two arrivals in order O2 then CO.
    # e^-2 > (32/87)^2 and conditional label weights are 1/D, 2/D.
    planter=Fraction(32,87)**2*Fraction(4,Df**2)
    b=planter
    for D in Ds: b*=expander_lower(D)
    scored.append((b,oe,cp,g,Ds,planter))
scored.sort(key=lambda x:x[0],reverse=True)
b8,OE,CP,G,NEW_D,PLANTER_NEW=scored[0]
assert OE==((-2,1),(-2,2)) and CP==(-4,1)
assert G['Ochild']==((7,1),(7,2)) and G['Cchild']==(5,1)
assert G['Dfinal']==(308,69,170)
assert NEW_D==[174,178,195,199,220,221,242,242,260,257,271,278,281,290,302,307,324,325]
assert b8>b7
# Parent occupied particles never appear in any accepted stage support; parent cursor is protected throughout.
for _,_,S,_ in G['stages']:
    assert G['occ'] <= S and CURSOR <= S
for c in range(2,11):
    assert G['occ'].isdisjoint(shift(READ,c-1,0)|shift(READ,c-1,2))
# Child planter support is entirely within the deterministically cleared 4-row corridor.
CORRIDOR={(x,y) for x in range(0,11) for y in range(4)}
assert G['pbuf'] <= CORRIDOR
assert all(o not in neigh(G['Cchild']) for o in G['Ochild'])
# Full clock union for blocks two spatial steps apart is disjoint.
assert distance_two_disjoint(G,9)
assert (min(x for x,y in G['co']),max(x for x,y in G['co']))==(-5,12)
assert (min(min(a[0],b[0]) for a,b in G['edges']),max(max(a[0],b[0]) for a,b in G['edges']))==(-6,13)

T8=sum((Fraction(8,D) for D in NEW_D),Fraction(0,1))+Fraction(8,308)
assert T8==Fraction(15096961711209168777703329328,24551648040723854903619591825)

print('PASS exact R08/E0011 asymmetric seed-class certificate')
print('full_stable_expander_boundaries=',full_stable)
print('projected_expander_descriptors=',len(INITS))
print('finite_family_1dependent_counts=',{L:len(v) for L,v in family.items()})
print('selected_parent_Oedge=',OE)
print('selected_parent_CO=',CP)
print('selected_parent_cursor=columns_0_1_rows_0_3')
print('selected_child_Oedge=',G['Ochild'])
print('selected_child_CO=',G['Cchild'])
print('selected_child_cursor=columns_9_10_rows_0_3')
print('selected_stage_D_units=',NEW_D)
print('selected_final_planter_D_counts=',G['Dfinal'])
print('full_clock_union_CO_x_span=',(min(x for x,y in G['co']),max(x for x,y in G['co'])))
print('full_clock_union_edge_endpoint_x_span=',(min(min(a[0],b[0]) for a,b in G['edges']),max(max(a[0],b[0]) for a,b in G['edges'])))
print('distance_two_shift=',18,'disjoint=',distance_two_disjoint(G,9))
print('selected_is_exact_best_among_L9_family=',all(b8>=row[0] for row in scored))
for b,oe,cp,g,Ds,p in scored:
    print('L9_candidate',oe,cp,'Dfinal=',g['Dfinal'][0],'log10_bound=',repr(log10frac(b)))
print('planter_new_exact=',f'{PLANTER_NEW.numerator}/{PLANTER_NEW.denominator}')
print('b8_gt_b7_exact=',b8>b7)
print('log10_b7_diagnostic=',repr(log10frac(b7)))
print('log10_b8_diagnostic=',repr(log10frac(b8)))
print('log10_gain_diagnostic=',repr(log10frac(b8/b7)))
print('T8_exact=',f'{T8.numerator}/{T8.denominator}')
print('T8_float=',repr(float(T8)))
print('b8_num_digits=',len(str(b8.numerator)),'b8_den_digits=',len(str(b8.denominator)))
