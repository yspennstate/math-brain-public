from fractions import Fraction
from math import factorial
from itertools import product

A = 0
def check(cond, msg):
    global A
    A += 1
    if not cond:
        raise AssertionError(msg)

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def mobius(n):
    if n == 1:
        return 1
    x = n
    parity = 0
    p = 2
    while p*p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        parity ^= 1
    return -1 if parity else 1

def Iq(q, m):
    num = sum(mobius(d) * q**(m//d) for d in divisors(m))
    check(num % m == 0, f"irreducible count divisibility q={q} m={m}")
    return num // m

# ----- direct GF(2) irreducibility for small m -----
def gf2_deg(p):
    return p.bit_length() - 1

def gf2_mod(f, g):
    dg = gf2_deg(g)
    while f and gf2_deg(f) >= dg:
        f ^= g << (gf2_deg(f) - dg)
    return f

def irreducible_gf2(f):
    m = gf2_deg(f)
    if m <= 0:
        return False
    for d in range(1, m//2 + 1):
        for lower in range(1 << d):
            g = (1 << d) | lower
            if gf2_mod(f, g) == 0:
                return False
    return True

for m in range(1, 9):
    direct = sum(
        irreducible_gf2((1 << m) | lower)
        for lower in range(1 << m)
    )
    check(direct == Iq(2, m), f"direct irreducibles m={m}")

# ----- finite coefficient bound behind analytic correction -----
# m I_2(m)-2^m is the nontrivial-divisor contribution.
# The proof uses |.| <= (# proper divisors)*2^(m/2) <= m*2^(ceil(m/2)).
for m in range(2, 121):
    err = abs(m * Iq(2, m) - 2**m)
    check(err <= m * 2**((m+1)//2), f"analytic-tail bound m={m}")

# ----- polynomial helpers for C_2(z)=sum I_2(m) z^m -----
def poly_mul(a, b, nmax):
    c = [0] * (min(len(a)+len(b)-1, nmax+1))
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if i+j > nmax:
                break
            if y:
                c[i+j] += x*y
    return c

def poly_pow(a, r, nmax):
    out = [1] + [0]*nmax
    for _ in range(r):
        out = poly_mul(out, a, nmax)
        if len(out) < nmax+1:
            out += [0]*(nmax+1-len(out))
    return out[:nmax+1]

def C_coeffs(q, N):
    return [0] + [Iq(q, m) for m in range(1, N+1)]

def deriv_coeffs(C, n, nmax):
    out = [0]*(nmax+1)
    for r in range(nmax+1):
        m = r+n
        if m < len(C):
            ff = 1
            for t in range(n):
                ff *= m-t
            out[r] = C[m]*ff
    return out

R = 6

def total_count(q, N):
    C = C_coeffs(q, N)
    P = poly_pow(C, R, N)
    ans = Fraction(factorial(N) * P[N], factorial(R))
    check(ans.denominator == 1, f"total count integral N={N}")
    return ans.numerator

def specified_partition_count(q, N, sizes):
    b = sum(sizes)
    qb = len(sizes)
    check(qb <= R and b <= N, "partition admissible")
    nmax = N-b
    C = C_coeffs(q, N)
    P = [1] + [0]*nmax
    for n in sizes:
        P = poly_mul(P, deriv_coeffs(C, n, nmax), nmax)
        if len(P) < nmax+1:
            P += [0]*(nmax+1-len(P))
    rem = R-qb
    if rem:
        P = poly_mul(P, poly_pow(C, rem, nmax), nmax)
        if len(P) < nmax+1:
            P += [0]*(nmax+1-len(P))
        coeff = Fraction(P[nmax], factorial(rem))
    else:
        coeff = Fraction(P[nmax], 1)
    ans = coeff * factorial(N-b)
    check(ans.denominator == 1, f"specified count integral N={N} sizes={sizes}")
    return ans.numerator

# Restricted growth strings enumerate all set partitions of [b].
def set_partitions(b):
    if b == 0:
        yield ()
        return
    a = [0]*b
    def rec(i, mx):
        if i == b:
            blocks = [[] for _ in range(mx+1)]
            for idx, v in enumerate(a):
                blocks[v].append(idx)
            yield tuple(tuple(x) for x in blocks)
            return
        for v in range(mx+2):
            a[i] = v
            yield from rec(i+1, max(mx, v))
    a[0] = 0
    yield from rec(1, 0)

# ----- exact SET_6(C_2) counts and restriction normalization -----
totals = {}
for N in range(6, 31):
    totals[N] = total_count(2, N)
    check(totals[N] > 0, f"positive assembly count N={N}")

check(totals[6] == 64, "N=6 exact total 2^6")
check(totals[7] == 1344, "N=7 exact total")

for N in range(6, 21):
    total = totals[N]
    for b in range(2, min(5, N)+1):
        mass = Fraction(0,1)
        for pi in set_partitions(b):
            sizes = tuple(len(B) for B in pi)
            if len(sizes) <= R:
                mass += Fraction(specified_partition_count(2, N, sizes), total)
        check(mass == 1, f"visible partition normalization N={N} b={b}")

# exact pair separation probabilities; positive and <=1
p11 = {}
for N in range(6, 31):
    total = totals[N]
    sep = Fraction(specified_partition_count(2, N, (1,1)), total)
    p11[N] = sep
    check(0 < sep <= 1, f"pair separation legality N={N}")

check(p11[6] == 1, "N=6 pair separation")
check(p11[7] == Fraction(20,21), "N=7 pair separation")
check(p11[8] == Fraction(165,182), "N=8 pair separation")

# root-support witness: SET_6 has exactly six nonempty components.
# At N=6 all six sizes are 1; at N=7 the multiset is (2,1,1,1,1,1).
all_singletons = Fraction(specified_partition_count(2,6,(1,1,1,1,1,1)), totals[6])
check(all_singletons == 1, "N=6 deterministic six-singleton root")

# For N=7, sum over the 21 specified partitions with one pair and five singletons.
pair5_prob = Fraction(specified_partition_count(2,7,(2,1,1,1,1,1)), totals[7])
check(pair5_prob == Fraction(1,21), "N=7 specified 2+1+... partition")
check(21*pair5_prob == 1, "N=7 deterministic size multiset 2+1^5")

# Attempt-grid legality for delta=min(N^-2,p11/2): a=delta/p11 <=1/2 exactly.
for N in range(6,31):
    sep = p11[N]
    delta = min(Fraction(1,N*N), sep/Fraction(2,1))
    a = delta/sep
    check(0 < a <= Fraction(1,2), f"attempt probability N={N}")

print("R11 I0054 C046 binary Frobenius-orbit assembly exact self-check")
print(f"ASSERTIONS={A}")
print("I2(1..14)=" + repr([Iq(2,m) for m in range(1,15)]))
print(f"TOTAL_N6={totals[6]}")
print(f"TOTAL_N7={totals[7]}")
print(f"P11_N7={p11[7]}")
print(f"P11_N8={p11[8]}")
print("ROOT_N6_DEGREE=6; SIZE_MULTISET=(1,1,1,1,1,1)")
print("ROOT_N7_DEGREE=6; SIZE_MULTISET=(2,1,1,1,1,1)")
print("ALL_EXACT_CHECKS_PASS")
