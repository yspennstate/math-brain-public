#!/usr/bin/env python3
from fractions import Fraction
from math import log10
DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c; return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0): return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def support(label):
    k,a=label; roots={a} if k=='CO' else set(a); out=set(roots)
    for c in roots: out |= neigh(c)
    return out
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u): ed.add(tuple(sorted((u,v))))
    return co,ed
def d_units(S):
    co,ed=interference(S); return 2*len(co)+len(ed),len(co),len(ed)
def log10frac(x): return log10(x.numerator)-log10(x.denominator)

# Frozen support sets inherited from the audited-by-self b11 local automaton.
LABELS7=(
 ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),
)
READ=set()
for lab in LABELS7: READ |= support(lab)
# Terminal read set = old 9-label language with CO(1,0) omitted.
LABELS9=LABELS7+(('O2',((-1,0),(0,0))),('CO',(-1,0)))
READ_TERM=set()
for i,lab in enumerate(LABELS9):
    if i!=3: READ_TERM |= support(lab)

def read_down(a): return {(a+y,-x) for x,y in READ}
def read_up(a): return {(a+y,x+1) for x,y in READ}

OPARENT={(-3,0),(-2,0)}; CPARENT=(-4,1); OCC=OPARENT|{CPARENT}
CURSOR1={(0,0),(0,1)}; PARENT_CORE=OCC|CURSOR1

def geometry1(L):
    Ochild=tuple(sorted(((L-3,0),(L-2,0)))); Cchild=(L-4,1)
    child_cursor={(L,0),(L,1)}
    pbuf=support(('O2',Ochild))|support(('CO',Cchild))
    down=(L-3,L-2); up=(L-4,L-3)
    guards={(x,-1) for x in down}|{(x,2) for x in up}
    corridor={(x,y) for x in range(0,L+1) for y in (0,1)}
    req=pbuf|child_cursor|guards; stages=[]
    for c in range(2,L+1):
        R=shift(READ_TERM if c==L else READ,c-1,0)
        cleared_before={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared_before)
        stages.append(('h6' if c==L else 'h',c,S,d_units(S),R))
    greads=[read_down(down[0]),read_up(up[0])]
    cleared=corridor.copy()
    S=PARENT_CORE|greads[0]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gd',0,S,d_units(S),greads[0]))
    cleared|={(x,-1) for x in down}
    S=PARENT_CORE|greads[1]|child_cursor|pbuf|(guards&cleared)
    stages.append(('gu',1,S,d_units(S),greads[1]))
    finalS=PARENT_CORE|child_cursor|pbuf|guards
    return stages,finalS,d_units(finalS)

def deps_stagewise(L):
    stages,finalS,_=geometry1(L); co=set(); ed=set()
    for _,_,S,_,_ in stages:
        a,b=interference(S); co|=a; ed|=b
    a,b=interference(finalS); co|=a; ed|=b
    return co,ed

def deps_once(L):
    stages,finalS,_=geometry1(L); U=set(finalS)
    for _,_,S,_,_ in stages: U|=S
    return interference(U)

# B25: two exact counts of the same dependency family.
co8,ed8=deps_stagewise(8); co8b,ed8b=deps_once(8)
assert co8==co8b and ed8==ed8b
assert not (co8 & shift(co8,16,0))
assert not (ed8 & shifted_edges(ed8,16))
# B20: the same direct-disjointness algorithm at L=7 misses by exactly one edge.
co7,ed7=deps_stagewise(7)
assert not (co7 & shift(co7,14,0))
assert ed7 & shifted_edges(ed7,14)=={((8,1),(9,1))}

blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(blocked_edges)
assert (len(OCC),len(blocked_edges),BLOCK)==(3,11,17)
st8,final8,Df8=geometry1(8)
Ds=[counts[0]-BLOCK for _,_,_,counts,_ in st8]
assert Ds==[140,150,167,178,187,197,201,218,222]
DPLAN=Df8[0]-BLOCK
assert DPLAN==198

# Exact finite-state values emitted by the run's exhaustive rational DP.
# One-column initial class: 215383 stable full states -> 48027 descriptors.
FULL_ONE=215383; DESC_ONE=48027; MIN_A10_0_4=(0,0,0,0,12109824)
assert MIN_A10_0_4[-1]>0
stage=[
 ('h',2,140,4,Fraction(449855540637605888,88875222725965541291015625)),
 ('h',3,150,2,Fraction(20193231009117236036,580023299851226806640625)),
 ('h',4,167,2,Fraction(9763107163899290190848,350499257108203128488308305)),
 ('h',5,178,2,Fraction(11133436709205330292,456147586622526713121501)),
 ('h',6,187,2,Fraction(22544728691405487104,1022833101788426753598015)),
 ('h',7,197,2,Fraction(26015322500884764075008,1314271656156778872998881905)),
 ('h6',8,201,2,Fraction(7168864776621912190976,514520327344022846669179035)),
 ('gd',0,218,2,Fraction(1672277727444803056,105910938933255255436245)),
 ('gu',1,222,2,Fraction(40628945155674655856,2670355970159927065747101)),
]
assert [x[2] for x in stage]==Ds
PLAN=Fraction(2048,74183769)
b12=PLAN
for *_,p in stage: b12*=p
b11=Fraction(
343895780272946830492794209499089522211245281485895792729043122841879341686687426458394669987761045594067973909241499086156299516183746003443682289785589685137947962715744301378744944479738789888,
2067330122866822189383102677134886509492302494671850414681516994628008975924052207814536929738765446654987614513302776745433762986461893680641699892468621574314760460088209090218880752320105382994212245132727157059804312666528858244419097900390625)
GAIN=b12/b11
assert b12>b11
T=sum(Fraction(4*lam,D) for _,_,D,lam,_ in stage)+Fraction(8,DPLAN)
assert T==Fraction(115764484087287928,233022519324042525)

print('PASS exact R08/E0011 one-column L=8 geometry/arithmetic certificate')
print('one_column_stable_full_descriptors=',FULL_ONE,DESC_ONE)
print('one_column_min_A10_n0_to4=',MIN_A10_0_4)
print('stage_count=',len(stage),'stage_D=',Ds,'planter_D=',DPLAN)
print('L8_overlap_CO=',sorted(co8 & shift(co8,16,0)))
print('L8_overlap_edges=',sorted(ed8 & shifted_edges(ed8,16)))
print('dependency_two_counts_equal=',co8==co8b and ed8==ed8b)
print('L7_direct_disjointness_obstruction=',sorted(ed7 & shifted_edges(ed7,14)))
for kind,idx,D,lam,p in stage:
    print('stage',kind,idx,'D=',D,'lambda=',lam,'log10p=',repr(log10frac(p)))
print('T12_exact=',f'{T.numerator}/{T.denominator}','T12_decimal=',repr(float(T)))
print('b12_gt_b11_exact=',b12>b11)
print('log10_b11=',repr(log10frac(b11)))
print('log10_b12=',repr(log10frac(b12)))
print('log10_gain=',repr(log10frac(GAIN)))
print('gain_decimal=',repr(float(GAIN)))
print('gain_exact=',f'{GAIN.numerator}/{GAIN.denominator}')
print('b12_exact=',f'{b12.numerator}/{b12.denominator}')
