#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log10
DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c; return {(x+dx,y+dy) for dx,dy in DIRS}
def support(label):
    k,a=label; roots={a} if k=='CO' else set(a); out=set(roots)
    for r in roots: out |= neigh(r)
    return out
def shift(S,dx=0,dy=0): return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx): return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u): ed.add(tuple(sorted((u,v))))
    return co,ed
L10=(('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),('O2',((-1,0),(0,0))),('CO',(-1,0)),('O2',((0,0),(1,0))))
A5=(('CO',(0,-1)),('O2',((0,-1),(0,0))),('CO',(1,1)),('O2',((0,1),(1,1))),('O2',((1,0),(1,1))))
L15=L10+A5
NEW=(('CO',(0,2)),('O2',((0,1),(0,2))))
L17=L15+NEW
P17={(-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),(0,-2),(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)}
P18=P17|{(0,3)}
xs=[x for x,y in P18]; ys=[y for x,y in P18]; ALL=[]
for x in range(min(xs)-1,max(xs)+2):
  for y in range(min(ys)-1,max(ys)+2):
    z=('CO',(x,y))
    if support(z)<=P18: ALL.append(z)
E=set()
for x in range(min(xs)-1,max(xs)+2):
  for y in range(min(ys)-1,max(ys)+2):
    u=(x,y)
    for v in neigh(u):
      e=tuple(sorted((u,v)))
      if e in E: continue
      E.add(e); z=('O2',e)
      if support(z)<=P18: ALL.append(z)
assert set(ALL)==set(L17) and len(ALL)==17
R7=set(); R10=set()
for z in L10[:7]: R7 |= support(z)
for z in L10: R10 |= support(z)
OCC={(-3,0),(-2,0),(-4,1)}; PARENT=OCC|{(0,0),(0,1)}
def geometry(L,Rterm):
    Ochild=tuple(sorted(((L-3,0),(L-2,0)))); Cchild=(L-4,1); cursor={(L,0),(L,1)}
    pbuf=support(('O2',Ochild))|support(('CO',Cchild))
    guards={(x,-1) for x in (L-3,L-2)}|{(x,2) for x in (L-4,L-3)}
    req=pbuf|cursor|guards; stages=[]
    for c in range(2,L+1):
      R=shift(Rterm if c==L else R7,c-1,0); cleared={(x,y) for x in range(c) for y in (0,1)}
      stages.append((c,PARENT|R|(req&cleared)))
    final=PARENT|cursor|pbuf|guards
    return stages,final
st,final=geometry(8,R10); termS=st[-1][1]
co,ed=interference(termS); bed={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(bed); DCOARSE=2*len(co)+len(ed); D=DCOARSE-BLOCK
assert (DCOARSE,BLOCK,D)==(231,17,214)
assert not (co & shift(co,16,0)); assert not (ed & shifted_edges(ed,16))
owned=[]
for g in co:
    if g not in OCC: owned.append(('CO',(g[0]-7,g[1])))
for e in ed:
    if e not in bed: owned.append(('O2',tuple(sorted(((e[0][0]-7,e[0][1]),(e[1][0]-7,e[1][1]))))))
gaps=[]
for z in owned:
    if z in set(L15): continue
    gaps.append((len(support(z)-P17),z,frozenset(support(z)-P17)))
one=[(z,m) for k,z,m in gaps if k==1]
assert len(one)==2 and {next(iter(m)) for z,m in one}=={(0,3)} and {z for z,m in one}==set(NEW)
rem=[(len(support(z)-P18),z) for z in owned if z not in set(L17)]
assert min(k for k,z in rem)==2
POLY=Fraction(2510638347558470307489501070035576665014272,12808276125197346372953971243679219712000000000)
lam=Fraction(43,20); r=lam-2
emr=sum(((-1)**k)*r**k/Fraction(factorial(k)) for k in range(8))
elow=Fraction(32,87)**2*emr
p18=elow*POLY
P18EX=Fraction(274528843496391434177359145335903444401907,12027551499283713181557247180800000000000000000)
assert p18==P18EX
p15=Fraction(229764455366845618711724942545032040908678194195997576585319159,10371549862797001958400000000000000000000000000000000000000000000000)
assert p18>p15
ratio=p18/p15
print('PASS exact R08/E0011 top-halo geometry and arithmetic certificate')
print('support_closed_labels_P18=',len(ALL))
print('unique_one_cell_gain=',(0,3),'new_labels=',NEW)
print('remaining_min_support_gap=',min(k for k,z in rem))
print('L8_shared_CO=',len(co & shift(co,16,0)),'L8_shared_O2=',len(ed & shifted_edges(ed,16)))
print('owned_D=',D)
print('lambda=43/20')
print('p18_exact=',f'{p18.numerator}/{p18.denominator}')
print('p18_over_p15=',repr(float(ratio)))
print('log10_gain=',repr(log10(ratio.numerator)-log10(ratio.denominator)))
