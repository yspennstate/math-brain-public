#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter

ASSERTIONS = 0
def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg or f"assertion {ASSERTIONS} failed")

def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)), F())

def threshold_weights(q):
    W = sum((F(1,u*(q-u)) for u in range(1,q)), F())
    return {u:F(1,u*(q-u))/W for u in range(1,q)}, W

def poly_values(q, coeffs, pts):
    out=[]
    for x in pts:
        v=0
        p=1
        for c in coeffs:
            v=(v+c*p)%q
            p=(p*x)%q
        out.append(v)
    return out

def split_prob_poly(q,d,pts,A,B):
    weights,_ = threshold_weights(q)
    tot=F()
    for u,wu in weights.items():
        cnt=0
        for coeffs in product(range(q), repeat=d):
            vals=poly_values(q,coeffs,pts)
            e1=all(vals[i]<u for i in A) and all(vals[i]>=u for i in B)
            e2=all(vals[i]>=u for i in A) and all(vals[i]<u for i in B)
            cnt += int(e1 or e2)
        tot += wu*F(cnt,q**d)
    return tot

def clip(poly,A,B,C,le=True):
    def v(P): return A*P[0]+B*P[1]-C
    def inside(P): return v(P)<=0 if le else v(P)>=0
    if not poly: return []
    out=[]
    seq=poly[1:]+poly[:1]
    for P,Q in zip(poly,seq):
        ip,iq=inside(P),inside(Q)
        vp,vq=v(P),v(Q)
        if ip: out.append(P)
        if ip != iq:
            s=vp/(vp-vq)
            out.append((P[0]+s*(Q[0]-P[0]),P[1]+s*(Q[1]-P[1])))
    return out

def area(poly):
    if len(poly)<3: return F()
    s=F()
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        s += P[0]*Q[1]-P[1]*Q[0]
    return abs(s)/2

def oriented_ap_area(t,Aset,Bset):
    # (Y0,Y1,Y2,Y3)=(a,a+b,a+2b,a+3b) mod 1, (a,b) uniform on T^2.
    tot=F()
    for ns in product(range(1),range(2),range(3),range(4)):
        poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
        for k,n in enumerate(ns):
            poly=clip(poly,F(1),F(k),F(n),le=False)
            poly=clip(poly,F(1),F(k),F(n+1),le=True)
            if not poly: break
            if k in Aset:
                poly=clip(poly,F(1),F(k),F(n)+t,le=True)
            elif k in Bset:
                poly=clip(poly,F(1),F(k),F(n)+t,le=False)
            if not poly: break
        tot += area(poly)
    return tot

# Harmonic threshold identity and pair normalization.
for q in [5,7,11,13]:
    weights,W=threshold_weights(q)
    check(sum(weights.values(),F())==1)
    check(W == F(2,q)*harmonic(q-1))
    p11 = split_prob_poly(q,2,[0,1],[0],[1])
    lam = F(1,1)/p11
    check(lam == F(q,q-1)*harmonic(q-1))
    # Pair law is independent of polynomial dimension d>=2.
    for d in [2,3,4]:
        check(split_prob_poly(q,d,[0,1],[0],[1]) == p11)

# Exact q=7 finite witnesses.
q=7
p11=split_prob_poly(q,2,[0,1],[0],[1])
lam=1/p11
check(p11==F(120,343))
check(lam==F(343,120))

specs=[
    ([0,1,2,3],[0,1],[2,3]),
    ([0,1,2,4],[0,1],[2,3]),
    ([0,1,2,3],[0],[1,2,3]),
]
expected2=[F(8,45),F(3,20),F(29,90)]
expected3=[F(19,90),F(13,70),F(13,45)]
expectedmix=[F(7,36),F(47,280),F(11,36)]
for (pts,A,B),e2,e3,em in zip(specs,expected2,expected3,expectedmix):
    r2=lam*split_prob_poly(q,2,pts,A,B)
    r3=lam*split_prob_poly(q,3,pts,A,B)
    check(r2==e2)
    check(r3==e3)
    check((r2+r3)/2==em)

# Relabel-invariant 2|2 rate multisets on seven labels.
def rate_for_sets(d,Aset,Bset):
    pts=sorted(set(Aset)|set(Bset))
    pos={x:i for i,x in enumerate(pts)}
    A=[pos[x] for x in Aset]
    B=[pos[x] for x in Bset]
    return lam*split_prob_poly(7,d,pts,A,B)

r2=[]
rmix=[]
for four in combinations(range(7),4):
    four=set(four); a0=min(four)
    for partner in sorted(four-{a0}):
        A={a0,partner}; B=four-A
        x2=rate_for_sets(2,A,B)
        x3=rate_for_sets(3,A,B)
        r2.append(x2)
        rmix.append((x2+x3)/2)
check(len(r2)==105)
check(Counter(r2)==Counter({F(8,45):63,F(3,20):42}))
check(Counter(rmix)==Counter({F(7,36):63,F(47,280):42}))
check(sum(r2,F())/105==F(1,6))
check(sum(rmix,F())/105==F(193,1050))

# Pairwise independence fools every 3-label binary split exactly:
# z0(1-z1)(1-z2)+(1-z0)z1z2 = z0-z0z1-z0z2+z1z2.
for bits in product([0,1],repeat=3):
    z0,z1,z2=bits
    lhs=z0*(1-z1)*(1-z2)+(1-z0)*z1*z2
    rhs=z0-z0*z1-z0*z2+z1*z2
    check(lhs==rhs)

# Continuous affine-hash obstruction for the balanced split 01|23.
# Exact polygon clipping verifies the piecewise area formula at a dense rational test set.
def p_formula(t):
    if t<=F(1,3):
        return t*t
    if t<=F(2,3):
        return -2*t*t+2*t-F(1,3)
    return (1-t)*(1-t)

tested=set()
for den in range(3,41):
    for num in range(1,den):
        t=F(num,den)
        if t in tested: continue
        tested.add(t)
        p=oriented_ap_area(t,{0,1},{2,3})+oriented_ap_area(t,{2,3},{0,1})
        check(p==p_formula(t),f"polygon formula failed t={t}: {p} vs {p_formula(t)}")

# The limiting normalized balanced rate is
# L = log 3 - (4/3)log 2, and L>1/6 since
# 6L-1 = log(729/256)-1 and 729/256 > 11/4 > e.
check(F(729,256)>F(11,4))
# Elementary exact tail bound: e = 1+1+1/2+sum_{n>=3}1/n! < 5/2+1/4 = 11/4.
check(F(5,2)+F(1,4)==F(11,4))

# Random-degree C056 uses D uniform on {2,...,L_N}; probability of a bad
# degree for a fixed k is <= (k-2)/(L_N-1), hence tends to zero as L_N->infinity.
for L in range(3,50):
    for k in range(2,15):
        bad=sum(1 for d in range(2,L+1) if d<k)
        check(F(bad,L-1)<=min(F(1),F(max(0,k-2),L-1)))

print("ALL_EXACT_CHECKS_PASS")
print("assertions",ASSERTIONS)
print("q7_pair_probability",p11)
print("q7_lambda",lam)
print("C055_2x2_rate_multiset",dict(Counter(r2)))
print("C056_2x2_rate_multiset",dict(Counter(rmix)))
print("C055_mean_normalized_2x2",sum(r2,F())/105)
print("C056_mean_normalized_2x2",sum(rmix,F())/105)
print("affine_limit_balanced_rate","log(3)-(4/3)log(2)")
print("ctcs_balanced_rate",F(1,6))
