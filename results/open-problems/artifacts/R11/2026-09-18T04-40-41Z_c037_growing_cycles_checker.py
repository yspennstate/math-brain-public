from fractions import Fraction
from itertools import permutations
from collections import Counter, defaultdict
from math import factorial, comb

CHECKS = 0
def check(cond, msg=""):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def e_sym(start, N, r):
    if r < 0:
        return Fraction(0)
    if r == 0:
        return Fraction(1)
    if r > N-start:
        return Fraction(0)
    e = [Fraction(0)]*(r+1)
    e[0] = Fraction(1)
    for j in range(start, N):
        x = Fraction(1, j)
        hi = min(r, j-start+1)
        for k in range(hi, 0, -1):
            e[k] += x*e[k-1]
    return e[r]

def H(start, end):
    if end < start:
        return Fraction(0)
    return sum((Fraction(1,j) for j in range(start,end+1)), Fraction(0))

def q2(start, end):
    if end < start:
        return Fraction(0)
    return sum((Fraction(1,j*j) for j in range(start,end+1)), Fraction(0))

def cycles(perm):
    n = len(perm)
    seen = [False]*n
    out = []
    for i in range(n):
        if not seen[i]:
            cyc = []
            x = i
            while not seen[x]:
                seen[x] = True
                cyc.append(x+1)
                x = perm[x]
            out.append(tuple(sorted(cyc)))
    return out

def restriction_partition(perm, b):
    blocks=[]
    for cyc in cycles(perm):
        vis=tuple(x for x in cyc if x<=b)
        if vis:
            blocks.append(vis)
    return tuple(sorted(blocks))

def formula_prob(N, R, blocks):
    b = sum(len(B) for B in blocks)
    q = len(blocks)
    prod = 1
    for B in blocks:
        prod *= factorial(len(B)-1)
    den = e_sym(1,N,R-1)
    if den == 0:
        return Fraction(0)
    return Fraction(prod, factorial(b-1)) * e_sym(b,N,R-q) / den

# 1. Exhaustive finite verification of the exact conditional restriction formula.
for N in range(3,8):
    byR = defaultdict(list)
    for p in permutations(range(N)):
        byR[len(cycles(p))].append(p)
    for R, ps in byR.items():
        for b in range(2, min(4,N)+1):
            cnt = Counter(restriction_partition(p,b) for p in ps)
            for blocks, c in cnt.items():
                got = Fraction(c, len(ps))
                expected = formula_prob(N,R,blocks)
                check(got == expected, ("restriction_formula",N,R,b,blocks,got,expected))

# 2. Unsigned Stirling / elementary-symmetric coefficient identity:
# c(N,R)=(N-1)! e_{R-1}(1,1/2,...,1/(N-1)).
def stirling1_unsigned(N,R):
    row=[0]*(R+1)
    row[0]=1
    for n in range(1,N+1):
        new=[0]*(R+1)
        for k in range(1,min(n,R)+1):
            new[k]=row[k-1]+(n-1)*row[k]
        row=new
    return row[R]
for N in range(2,25):
    for R in range(1,N+1):
        lhs=stirling1_unsigned(N,R)
        rhs=factorial(N-1)*e_sym(1,N,R-1)
        check(rhs.denominator == 1 and rhs.numerator == lhs, ("stirling_e",N,R))

# 3. Collision sandwich:
# S^r - C(r,2) Q S^(r-2) <= r! e_r <= S^r.
for N in (10,20,40,80):
    for start in (1,2,3,4):
        for r in range(0,min(8,N-start)+1):
            S=H(start,N-1)
            Q=q2(start,N-1)
            er=e_sym(start,N,r)
            mid=factorial(r)*er
            upper=S**r
            if r<2:
                lower=upper
            else:
                lower=upper-comb(r,2)*Q*(S**(r-2))
            check(lower <= mid <= upper, ("collision",N,start,r,lower,mid,upper))

# 4. Exact normalized generator identities.
# For m=R-2, binary rate divided by B(i,j) is e_m^{(b)}/e_m^{(2)}.
# A q-way rate normalized by the pair split is prefactor*e_{m-q+2}^{(b)}/e_m^{(2)}.
for N in range(6,40):
    for R in range(2,min(N,8)+1):
        m=R-2
        den=e_sym(2,N,m)
        if den == 0:
            continue
        for b in range(2,min(6,N)+1):
            ratio=e_sym(b,N,m)/den
            check(Fraction(0) <= ratio <= 1, ("binary_ratio",N,R,b))
            if R>=3 and b>=3:
                q3=e_sym(b,N,m-1)/den
                check(q3 >= 0, ("q3_ratio",N,R,b))

# 5. Sharp obstruction from the 3-label binary split.
# e_m^{(2)} = e_m^{(3)} + (1/2)e_{m-1}^{(3)}
# and e_{m-1}^{(3)}/e_m^{(3)} >= m/S_3.
for N in range(6,80):
    for R in range(3,min(N,10)+1):
        m=R-2
        e2=e_sym(2,N,m)
        e3=e_sym(3,N,m)
        em1=e_sym(3,N,m-1)
        check(e2 == e3 + Fraction(1,2)*em1, ("remove_half",N,R))
        S3=H(3,N-1)
        check(em1*S3 >= m*e3, ("ratio_lower",N,R))
        sharp_upper = Fraction(1,1) / (Fraction(1,1) + Fraction(m,2)/S3)
        check(e3/e2 <= sharp_upper, ("necessity",N,R,e3/e2,sharp_upper))

# 6. Exact pair-separation formula and crude legality lower bound.
# p11=e_{R-2}^{(2)}/e_{R-1}^{(1)}.
# Conditional on any R nonempty cycle sizes, exchangeability gives
# pair separation >= (R-1)(2N-R)/(N(N-1)).
for N in range(4,60):
    for R in range(2,min(N,10)+1):
        p11=e_sym(2,N,R-2)/e_sym(1,N,R-1)
        lower=Fraction((R-1)*(2*N-R), N*(N-1))
        check(p11 >= lower, ("pair_lower",N,R,p11,lower))

# 7. Concrete C037 schedule: R_N=2+floor(log2(floor(log2 N))) for N>=4.
# Integer-only definition: L=floor(log2 N)=bit_length-1, floor(log2 L)=bit_length-1.
def R037(N):
    assert N>=4
    L=N.bit_length()-1
    return 2+(L.bit_length()-1)

expected = {4:3, 8:3, 16:4, 32:4, 64:4, 128:4, 256:5, 512:5, 1024:5, 4096:5, 65536:6}
for N,val in expected.items():
    check(R037(N)==val, ("R037",N,R037(N),val))
    check(2 <= R037(N) <= N, ("R037_range",N))
check(R037(256)==5, "finite root-degree witness")

# Exact finite trend checks (not proofs of the asymptotic theorem):
# along selected powers, q=2 correction improves within each R plateau,
# and q=3 normalized elementary-sym factor decreases within each plateau.
for Ns in ((16,32,64,128),(256,512,1024,2048,4096)):
    vals2=[]
    vals3=[]
    for N in Ns:
        R=R037(N); m=R-2
        vals2.append(e_sym(3,N,m)/e_sym(2,N,m))
        vals3.append(e_sym(3,N,m-1)/e_sym(2,N,m))
    for a,b in zip(vals2,vals2[1:]):
        check(a < b, ("binary_plateau_monotone",Ns,a,b))
    for a,b in zip(vals3,vals3[1:]):
        check(a > b, ("ternary_plateau_monotone",Ns,a,b))

print("R11-I0054-U016-C037 exact self-check")
print(f"checks={CHECKS}")
print("schedule=R_N=2+floor(log2(floor(log2 N))) for N>=4")
print("N256_root_degree=5")
import hashlib
for N in (16,32,64,128,256,512,1024,2048,4096):
    R=R037(N); m=R-2
    br=e_sym(3,N,m)/e_sym(2,N,m)
    tr=e_sym(3,N,m-1)/e_sym(2,N,m)
    bsha=hashlib.sha256(str(br).encode()).hexdigest()[:16]
    tsha=hashlib.sha256(str(tr).encode()).hexdigest()[:16]
    print(f"N={N} R={R} binary_factor_float={float(br):.12f} binary_sha16={bsha} ternary_factor_float={float(tr):.12f} ternary_sha16={tsha}")
print("ALL_EXACT_CHECKS_PASS")