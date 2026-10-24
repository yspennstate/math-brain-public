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
L10=(
 ('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),
 ('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)),
 ('O2',((-1,0),(0,0))),('CO',(-1,0)),('O2',((0,0),(1,0))))
CORE=set()
for z in L10: CORE |= support(z)
assert len(CORE)==14
HALO={(0,-2),(0,3),(1,2),(2,1)}
P=CORE|HALO

def all_labels(P):
    xs=[x for x,y in P]; ys=[y for x,y in P]; out=[]
    for x in range(min(xs)-1,max(xs)+2):
        for y in range(min(ys)-1,max(ys)+2):
            z=('CO',(x,y))
            if support(z)<=P: out.append(z)
    E=set()
    for x in range(min(xs)-1,max(xs)+2):
        for y in range(min(ys)-1,max(ys)+2):
            u=(x,y)
            for v in neigh(u):
                e=tuple(sorted((u,v)))
                if e in E: continue
                E.add(e); z=('O2',e)
                if support(z)<=P: out.append(z)
    return set(out)
ALL=all_labels(P); NEW=ALL-set(L10)
EXPECTED={('CO',(0,-1)),('O2',((0,-1),(0,0))),('CO',(1,1)),
          ('O2',((0,1),(1,1))),('O2',((1,0),(1,1))),
          ('CO',(0,2)),('O2',((0,1),(0,2)))}
assert len(ALL)==17 and NEW==EXPECTED
READ7=set()
for z in L10[:7]: READ7 |= support(z)
OCC={(-3,0),(-2,0),(-4,1)}; PARENT=OCC|{(0,0),(0,1)}
def geometry(L):
    Ochild=tuple(sorted(((L-3,0),(L-2,0)))); Cchild=(L-4,1); cursor={(L,0),(L,1)}
    pbuf=support(('O2',Ochild))|support(('CO',Cchild))
    guards={(x,-1) for x in (L-3,L-2)}|{(x,2) for x in (L-4,L-3)}
    req=pbuf|cursor|guards; stages=[]
    for c in range(2,L+1):
        R=shift(CORE if c==L else READ7,c-1,0); cleared={(x,y) for x in range(c) for y in (0,1)}
        stages.append(PARENT|R|(req&cleared))
    return stages
termS=geometry(8)[-1]
co,ed=interference(termS); bed={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
local_owned=set()
for g in co:
    if g not in OCC: local_owned.add(('CO',(g[0]-7,g[1])))
for e in ed:
    if e not in bed:
        local_owned.add(('O2',tuple(sorted(((e[0][0]-7,e[0][1]),(e[1][0]-7,e[1][1]))))))
assert NEW <= local_owned
D=2*len(co)+len(ed)-(2*len(OCC)+len(bed))
assert D==214
assert not (co & shift(co,16,0)); assert not (ed & shifted_edges(ed,16))
ext=('CO',(0,-3))
assert ext not in local_owned and (0,-2) in support(ext) and not (support(ext)&CORE)
ROB_NUM=248042286707559887050495146109132661542301362814976
ROB_DEN=1280827612519734637295397124367921971200000000000000000
poly=Fraction(ROB_NUM,ROB_DEN)
r=Fraction(29,200)
exp_r=sum(((-1)**k)*r**k/Fraction(factorial(k)) for k in range(8))
elow=Fraction(32,87)**2*exp_r
prob=elow*poly
PROB=Fraction(11357683958175627230527864078759314996182455956063867773,
              501147979136821382564885299200000000000000000000000000000000)
assert prob==PROB
p14=Fraction(103936503566984629647143194039811221052609,
             6221649932703678742303190625000000000000000000)
ratio=prob/p14
RATIO=Fraction(8279751605510032251054812913415540632217010391970559606517,
               6103178097198250600945438022675389091881789947904000000000)
assert ratio==RATIO and ratio>1
print('PASS exact R08/E0011 adversarial-boundary geometry/arithmetic certificate')
print('core_cells=',len(CORE),'halo_cells=',len(HALO),'old_labels=',len(L10),'new_labels=',len(NEW))
print('new_labels=',sorted(NEW,key=repr))
print('all_new_clocks_already_owned=True')
print('external_refresh_witness=',ext,'support=',sorted(support(ext)))
print('owned_D=',D,'L8_shared_CO=',len(co & shift(co,16,0)),'L8_shared_O2=',len(ed & shifted_edges(ed,16)))
print('lambda=429/200')
print('robust_terminal_exact=',f'{prob.numerator}/{prob.denominator}')
print('robust_over_b14_terminal_exact=',f'{ratio.numerator}/{ratio.denominator}')
print('robust_over_b14_terminal=',repr(float(ratio)))
print('log10_gain_over_b14=',repr(log10(ratio.numerator)-log10(ratio.denominator)))
