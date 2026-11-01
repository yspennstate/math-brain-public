from fractions import Fraction
from math import comb, factorial
from itertools import combinations, permutations


def falling(a,k):
    out=1
    for i in range(k): out*=a-i
    return out

def rising(a,k):
    out=1
    for i in range(k): out*=a+i
    return out

def W(N,M,n,k):
    def Q(s): return Fraction(falling(M,s), falling(N,s))
    return Q(2*n-k)/(Q(n)*Q(n))

# Newton coefficient identity: Delta^j W(0)=W(0)*(N-M)_j/(M-2n+1)^(overline j)
for n in range(3,7):
    N=comb(n+3,2) # auxiliary host edge count large enough
    M=3*n+5
    assert M>=2*n and N>M
    for j in range(0,n+1):
        delta=sum(Fraction((-1)**(j-i)*comb(j,i),1)*W(N,M,n,i) for i in range(j+1))
        rhs=W(N,M,n,0)*Fraction(falling(N-M,j), rising(M-2*n+1,j))
        assert delta==rhs, (n,j,delta,rhs)

# Count j-edge subsets of C_n by number r of runs.
def run_count(bits):
    n=len(bits)
    if all(bits): return 0  # whole cycle treated separately
    return sum(1 for i in range(n) if bits[i] and not bits[i-1])
for n in range(4,11):
    for j in range(1,n):
        obs={}
        for S in combinations(range(n),j):
            bits=[0]*n
            for i in S: bits[i]=1
            r=run_count(bits)
            obs[r]=obs.get(r,0)+1
        for r,cnt in obs.items():
            formula=Fraction(n,r)*comb(j-1,r-1)*comb(n-j-1,r-1)
            assert formula.denominator==1 and formula.numerator==cnt, (n,j,r,cnt,formula)

# For C_n, a proper linear forest S with j edges and r runs is contained in
# exactly 2^r (n-j-1)!/2 undirected Hamilton cycles.
# Verify by direct enumeration for n<=8 on one representative of every (j,r) realized.
def canonical_cycle(edges,n):
    return frozenset(frozenset(e) for e in edges)
def all_ham_cycles(n):
    out=set()
    for perm in permutations(range(1,n)):
        cyc=(0,)+perm
        edges=[(cyc[i],cyc[(i+1)%n]) for i in range(n)]
        out.add(canonical_cycle(edges,n))
    return out
for n in range(4,9):
    cycles=all_ham_cycles(n)
    assert len(cycles)==factorial(n-1)//2
    base=[frozenset((i,(i+1)%n)) for i in range(n)]
    seen=set()
    for j in range(1,n):
        for Sidx in combinations(range(n),j):
            bits=[0]*n
            for i in Sidx: bits[i]=1
            r=run_count(bits)
            if (j,r) in seen: continue
            seen.add((j,r))
            S={base[i] for i in Sidx}
            actual=sum(1 for C in cycles if S.issubset(C))
            expected=(2**r)*factorial(n-j-1)//2
            assert actual==expected, (n,j,r,actual,expected)

print('R16 H0022 exact Newton/Hamilton overlap self-check')
print('Newton finite-difference identity: PASS')
print('Circular subset run-count formula: PASS')
print('Hamilton-cycle containment count for n<=8: PASS')
print('ALL_EXACT_CHECKS_PASS')
