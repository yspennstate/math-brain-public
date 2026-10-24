from itertools import product
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction
from math import factorial, log10

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

# At p=1/2 in the protected block, conditional on a protected arrival,
# one specified CO-site clock has probability 1/301 = 2/602 and one
# specified O2-edge clock has probability 1/602. Reaction-choice
# denominators divide 4 for CO and 3*3 for O2, so H=602*36 is a common
# exact one-step denominator.
H=602*36

@lru_cache(None)
def trans_int(s,li):
    kind,arg=LABELS[li]
    out=defaultdict(int)
    if kind=='CO':
        c=arg; a=list(s); i=IDX[c]
        if a[i]!=0:
            out[s]+=72                  # (2/602)*36
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
        out[s]+=36                      # (1/602)*36
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

mins=[]
worsts=[]
for n in range(0,25):
    mn=None; wi=None
    for s in INITS:
        q=A(n,s)
        if mn is None or q<mn:
            mn=q; wi=s
    mins.append(mn); worsts.append(wi)

assert mins[0]==mins[1]==mins[2]==mins[3]==0
assert mins[4]==127650816
assert all(x>0 for x in mins[4:])

stage4=Fraction(mins[4],H**4)
assert stage4==Fraction(19,32834164804)

# Previous b4 used the 100-word 21-mark expander stage
# (25/12)*301^-16*602^-5 and a 432-arrival Poisson-at-its-mean factor.
old_stage=Fraction(25,12)*Fraction(1,301)**16*Fraction(1,602)**5
stage_ratio=stage4/old_stage
assert stage_ratio>1

M_old=432
M_new=6 + 20*4 + 2*3
assert M_new==92
old_time=Fraction(32,87)**M_old * Fraction(M_old**M_old,factorial(M_old))
new_time=Fraction(32,87)**M_new * Fraction(M_new**M_new,factorial(M_new))
time_ratio=new_time/old_time
total_ratio=(stage_ratio**20)*time_ratio
assert total_ratio>1

# Direct full-block expressions: 4 robust eraser variants; 4 variants for
# each of two planters and two child orders give 4*4*4*2=128 outside
# variants; choose the interleaving of the two ten-stage row chains in
# C(20,10) ways. Eraser+planters use 8 CO and 4 O2 protected labels.
from math import comb
outer = Fraction(comb(20,10)*128*35,486)*Fraction(1,301)**8*Fraction(1,602)**4
b4_direct = outer * old_stage**20 * old_time
b5_direct = outer * stage4**20 * new_time
assert b5_direct/b4_direct == total_ratio
assert b5_direct > b4_direct

print('PASS exact R08/E0011 budgeted-prefix-DAG certificate')
print('full_stable_states=',full_stable)
print('projected_initial_states=',len(INITS))
print('ignored_cells=',IRRELEVANT)
print('one_step_common_denominator=',H)
print('budget_minima_n0_to_n24=',mins)
print('first_uniformly_positive_budget=4')
print('worst_state_at_budget4=',worsts[4])
print('stage4_exact=',f'{stage4.numerator}/{stage4.denominator}')
print('old_21mark_stage=(25/12)*301^-16*602^-5')
print('stage_ratio_num=',stage_ratio.numerator)
print('stage_ratio_den=',stage_ratio.denominator)
print('stage_ratio_gt_1=',stage_ratio>1)
print('old_macro_marks=',M_old)
print('new_macro_marks=',M_new)
print('time_ratio_exact= [(32/87)^92*92^92/92!] / [(32/87)^432*432^432/432!]')
print('time_ratio_gt_1=',time_ratio>1)
print('total_ratio_gt_1=',total_ratio>1)
print('b5_direct_symbolic= C(20,10)*128*(35/486)*301^-8*602^-4*(19/32834164804)^20*(32/87)^92*92^92/92!')
print('b5_gt_b4_exact=',b5_direct>b4_direct)
print('log10_b5_for_scale=',log10(b5_direct.numerator)-log10(b5_direct.denominator))
print('log10_stage_ratio=',log10(stage_ratio.numerator)-log10(stage_ratio.denominator))
print('log10_time_ratio=',log10(time_ratio.numerator)-log10(time_ratio.denominator))
print('log10_total_gain_over_b4=',log10(total_ratio.numerator)-log10(total_ratio.denominator))
print('A_cache=',A.cache_info())
print('transition_cache=',trans_int.cache_info())
