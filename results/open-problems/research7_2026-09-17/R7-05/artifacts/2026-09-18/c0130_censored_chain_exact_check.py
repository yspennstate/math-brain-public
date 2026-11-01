from fractions import Fraction
from math import comb
import sympy as sp


def trans_row(i, ps, N):
    """Exact law of F_{i+1}: entries 0..N-1 and tail >=N."""
    M = len(ps)
    m = i + 1
    probs = [Fraction(0) for _ in range(N)]
    tail = Fraction(0)

    if m >= M:
        # Poisson-binomial law for K successes among the M cookies.
        ak = [Fraction(0) for _ in range(M + 1)]
        ak[0] = Fraction(1)
        for p in ps:
            new = [Fraction(0) for _ in range(M + 1)]
            for k in range(M):
                new[k] += ak[k] * (1 - p)
                new[k + 1] += ak[k] * p
            ak = new

        for k, a in enumerate(ak):
            r = m - k
            c = M - k
            if r == 0:
                if c < N:
                    probs[c] += a
                else:
                    tail += a
            else:
                partial = Fraction(0)
                for jf in range(max(0, N - c)):
                    # failures before r fair successes
                    pr = Fraction(comb(r + jf - 1, jf), 2 ** (r + jf))
                    probs[c + jf] += a * pr
                    partial += pr
                tail += a * (1 - partial)
    else:
        # Exact finite-state recursion until m successes; after the first M
        # trials the success probability is 1/2.
        states = {(0, 0): Fraction(1)}
        t = 0
        while states:
            new = {}
            p = ps[t] if t < M else Fraction(1, 2)
            for (s, f), pr in states.items():
                if s + 1 == m:
                    if f < N:
                        probs[f] += pr * p
                    else:
                        tail += pr * p
                else:
                    new[(s + 1, f)] = new.get((s + 1, f), Fraction(0)) + pr * p

                if f + 1 >= N:
                    tail += pr * (1 - p)
                else:
                    new[(s, f + 1)] = new.get((s, f + 1), Fraction(0)) + pr * (1 - p)
            states = new
            t += 1

    assert sum(probs, Fraction(0)) + tail == 1
    return probs, tail


def h0_brackets(ps, N):
    # M=3, boundary S={0,1}; interior tail states 2,...,N-1.
    inds = list(range(2, N))
    n = len(inds)
    A = [[Fraction(int(a == b)) for b in range(n)] for a in range(n)]
    b0 = [Fraction(0) for _ in range(n)]
    hi = [Fraction(0) for _ in range(n)]

    for ai, i in enumerate(inds):
        probs, tail = trans_row(i, ps, N)
        b0[ai] = probs[0]
        hi[ai] = tail
        for bj, j in enumerate(inds):
            A[ai][bj] -= probs[j]

    A = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    b0 = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in b0])
    hi = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in hi])
    lower = A.LUsolve(b0)
    upper = A.LUsolve(b0 + hi)
    return inds, lower, upper


def B00_B10_brackets(ps, N):
    inds, lower, upper = h0_brackets(ps, N)
    hL = {i: lower[k] for k, i in enumerate(inds)}
    hU = {i: upper[k] for k, i in enumerate(inds)}
    out = []

    for r in [0, 1]:
        probs, tail = trans_row(r, ps, N)
        lo = sp.Rational(probs[0].numerator, probs[0].denominator)
        up = lo + sp.Rational(tail.numerator, tail.denominator)
        for i in inds:
            pr = sp.Rational(probs[i].numerator, probs[i].denominator)
            lo += pr * hL[i]
            up += pr * hU[i]
        out.append((sp.factor(lo), sp.factor(up)))
    return out


p = Fraction(4, 5)
ps = [p, p, p]
delta_minus_1 = sp.Rational(4, 5)
c0 = sp.Rational(132, 125)
c1 = sp.Rational(48, 125)
p1 = sp.Rational(4, 5)

previous_lo = None
previous_up = None
for N in [8, 10, 12]:
    (B00L, B00U), (B10L, B10U) = B00_B10_brackets(ps, N)

    # B01=1-B00.  kappa=B01/B10.
    kappa_lo = sp.factor((1 - B00U) / B10U)
    kappa_up = sp.factor((1 - B00L) / B10L)

    # p_esc decreases in kappa because c1>0.
    p_lo = sp.factor(p1 * delta_minus_1 / (c0 + c1 * kappa_up))
    p_up = sp.factor(p1 * delta_minus_1 / (c0 + c1 * kappa_lo))

    if previous_lo is not None:
        assert p_lo >= previous_lo
        assert p_up <= previous_up
    previous_lo, previous_up = p_lo, p_up

    print(f"N={N}")
    print(f"B00 in [{B00L}, {B00U}]")
    print(f"B10 in [{B10L}, {B10U}]")
    print(f"kappa in [{kappa_lo}, {kappa_up}]")
    print(f"p_esc in [{p_lo}, {p_up}]")
    print(f"decimal p_esc in [{float(p_lo):.15f}, {float(p_up):.15f}]")
    print()

old_lo = sp.Rational(52, 105)
old_up = sp.Rational(20, 33)
assert previous_lo > old_lo
assert previous_up < old_up
print(f"reduced previous bound = [{old_lo}, {old_up}]")
print("nested truncation intervals verified exactly for N=8,10,12")
print("N=12 interval strictly improves the reduced stationary-balance-only interval")
print("ALL_EXACT_CHECKS_PASS")
