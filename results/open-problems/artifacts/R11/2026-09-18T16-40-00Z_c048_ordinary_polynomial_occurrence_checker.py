from fractions import Fraction
from itertools import combinations

ASSERTIONS = 0

def ck(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)


def deg(p):
    return p.bit_length() - 1


def pmod(a, b):
    db = deg(b)
    while a and deg(a) >= db:
        a ^= b << (deg(a) - db)
    return a


def pdiv_exact(a, b):
    q = 0
    r = a
    db = deg(b)
    while r and deg(r) >= db:
        sh = deg(r) - db
        q ^= 1 << sh
        r ^= b << sh
    assert r == 0
    return q


def mu(n):
    x = n
    p = 2
    c = 0
    while p*p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if e >= 2:
                return 0
            c += 1
        p += 1
    if x > 1:
        c += 1
    return -1 if c % 2 else 1


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def I2(m):
    return sum(mu(d) * 2**(m//d) for d in divisors(m)) // m


def is_irreducible(p):
    d = deg(p)
    if d <= 0:
        return False
    for e in range(1, d//2 + 1):
        for low in range(1 << e):
            g = (1 << e) | low
            if pmod(p, g) == 0:
                return False
    return True


IRR = {}
for m in range(1, 13):
    IRR[m] = [(1 << m) | low for low in range(1 << m)
              if is_irreducible((1 << m) | low)]
    ck(len(IRR[m]) == I2(m), f"irreducible count m={m}")


def factor_mults(p):
    rem = p
    out = []
    D = deg(p)
    for m in range(1, D+1):
        for g in IRR.get(m, []):
            v = 0
            while rem != 1 and pmod(rem, g) == 0:
                rem = pdiv_exact(rem, g)
                v += 1
            if v:
                out.append((g, m, v))
            if rem == 1:
                return out
    assert rem == 1
    return out


def falling(n, r):
    if r > n:
        return 0
    z = 1
    for a in range(r):
        z *= n-a
    return z


def A_formula(N, m):
    return I2(m) * sum(2**(N-r*m) for r in range(1, N//m + 1))


def W(N, m):
    return Fraction(A_formula(N, m), 2**N)


def kappa(N):
    return sum((W(N,m) for m in range(1,N+1)), Fraction())


def s_hyp(N, m, i, j):
    return Fraction(
        falling(m,i)*falling(N-m,j) + falling(m,j)*falling(N-m,i),
        falling(N,i+j),
    )


def qrate(N, i, j):
    return sum((W(N,m)*s_hyp(N,m,i,j) for m in range(1,N+1)), Fraction())


# 1. Brute-factor every monic F_2 polynomial through degree 9 and verify
#    the exact indexed-occurrence count A_{N,m}.
for N in range(1, 10):
    counts = [0]*(N+1)
    occ = 0
    for low in range(1 << N):
        f = (1 << N) | low
        fac = factor_mults(f)
        ck(sum(m*v for _,m,v in fac) == N, f"factor-degree N={N}, f={f}")
        for _,m,v in fac:
            counts[m] += v
            occ += v
    for m in range(1,N+1):
        ck(counts[m] == A_formula(N,m), f"occurrence formula N={N},m={m}")
    ck(Fraction(occ,2**N) == kappa(N), f"kappa double count N={N}")

# 2. Independently enumerate subsets and verify the hypergeometric visible law.
for N in range(2, 10):
    universe = tuple(range(N))
    for m in range(1,N):
        subsets = list(combinations(universe,m))
        den = len(subsets)
        for i in range(1, min(4,N)):
            for j in range(1, min(4,N-i)+1):
                if i+j > N:
                    continue
                L = set(range(i))
                R = set(range(i,i+j))
                good = 0
                for A_tuple in subsets:
                    A = set(A_tuple)
                    if (L <= A and R.isdisjoint(A)) or (R <= A and L.isdisjoint(A)):
                        good += 1
                ck(Fraction(good,den) == s_hyp(N,m,i,j),
                   f"subset hypergeom N={N},m={m},i={i},j={j}")

# 3. Exact domination used by the convergence proof.
for N in range(2, 101):
    for m in range(1,N+1):
        ck(W(N,m) <= Fraction(2,m), f"W<=2/m N={N},m={m}")
    H = sum((Fraction(1,m) for m in range(1,N+1)), Fraction())
    ck(kappa(N) <= 2*H, f"kappa<=2H N={N}")

# 4. Exact N=4 ordinary-polynomial witness.
ck(kappa(4) == Fraction(21,8), "N4 ordinary kappa")
ck(qrate(4,1,1) == Fraction(61,48), "N4 ordinary q11")
ck(qrate(4,2,2) == Fraction(5,48), "N4 ordinary q22")
ck(qrate(4,1,3) == Fraction(17,32), "N4 ordinary q13")
ck(qrate(4,2,2)/qrate(4,1,1) == Fraction(5,61), "N4 ratio22")
ck(qrate(4,1,3)/qrate(4,1,1) == Fraction(51,122), "N4 ratio13")

# 5. Independently recover the previous squarefree N=4 comparator by brute force.
def squarefree_q(N,i,j):
    S = 0
    total = Fraction()
    occ = 0
    for low in range(1 << N):
        f = (1 << N) | low
        fac = factor_mults(f)
        if all(v == 1 for _,_,v in fac):
            S += 1
            for _,m,_ in fac:
                occ += 1
                total += s_hyp(N,m,i,j)
    return S, Fraction(occ,S), total/S

S4, k4sf, q11sf = squarefree_q(4,1,1)
_, _, q22sf = squarefree_q(4,2,2)
_, _, q13sf = squarefree_q(4,1,3)
ck(S4 == 8, "squarefree count N4")
ck(k4sf == Fraction(7,4), "squarefree kappa N4")
ck(q11sf == Fraction(17,24), "squarefree q11 N4")
ck(q22sf == Fraction(1,24), "squarefree q22 N4")
ck(q13sf == Fraction(5,16), "squarefree q13 N4")
ck(q22sf/q11sf == Fraction(1,17), "squarefree ratio N4")
ck((q22sf/q11sf, q13sf/q11sf) !=
   (qrate(4,2,2)/qrate(4,1,1), qrate(4,1,3)/qrate(4,1,1)),
   "ordinary differs from squarefree")

# 6. Exact dyadic finite-N diagnostics toward the beta rates.
targets = {
    (1,1): Fraction(1,1),
    (1,2): Fraction(1,2),
    (2,2): Fraction(1,6),
    (1,3): Fraction(1,3),
}
rows = []
for N in (8,16,32,64,128):
    vals = {}
    for ij,target in targets.items():
        v = qrate(N,*ij)
        vals[ij] = v
        ck(abs(v-target) < Fraction(2,1), f"finite diagnostic bounded N={N},ij={ij}")
    rows.append((N, kappa(N), vals))
for ij,target in targets.items():
    errors = [abs(vals[ij]-target) for _,_,vals in rows]
    for a,b in zip(errors, errors[1:]):
        ck(b < a, f"dyadic error decrease ij={ij}: {a}->{b}")

print("U027/C048 exact arithmetic self-check")
print("N  kappa  q11  q12  q22  q13")
for N,kap,vals in rows:
    print(N, kap, vals[(1,1)], vals[(1,2)], vals[(2,2)], vals[(1,3)])
print("N4_ordinary",
      "kappa="+str(kappa(4)),
      "q11="+str(qrate(4,1,1)),
      "q22="+str(qrate(4,2,2)),
      "q13="+str(qrate(4,1,3)),
      "ratios="+str(qrate(4,2,2)/qrate(4,1,1))+","+str(qrate(4,1,3)/qrate(4,1,1)))
print("N4_squarefree",
      "S="+str(S4),
      "q11="+str(q11sf),
      "q22="+str(q22sf),
      "q13="+str(q13sf),
      "ratio22="+str(q22sf/q11sf))
print("ASSERTIONS", ASSERTIONS)
print("ALL_EXACT_CHECKS_PASS")
