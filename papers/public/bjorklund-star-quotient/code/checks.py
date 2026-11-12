"""Exact checks for the star quotient of Sym_fin(N_0) (Bjorklund 2014, Appendix II, Problem 2).

Python 3, standard library only. Permutations of {0,...,N} are tuples g with g[x] the image of x.
Every check is exact (integers and fractions); the script prints ALL PASS at the end.
"""
from fractions import Fraction
from itertools import permutations
import random

ok = 0


def check(cond, msg):
    global ok
    if not cond:
        raise SystemExit("FAIL: " + msg)
    ok += 1


def tau(n, N):
    """The transposition (0 n) on {0,...,N}."""
    g = list(range(N + 1))
    g[0], g[n] = n, 0
    return tuple(g)


def mul(a, b):
    """Composition a*b: first b, then a."""
    return tuple(a[b[x]] for x in range(len(b)))


def transposition(i, j, N):
    g = list(range(N + 1))
    g[i], g[j] = j, i
    return tuple(g)


# 1. tau_i tau_j tau_i = (i j) for distinct i, j >= 1.
for N in range(2, 9):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                check(mul(tau(i, N), mul(tau(j, N), tau(i, N))) == transposition(i, j, N), f"conjugation {i},{j},{N}")
print("1. tau_i tau_j tau_i = (i j) for 1 <= i != j <= N <= 8")

# 2. The star transpositions generate Sym({0..N}) as a semigroup: products of them reach all (N+1)! permutations.
for N in range(1, 7):
    gens = [tau(n, N) for n in range(1, N + 1)]
    e = tuple(range(N + 1))
    seen = {e}
    frontier = [e]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = mul(s, g)
                if h not in seen:
                    seen.add(h)
                    new.append(h)
        frontier = new
    fact = 1
    for k in range(2, N + 2):
        fact *= k
    check(len(seen) == fact, f"generation N={N}")
print("2. positive words in tau_1..tau_N give all (N+1)! permutations of {0..N}, N <= 6")

# 3. gH -> g(0) is a bijection G/H -> X and is equivariant: (s g)(0) = s(g(0)); g, g' in one coset iff g(0) = g'(0).
for N in range(1, 6):
    perms = list(permutations(range(N + 1)))
    for g in perms:
        for n in range(1, N + 1):
            s = tau(n, N)
            check(mul(s, g)[0] == s[g[0]], "equivariance")
    H = [h for h in perms if h[0] == 0]
    for g in perms[:40]:
        coset = {mul(g, h) for h in H}
        check(coset == {p for p in perms if p[0] == g[0]}, "coset = fibre of g -> g(0)")
print("3. gH -> g(0) is well defined, injective on cosets and equivariant (N <= 5)")

# 4. The rows of the quotient operator: (Pu)(0) = sum_n p_n u(n); (Pu)(k) = p_k u(0) + (1 - p_k) u(k).
random.seed(1)
N = 12
p = [None] + [Fraction(1, 2 ** n) for n in range(1, N)] + [Fraction(1, 2 ** (N - 1))]
check(sum(p[1:]) == 1, "p sums to 1 on the truncation")
u = [Fraction(random.randint(-50, 50), random.randint(1, 9)) for _ in range(N + 1)]
for x in range(N + 1):
    Pu = sum(p[n] * u[tau(n, N)[x]] for n in range(1, N + 1))
    if x == 0:
        check(Pu == sum(p[n] * u[n] for n in range(1, N + 1)), "center row")
    else:
        check(Pu == p[x] * u[0] + (1 - p[x]) * u[x], f"leaf row {x}")
print("4. kernel rows on the truncation {0..12} with p_n = 2^-n (last mass doubled), random rational u")

# 5. Leaf equations: Pu(k) = u(k) + c  <=>  u(k) = u(0) - c / p_k; then p_k u(k) = p_k u(0) - c -> -c.
c = Fraction(3, 7)
u0 = Fraction(-5, 2)
for k in range(1, 61):
    pk = Fraction(1, 2 ** k)
    uk = u0 - c / pk
    check(pk * u0 + (1 - pk) * uk == uk + c, f"leaf equation k={k}")
    check(pk * uk == pk * u0 - c, f"center summand k={k}")
term60 = Fraction(1, 2 ** 60) * (u0 - c * 2 ** 60)
check(abs(term60 + c) < Fraction(1, 10 ** 17), "summand within 1e-17 of -c at k = 60")
print(f"5. with c = 3/7, u(0) = -5/2: leaf equations hold for u(k) = u(0) - c 2^k, and p_60 u(60) + c = {float(term60 + c):.3e}")

# 6. Constants satisfy Pu = u (c = 0) on the truncation.
for x in range(N + 1):
    check(sum(p[n] * Fraction(7) for n in range(1, N + 1)) == 7, "constants")
print("6. constant functions are harmonic")

print(f"ALL PASS ({ok} checks)")
