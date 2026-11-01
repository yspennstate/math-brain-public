from fractions import Fraction
from itertools import combinations, product
from math import isqrt, comb

ASSERTIONS=0
def check(cond,msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def ceil_sqrt(n):
    r=isqrt(n)
    return r if r*r==n else r+1

def eps_c078(N):
    L=ceil_sqrt(N)
    return Fraction(L-1,L)

def pi(bit,x):
    return x if bit else 1-x

def trans_gap(a,b,x,eps,gap):
    rho=eps**gap
    return (1-rho)*pi(b,x) + (rho if a==b else 0)

def patt_positions(positions,bits,x,eps):
    p=pi(bits[0],x)
    for q in range(len(bits)-1):
        p*=trans_gap(bits[q],bits[q+1],x,eps,positions[q+1]-positions[q])
    return p

def iid_patt(bits,x):
    p=Fraction(1)
    for b in bits:
        p*=pi(b,x)
    return p

def Amean(N,eps):
    return Fraction(2,N*(N-1))*sum(Fraction(N-d)*(eps**d) for d in range(1,N))

def mark_split_prob_shuffled(N,m,i,x,eps):
    # Fixed specified i | m-i label split after a uniform random ambient permutation.
    tot=Fraction(0)
    den=comb(N,m)*comb(m,i)
    for pos in combinations(range(N),m):
        for red_idx in combinations(range(m),i):
            R=set(red_idx)
            bits=tuple(1 if q in R else 0 for q in range(m))
            compbits=tuple(1-b for b in bits)
            tot += patt_positions(pos,bits,x,eps)+patt_positions(pos,compbits,x,eps)
    return tot/Fraction(den)

def mark_split_prob_iid(m,i,x):
    return x**i*(1-x)**(m-i) + x**(m-i)*(1-x)**i

def split_rate_shuffled(N,m,i,eps):
    s=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        lam=Fraction(N,2*j*(N-j))
        s += lam*mark_split_prob_shuffled(N,m,i,x,eps)
    return s

def split_rate_iid(N,m,i):
    s=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        lam=Fraction(N,2*j*(N-j))
        s += lam*mark_split_prob_iid(m,i,x)
    return s

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

print("R11-I0054 U057/U058/C078 shuffled-sticky exact self-check")

# Proposal normalization.
for N in range(2,16):
    total=sum((Fraction(N,2*j*(N-j)) for j in range(1,N)),Fraction(0))
    check(total==H(N-1), f"proposal normalization N={N}")

# Exact Markov pattern factor bound, including arbitrary sampled gaps.
for N in range(2,10):
    eps=eps_c078(N)
    for j in range(1,N):
        x=Fraction(j,N)
        for m in range(2,min(5,N)+1):
            for pos in combinations(range(N),m):
                gaps=[pos[q+1]-pos[q] for q in range(m-1)]
                s_rho=sum((eps**g for g in gaps),Fraction(0))
                for bits in product([0,1], repeat=m):
                    if all(b==bits[0] for b in bits):
                        continue
                    pe=patt_positions(pos,bits,x,eps)
                    p0=iid_patt(bits,x)
                    check(abs(pe-p0) <= x*(1-x)*s_rho,
                          f"pattern bound N={N} j={j} m={m} pos={pos} bits={bits}")

# Mean-persistence formula and its elementary upper bound.
for N in range(2,50):
    eps=eps_c078(N)
    A=Amean(N,eps)
    delta=1-eps
    check(A>=0 and A<=1, f"A range N={N}")
    check(A <= Fraction(2,1)/((N-1)*delta), f"A upper N={N}")

# Exact pair rate formula for shuffled model.
for N in range(2,13):
    eps=eps_c078(N)
    A=Amean(N,eps)
    q=split_rate_shuffled(N,2,1,eps)
    rhs=Fraction(N-1,N)*(1-A)
    check(q==rhs, f"pair rate N={N}: {q} != {rhs}")

# General shuffled split-rate comparison against iid and the U058 bound.
for N in range(3,10):
    eps=eps_c078(N)
    A=Amean(N,eps)
    for m in range(2,min(5,N)+1):
        for i in range(1,m):
            q=split_rate_shuffled(N,m,i,eps)
            q0=split_rate_iid(N,m,i)
            bd=Fraction(comb(m,2)*(N-1),N)*A
            check(abs(q-q0) <= bd, f"rate bound N={N} m={m} i={i}")

# Fixed-order adjacent-pair exact formula from U057.
for N in range(2,30):
    eps=Fraction(1,N+1)  # arbitrary rational test schedule
    q=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        lam=Fraction(N,2*j*(N-j))
        splitp=2*x*(1-x)*(1-eps)
        q += lam*splitp
    check(q==Fraction(N-1,N)*(1-eps), f"fixed-order pair N={N}")

# C078 exact N=4 witness: eps=1/2.
N=4
eps=eps_c078(N)
check(eps==Fraction(1,2),"N4 eps")
q13=split_rate_shuffled(N,4,1,eps)
q22=split_rate_shuffled(N,4,2,eps)
check(q13==Fraction(37,256), f"N4 q13 {q13}")
check(q22==Fraction(25,256), f"N4 q22 {q22}")
root_total=4*q13+3*q22
bal_prob=3*q22/root_total
check(root_total==Fraction(223,256), f"N4 total {root_total}")
check(bal_prob==Fraction(75,223), f"N4 bal {bal_prob}")
check(bal_prob!=Fraction(3,11),"source distinction")
check(q13/q22 != Fraction(2,1),"not global rescale of source")

print("C078_eps_N4=", eps)
print("C078_N4_specified_1|3_rate=", q13)
print("C078_N4_specified_2|2_rate=", q22)
print("C078_N4_total_root_rate=", root_total)
print("C078_N4_balanced_root_probability=", bal_prob)
print("CTCS4_balanced_root_probability=", Fraction(3,11))
print("C078_N4_rate_ratio_q13_over_q22=", q13/q22)
print("CTCS4_rate_ratio_q13_over_q22=", Fraction(2,1))
for N in [4,9,16,25,36,49]:
    eps=eps_c078(N); A=Amean(N,eps)
    print(f"N={N} eps={eps} N(1-eps)={N*(1-eps)} A_N={A} pair_rate={Fraction(N-1,N)*(1-A)}")
print("ASSERTIONS=",ASSERTIONS)
print("ALL_EXACT_CHECKS_PASS")
