#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import product

DIRS=((1,0),(-1,0),(0,1),(0,-1))
ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
FIXED={(-1,0),(-1,1),(0,0),(0,1)}
def patch_for(active):
    cells=set(active)
    for x,y in tuple(active):
        for dx,dy in DIRS: cells.add((x+dx,y+dy))
    cells=tuple(sorted(cells)); return cells,{c:i for i,c in enumerate(cells)}
CELLS,IDX=patch_for(ACTIVE)

LABELS=(
 ('CO',(0,0)),
 ('O2',((-1,1),(0,1))),
 ('CO',(0,1)),
 ('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),
 ('O2',((0,0),(0,1))),
 ('CO',(-1,1)),
)
CODES=[(1, 0, 0, 0, 2, 2, 2, 3, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 0, 2, 2, 3, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 0, 2, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 0, 2, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 0, 2, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 0, 2, 2, 3, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 0, 2, 3, 2, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 0, 3, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 2, 0, 3, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 2, 3, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 2, 3, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 2, 0, 2, 2, 3, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 2, 3, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 0, 2, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 2, 0, 2, 3, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 0, 2, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 0, 2, 3, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 3, 4, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 4, 3, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 3, 0, 4, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 3, 0, 2, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 3, 4, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 2, 3, 2, 0, 4, 5, 3, 0, 3, 2, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 3, 2, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 3, 2, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 2, 0, 3, 2, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 2, 0, 3, 2, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 0, 3, 2, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 2, 0, 2, 3, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 2, 0, 3, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 2, 0, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 0, 2, 2, 0, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 0, 2, 2, 0, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 2, 0, 3, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 0, 2, 2, 3, 0, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 0, 2, 3, 0, 2, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 2, 0, 0, 2, 2, 3, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 2, 0, 0, 2, 3, 0, 2, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 2, 0, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 0, 3, 4, 3, 5, 6), (1, 0, 2, 0, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 3, 4, 5, 6), (1, 0, 2, 0, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 2, 0, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 3, 2, 0, 4, 3, 5, 6), (1, 0, 2, 0, 0, 3, 2, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 0, 2, 0, 2, 0, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6), (1, 2, 0, 0, 0, 2, 3, 2, 0, 4, 5, 3, 0, 2, 2, 3, 0, 4, 3, 5, 6)]

def stable(s):
    for x,y in CELLS:
        a=s[IDX[(x,y)]]
        for dx,dy in ((1,0),(0,1)):
            q=(x+dx,y+dy)
            if q in IDX and (a,s[IDX[q]]) in ((1,2),(2,1)): return False
    return True

def co_out(s,c):
    s=list(s); i=IDX[c]
    if s[i]!=0: return ((tuple(s),Fraction(1)),)
    s[i]=1
    x,y=c
    os=[(x+dx,y+dy) for dx,dy in DIRS if (x+dx,y+dy) in IDX and s[IDX[(x+dx,y+dy)]]==2]
    if not os: return ((tuple(s),Fraction(1)),)
    p=Fraction(1,len(os)); out={}
    for q in os:
        t=s.copy(); t[i]=0; t[IDX[q]]=0; tt=tuple(t)
        out[tt]=out.get(tt,Fraction(0))+p
    return tuple(out.items())

def o2_out(s,a,b):
    s=list(s); ia,ib=IDX[a],IDX[b]
    if s[ia]!=0 or s[ib]!=0: return ((tuple(s),Fraction(1)),)
    s[ia]=s[ib]=2
    choices=[]
    for c in (a,b):
        x,y=c
        cs=[(x+dx,y+dy) for dx,dy in DIRS if (x+dx,y+dy) in IDX and s[IDX[(x+dx,y+dy)]]==1]
        choices.append(cs if cs else [None])
    pa=Fraction(1,len(choices[0])); pb=Fraction(1,len(choices[1])); out={}
    for qa in choices[0]:
        for qb in choices[1]:
            t=s.copy()
            if qa is not None: t[ia]=0; t[IDX[qa]]=0
            if qb is not None: t[ib]=0; t[IDX[qb]]=0
            tt=tuple(t); out[tt]=out.get(tt,Fraction(0))+pa*pb
    return tuple(out.items())

def support(label):
    kind,arg=label
    roots={arg} if kind=='CO' else set(arg)
    out=set(roots)
    for x,y in roots:
        for dx,dy in DIRS: out.add((x+dx,y+dy))
    return out

READ=set()
for lab in LABELS: READ |= support(lab)
RELEVANT=tuple(sorted((READ & set(CELLS))-FIXED))
IRRELEVANT=tuple(sorted(set(CELLS)-FIXED-set(RELEVANT)))
assert RELEVANT==((-2,0),(-2,1),(-1,-1),(-1,2),(0,-1),(0,2),(1,-1),(1,0),(1,1),(2,0))
assert IRRELEVANT==((1,2),(2,1))
assert not (set(IRRELEVANT)&READ)
assert not (set(IRRELEVANT)&ACTIVE)

VAR=tuple(c for c in CELLS if c not in FIXED)
representatives={}
full_stable=0
for vals in product((0,1,2),repeat=len(VAR)):
    s=[0]*len(CELLS)
    for c,v in zip(VAR,vals): s[IDX[c]]=v
    s=tuple(s)
    if not stable(s): continue
    full_stable += 1
    d=tuple(s[IDX[c]] for c in RELEVANT)
    representatives.setdefault(d,s)
assert full_stable==50785
assert len(representatives)==12201
INITS=tuple(representatives.values())
TARGET_IDX=tuple(IDX[c] for c in ACTIVE)

def is_target(s): return all(s[i]==0 for i in TARGET_IDX)

def min_prob(code):
    word=tuple(LABELS[i] for i in code)
    @lru_cache(None)
    def V(k,s):
        if k==len(word): return Fraction(int(is_target(s)),1)
        kind,arg=word[k]
        outs=co_out(s,arg) if kind=='CO' else o2_out(s,*arg)
        return sum(p*V(k+1,t) for t,p in outs)
    return min(V(0,s) for s in INITS)

mins=[]
for i,code in enumerate(CODES):
    q=min_prob(tuple(code))
    mins.append(q)
    assert q==Fraction(1,48), (i,q)

def mirror_coord(c): return (c[0],1-c[1])
def mirror_label(label):
    kind,arg=label
    if kind=='CO': return (kind,mirror_coord(arg))
    return (kind,(mirror_coord(arg[0]),mirror_coord(arg[1])))
def decode(code): return tuple(LABELS[i] for i in code)
WORDS=tuple(decode(tuple(c)) for c in CODES)
MIRRORS=tuple(tuple(mirror_label(x) for x in w) for w in WORDS)
assert len(set(WORDS))==50
assert len(set(MIRRORS))==50
assert len(set(WORDS+MIRRORS))==100

base_weight=sum(mins,Fraction(0))
full_weight=2*base_weight
old_full_weight=Fraction(7,24)
gain_stage=full_weight/old_full_weight
assert base_weight==Fraction(25,24)
assert full_weight==Fraction(25,12)
assert gain_stage==Fraction(50,7)

print("PASS exact R08/E0011 100-word one-column automaton library")
print(f"full_stable_states={full_stable}")
print(f"relevant_descriptor_states={len(INITS)}")
print(f"irrelevant_cells={IRRELEVANT}")
print("all_50_base_minima=1/48")
print(f"base_word_count={len(WORDS)}")
print(f"reflection_closed_word_count={len(set(WORDS+MIRRORS))}")
print(f"base_total_reaction_weight={base_weight}")
print(f"reflection_closed_reaction_weight={full_weight}")
print(f"previous_reflection_closed_weight={old_full_weight}")
print(f"per_expander_gain={gain_stage}")
print(f"twenty_expander_gain=({gain_stage})^20")
