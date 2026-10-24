#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
DIRS=((1,0),(-1,0),(0,1),(0,-1))
def patch_for(active):
    cells=set(active)
    for x,y in tuple(active):
        for dx,dy in DIRS: cells.add((x+dx,y+dy))
    cells=tuple(sorted(cells)); return cells,{c:i for i,c in enumerate(cells)}
def stable(s,cells,idx):
    for x,y in cells:
        a=s[idx[(x,y)]]
        for dx,dy in ((1,0),(0,1)):
            q=(x+dx,y+dy)
            if q in idx and (a,s[idx[q]]) in ((1,2),(2,1)): return False
    return True
def co_out(s,c,idx):
    s=list(s); i=idx[c]
    if s[i]!=0: return ((tuple(s),Fraction(1)),)
    s[i]=1; x,y=c; os=[]
    for dx,dy in DIRS:
        q=(x+dx,y+dy)
        if q in idx and s[idx[q]]==2: os.append(q)
    if not os: return ((tuple(s),Fraction(1)),)
    p=Fraction(1,len(os)); out={}
    for q in os:
        t=s.copy(); t[i]=0; t[idx[q]]=0; tt=tuple(t); out[tt]=out.get(tt,Fraction(0))+p
    return tuple(out.items())
def o2_out(s,a,b,idx):
    s=list(s); ia,ib=idx[a],idx[b]
    if s[ia]!=0 or s[ib]!=0: return ((tuple(s),Fraction(1)),)
    s[ia]=s[ib]=2; choices=[]
    for c in (a,b):
        x,y=c; cs=[]
        for dx,dy in DIRS:
            q=(x+dx,y+dy)
            if q in idx and s[idx[q]]==1: cs.append(q)
        choices.append(cs if cs else [None])
    pa=Fraction(1,len(choices[0])); pb=Fraction(1,len(choices[1])); out={}
    for qa in choices[0]:
        for qb in choices[1]:
            t=s.copy()
            if qa is not None: t[ia]=0; t[idx[qa]]=0
            if qb is not None: t[ib]=0; t[idx[qb]]=0
            tt=tuple(t); out[tt]=out.get(tt,Fraction(0))+pa*pb
    return tuple(out.items())
def min_success(word,inits,active,idx):
    word=tuple(word)
    @lru_cache(maxsize=None)
    def V(k,s):
        if k==len(word): return Fraction(int(all(s[idx[c]]==0 for c in active)),1)
        kind,arg=word[k]
        outs=co_out(s,arg,idx) if kind=='CO' else o2_out(s,*arg,idx)
        return sum(p*V(k+1,t) for t,p in outs)
    return min(V(0,s) for s in inits)
def diag_mirror_eraser(word):
    f=lambda c:(-c[1],-c[0]); out=[]
    for kind,arg in word: out.append((kind,f(arg)) if kind=='CO' else (kind,(f(arg[0]),f(arg[1]))))
    return tuple(out)
def diag_mirror_planter(word):
    f=lambda c:(3-c[1],3-c[0]); out=[]
    for kind,arg in word: out.append((kind,f(arg)) if kind=='CO' else (kind,(f(arg[0]),f(arg[1]))))
    return tuple(out)
ACTIVE={(x,y) for x in (-1,0) for y in (0,1)}; CELLS,IDX=patch_for(ACTIVE)
FIX={(-1,1):2,(0,0):1,(-1,0):0,(0,1):0}; VAR=tuple(c for c in CELLS if c not in FIX)
INITS=[]
for vals in product((0,1,2),repeat=len(VAR)):
    s=[0]*len(CELLS)
    for c,v in FIX.items(): s[IDX[c]]=v
    for c,v in zip(VAR,vals): s[IDX[c]]=v
    s=tuple(s)
    if stable(s,CELLS,IDX): INITS.append(s)
assert len(INITS)==625
A=('CO',(0,1));B=('O2',((-1,0),(-1,1)));C=('CO',(0,0));BASE=(A,B,A,C,B,A)
WORDS=tuple(sorted(set(permutations(BASE)))); assert len(WORDS)==60
GOOD=[]
for w in WORDS:
    q=min_success(w,INITS,ACTIVE,IDX)
    if q>0: GOOD.append((w,q))
assert len(GOOD)==2 and all(q==Fraction(35,486) for _,q in GOOD)
MIRS=tuple(diag_mirror_eraser(w) for w,_ in GOOD); assert len(set(tuple(w for w,_ in GOOD)+MIRS))==4
ER_GAIN=Fraction(4,2); assert ER_GAIN==2
BOX={(x,y) for x in range(4) for y in range(4)}; PCELLS,PIDX=patch_for(BOX); INIT=tuple(0 for _ in PCELLS)
O=('O2',((1,1),(1,2)));CO=('CO',(2,1)); PWORDS=tuple(sorted(set(permutations((O,CO,CO))))); assert len(PWORDS)==3
TO=(1,2);TC=(2,1)
def psucc(word):
    d={INIT:Fraction(1)}
    for kind,arg in word:
        nd={}
        for s,ps in d.items():
            outs=co_out(s,arg,PIDX) if kind=='CO' else o2_out(s,*arg,PIDX)
            for t,p in outs: nd[t]=nd.get(t,Fraction(0))+ps*p
        d=nd
    def good(t): return t[PIDX[TO]]==2 and t[PIDX[TC]]==1 and all(t[PIDX[c]]==0 for c in BOX-{TO,TC})
    return sum(p for t,p in d.items() if good(t))
PQ=tuple(psucc(w) for w in PWORDS); assert sorted(PQ)==[Fraction(0),Fraction(1),Fraction(1)]
PG=tuple(w for w,q in zip(PWORDS,PQ) if q==1); PM=tuple(diag_mirror_planter(w) for w in PG); assert len(set(PG+PM))==4
PL_GAIN=Fraction(4,2); assert PL_GAIN==2
print('PASS exact R08/E0011 eraser+planter library amplification')
print(f'eraser_stable_boundary_states={len(INITS)}')
print(f'eraser_all_multiset_permutations={len(WORDS)}')
print(f'eraser_good_base_orders={len(GOOD)}')
print(f'eraser_good_minimum={GOOD[0][1]}')
print(f'eraser_reflection_closed_variant_count={len(set(tuple(w for w,_ in GOOD)+MIRS))}')
print(f'eraser_gain={ER_GAIN}')
print(f'planter_all_multiset_permutations={len(PWORDS)}')
print(f'planter_success_probabilities={list(map(str,PQ))}')
print(f'planter_reflection_closed_variant_count={len(set(PG+PM))}')
print(f'planter_gain_per_child={PL_GAIN}')
print('combined_eraser_two_planters_gain=8')
