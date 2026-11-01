#!/usr/bin/env python3
from itertools import product
from functools import lru_cache
from fractions import Fraction
from math import factorial, log10

DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c
    return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0): return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def support(label):
    k,a=label
    roots={a} if k=="CO" else set(a)
    out=set(roots)
    for r in roots: out |= neigh(r)
    return out
def interference(S):
    co=set(S)
    for s in tuple(S): co |= neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u): ed.add(tuple(sorted((u,v))))
    return co,ed
def d_units(S):
    co,ed=interference(S)
    return 2*len(co)+len(ed)
def lg(x): return log10(x.numerator)-log10(x.denominator)

LABELS10=(
 ("CO",(0,0)),
 ("O2",((-1,1),(0,1))),
 ("CO",(0,1)),
 ("CO",(1,0)),
 ("O2",((-1,0),(-1,1))),
 ("O2",((0,0),(0,1))),
 ("CO",(-1,1)),
 ("O2",((-1,0),(0,0))),
 ("CO",(-1,0)),
 ("O2",((0,0),(1,0))),
)
TERM8=(0,1,2,4,5,6,7,8)
READ7=set(); READ8=set(); READ10=set()
for lab in LABELS10[:7]: READ7 |= support(lab)
for i in TERM8: READ8 |= support(LABELS10[i])
for lab in LABELS10: READ10 |= support(lab)
assert READ10==READ7
assert READ10-READ8=={(1,-1),(2,0)}

OPARENT={(-3,0),(-2,0)}
CPARENT=(-4,1)
OCC=OPARENT|{CPARENT}
CURSOR1={(0,0),(0,1)}
PARENT_CORE=OCC|CURSOR1
def read_down(a,R): return {(a+y,-x) for x,y in R}
def read_up(a,R): return {(a+y,x+1) for x,y in R}
def geometry(L,Rterm):
    Ochild=tuple(sorted(((L-3,0),(L-2,0))))
    Cchild=(L-4,1)
    child_cursor={(L,0),(L,1)}
    pbuf=support(("O2",Ochild))|support(("CO",Cchild))
    down=(L-3,L-2); up=(L-4,L-3)
    guards={(x,-1) for x in down}|{(x,2) for x in up}
    corridor={(x,y) for x in range(0,L+1) for y in (0,1)}
    req=pbuf|child_cursor|guards
    stages=[]
    for c in range(2,L+1):
        R=shift(Rterm if c==L else READ7,c-1,0)
        cleared={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared)
        stages.append(("h_term" if c==L else "h",c,S,R))
    gd,gu=read_down(down[0],READ7),read_up(up[0],READ7)
    cleared=corridor.copy()
    stages.append(("gd",0,PARENT_CORE|gd|child_cursor|pbuf|(guards&cleared),gd))
    cleared|={(x,-1) for x in down}
    stages.append(("gu",1,PARENT_CORE|gu|child_cursor|pbuf|(guards&cleared),gu))
    final=PARENT_CORE|child_cursor|pbuf|guards
    return stages,final

def deps(L,Rterm):
    stages,final=geometry(L,Rterm)
    co=set(); ed=set()
    for _,_,S,_ in stages:
        a,b=interference(S); co|=a; ed|=b
    a,b=interference(final); co|=a; ed|=b
    return co,ed,stages,final

co8,ed8,st8,final8=deps(8,READ10)
assert not (co8 & shift(co8,16,0))
assert not (ed8 & shifted_edges(ed8,16))
blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(blocked_edges)
assert (len(OCC),len(blocked_edges),BLOCK)==(3,11,17)
terminal_S=[S for kind,c,S,R in st8 if kind=="h_term"][0]
assert d_units(terminal_S)==231
DNEW=d_units(terminal_S)-BLOCK
assert DNEW==214

SC=tuple(sorted(READ10))
CEL=((-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),
     (0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1))
IDX={c:i for i,c in enumerate(SC)}
FIDX={c:i for i,c in enumerate(CEL)}
P3=[1]
for _ in range(20): P3.append(P3[-1]*3)
def gettr(s,i): return (s//P3[i])%3
def settr(s,i,v): return s+(v-gettr(s,i))*P3[i]
def nidx(c): return [IDX[q] for q in neigh(c) if q in IDX]
@lru_cache(None)
def trans(s,li):
    kind,arg=LABELS10[li]
    out={}
    if kind=="CO":
        i=IDX[arg]
        if gettr(s,i)!=0: return ((s,72),)
        a=settr(s,i,1)
        os=[q for q in nidx(arg) if gettr(a,q)==2]
        if not os: return ((a,72),)
        assert 72%len(os)==0
        w=72//len(os)
        for q in os:
            t=settr(settr(a,i,0),q,0)
            out[t]=out.get(t,0)+w
    else:
        u,v=arg; iu,iv=IDX[u],IDX[v]
        if gettr(s,iu)!=0 or gettr(s,iv)!=0: return ((s,36),)
        a=settr(settr(s,iu,2),iv,2)
        cu=[q for q in nidx(u) if gettr(a,q)==1] or [-1]
        cv=[q for q in nidx(v) if gettr(a,q)==1] or [-1]
        den=len(cu)*len(cv); assert 36%den==0
        w=36//den
        for qu in cu:
            for qv in cv:
                t=a
                if qu!=-1: t=settr(settr(t,iu,0),qu,0)
                if qv!=-1: t=settr(settr(t,iv,0),qv,0)
                out[t]=out.get(t,0)+w
    return tuple(sorted(out.items()))

TARGET=((-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1))
TIDX=tuple(IDX[c] for c in TARGET)
def target(s): return all(gettr(s,i)==0 for i in TIDX)
@lru_cache(None)
def A(n,s,mask):
    if n==0: return int(target(s))
    z=0
    for li in range(10):
        if not ((mask>>li)&1): continue
        for t,w in trans(s,li): z += w*A(n-1,t,mask)
    return z

def enum_inits():
    fixed={(-2,0),(-2,1),(-1,0),(-1,1),(0,0),(0,1)}
    var=[c for c in CEL if c not in fixed]
    desc=set(); full=0
    for vals in product((0,1,2),repeat=len(var)):
        d={c:0 for c in fixed}; d.update(zip(var,vals))
        ok=True
        for c in CEL:
            a=d[c]
            for q in ((c[0]+1,c[1]),(c[0],c[1]+1)):
                if q in d and (a,d[q]) in ((1,2),(2,1)):
                    ok=False; break
            if not ok: break
        if not ok: continue
        full+=1; s=0
        for i,c in enumerate(SC): s += d[c]*P3[i]
        desc.add(s)
    return full,sorted(desc)
FULL,INITS=enum_inits()
assert (FULL,len(INITS))==(7255,1743)
N=8

def stage_poly(D,mask,lam):
    H=36*D
    mn=None
    for s in INITS:
        z=Fraction(0)
        for n in range(N+1):
            z += Fraction(A(n,s,mask), factorial(n)*H**n)*lam**n
        if mn is None or z<mn: mn=z
    return mn

MASK8=sum(1<<i for i in TERM8)
pold=Fraction(32,87)**2 * stage_poly(201,MASK8,Fraction(2))
POLD_STORED=Fraction(7168864776621912190976,514520327344022846669179035)
assert pold==POLD_STORED

r=Fraction(3,50)
exp_minus_r_lower=1-r+r*r/Fraction(2)-r**3/Fraction(6)
lam=Fraction(103,50)
pnew=Fraction(32,87)**2 * exp_minus_r_lower * stage_poly(DNEW,(1<<10)-1,lam)
PNEW_STORED=Fraction(
 103936503566984629647143194039811221052609,
 6221649932703678742303190625000000000000000000)
assert pnew==PNEW_STORED
assert pnew>pold

pboot=Fraction(6183007688263727208881325190913,1204952248442880000000000000000000000000)
p150=Fraction(20193231009117236036,580023299851226806640625)
p167=Fraction(9763107163899290190848,350499257108203128488308305)
p178=Fraction(11133436709205330292,456147586622526713121501)
p187=Fraction(22544728691405487104,1022833101788426753598015)
p197=Fraction(26015322500884764075008,1314271656156778872998881905)
p218=Fraction(1672277727444803056,105910938933255255436245)
p222=Fraction(40628945155674655856,2670355970159927065747101)
plan198=Fraction(2048,74183769)
b13=pboot*p150*p167*p178*p187*p197*pold*p218*p222*plan198
b14=b13/pold*pnew
assert b14>b13

p191=Fraction(32174057841088741889352078572126208,1524916181058564276415872049475569582080)
p211=Fraction(57085003286130579675209813685436416,3382506790988617846636155362604881018880)
plan191=Fraction(8192,276124689)
K7=pboot*p150*p167*p178*p191*p211*p211*plan191
qstar=b13/K7
a=Fraction(6,97)
U8=Fraction(1,1-a)*a**8*Fraction(3,8)**8*Fraction(8**8,factorial(8))
assert U8==Fraction(9565938,257342536062789905)
assert U8<qstar

print("PASS exact R08/E0011 maximal-terminal metric certificate")
print("generated_shield_full=",FULL,"descriptors=",len(INITS))
print("L8_full10_shared_CO=",len(co8 & shift(co8,16,0)))
print("L8_full10_shared_O2=",len(ed8 & shifted_edges(ed8,16)))
print("L8_terminal_coarse_D=",d_units(terminal_S),"blocked_units=",BLOCK,"owned_D=",DNEW)
print("pold_exact=",f"{pold.numerator}/{pold.denominator}")
print("pnew_exact=",f"{pnew.numerator}/{pnew.denominator}")
print("pnew_over_pold=",repr(float(pnew/pold)))
print("log10_pnew_over_pold=",repr(lg(pnew/pold)))
print("log10_b13=",repr(lg(b13)))
print("log10_b14=",repr(lg(b14)))
print("b14_gt_b13_exact=",b14>b13)
print("L7_8label_tail_upper_if_minlen_ge8=",f"{U8.numerator}/{U8.denominator}")
print("qstar_exact=",f"{qstar.numerator}/{qstar.denominator}")
print("tail_upper_lt_qstar_exact=",U8<qstar)
print("qstar_over_tail_upper=",repr(float(qstar/U8)))
