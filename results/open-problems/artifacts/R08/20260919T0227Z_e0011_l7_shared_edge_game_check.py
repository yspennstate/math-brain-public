#!/usr/bin/env python3
from itertools import product
from functools import lru_cache
from collections import Counter
from fractions import Fraction
from math import factorial, log10

DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c
    return {(x+dx,y+dy) for dx,dy in DIRS}
def shift(S,dx=0,dy=0):
    return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):
    return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def support(label):
    k,a=label
    roots={a} if k=="CO" else set(a)
    out=set(roots)
    for r in roots:
        out |= neigh(r)
    return out
def interference(S):
    co=set(S)
    for s in tuple(S):
        co |= neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u):
            ed.add(tuple(sorted((u,v))))
    return co,ed
def d_units(S):
    co,ed=interference(S)
    return 2*len(co)+len(ed)
def log10frac(x):
    return log10(x.numerator)-log10(x.denominator)

# Frozen local language from the certified one-column R08 construction.
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
LABELS7=LABELS10[:7]
READ=set()
for lab in LABELS7:
    READ |= support(lab)
TERM_ORIG=(0,1,2,4,5,6,7,8)
TERM=tuple(LABELS10[i] for i in TERM_ORIG)
READ_TERM=set()
for lab in TERM:
    READ_TERM |= support(lab)

# Exact current one-column geometry.
OPARENT={(-3,0),(-2,0)}
CPARENT=(-4,1)
OCC=OPARENT|{CPARENT}
CURSOR1={(0,0),(0,1)}
PARENT_CORE=OCC|CURSOR1
def read_down(a):
    return {(a+y,-x) for x,y in READ}
def read_up(a):
    return {(a+y,x+1) for x,y in READ}
def geometry(L):
    Ochild=tuple(sorted(((L-3,0),(L-2,0))))
    Cchild=(L-4,1)
    child_cursor={(L,0),(L,1)}
    pbuf=support(("O2",Ochild))|support(("CO",Cchild))
    down=(L-3,L-2)
    up=(L-4,L-3)
    guards={(x,-1) for x in down}|{(x,2) for x in up}
    corridor={(x,y) for x in range(0,L+1) for y in (0,1)}
    req=pbuf|child_cursor|guards
    stages=[]
    for c in range(2,L+1):
        R=shift(READ_TERM if c==L else READ,c-1,0)
        cleared={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared)
        stages.append(("h_term" if c==L else "h",c,S,R))
    gd,gu=read_down(down[0]),read_up(up[0])
    cleared=corridor.copy()
    S=PARENT_CORE|gd|child_cursor|pbuf|(guards&cleared)
    stages.append(("gd",0,S,gd))
    cleared|={(x,-1) for x in down}
    S=PARENT_CORE|gu|child_cursor|pbuf|(guards&cleared)
    stages.append(("gu",1,S,gu))
    final=PARENT_CORE|child_cursor|pbuf|guards
    return stages,final
def deps(L):
    stages,final=geometry(L)
    co=set(); ed=set()
    for _,_,S,_ in stages:
        a,b=interference(S); co|=a; ed|=b
    a,b=interference(final); co|=a; ed|=b
    return co,ed,stages,final

co8,ed8,_,_=deps(8)
assert not (co8 & shift(co8,16,0))
assert not (ed8 & shifted_edges(ed8,16))

co7,ed7,st7,final7=deps(7)
E7=((8,1),(9,1))
assert not (co7 & shift(co7,14,0))
assert ed7 & shifted_edges(ed7,14)=={E7}
touch=[]
for j,(kind,c,S,R) in enumerate(st7):
    if E7 in interference(S)[1]:
        touch.append((j,kind,c,tuple(sorted(support(("O2",E7)) & S))))
assert touch==[
 (5,"h_term",7,((7,1),)),
 (6,"gd",0,((7,1),)),
 (7,"gu",1,((7,1),)),
]
assert support(("O2",E7)) & final7 == {(7,1)}

# Fixed parent particles make 3 CO clocks and 11 incident O2 clocks blocked.
blocked_edges={tuple(sorted((u,v))) for u in OCC for v in neigh(u)}
BLOCK=2*len(OCC)+len(blocked_edges)
assert (len(OCC),len(blocked_edges),BLOCK)==(3,11,17)
# Remove the one shared edge from the left block's owned hazard precisely where
# the robust terminal construction makes it an environment input.
coarse=[d_units(S) for _,_,S,_ in st7]
owned=[]
for kind,c,S,R in st7:
    owned.append(d_units(S)-BLOCK-(1 if E7 in interference(S)[1] else 0))
owned_final=d_units(final7)-BLOCK-1
assert coarse==[157,167,184,195,208,212,229,229]
assert owned==[140,150,167,178,191,194,211,211]
assert owned_final==191

# In terminal local coordinates (global shift +6), E7 is the outside edge
# ((2,1),(3,1)). Its only possible effect on the owned state READ_TERM is:
# leave it unchanged, or delete a CO at local target site (1,1).
SC=tuple(sorted(READ))
IDX={c:i for i,c in enumerate(SC)}
assert (1,1) in IDX
CEL=((-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),
     (0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1))
FIDX={c:i for i,c in enumerate(CEL)}
FIXED={(-2,0),(-2,1),(-1,0),(-1,1),(0,0),(0,1)}
VAR=tuple(c for c in CEL if c not in FIXED)
def stable_full(d):
    for c in CEL:
        a=d[c]
        for dx,dy in ((1,0),(0,1)):
            q=(c[0]+dx,c[1]+dy)
            if q in FIDX:
                b=d[q]
                if (a,b) in ((1,2),(2,1)):
                    return False
    return True
INITS=set()
full=0
for vals in product((0,1,2),repeat=len(VAR)):
    d={c:0 for c in FIXED}
    d.update(dict(zip(VAR,vals)))
    if stable_full(d):
        full+=1
        INITS.add(tuple(d[c] for c in SC))
assert (full,len(INITS))==(7255,1743)

TARGET=((-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1))
TIDX=tuple(IDX[c] for c in TARGET)
def is_target(s):
    return all(s[i]==0 for i in TIDX)

@lru_cache(None)
def trans(s,li):
    kind,arg=TERM[li]
    out=set()
    a=list(s)
    if kind=="CO":
        i=IDX[arg]
        if a[i]!=0:
            return frozenset((s,))
        a[i]=1
        os=[q for q in neigh(arg) if q in IDX and a[IDX[q]]==2]
        if not os:
            return frozenset((tuple(a),))
        for q in os:
            t=a.copy()
            t[i]=0
            t[IDX[q]]=0
            out.add(tuple(t))
        return frozenset(out)
    u,v=arg
    iu,iv=IDX[u],IDX[v]
    if a[iu]!=0 or a[iv]!=0:
        return frozenset((s,))
    a[iu]=a[iv]=2
    cu=[q for q in neigh(u) if q in IDX and a[IDX[q]]==1] or [None]
    cv=[q for q in neigh(v) if q in IDX and a[IDX[q]]==1] or [None]
    for qu in cu:
        for qv in cv:
            t=a.copy()
            if qu is not None:
                t[iu]=0
                t[IDX[qu]]=0
            if qv is not None:
                t[iv]=0
                t[IDX[qv]]=0
            out.add(tuple(t))
    return frozenset(out)

DEL=IDX[(1,1)]
def edge_closure(states):
    out=set(states)
    for s in tuple(states):
        if s[DEL]==1:
            t=list(s)
            t[DEL]=0
            out.add(tuple(t))
    return frozenset(out)
def step(B,li):
    out=set()
    for s in B:
        out.update(trans(s,li))
    return edge_closure(out)

# A single owned word works for every stable generated-shield input, every
# instantaneous reaction branch, and every timing of the unowned shared edge.
WORD=(3,0,0,0,2,2,0,2,3,4,4,0,4,7,7,7,1,0,7,0,1)
B=edge_closure(INITS)
sizes=[len(B)]
for li in WORD:
    B=step(B,li)
    sizes.append(len(B))
assert all(is_target(s) for s in B)
assert len(B)==18

# The word is deliberately not asserted shortest.  It has 14 CO marks and 7 O2
# marks.  In a terminal window whose owned hazard has D=194 units, the exact
# cylinder event "exactly these 21 owned marks in this order" has the following
# rational lower bound, using e^-1 > 32/87.
types=Counter(TERM[i][0] for i in WORD)
assert types==Counter({"CO":14,"O2":7})
m=len(WORD)
D=194
qword=Fraction(32,87)**m * Fraction(m**m,factorial(m)) * Fraction(2**14,D**m)

# Previously certified exact factors needed only to show the L=7 robust-word
# block is positive but does NOT improve the frozen metric b13.
pboot=Fraction(
 6183007688263727208881325190913,
 1204952248442880000000000000000000000000)
p150=Fraction(20193231009117236036,580023299851226806640625)
p167=Fraction(9763107163899290190848,350499257108203128488308305)
p178=Fraction(11133436709205330292,456147586622526713121501)
p187=Fraction(22544728691405487104,1022833101788426753598015)
p197=Fraction(26015322500884764075008,1314271656156778872998881905)
p201=Fraction(7168864776621912190976,514520327344022846669179035)
p218=Fraction(1672277727444803056,105910938933255255436245)
p222=Fraction(40628945155674655856,2670355970159927065747101)
plan198=Fraction(2048,74183769)
b13=pboot*p150*p167*p178*p187*p197*p201*p218*p222*plan198

# Exact new L=7 nonterminal/guard factors are re-derived by the companion C++
# checker for this run.
p191=Fraction(
 32174057841088741889352078572126208,
 1524916181058564276415872049475569582080)
p211=Fraction(
 57085003286130579675209813685436416,
 3382506790988617846636155362604881018880)
plan191=Fraction(8192,276124689)
b7word=pboot*p150*p167*p178*p191*qword*p211*p211*plan191
assert b7word>0
assert b7word<b13

print("PASS exact R08/E0011 L=7 shared-edge robust-word game certificate")
print("generated_shield_full=",full,"descriptors=",len(INITS))
print("L7_shared_CO=",sorted(co7 & shift(co7,14,0)))
print("L7_shared_edges=",sorted(ed7 & shifted_edges(ed7,14)))
print("L7_shared_edge_touch=",touch)
print("L7_owned_stage_D=",owned,"planter_D=",owned_final)
print("robust_word_length=",len(WORD),"word=",WORD)
print("robust_word_types=",dict(types))
print("belief_sizes=",sizes)
print("final_belief_size=",len(B),"all_target=",all(is_target(s) for s in B))
print("qword_exact=",f"{qword.numerator}/{qword.denominator}")
print("log10_qword=",repr(log10frac(qword)))
print("b7word_positive=",b7word>0)
print("b7word_lt_b13_exact=",b7word<b13)
print("log10_b7word=",repr(log10frac(b7word)))
print("log10_b13=",repr(log10frac(b13)))
print("log10_b7word_over_b13=",repr(log10frac(b7word/b13)))
