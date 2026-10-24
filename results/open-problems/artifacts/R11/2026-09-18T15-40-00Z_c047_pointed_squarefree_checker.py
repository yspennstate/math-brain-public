from fractions import Fraction
from math import gcd, factorial

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    if n == 1:
        return 1
    x=n; p=2; cnt=0
    while p*p<=x:
        if x%p==0:
            x//=p; cnt+=1
            if x%p==0:
                return 0
            while x%p==0:
                x//=p
        p+=1
    if x>1: cnt+=1
    return -1 if cnt%2 else 1

def I2(m):
    return sum(mobius(d)*(2**(m//d)) for d in divisors(m))//m

def S(n):
    if n < 0: return 0
    if n == 0: return 1
    if n == 1: return 2
    return 2**(n-1)

def B_excl(n,m):
    # [z^n] F(z)/(1+z^m), F=(1-2z^2)/(1-2z)
    if n < 0: return 0
    total = 0
    r = 0
    while n-r*m >= 0:
        total += (-1)**r * S(n-r*m)
        r += 1
    return total

def A_nm(N,m):
    if not (1 <= m <= N): return 0
    return I2(m)*B_excl(N-m,m)

def kappa(N):
    return Fraction(sum(A_nm(N,m) for m in range(1,N+1)), S(N))

def falling(x,r):
    if r < 0: raise ValueError
    out=1
    for t in range(r):
        out *= x-t
    return out

def split_prob(N,m,i,j):
    b=i+j
    den=falling(N,b)
    num=falling(m,i)*falling(N-m,j)+falling(m,j)*falling(N-m,i)
    return Fraction(num,den)

def qrate(N,i,j):
    return sum(Fraction(A_nm(N,m),S(N))*split_prob(N,m,i,j)
               for m in range(1,N+1))

def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

# --- GF(2) polynomial arithmetic, independent finite enumeration ---
def deg(p):
    return p.bit_length()-1

def poly_mod(a,b):
    db=deg(b)
    while a and deg(a)>=db:
        a ^= b << (deg(a)-db)
    return a

def poly_gcd(a,b):
    while b:
        a,b = b, poly_mod(a,b)
    return a

def poly_derivative(p):
    # in F2, only odd exponents survive and drop by one
    out=0
    e=1
    while (1<<e) <= p:
        if (p>>e)&1 and e%2==1:
            out ^= 1<<(e-1)
        e+=1
    return out

def is_squarefree(p):
    d=poly_derivative(p)
    if d == 0:
        return deg(p) <= 0
    return poly_gcd(p,d)==1

def monic_polys(n):
    # degree exactly n, monic
    for low in range(1<<n):
        yield (1<<n)|low

def is_irreducible_bruteforce(p):
    n=deg(p)
    if n <= 0:
        return False
    for d in range(1,n//2+1):
        for q in monic_polys(d):
            if poly_mod(p,q)==0:
                return False
    return True

def irreducibles_upto(n):
    out={}
    for d in range(1,n+1):
        out[d]=[p for p in monic_polys(d) if is_irreducible_bruteforce(p)]
    return out

IRR = irreducibles_upto(10)

def distinct_irred_factor_degrees(p):
    fac=[]
    for d in range(1,deg(p)+1):
        for g in IRR.get(d,[]):
            if poly_mod(p,g)==0:
                fac.append(d)
    return fac

# 1) irreducible counts and exact squarefree enumeration.
for m in range(1,11):
    check(len(IRR[m]) == I2(m), f"I2 direct mismatch m={m}")
check([I2(m) for m in range(1,9)] == [2,1,2,3,6,9,18,30], "I2 initial sequence")

direct_S={}
direct_A={}
for N in range(1,10):
    sq=[]
    incidence={m:0 for m in range(1,N+1)}
    for p in monic_polys(N):
        if is_squarefree(p):
            sq.append(p)
            ds=distinct_irred_factor_degrees(p)
            check(sum(ds)==N, f"factor degrees don't sum N={N}, p={p}")
            # squarefree => each distinct irreducible divisor occurs once;
            # degree multiplicities can repeat, so count each factor degree occurrence.
            for d in ds:
                incidence[d]+=1
    direct_S[N]=len(sq)
    direct_A[N]=incidence
    check(len(sq)==S(N), f"squarefree count N={N}")
    for m in range(1,N+1):
        check(incidence[m]==A_nm(N,m), f"incidence count N={N},m={m}")

# 2) exact Euler product coefficient / exclusion recurrence identities.
for N in range(1,161):
    check(sum(A_nm(N,m) for m in range(1,N+1)) >= 0, f"A total sign N={N}")
    for m in range(1,N+1):
        b=B_excl(N-m,m)
        check(b>=0, f"B negative N={N},m={m}")
        check(b + B_excl(N-2*m,m) == S(N-m), f"exclusion recurrence N={N},m={m}")
        check(A_nm(N,m) == I2(m)*b, "A identity")
        # universal simple domination used in the proof:
        check(Fraction(A_nm(N,m),S(N)) <= Fraction(2,m),
              f"W domination N={N},m={m}")

# 3) marked generating-function double count of kappa_N.
# Direct small-N enumeration vs incidence formula.
for N in range(2,10):
    total_direct=sum(direct_A[N].values())
    total_formula=sum(A_nm(N,m) for m in range(1,N+1))
    check(total_direct==total_formula, f"kappa double count N={N}")
    check(kappa(N)==Fraction(total_direct,direct_S[N]), f"kappa direct N={N}")

expected_kappa = {
    2: Fraction(3,2), 3: Fraction(3,2), 4: Fraction(7,4),
    5: Fraction(7,4), 6: Fraction(31,16), 7: Fraction(2,1),
    8: Fraction(67,32), 9: Fraction(139,64)
}
for N,v in expected_kappa.items():
    check(kappa(N)==v, f"kappa witness N={N}")

# 4) exact split probabilities/rates and normalization sanity.
for N in range(4,31):
    for b in range(2,min(6,N)+1):
        # For a fixed m, summing probabilities over all unordered nontrivial
        # bipartitions of a fixed b-set equals probability that selected factor
        # sees some but not all visible labels.
        for m in range(1,N+1):
            total=Fraction(0)
            # enumerate each unordered subset/complement once: subsets containing label 0.
            for mask in range(1,1<<b):
                if not (mask & 1): continue
                if mask == (1<<b)-1: continue
                i=mask.bit_count(); j=b-i
                total += split_prob(N,m,i,j)
            invis=Fraction(falling(m,b)+falling(N-m,b), falling(N,b))
            check(total == 1-invis, f"split normalization N={N},m={m},b={b}")

# 5) exact N=4 frozen-equivalence witness.
check(S(4)==8, "S4")
check({m:A_nm(4,m) for m in range(1,5)} == {1:6,2:1,3:4,4:3}, "N4 incidence profile")
check(kappa(4)==Fraction(7,4), "kappa4")
check(qrate(4,1,1)==Fraction(17,24), "q11 N4")
check(qrate(4,2,2)==Fraction(1,24), "q22 N4")
check(qrate(4,1,3)==Fraction(5,16), "q13 N4")
check(qrate(4,2,2)/qrate(4,1,1)==Fraction(1,17), "N4 rate-ratio witness")

# 6) exact convergence diagnostics at a large finite N.
diagnostics = [
    (1,1,Fraction(1,1), Fraction(1,20)),
    (1,2,Fraction(1,2), Fraction(1,40)),
    (2,2,Fraction(1,6), Fraction(1,250)),
    (1,3,Fraction(1,3), Fraction(1,50)),
    (2,3,Fraction(1,12), Fraction(1,500)),
]
Ndiag=160
for i,j,target,tol in diagnostics:
    q=qrate(Ndiag,i,j)
    check(abs(q-target)<tol, f"diag rate {i},{j}: {q} vs {target}")

# 7) growth control for the raw-step compiler.
for N in range(2,501):
    # kappa_N <= 2 H_N from W<=2/m.
    H=sum(Fraction(1,m) for m in range(1,N+1))
    check(kappa(N) <= 2*H, f"kappa harmonic bound N={N}")

print(f"ASSERTIONS={ASSERTIONS}")
print("I2_1_8=" + ",".join(map(str,[I2(m) for m in range(1,9)])))
print("N4_incidence=" + ",".join(f"{m}:{A_nm(4,m)}" for m in range(1,5)))
print(f"N4_kappa={kappa(4)}")
print(f"N4_q11={qrate(4,1,1)}")
print(f"N4_q22={qrate(4,2,2)}")
print(f"N4_q13={qrate(4,1,3)}")
print(f"N4_q22_over_q11={qrate(4,2,2)/qrate(4,1,1)}")
for i,j,target,tol in diagnostics:
    print(f"N160_q_{i}_{j}={qrate(160,i,j)} target={target}")
print("ALL_EXACT_CHECKS_PASS")
