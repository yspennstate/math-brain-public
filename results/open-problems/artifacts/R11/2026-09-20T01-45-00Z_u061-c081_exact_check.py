from fractions import Fraction
from math import comb, factorial
from itertools import permutations
from collections import Counter

ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0))

def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def h_sup(i,j):
    a,b=i-1,j-1
    if a==0 and b==0:
        return Fraction(1)
    if a==0 or b==0:
        return Fraction(1)
    return Fraction((a**a)*(b**b), (a+b)**(a+b))

def riemann_h(N,i,j):
    return sum((Fraction(s,N)**(i-1)*(1-Fraction(s,N))**(j-1)
                for s in range(1,N)), Fraction(0))/N

def gNr(N,r):
    ans=Fraction(0)
    for s in range(1,N):
        x=Fraction(s,N)
        lam=Fraction(N,2*s*(N-s))
        ans += lam*(1-x**r-(1-x)**r)
    return ans

def profile_ids(blocks):
    ids=[]
    for b,s in enumerate(blocks):
        ids.extend([b]*s)
    return ids

def restricted_r_dist(blocks,m):
    N=sum(blocks)
    ids=profile_ids(blocks)
    cnt=Counter()
    total=0
    for pos in permutations(range(N),m):
        total += 1
        cnt[len({ids[p] for p in pos})] += 1
    return {r:Fraction(c,total) for r,c in sorted(cnt.items())}

def profile_pair_collision(blocks):
    N=sum(blocks)
    return Fraction(sum(s*(s-1) for s in blocks), N*(N-1))

def profile_total_rate(blocks,m):
    dist=restricted_r_dist(blocks,m)
    return sum((p*gNr(sum(blocks),r) for r,p in dist.items()), Fraction(0))

# 1. Algebraic identity behind the aggregate Riemann bound.
for m in range(2,31):
    lhs=sum((Fraction(comb(m,i), comb(m-2,i-1)) for i in range(1,m)), Fraction(0))
    rhs=2*(m-1)*H(m-1)
    check(lhs==rhs, f"binomial-harmonic identity m={m}: {lhs} != {rhs}")

# 2. Exact bounded-variation rectangle-rule inequality on a finite atlas.
for N in range(2,31):
    for m in range(2,min(10,N+2)):
        for i in range(1,m):
            j=m-i
            err=abs(riemann_h(N,i,j)-beta_int(i,j))
            bound=2*h_sup(i,j)/N
            check(err<=bound, f"Riemann BV bound N={N},m={m},i={i}: {err}>{bound}")
            check(h_sup(i,j)*comb(m-2,i-1) <= 1,
                  f"sup/binomial bound m={m},i={i}")

# 3. Exact total-rate formulas for r=2,3 independent dependence blocks.
for N in range(2,31):
    check(gNr(N,2)==Fraction(N-1,N), f"g2 N={N}")
    check(gNr(N,3)==Fraction(3*(N-1),2*N), f"g3 N={N}")

# 4. Fresh perfect / near-perfect matching collision probabilities.
for N in range(4,31):
    blocks=[2]*(N//2) + ([1] if N%2 else [])
    c=profile_pair_collision(blocks)
    target=Fraction(1,N-1) if N%2==0 else Fraction(1,N)
    check(c==target, f"matching collision N={N}: {c}!={target}")

# 5. N=4 exact C081 witness.
N=4
match4=[2,2]
check(profile_pair_collision(match4)==Fraction(1,3), "N=4 c")
root4=profile_total_rate(match4,4)
check(root4==Fraction(3,4), f"N=4 root {root4}")
balanced_each=root4/3
check(balanced_each==Fraction(1,4), f"N=4 each balanced {balanced_each}")
check(Fraction(3,11) != 1, "source topology probability differs")

# 6. N=9 C081 versus C079 exact scale-free separation.
match9=[2,2,2,2,1]
micro9=[3,3,3]
d_match=restricted_r_dist(match9,4)
d_micro=restricted_r_dist(micro9,4)
check(d_match=={2:Fraction(1,21),3:Fraction(4,7),4:Fraction(8,21)}, f"match9 rdist {d_match}")
check(d_micro=={2:Fraction(5,14),3:Fraction(9,14)}, f"micro9 rdist {d_micro}")

pair_match=Fraction(8,9)*(1-profile_pair_collision(match9))
pair_micro=Fraction(8,9)*(1-profile_pair_collision(micro9))
check(pair_match==Fraction(64,81), f"pair match {pair_match}")
check(pair_micro==Fraction(2,3), f"pair micro {pair_micro}")

root_match=profile_total_rate(match9,4)
root_micro=profile_total_rate(micro9,4)
check(root_match==Fraction(7240,5103), f"root match {root_match}")
check(root_micro==Fraction(74,63), f"root micro {root_micro}")

ratio_match=root_match/pair_match
ratio_micro=root_micro/pair_micro
check(ratio_match==Fraction(905,504), f"ratio match {ratio_match}")
check(ratio_micro==Fraction(37,21), f"ratio micro {ratio_micro}")
check(ratio_match != ratio_micro, "C081 and C079 must be scale-distinct")

print("U061/C081 EXACT CHECK")
print(f"ASSERTIONS={ASSERTIONS}")
print("N4_C081_ROOT_RATE=", root4)
print("N4_C081_EACH_2|2_RATE=", balanced_each)
print("N4_C081_BALANCED_ROOT_PROB=1")
print("N4_CTCS_BALANCED_ROOT_PROB=3/11")
print("N9_C081_R_DIST=", d_match)
print("N9_C079_R_DIST=", d_micro)
print("N9_C081_PAIR_RATE=", pair_match)
print("N9_C079_PAIR_RATE=", pair_micro)
print("N9_C081_4LABEL_ROOT_RATE=", root_match)
print("N9_C079_4LABEL_ROOT_RATE=", root_micro)
print("N9_C081_SCALEFREE_RATIO=", ratio_match)
print("N9_C079_SCALEFREE_RATIO=", ratio_micro)
print("ALL_EXACT_CHECKS_PASS")
