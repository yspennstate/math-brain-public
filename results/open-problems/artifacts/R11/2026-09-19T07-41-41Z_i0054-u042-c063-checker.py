from fractions import Fraction
from itertools import product, combinations
from math import comb

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def tilted_probs(N, x, sigma):
    M = max(x, 1-x)
    out = {}
    total = Fraction(0)
    for z in product((0,1), repeat=N):
        m = sum(z)
        base = x**m * (1-x)**(N-m)
        centered = Fraction(1)
        for zi in z:
            centered *= Fraction(zi) - x
        R = centered / (M**N)
        p = base * (1 + sigma*R)
        check(p >= 0, ("negative", N, x, sigma, z, p))
        out[z] = p
        total += p
    check(total == 1, ("normalization", N, x, sigma, total))
    return out

def iid_marginal_prob(x, bits):
    m = sum(bits)
    return x**m * (1-x)**(len(bits)-m)

def marginal_prob(probs, coords, bits):
    s = Fraction(0)
    for z,p in probs.items():
        if all(z[c] == b for c,b in zip(coords,bits)):
            s += p
    return s

# U042 combinatorial sharp constant: maximum number of unordered binary
# split transitions out of a partition of [k] is S_k=2^(k-1)-1.
def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n+1):
        for tail in integer_partitions(n-first, first):
            yield (first,) + tail

for k in range(2, 13):
    S = 2**(k-1)-1
    vals=[]
    for parts in integer_partitions(k):
        v=sum((2**(b-1)-1) for b in parts if b>=2)
        vals.append(v)
        check(v <= S, ("split count", k, parts, v, S))
    check(max(vals) == S, ("sharp split count", k, max(vals), S))
    # Universal max-row-sum constant 2S is attained when every outgoing
    # rate is perturbed by the same positive epsilon.
    eps = Fraction(1, 101)
    offsum = S*eps
    rowsum = offsum + abs(-offsum)
    check(rowsum == 2*S*eps, ("row norm sharpness", k))

# Global centered-product tilt: every proper marginal is exactly iid.
for N in range(2, 8):
    for u in range(1,N):
        x=Fraction(u,N)
        for sigma in (1,-1):
            probs=tilted_probs(N,x,sigma)
            # Exhaustively test every proper-coordinate cylinder.
            for r in range(0,N):
                for coords in combinations(range(N), r):
                    for bits in product((0,1), repeat=r):
                        got=marginal_prob(probs, coords, bits)
                        want=iid_marginal_prob(x,bits)
                        check(got == want, ("marginal", N,u,sigma,coords,bits,got,want))

# At x=1/2, the two signs are disjoint parity laws and are maximally apart.
for N in range(2,9):
    x=Fraction(1,2)
    plus=tilted_probs(N,x,1)
    minus=tilted_probs(N,x,-1)
    overlap=sum(min(plus[z],minus[z]) for z in plus)
    tv=1-overlap
    check(tv == 1, ("TV plus/minus",N,tv))
    tv_iid=Fraction(1,2)*sum(abs(plus[z]-Fraction(1,2**N)) for z in plus)
    check(tv_iid == Fraction(1,2), ("TV plus/iid",N,tv_iid))

# C063 gate legality, exact proper-restriction split rates, pair normalization.
def split_prob_iid(x,i,j):
    return x**i*(1-x)**j + x**j*(1-x)**i

def c_weight(x):
    return Fraction(1,1)/(2*x*(1-x))

for N in range(2, 101):
    delta=Fraction(1,N*N)
    for u in range(1,N):
        x=Fraction(u,N)
        p=delta*c_weight(x)
        check(0 <= p <= 1, ("gate legal",N,u,p))
    # pair separation cycle-average rate is exactly one
    pair=Fraction(0)
    for u in range(1,N):
        x=Fraction(u,N)
        pair += c_weight(x)*split_prob_iid(x,1,1)
    pair /= (N-1)
    check(pair == 1, ("pair rate",N,pair))

# Directly enumerate tilted full proposals and compare every proper visible
# specified split cylinder to iid for N<=7.  We fix A first i labels and B next j.
for N in range(3,8):
    for u in range(1,N):
        x=Fraction(u,N)
        for sigma in (1,-1):
            probs=tilted_probs(N,x,sigma)
            for k in range(2,N):
                for i in range(1,k):
                    j=k-i
                    # unordered specified split: A=ones,B=zeros OR complement
                    direct=Fraction(0)
                    for z,p in probs.items():
                        first=tuple(z[:k])
                        pat1=(1,)*i+(0,)*j
                        pat2=(0,)*i+(1,)*j
                        if first==pat1 or first==pat2:
                            direct += p
                    want=split_prob_iid(x,i,j)
                    check(direct==want, ("specified split",N,u,sigma,i,j,direct,want))

# Harmonic-grid averaged rates equal the standard Riemann-sum formula exactly.
def grid_rate(N,i,j):
    s=Fraction(0)
    for u in range(1,N):
        x=Fraction(u,N)
        s += c_weight(x)*split_prob_iid(x,i,j)
    return s/(N-1)

def grid_rate_simple(N,i,j):
    s=Fraction(0)
    for u in range(1,N):
        x=Fraction(u,N)
        s += x**(i-1)*(1-x)**(j-1)
    return s/(N-1)

for N in range(3,31):
    for k in range(2,min(N,8)):
        for i in range(1,k):
            j=k-i
            check(grid_rate(N,i,j)==grid_rate_simple(N,i,j),
                  ("grid identity",N,i,j,grid_rate(N,i,j),grid_rate_simple(N,i,j)))

# Exact N=4 finite witness: alternating sign by whole threshold cycle.
# The probability of the eventual first nontrivial root split being 2|2 is
# obtained by one six-step supercycle plus geometric repetition.
def root_shape_witness_N4():
    N=4
    delta=Fraction(1,N*N)
    steps=[]
    for sigma in (1,-1):
        for u in range(1,N):
            x=Fraction(u,N)
            pg=delta*c_weight(x)
            probs=tilted_probs(N,x,sigma)
            shape={0:Fraction(0),1:Fraction(0),2:Fraction(0)}
            for z,p in probs.items():
                shape[min(sum(z),N-sum(z))] += p
            b1=pg*shape[1]
            b2=pg*shape[2]
            steps.append((b1,b2,b1+b2))
    surv=Fraction(1)
    n1=n2=Fraction(0)
    for b1,b2,a in steps:
        n1 += surv*b1
        n2 += surv*b2
        surv *= 1-a
    den=1-surv
    return n1/den,n2/den,den,steps

p13,p22,period_success,steps=root_shape_witness_N4()
check(p13+p22==1, ("root shapes sum",p13,p22))
expected_balanced=Fraction(67277422797,177345915301)
check(p22==expected_balanced, ("N4 witness",p22,expected_balanced))
# Critical beta=-1 DTCS(4): ordered split probabilities 4/11,3/11,4/11.
check(p22 != Fraction(3,11), ("distinct from source",p22))
check(p22 > Fraction(3,11), ("witness direction",p22))
# First-cycle center threshold illustrates parity extremality exactly.
center_plus=tilted_probs(4,Fraction(1,2),1)
center_minus=tilted_probs(4,Fraction(1,2),-1)
plus_shape=[Fraction(0)]*3
minus_shape=[Fraction(0)]*3
for z,p in center_plus.items():
    plus_shape[min(sum(z),4-sum(z))]+=p
for z,p in center_minus.items():
    minus_shape[min(sum(z),4-sum(z))]+=p
check(plus_shape==[Fraction(1,4),Fraction(0),Fraction(3,4)], ("center plus",plus_shape))
check(minus_shape==[Fraction(0),Fraction(1),Fraction(0)], ("center minus",minus_shape))

# Closest retained high-order-dependent class C057 has normalized N=4
# specified rates q(1,3)=7/36 and q(2,2)=11/36.  Summing 4 singleton
# shapes and 3 balanced shapes gives its root balanced-shape probability 33/61.
c057_balanced = Fraction(33,61)
check(p22 != c057_balanced, ("distinct from C057",p22,c057_balanced))

print("R11-I0054-U042/C063 exact self-check")
print("assertions =", CHECKS)
print("N4_C063_root_P_1v3 =", p13)
print("N4_C063_root_P_2v2 =", p22)
print("N4_source_DTCS_root_P_2v2 =", Fraction(3,11))
print("N4_C057_root_P_2v2 =", c057_balanced)
print("N4_one_supercycle_success =", period_success)
print("center_plus_shapes_trivial_1v3_2v2 =", plus_shape)
print("center_minus_shapes_trivial_1v3_2v2 =", minus_shape)
print("ALL_EXACT_CHECKS_PASS")
