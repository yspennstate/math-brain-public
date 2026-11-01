#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import product

DIRS=((1,0),(-1,0),(0,1),(0,-1))

def patch_for(active):
    cells=set(active)
    for x,y in tuple(active):
        for dx,dy in DIRS:
            cells.add((x+dx,y+dy))
    cells=tuple(sorted(cells)); idx={c:i for i,c in enumerate(cells)}
    return cells,idx

def stable(s,cells,idx):
    for x,y in cells:
        a=s[idx[(x,y)]]
        for dx,dy in ((1,0),(0,1)):
            q=(x+dx,y+dy)
            if q in idx:
                b=s[idx[q]]
                if (a,b) in ((1,2),(2,1)):
                    return False
    return True

def co_out(s,c,idx):
    s=list(s); i=idx[c]
    if s[i]!=0: return ((tuple(s),Fraction(1)),)
    s[i]=1
    x,y=c
    os=[(x+dx,y+dy) for dx,dy in DIRS if (x+dx,y+dy) in idx and s[idx[(x+dx,y+dy)]]==2]
    if not os: return ((tuple(s),Fraction(1)),)
    p=Fraction(1,len(os)); res={}
    for q in os:
        t=s.copy(); t[i]=0; t[idx[q]]=0; tt=tuple(t)
        res[tt]=res.get(tt,Fraction(0))+p
    return tuple(res.items())

def o2_out(s,a,b,idx):
    s=list(s); ia,ib=idx[a],idx[b]
    if s[ia]!=0 or s[ib]!=0: return ((tuple(s),Fraction(1)),)
    s[ia]=s[ib]=2
    choices=[]
    for c in (a,b):
        x,y=c
        cs=[(x+dx,y+dy) for dx,dy in DIRS if (x+dx,y+dy) in idx and s[idx[(x+dx,y+dy)]]==1]
        choices.append(cs if cs else [None])
    pa=Fraction(1,len(choices[0])); pb=Fraction(1,len(choices[1])); res={}
    for qa in choices[0]:
        for qb in choices[1]:
            t=s.copy()
            if qa is not None: t[ia]=0; t[idx[qa]]=0
            if qb is not None: t[ib]=0; t[idx[qb]]=0
            tt=tuple(t); res[tt]=res.get(tt,Fraction(0))+pa*pb
    return tuple(res.items())

ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
CELLS,IDX=patch_for(ACTIVE)
FIXED={(-1,0),(-1,1),(0,0),(0,1)}
VAR=tuple(c for c in CELLS if c not in FIXED)
BASE=(
    ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,0)),('CO',(0,1)),('CO',(0,0)),('CO',(0,1)),
    ('CO',(1,0)),('CO',(0,1)),('CO',(0,0)),('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(1,0)),
    ('CO',(0,0)),('CO',(0,1)),('CO',(0,1)),('CO',(1,0)),('CO',(0,0)),('O2',((-1,0),(-1,1))),('CO',(1,0)),
    ('O2',((0,0),(0,1))),('CO',(-1,1)))
SWAPS=(0,3,4,5,6,7,14,15,17)

def swapped(i):
    w=list(BASE); w[i],w[i+1]=w[i+1],w[i]
    return tuple(w)

def mirror_word(word):
    def f(c): return (c[0],1-c[1])
    out=[]
    for kind,arg in word:
        if kind=='CO': out.append((kind,f(arg)))
        else: out.append((kind,(f(arg[0]),f(arg[1]))))
    return tuple(out)

INITS=[]
for vals in product((0,1,2), repeat=len(VAR)):
    s=[0]*len(CELLS)
    for c,v in zip(VAR,vals): s[IDX[c]]=v
    s=tuple(s)
    if stable(s,CELLS,IDX): INITS.append(s)
assert len(INITS)==50785

def min_prob(word):
    word=tuple(word)
    @lru_cache(maxsize=None)
    def V(k,s):
        if k==len(word):
            return Fraction(int(all(s[IDX[c]]==0 for c in ACTIVE)),1)
        kind,arg=word[k]
        outs=co_out(s,arg,IDX) if kind=='CO' else o2_out(s,*arg,IDX)
        return sum(p*V(k+1,t) for t,p in outs)
    return min(V(0,s) for s in INITS)

words=(BASE,)+tuple(swapped(i) for i in SWAPS)
assert len(words)==10 and len(set(words))==10
mins=tuple(min_prob(w) for w in words)
expected=(Fraction(1,72),Fraction(1,48))+tuple(Fraction(1,72) for _ in range(8))
assert mins==expected, (mins,expected)
mirrors=tuple(mirror_word(w) for w in words)
all20=words+mirrors
assert len(set(all20))==20
base_weight=sum(mins,Fraction(0))
full_weight=2*base_weight
old_weight=2*Fraction(1,72)
gain_stage=full_weight/old_weight
assert base_weight==Fraction(7,48)
assert full_weight==Fraction(7,24)
assert old_weight==Fraction(1,36)
assert gain_stage==Fraction(21,2)
assert gain_stage**20>1

print('PASS exact R08/E0011 local-word-library amplification')
print(f'stable_boundary_states={len(INITS)}')
print(f'base_variant_count={len(words)}')
print(f'base_minima={list(map(str,mins))}')
print(f'mirror_variant_count={len(mirrors)}')
print(f'all_variants_pairwise_distinct={len(set(all20))==20}')
print(f'base_total_reaction_weight={base_weight}')
print(f'full_reflection_closed_weight={full_weight}')
print(f'old_two_variant_weight={old_weight}')
print(f'per_expander_gain={gain_stage}')
print(f'twenty_expander_gain=({gain_stage})^20')
print(f'gain_exact_gt_1={gain_stage**20>1}')
print('new_Bcat_lower=b2*(21/2)^20')
