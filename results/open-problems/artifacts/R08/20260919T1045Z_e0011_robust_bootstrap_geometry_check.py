#!/usr/bin/env python3
from fractions import Fraction
DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c; return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0): return {(x+dx,y+dy) for x,y in S}
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
OLD=(
 ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),
 ('O2',((-1,0),(0,0))),('CO',(-1,0)),('O2',((0,0),(1,0))),
)
NEW=(
 ('CO',(0,-1)),('CO',(0,2)),('CO',(1,1)),
 ('O2',((0,-1),(0,0))),('O2',((0,1),(0,2))),
 ('O2',((0,1),(1,1))),('O2',((1,0),(1,1))),
)
P={(-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),(0,-2),(0,-1),(0,0),(0,1),(0,2),(0,3),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)}
assert all(support(l)<=P for l in OLD+NEW)
LABELS7=(
 ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),
)
READ=set()
for lab in LABELS7: READ |= support(lab)
OPARENT={(-3,0),(-2,0)}; CPARENT=(-4,1); OCC=OPARENT|{CPARENT}; CURSOR1={(0,0),(0,1)}; PARENT_CORE=OCC|CURSOR1
L=8
Ochild=((L-3,0),(L-2,0)); Cchild=(L-4,1); child_cursor={(L,0),(L,1)}
pbuf=support(('O2',Ochild))|support(('CO',Cchild)); down=(L-3,L-2); up=(L-4,L-3)
guards={(x,-1) for x in down}|{(x,2) for x in up}
c=2
R=shift(READ,c-1,0); cleared_before={(x,y) for x in range(0,c) for y in (0,1)}
S=PARENT_CORE|R|((pbuf|child_cursor|guards)&cleared_before)
D0,nco,ned=d_units(S)
blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(blocked_edges)
assert (len(OCC),len(blocked_edges),BLOCK)==(3,11,17)
assert D0-BLOCK==140
co,ed=interference(S)
def shifted_label(l):
    k,a=l
    if k=='CO': return (k,(a[0]+1,a[1]))
    return (k,tuple((x+1,y) for x,y in a))
def owned(l):
    k,a=shifted_label(l)
    if k=='CO': return a in co
    return tuple(sorted(a)) in ed
assert all(owned(l) for l in OLD+NEW)
print('PASS R08/E0011 bootstrap halo geometry')
print('stage_h2_raw_units=',D0,'blocked_units=',BLOCK,'owned_D=',D0-BLOCK)
print('old_labels=',len(OLD),'new_labels=',len(NEW),'all_17_already_owned=',all(owned(l) for l in OLD+NEW))
print('new_labels_local=',NEW)
print('new_labels_shifted=',tuple(shifted_label(l) for l in NEW))
old_poly=4642311559640512826443825152
new_poly=7492177630527378997219688448
old_boot=Fraction(449855540637605888,88875222725965541291015625)
gain_new_over_old=Fraction(new_poly,old_poly)
new_boot=old_boot*gain_new_over_old
current_gain_over_old=Fraction(34717319668318843590202198742697856944700233990464479,
                               34245904058199771001461521651828906250000000000000000)
current_boot=old_boot*current_gain_over_old
gain_vs_current=new_boot/current_boot
assert new_boot > current_boot > old_boot
assert new_boot == Fraction(80668567688839168,9875024747329504587890625)
assert gain_vs_current == Fraction(3035047884064870809017076077339859545315170762500000000000000000000,
                                   1906467115341816615178741523321245913280178771097328202961614705231)
print('old_boot=',f'{old_boot.numerator}/{old_boot.denominator}')
print('current_boot_87_over_20=',f'{current_boot.numerator}/{current_boot.denominator}')
print('new_robust_boot=',f'{new_boot.numerator}/{new_boot.denominator}')
print('gain_new_over_old=',f'{gain_new_over_old.numerator}/{gain_new_over_old.denominator}',float(gain_new_over_old))
print('gain_new_over_current=',f'{gain_vs_current.numerator}/{gain_vs_current.denominator}',float(gain_vs_current))
