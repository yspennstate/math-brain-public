#!/usr/bin/env python3
# R15 / I0124 exact certificate for the 287- and 286-cap exclusions.
# All arithmetic is exact integer/Fraction arithmetic.
from fractions import Fraction
from math import comb

DIRS=(3**7-1)//2
AFF_H=3*DIRS
assert DIRS==1093 and AFF_H==3279

def moments(N):
    s1=DIRS*N
    c2=364*comb(N,2)
    c3=121*comb(N,3)
    s2=2*c2+s1
    s3=6*c3+6*c2+s1
    mu=Fraction(N,3)
    D2=Fraction(s2)-2*mu*s1+AFF_H*mu**2
    D3=Fraction(s3)-3*mu*s2+3*mu**2*s1-AFF_H*mu**3
    return D2,D3

def types(N):
    # Sorted parallel-slice sizes. c<=112 is the AG(6,3) maximum.
    # Proposition 4.1(b) excludes b+c>=222 for N=286,287:
    # it would force a<=55, hence b+c=N-a>=231 while b+c<=224.
    out=[]
    for a in range(113):
        for b in range(a,113):
            c=N-a-b
            if b<=c<=112 and b+c<=221:
                out.append((a,b,c))
    return out

def q23(t,N):
    mu=Fraction(N,3)
    xs=[Fraction(z)-mu for z in t]
    return sum(x*x for x in xs),sum(x*x*x for x in xs)

def convex_Q_lower(N,fixed):
    P=comb(N,2)
    M=3**7-N
    rem=P-sum(fixed)
    free=M-len(fixed)
    assert rem>=0 and free>0
    lo,hi=divmod(rem,free)
    # fixed lower bounds are all > the free average in every use below,
    # so the convex minimum sets them at equality and equalizes the rest.
    assert all(r>=lo+1 for r in fixed)
    return sum(comb(r,2) for r in fixed)+(free-hi)*comb(lo,2)+hi*comb(lo+1,2)

def r_lower(s):
    # s large hyperplanes through one anchor; each supplies >=54 projective
    # directions and two distinct hyperplanes overlap in <=20 directions.
    num=54*54*s
    den=54+20*(s-1)
    return (num+den-1)//den

assert r_lower(23)==136 and r_lower(24)==137

def parts_nondec(total,k,maxpart=23,low=1):
    if k==0:
        if total==0: yield ()
        return
    maxx=min(maxpart,total//k)
    for x in range(low,maxx+1):
        rem=total-x
        if rem < x*(k-1) or rem > maxpart*(k-1):
            continue
        for tail in parts_nondec(rem,k-1,maxpart,x):
            yield (x,)+tail

DATA = {
287: {
 "D2": Fraction(545300,3),
 "D3": Fraction(-23012234,9),
 "ntypes":221,
 "Lcoef":(Fraction(1600,316953),Fraction(-547,70434),Fraction(-41,70434)),
 "Leq":[(66,109,112),(69,109,109),(95,96,96)],
 "Lobj":Fraction(321987,3913),
 "L":83,
 "Qcoef":(Fraction(865943993267,88128),Fraction(43711021,19584),Fraction(145405,9792)),
 "Qeq":[(66,109,112),(87,88,112),(95,96,96)],
 "sumv":Fraction(12084989140531,1088),
 "Qfrac":Fraction(37715502131,88128),
 "Q":427962,
 "k_cut":10,
 "best":(448617,(16,21,23,23),(132,135,136,136)),
},
286: {
 "D2": Fraction(543686,3),
 "D3": Fraction(-22768174,9),
 "ntypes":230,
 "Lcoef":(Fraction(1681,324324),Fraction(-547,72072),Fraction(-5,9009)),
 "Leq":[(65,109,112),(68,109,109),(95,95,96)],
 "Lobj":Fraction(205675,6006),
 "L":35,
 "Qcoef":(Fraction(33596488355,3468),Fraction(5125659,2312),Fraction(17079,1156)),
 "Qeq":[(65,109,112),(87,87,112),(95,95,96)],
 "sumv":Fraction(6330786179495,578),
 "Qfrac":Fraction(19872255895,46818),
 "Q":424457,
 "k_cut":15,
 "best":(428950,(12,23),(128,136)),
}
}

for N,d in DATA.items():
    D2,D3=moments(N)
    assert (D2,D3)==(d["D2"],d["D3"])
    T=types(N)
    assert len(T)==d["ntypes"]

    l0,l2,l3=d["Lcoef"]
    eq=[]
    for t in T:
        q2,q3=q23(t,N)
        e=sum(z>=110 for z in t)
        slack=Fraction(e)-(l0+l2*q2+l3*q3)
        assert slack>=0
        if slack==0: eq.append(t)
    assert eq==d["Leq"]
    Lobj=l0*DIRS+l2*D2+l3*D3
    assert Lobj==d["Lobj"]
    L=(Lobj.numerator+Lobj.denominator-1)//Lobj.denominator
    assert L==d["L"]

    c0,c2,c3=d["Qcoef"]
    eq=[]
    for t in T:
        q2,q3=q23(t,N)
        v4=sum(comb(z,4) for z in t)
        slack=c0+c2*q2+c3*q3-v4
        assert slack>=0
        if slack==0: eq.append(t)
    assert eq==d["Qeq"]
    sumv=c0*DIRS+c2*D2+c3*D3
    assert sumv==d["sumv"]
    Qfrac=(sumv-40*comb(N,4))/81
    assert Qfrac==d["Qfrac"]
    Q=Qfrac.numerator//Qfrac.denominator
    assert Q==d["Q"]

    # k distinct anchors with r>=54. At k_cut the midpoint energy already
    # exceeds the upper bound, so only smaller k need support-distribution search.
    assert convex_Q_lower(N,[54]*d["k_cut"])>Q
    kmin=(L+22)//23
    overall=None
    for k in range(kmin,d["k_cut"]):
        local=None
        for svec in parts_nondec(L,k):
            rs=tuple(r_lower(s) for s in svec)
            q=convex_Q_lower(N,list(rs))
            cand=(q,svec,rs)
            if local is None or cand[0]<local[0]:
                local=cand
        assert local is not None
        if overall is None or local[0]<overall[0]:
            overall=local
    assert overall==d["best"]
    assert overall[0]>Q

# The same third-moment relaxation genuinely stops at N=285:
# a nonnegative rational combination of three no-110 direction types
# exactly matches the first three directional moments.
N=285
T=types(N)
support=[(67,109,109),(94,94,97),(94,95,96)]
weights=[Fraction(923542,6075),Fraction(43373,6075),Fraction(126068,135)]
assert all(t in T and max(t)<=109 for t in support)
D2,D3=moments(N)
assert sum(weights)==DIRS
assert sum(w*q23(t,N)[0] for w,t in zip(weights,support))==D2
assert sum(w*q23(t,N)[1] for w,t in zip(weights,support))==D3
assert all(w>0 for w in weights)

print("PASS R15 I0124 exact no-287/no-286 certificate")
for N in (287,286):
    d=DATA[N]
    print(f"N={N}; types={d['ntypes']}; D2={d['D2']}; D3={d['D3']}")
    print(f"N={N}; large110_lower={d['Lobj']} -> L>={d['L']}; Q<={d['Qfrac']} -> Q<={d['Q']}")
    print(f"N={N}; anchor_support<=23; best_Q_lower={d['best'][0]} at supports={d['best'][1]} r={d['best'][2]}")
    print(f"N={N}; contradiction_gap={d['best'][0]-d['Q']}")
print("N=285; three-moment relaxation has exact no-110 feasible mixture:")
print("support=[(67,109,109),(94,94,97),(94,95,96)]")
print("weights=[923542/6075,43373/6075,126068/135]")
print("CONCLUSION: no 287-cap and no 286-cap; c_7,3 <= 285; current method stalls at 285.")
