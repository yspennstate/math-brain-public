#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb, factorial

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
                if (a,b) in ((1,2),(2,1)): return False
    return True

def co_prob_outcomes(s,c,idx):
    s=list(s); i=idx[c]
    if s[i]!=0: return {tuple(s):Fraction(1)}
    s[i]=1
    x,y=c
    os=[]
    for dx,dy in DIRS:
        q=(x+dx,y+dy)
        if q in idx and s[idx[q]]==2: os.append(q)
    if not os: return {tuple(s):Fraction(1)}
    out={}; p=Fraction(1,len(os))
    for q in os:
        t=s.copy(); t[i]=0; t[idx[q]]=0; tt=tuple(t)
        out[tt]=out.get(tt,Fraction(0))+p
    return out

def o2_prob_outcomes(s,a,b,idx):
    s=list(s); ia,ib=idx[a],idx[b]
    if s[ia]!=0 or s[ib]!=0: return {tuple(s):Fraction(1)}
    s[ia]=s[ib]=2
    choices=[]
    for c in (a,b):
        x,y=c; cs=[]
        for dx,dy in DIRS:
            q=(x+dx,y+dy)
            if q in idx and s[idx[q]]==1: cs.append(q)
        choices.append(cs if cs else [None])
    out={}
    pa=Fraction(1,len(choices[0])); pb=Fraction(1,len(choices[1]))
    for qa in choices[0]:
        for qb in choices[1]:
            t=s.copy()
            if qa is not None:
                t[ia]=0; t[idx[qa]]=0
            if qb is not None:
                t[ib]=0; t[idx[qb]]=0
            tt=tuple(t); out[tt]=out.get(tt,Fraction(0))+pa*pb
    return out

def apply_word_prob(s,word,idx):
    dist={s:Fraction(1)}
    for kind,arg in word:
        new={}
        for st,ps in dist.items():
            outs=co_prob_outcomes(st,arg,idx) if kind=='CO' else o2_prob_outcomes(st,*arg,idx)
            for tt,p in outs.items(): new[tt]=new.get(tt,Fraction(0))+ps*p
        dist=new
    return dist

def transform_word(word, f):
    out=[]
    for kind,arg in word:
        if kind=='CO': out.append((kind,f(arg)))
        else: out.append((kind,(f(arg[0]),f(arg[1]))))
    return tuple(out)

EXP_ACTIVE={(x,y) for x in (-1,0,1) for y in (0,1)}
EXP_CELLS,EXP_IDX=patch_for(EXP_ACTIVE)
EXP_FIXED_VACANT={(-1,0),(-1,1),(0,0),(0,1)}
EXP_VARIABLE=tuple(c for c in EXP_CELLS if c not in EXP_FIXED_VACANT)
EXP_WORD=(
('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,0)),('CO',(0,1)),('CO',(0,0)),('CO',(0,1)),
('CO',(1,0)),('CO',(0,1)),('CO',(0,0)),('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(1,0)),
('CO',(0,0)),('CO',(0,1)),('CO',(0,1)),('CO',(1,0)),('CO',(0,0)),('O2',((-1,0),(-1,1))),('CO',(1,0)),
('O2',((0,0),(0,1))),('CO',(-1,1)))
EXP_WORD_MIRROR=transform_word(EXP_WORD, lambda c:(c[0],1-c[1]))
assert EXP_WORD_MIRROR != EXP_WORD

ERASE_ACTIVE={(x,y) for x in (-1,0) for y in (0,1)}
ERASE_CELLS,ERASE_IDX=patch_for(ERASE_ACTIVE)
ERASE_FIXED={(-1,1):2,(0,0):1,(-1,0):0,(0,1):0}
ERASE_VARIABLE=tuple(c for c in ERASE_CELLS if c not in ERASE_FIXED)
ERASE_WORD=(('CO',(0,1)),('O2',((-1,0),(-1,1))),('CO',(0,1)),('CO',(0,0)),('O2',((-1,0),(-1,1))),('CO',(0,1)))
ERASE_WORD_MIRROR=transform_word(ERASE_WORD, lambda c:(-c[1],-c[0]))
assert ERASE_WORD_MIRROR != ERASE_WORD

PLANT_WORD=(('O2',((1,1),(1,2))),('CO',(2,1)),('CO',(2,1)))
PLANT_WORD_MIRROR=transform_word(PLANT_WORD, lambda c:(3-c[1],3-c[0]))
assert PLANT_WORD_MIRROR != PLANT_WORD

def min_success_exp(word):
    m=None; count=0
    for vals in product((0,1,2), repeat=len(EXP_VARIABLE)):
        s=[0]*len(EXP_CELLS)
        for c,v in zip(EXP_VARIABLE,vals): s[EXP_IDX[c]]=v
        s=tuple(s)
        if not stable(s,EXP_CELLS,EXP_IDX): continue
        count+=1
        dist=apply_word_prob(s,word,EXP_IDX)
        p=sum(pr for t,pr in dist.items() if all(t[EXP_IDX[c]]==0 for c in EXP_ACTIVE))
        m=p if m is None or p<m else m
    assert count==50785
    return m

def min_success_erase(word):
    m=None; count=0
    for vals in product((0,1,2), repeat=len(ERASE_VARIABLE)):
        s=[0]*len(ERASE_CELLS)
        for c,v in ERASE_FIXED.items(): s[ERASE_IDX[c]]=v
        for c,v in zip(ERASE_VARIABLE,vals): s[ERASE_IDX[c]]=v
        s=tuple(s)
        if not stable(s,ERASE_CELLS,ERASE_IDX): continue
        count+=1
        dist=apply_word_prob(s,word,ERASE_IDX)
        p=sum(pr for t,pr in dist.items() if all(t[ERASE_IDX[c]]==0 for c in ERASE_ACTIVE))
        m=p if m is None or p<m else m
    assert count==625
    return m

# Exact elementary bound on e.
e6=sum(Fraction(1,factorial(k)) for k in range(7))
e_upper=e6+Fraction(1,factorial(6)*6)
assert e_upper < Fraction(87,32)

q_exp=min_success_exp(EXP_WORD)
q_exp_m=min_success_exp(EXP_WORD_MIRROR)
q_erase=min_success_erase(ERASE_WORD)
q_erase_m=min_success_erase(ERASE_WORD_MIRROR)
assert q_exp==q_exp_m==Fraction(1,72)
assert q_erase==q_erase_m==Fraction(35,486)
assert PLANT_WORD_MIRROR != PLANT_WORD

# 2 eraser variants * 2^20 expander mirror choices * C(20,10) row-chain shuffles
# * 2 planter orders * 2^2 planter mirror choices.
K=(2**24)*comb(20,10)
assert K==3099691319296

# Each prescribed one-mark slot has probabilities e^-1/301 (CO) and e^-1/602 (O2).
# e<87/32 gives the rational lower bounds below.
pco=Fraction(32,87*301)
po2=Fraction(32,87*602)
assert pco==Fraction(32,26187)
assert po2==Fraction(16,26187)

new_lb = Fraction(K,1) * q_erase * (q_exp**20) * (pco**328) * (po2**104)
old_lb = Fraction(1, (3**432)*(1204**328)*(19264**104))
assert new_lb > old_lb

# B13 obstruction: exact 3-event cycle containing the minimal C-0-O interface seed.
line_cells=((-1,0),(0,0),(1,0),(2,0),(3,0),(1,1),(2,1),(1,-1),(2,-1))
line_idx={c:i for i,c in enumerate(line_cells)}
A=[0]*len(line_cells); A[line_idx[(0,0)]]=1; A[line_idx[(2,0)]]=2; A=tuple(A)
assert stable(A,line_cells,line_idx)
D=co_prob_outcomes(A,(1,0),line_idx); assert len(D)==1
S1=next(iter(D)); assert S1[line_idx[(0,0)]]==1 and S1[line_idx[(2,0)]]==0
D=o2_prob_outcomes(S1,(1,0),(2,0),line_idx); assert len(D)==1
S2=next(iter(D)); assert S2[line_idx[(0,0)]]==0 and S2[line_idx[(2,0)]]==2
D=co_prob_outcomes(S2,(0,0),line_idx); assert len(D)==1
A2=next(iter(D)); assert A2==A

print('PASS exact R08/E0011 ensemble-amplification core')
print(f'q_exp_min={q_exp}')
print(f'q_exp_mirror_min={q_exp_m}')
print(f'q_erase_min={q_erase}')
print(f'q_erase_mirror_min={q_erase_m}')
print(f'e_upper={e_upper} < 87/32')
print(f'full_word_multiplicity_K={K}')
print(f'pco_slot_lower={pco}')
print(f'po2_slot_lower={po2}')
print('new_Bcat_lower=K*(35/486)*(1/72)^20*(32/26187)^328*(16/26187)^104')
print('old_Bcat_lower=1/(3^432*1204^328*19264^104)')
print(f'new_gt_old={new_lb > old_lb}')
print('b13_three_event_cycle_verified=True')
