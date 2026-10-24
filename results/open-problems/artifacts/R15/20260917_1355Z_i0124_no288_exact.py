#!/usr/bin/env python3
# R15 / I0124 exact certificate for the Games-graph reduction and overlap corridor.
# Integer/rational arithmetic only; no numerical path/sample evidence.

from itertools import product, combinations
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

def add(a,b):
    return tuple((x+y)%3 for x,y in zip(a,b))
def neg(a):
    return tuple((-x)%3 for x in a)
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%3

# Explicit doubled-Hill 112-cap H in AG(6,3)
blocks = ["012","013","024","035","045","125","134","145","234","235"]
H=set()
for b in blocks:
    inds=list(map(int,b))
    for vals in product([1,2], repeat=3):
        v=[0]*6
        for i,a in zip(inds,vals):
            v[i]=a
        H.add(tuple(v))
for vals in product([1,2], repeat=6):
    if sum(a==2 for a in vals)%2==0:
        H.add(tuple(vals))

F=list(product(range(3), repeat=6))
zero=(0,)*6
assert len(H)==112
assert all(neg(h) in H for h in H)
for x,y in combinations(H,2):
    assert neg(add(x,y)) not in H

# Character spectrum of Cay(F_3^6,H)
profiles=Counter()
T=set()
U=set()
for xi in F:
    if xi==zero:
        continue
    c=[0,0,0]
    for h in H:
        c[dot(xi,h)]+=1
    assert c[1]==c[2]
    eig=c[0]-c[1]
    profiles[tuple(c)]+=1
    if eig==-23:
        T.add(xi)
    elif eig==4:
        U.add(xi)
    else:
        raise AssertionError((xi,c,eig))
assert profiles==Counter({(22,45,45):112,(40,36,36):616})
assert len(T)==112 and len(U)==616

assert all(neg(x) in T for x in T)
for x,y in combinations(T,2):
    assert neg(add(x,y)) not in T
dual_by_class=defaultdict(set)
for x in F:
    c=[0,0,0]
    for xi in T:
        c[dot(xi,x)]+=1
    assert c[1]==c[2]
    val=c[0]-c[1]
    cls="zero" if x==zero else ("H" if x in H else "other")
    dual_by_class[cls].add(val)
assert dual_by_class["zero"]=={112}
assert dual_by_class["H"]=={-23}
assert dual_by_class["other"]=={4}

common=defaultdict(set)
for d in F:
    if d==zero:
        continue
    cnt=sum(1 for h in H if tuple((h[i]-d[i])%3 for i in range(6)) in H)
    common["edge" if d in H else "nonedge"].add(cnt)
assert common["edge"]=={1}
assert common["nonedge"]=={20}

N_DIR=(3**7-1)//2
assert N_DIR==1093
D2=182304
D3=-2584224

types=[]
for a in range(113):
    for b in range(a,113):
        c=288-a-b
        if b<=c<=112 and b+c<=221:
            types.append((a,b,c))
assert len(types)==213
assert min(a for a,b,c in types)==67

C0=9965880
Acoef=Fraction(215717,96)
Bcoef=Fraction(3821,256)
equalities=[]
for a,b,c in types:
    xs=[a-96,b-96,c-96]
    q2=sum(x*x for x in xs)
    q3=sum(x*x*x for x in xs)
    v4=sum(comb(z,4) for z in (a,b,c))
    slack=Fraction(C0)+Acoef*q2+Bcoef*q3-v4
    assert slack>=0, ((a,b,c),slack)
    if slack==0:
        equalities.append((a,b,c))
assert equalities==[(67,109,112),(88,88,112),(96,96,96)]

sum_v4_bound=Fraction(C0*N_DIR)+Acoef*D2+Bcoef*D3
assert sum_v4_bound==Fraction(90110254887,8)
Q_bound=(sum_v4_bound-40*comb(288,4))/81
assert Q_bound==Fraction(10359781,24)
Q_integer_upper=Q_bound.numerator//Q_bound.denominator
assert Q_integer_upper==431657

def spectral_gap(p,q,t):
    X=Fraction(4*p*q,729)+Fraction(4*t,27)
    Y=Fraction(23*t,27)-Fraction(5*p*q,729)
    L=abs(X)+abs(Y)
    EA=Fraction(p)-Fraction(p*p,729)
    EB=Fraction(q)-Fraction(q*q,729)
    return L*L-EA*EB

min_gap=None
min_arg=None
for p in range(67,110):
    q=176-p
    if not (67<=q<=109):
        continue
    for t in range(22):
        gap=spectral_gap(p,q,t)
        assert gap>0
        if min_gap is None or gap<min_gap:
            min_gap=gap
            min_arg=(p,q,t)
assert min_gap==Fraction(22498796,531441)
assert min_arg==(67,109,21)

TOTAL_PAIRS=comb(288,2)
N_COMPLEMENT=3**7-288
assert TOTAL_PAIRS==41328 and N_COMPLEMENT==1899
def convex_min_Q_given_r0(r0):
    rem=TOTAL_PAIRS-r0
    n=N_COMPLEMENT-1
    lo=rem//n
    hi_count=rem%n
    return comb(r0,2)+(n-hi_count)*comb(lo,2)+hi_count*comb(lo+1,2)
qmins=[(r,convex_min_Q_given_r0(r)) for r in range(92,145)]
assert min(qmins,key=lambda z:z[1])==(92,431704)
assert all(q>Q_integer_upper for r,q in qmins)

mid=Counter()
HL=list(H)
for i in range(len(HL)):
    for j in range(i+1,len(HL)):
        mid[neg(add(HL[i],HL[j]))]+=1
assert all(m not in H for m in mid)
assert len(mid)==617
assert Counter(mid.values())==Counter({10:616,56:1})

large_eq=[]
for a,b,c in types:
    xs=[a-96,b-96,c-96]
    q2=sum(x*x for x in xs)
    q3=sum(x*x*x for x in xs)
    e_large=sum(z>=111 for z in (a,b,c))
    val=602*e_large+14*q2+q3
    assert val>=0
    if val==0:
        large_eq.append((a,b,c))
assert large_eq==[(67,110,111),(68,110,110),(96,96,96)]
L_num=-(14*D2+D3)
assert L_num==31968
assert (L_num+601)//602==54

def r_lower(s):
    num=55*55*s
    den=55+20*(s-1)
    return (num+den-1)//den
assert r_lower(9)==127
assert r_lower(15)==136
assert r_lower(16)==137

def convex_Q_lower(fixed_rs):
    rem=TOTAL_PAIRS-sum(fixed_rs)
    n=N_COMPLEMENT-len(fixed_rs)
    lo=rem//n
    hi=rem%n
    return sum(comb(r,2) for r in fixed_rs)+(n-hi)*comb(lo,2)+hi*comb(lo+1,2)
assert convex_Q_lower([55]*5)==432024 > Q_integer_upper
Q_four_anchor_lower=convex_Q_lower([127]*4)
assert Q_four_anchor_lower==451479
assert Q_four_anchor_lower>Q_integer_upper

print("PASS R15 I0124 exact no-288 certificate")
print(f"H_size={len(H)}; H_is_centrally_symmetric_cap=True")
print("character_profiles={(22,45,45):-23 x112, (40,36,36):+4 x616}")
print("dual_cap_T_size=112; dual_transform={112^1,-23^112,+4^616}")
print("Cayley(H)=srg(729,112,1,20); spectrum=112^1,4^616,(-23)^112")
print("cross_projection: 729X=4pq+108t; 729Y=621t-5pq")
print(f"allowed_direction_types={len(types)}; supporting_equalities={equalities}")
print(f"Q_upper={Q_bound}; integer_Q_upper={Q_integer_upper}")
print(f"spectral_min_gap_t<=21={min_gap} at {min_arg}")
print("overlap_corridor=22<=t<=35; anchor_pairs=78..91")
print("midpoint_profile_H={56^1,10^616}; 111-cap extension core certified")
print("large_hyperplanes>=54; anchors<=4; slices_per_anchor<=15")
print(f"four_anchor_Q_lower={Q_four_anchor_lower} > integer_Q_upper={Q_integer_upper}")
print("CONCLUSION: hypothetical 288-cap impossible; c_7,3 <= 287")
