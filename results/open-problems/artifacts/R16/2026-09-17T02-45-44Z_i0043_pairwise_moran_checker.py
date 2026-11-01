from fractions import Fraction

# Exact self-check for two finite arithmetic claims used in the R16/I0043 report.
# (1) One- and two-point marginals do not determine a three-cell union event.
# (2) The level-tree lower-bound term in the critical Moran energy calculation
#     has the stated exact rational form and harmonic lower bound.

EVEN = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
ODD = [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def stats(states):
    m = len(states)
    singles = tuple(Fraction(sum(s[i] for s in states), m) for i in range(3))
    pairs = tuple(
        Fraction(sum(s[i] * s[j] for s in states), m)
        for i, j in [(0, 1), (0, 2), (1, 2)]
    )
    union = Fraction(sum(1 for s in states if any(s)), m)
    return singles, pairs, union


se, pe, ue = stats(EVEN)
so, po, uo = stats(ODD)
assert se == so == (Fraction(1, 2),) * 3
assert pe == po == (Fraction(1, 4),) * 3
assert ue == Fraction(3, 4)
assert uo == Fraction(1, 1)

print("PAIRWISE_MARGINAL_OBSTRUCTION")
print(f"even singles={se} pairs={pe} union={ue}")
print(f"odd  singles={so} pairs={po} union={uo}")
print("same 1-point marginals: PASS")
print("same 2-point marginals: PASS")
print("different union probabilities: PASS")
print()

# For the critical Moran test set in the report, ell_n^{-alpha}=a_n=2^n N/(N+n).
# The energy lower-bound contribution at level n is
# (a_n-a_{n-1}) 2^{-n}
# = N(N+n-2)/(2(N+n)(N+n-1))
# >= N/(4(N+n-1)) when N>=3.
N = 10
partial = Fraction(0)
for n in range(1, 1001):
    a_n = Fraction((2**n) * N, N + n)
    a_prev = Fraction((2 ** (n - 1)) * N, N + n - 1)
    term = (a_n - a_prev) * Fraction(1, 2**n)
    formula = Fraction(N * (N + n - 2), 2 * (N + n) * (N + n - 1))
    lower = Fraction(N, 4 * (N + n - 1))
    assert term == formula
    assert term >= lower
    partial += term

print("MORAN_TREE_ENERGY_IDENTITY_SELF_CHECK")
print(f"N={N}, checked n=1..1000")
print("term_n=(a_n-a_{n-1})2^{-n}")
print("exact identity term_n=N(N+n-2)/(2(N+n)(N+n-1)): PASS")
print("harmonic lower bound term_n >= N/(4(N+n-1)): PASS")
print(f"finite partial sum n<=1000 = {partial}")
print(f"finite partial sum decimal = {float(partial):.15f}")
print("ALL_EXACT_CHECKS_PASS")
