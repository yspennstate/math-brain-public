from fractions import Fraction
from itertools import combinations

ASSERTIONS = 0

def check(cond, payload=None):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(payload)

def H(n):
    return sum((Fraction(1,r) for r in range(1,n+1)), Fraction(0))

def pi(N,j):
    x = Fraction(j,N)
    return (1-x, x)

def K(N,j,eps):
    p = pi(N,j)
    return [[(1-eps)*p[b] + eps*Fraction(int(a==b),1) for b in (0,1)] for a in (0,1)]

def matmul(A,B):
    return [[sum((A[i][r]*B[r][j] for r in range(2)), Fraction(0))
             for j in range(2)] for i in range(2)]

def matpow(A,d):
    R=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    for _ in range(d):
        R=matmul(R,A)
    return R

def K_closed(N,j,eps,d):
    p=pi(N,j)
    return [[eps**d*Fraction(int(a==b),1)+(1-eps**d)*p[b] for b in (0,1)] for a in (0,1)]

def selected_pattern_prob(N,j,eps,V,ones):
    V=tuple(sorted(V)); ones=frozenset(ones)
    p=pi(N,j)
    bits=[1 if v in ones else 0 for v in V]
    ans=p[bits[0]]
    for q in range(len(V)-1):
        d=V[q+1]-V[q]
        Kd=K_closed(N,j,eps,d)
        ans *= Kd[bits[q]][bits[q+1]]
    return ans

def iid_selected_pattern_prob(N,j,V,ones):
    V=tuple(sorted(V)); ones=frozenset(ones)
    p=pi(N,j)
    ans=Fraction(1)
    for v in V:
        ans *= p[1 if v in ones else 0]
    return ans

def lam(N,j):
    return Fraction(N, 2*j*(N-j))

def split_rate(N,V,A,eps):
    V=tuple(sorted(V)); A=frozenset(A)
    Ac=frozenset(set(V)-set(A))
    ans=Fraction(0)
    for j in range(1,N):
        ans += lam(N,j)*(selected_pattern_prob(N,j,eps,V,A)
                         + selected_pattern_prob(N,j,eps,V,Ac))
    return ans

def iid_split_rate(N,V,A):
    V=tuple(sorted(V)); A=frozenset(A)
    Ac=frozenset(set(V)-set(A))
    ans=Fraction(0)
    for j in range(1,N):
        ans += lam(N,j)*(iid_selected_pattern_prob(N,j,V,A)
                         + iid_selected_pattern_prob(N,j,V,Ac))
    return ans

def canon_splits(V):
    V=tuple(sorted(V))
    v0=V[0]
    rest=V[1:]
    for r in range(0,len(rest)):
        for T in combinations(rest,r):
            A=frozenset((v0,)+T)
            if len(A)==len(V):
                continue
            yield A

print("R11-I0054 U056/C077 sticky-Markov harmonic-grid exact self-check")

# Kernel/stationarity/d-step formula and raw proposal normalization.
for N in range(2,10):
    eps=Fraction(1,N)
    check(sum((lam(N,j) for j in range(1,N)),Fraction(0))==H(N-1), ("proposal",N))
    for j in range(1,N):
        p=pi(N,j); M=K(N,j,eps)
        for a in (0,1):
            check(sum(M[a])==1, ("rowsum",N,j,a))
            for b in (0,1):
                check(M[a][b]>=0, ("nonnegative",N,j,a,b))
        for b in (0,1):
            stat=sum((p[a]*M[a][b] for a in (0,1)),Fraction(0))
            check(stat==p[b], ("stationary",N,j,b,stat,p[b]))
        for d in range(1,N+2):
            check(matpow(M,d)==K_closed(N,j,eps,d), ("power",N,j,d,matpow(M,d),K_closed(N,j,eps,d)))

# Exhaustive visible split rate comparison against iid harmonic-grid model.
for N in range(2,9):
    eps=Fraction(1,N)
    labels=tuple(range(1,N+1))
    for m in range(2,min(5,N)+1):
        bound=Fraction(m-1,N)*H(N-1)
        for V in combinations(labels,m):
            for A in canon_splits(V):
                q=split_rate(N,V,A,eps)
                qi=iid_split_rate(N,V,A)
                check(q>=0, ("split_nonnegative",N,V,A,q))
                check(abs(q-qi)<=bound, ("generator_bound",N,V,A,q,qi,bound))

# Exact pair formula: distance d leaves persistence eps^d.
for N in range(2,10):
    eps=Fraction(1,N)
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            d=b-a
            q=split_rate(N,(a,b),frozenset((a,)),eps)
            rhs=Fraction(0)
            for j in range(1,N):
                x=Fraction(j,N)
                rhs += lam(N,j)*2*x*(1-x)*(1-eps**d)
            check(q==rhs, ("pair_formula",N,a,b,q,rhs))

# N=4 exact frozen-equivalence witness.
N=4
eps=Fraction(1,4)
V=(1,2,3,4)
single=[split_rate(N,V,frozenset((i,)),eps) for i in V]
balanced=[
    split_rate(N,V,frozenset((1,2)),eps),
    split_rate(N,V,frozenset((1,3)),eps),
    split_rate(N,V,frozenset((1,4)),eps),
]
check(single==[Fraction(477,2048),Fraction(297,2048),Fraction(297,2048),Fraction(477,2048)], ("single",single))
check(balanced==[Fraction(423,2048),Fraction(135,2048),Fraction(243,2048)], ("balanced",balanced))
total=sum(single, Fraction(0))+sum(balanced, Fraction(0))
check(total==Fraction(2349,2048), ("total",total))
pbal=sum(balanced,Fraction(0))/total
check(pbal==Fraction(89,261), ("pbal",pbal))
check(pbal!=Fraction(3,11), ("source_pbal",pbal))
check(len(set(single))>1, ("singleton_anisotropy",single))
check(len(set(balanced))>1, ("balanced_anisotropy",balanced))

# Pair separation is always positive, so every nonsingleton block has positive exit hazard.
for N in range(2,10):
    eps=Fraction(1,N)
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            q=split_rate(N,(a,b),frozenset((a,)),eps)
            check(q>0, ("pair_positive",N,a,b,q))

print("N4_singleton_rates=", [str(x) for x in single])
print("N4_balanced_rates=", [str(x) for x in balanced])
print("N4_total_root_rate=", total)
print("N4_balanced_root_probability=", pbal)
print("CTCS4_balanced_root_probability=", Fraction(3,11))
print("ASSERTIONS=", ASSERTIONS)
print("ALL_EXACT_CHECKS_PASS")