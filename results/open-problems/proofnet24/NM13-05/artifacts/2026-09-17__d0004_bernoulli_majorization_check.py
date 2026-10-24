from fractions import Fraction

# Exact checker for the finite asymmetric D0004 witness used in the
# 2026-09-17 NM13-05 run.
#
# Law: P(X=3)=2/5, P(X=-2)=3/5.  On a five-equal-atom realization,
# the source n=3 norm inequalities reduce to weak-majorization checks
# between nonnegative five-vectors.  Every prefix difference below is
# affine in t on each breakpoint interval, so exact endpoint/slope checks
# certify the inequalities for every real t.


def add(f, g):
    return (f[0] + g[0], f[1] + g[1])


def sub(f, g):
    return (f[0] - g[0], f[1] - g[1])


def val(f, t):
    return f[0] * t + f[1]


def prefix(entries, k):
    out = (Fraction(0), Fraction(0))
    for f in entries[:k]:
        out = add(out, f)
    return out


def nonnegative_on_interval(f, lo, hi):
    """Check affine f(t)>=0 on [lo,hi], allowing one infinite endpoint."""
    a, _ = f
    if lo is None:
        # t -> -infinity. Positive slope would force f -> -infinity.
        if a > 0:
            return False
        return val(f, hi) >= 0
    if hi is None:
        # t -> +infinity. Negative slope would force f -> -infinity.
        if a < 0:
            return False
        return val(f, lo) >= 0
    return min(val(f, lo), val(f, hi)) >= 0


# N+ : (X-t)_+  versus  2(X+t/2)_- = (-2X-t)_+.
# Entries are listed in decreasing order on each interval.
plus_intervals = [
    (
        None,
        Fraction(-6),
        [(Fraction(-1), Fraction(3))] * 2
        + [(Fraction(-1), Fraction(-2))] * 3,
        [(Fraction(-1), Fraction(4))] * 3
        + [(Fraction(-1), Fraction(-6))] * 2,
    ),
    (
        Fraction(-6),
        Fraction(-2),
        [(Fraction(-1), Fraction(3))] * 2
        + [(Fraction(-1), Fraction(-2))] * 3,
        [(Fraction(-1), Fraction(4))] * 3 + [(Fraction(0), Fraction(0))] * 2,
    ),
    (
        Fraction(-2),
        Fraction(3),
        [(Fraction(-1), Fraction(3))] * 2 + [(Fraction(0), Fraction(0))] * 3,
        [(Fraction(-1), Fraction(4))] * 3 + [(Fraction(0), Fraction(0))] * 2,
    ),
]

for lo, hi, lhs, rhs in plus_intervals:
    for k in range(1, 6):
        diff = sub(prefix(rhs, k), prefix(lhs, k))
        assert nonnegative_on_interval(diff, lo, hi), ("N+", lo, hi, k, diff)
# For t>=3 the left side vanishes identically.


# N- : (X-t)_-  versus  2(X+t/2)_+ = (2X+t)_+.
minus_intervals = [
    (
        Fraction(-2),
        Fraction(3),
        [(Fraction(1), Fraction(2))] * 3 + [(Fraction(0), Fraction(0))] * 2,
        [(Fraction(1), Fraction(6))] * 2 + [(Fraction(0), Fraction(0))] * 3,
    ),
    (
        Fraction(3),
        Fraction(4),
        [(Fraction(1), Fraction(2))] * 3 + [(Fraction(1), Fraction(-3))] * 2,
        [(Fraction(1), Fraction(6))] * 2 + [(Fraction(0), Fraction(0))] * 3,
    ),
    (
        Fraction(4),
        None,
        [(Fraction(1), Fraction(2))] * 3 + [(Fraction(1), Fraction(-3))] * 2,
        [(Fraction(1), Fraction(6))] * 2 + [(Fraction(1), Fraction(-4))] * 3,
    ),
]

for lo, hi, lhs, rhs in minus_intervals:
    for k in range(1, 6):
        diff = sub(prefix(rhs, k), prefix(lhs, k))
        assert nonnegative_on_interval(diff, lo, hi), ("N-", lo, hi, k, diff)
# For t<=-2 the left side vanishes identically.


# Exact nonmixability: with k positive (+3) values among three coordinates,
# the sum is 3k-2(3-k)=5k-6, never zero.
threefold_sums = [5 * k - 6 for k in range(4)]
assert 0 not in threefold_sums

print("D0004 finite Bernoulli majorization check")
print("law: P(X=3)=2/5, P(X=-2)=3/5, mean=0")
print("N+ weak-majorization prefixes: PASS for every real t")
print("N- weak-majorization prefixes: PASS for every real t")
print("possible three-fold sums:", threefold_sums)
print("3-CM zero-sum feasibility: FAIL exactly")
print("ALL_EXACT_CHECKS_PASS")
