from fractions import Fraction
from itertools import permutations, product
from math import factorial

# C27 independent exact checker for the imported HARD10-03 NEW-L98/99 bound.
# It certifies a literal rational exponent below the analytic optimum and
# exhaustively searches the deterministic singleton-block cycle core through k=8.


def ln_bounds(x: Fraction, N: int = 160):
    assert x > 0
    if x < 1:
        lo, hi = ln_bounds(1 / x, N)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    zz = z * z
    p = z
    s = Fraction(0, 1)
    for j in range(N):
        if j:
            p *= zz
        s += p / (2 * j + 1)
    lo = 2 * s
    tail = 2 * p * zz / ((2 * N + 1) * (1 - zz))
    return lo, lo + tail


def e_bounds(M: int = 35):
    s = Fraction(0, 1)
    fact = 1
    for j in range(M + 1):
        if j:
            fact *= j
        s += Fraction(1, fact)
    fact_next = fact * (M + 1)
    tail = Fraction(1, fact_next) * Fraction(M + 2, M + 1)
    return s, s + tail


# Near-optimal rational u and literal certified exponent.
u = Fraction(11340541, 4000000)
eps = Fraction(590451719447, 1250000000000)
x = (1 + u) / 2
lnx_lo, _ = ln_bounds(x)
_, ln2_hi = ln_bounds(Fraction(2, 1))
e_lo, e_hi = e_bounds()
inv_e_hi = 1 / e_lo

# E(u) = [ln((1+u)/2) - (u^2-1)/(8e)] / ln 2.
# The following exact rational gap proves E(u) > eps.
gap = lnx_lo - ((u * u - 1) / 8) * inv_e_hi - eps * ln2_hi
assert gap > 0

# Exact rational bracket for the unique optimizer u_* solving u(1+u)=4e.
u_lo = Fraction(28351352, 10_000_000)
u_hi = Fraction(28351353, 10_000_000)
assert u_lo * (1 + u_lo) - 4 * e_hi < 0
assert u_hi * (1 + u_hi) - 4 * e_lo > 0
assert u_lo < u < u_hi


def directed_cycle_edges(cyc):
    k = len(cyc)
    return [(cyc[i], cyc[(i + 1) % k]) for i in range(k)]


def lex_spanning_tree(cyc):
    # Deterministic spanning tree of the undirected transition graph.
    und = sorted({tuple(sorted(e)) for e in directed_cycle_edges(cyc)})
    parent = list(range(len(cyc)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    tree = []
    for a, b in und:
        if union(a, b):
            tree.append((a, b))
            if len(tree) == len(cyc) - 1:
                break
    assert len(tree) == len(cyc) - 1
    return tree


# Counterexample-first finite search for the deterministic core used in NEW-L98.
# For every anchored directed k-cycle through k=8 and every binary block coloring,
# Z is the number of bichromatic edges in the deterministic spanning tree and N
# is the number of red-to-blue directed cycle transitions.  The theorem needs
# only 2N >= Z.  We also seek a counterexample to the tempting strengthening N>=Z.
cases = 0
bad_core = None
false_strengthening = None
for k in range(2, 9):
    for tail in permutations(range(1, k)):
        cyc = (0,) + tail
        tree = lex_spanning_tree(cyc)
        directed = directed_cycle_edges(cyc)
        for colors in product((0, 1), repeat=k):
            z = sum(colors[a] != colors[b] for a, b in tree)
            n_rb = sum(colors[a] == 0 and colors[b] == 1 for a, b in directed)
            n_br = sum(colors[a] == 1 and colors[b] == 0 for a, b in directed)
            assert n_rb == n_br
            if 2 * n_rb < z and bad_core is None:
                bad_core = (k, cyc, colors, tuple(tree), z, n_rb)
            if n_rb < z and false_strengthening is None:
                false_strengthening = (k, cyc, colors, tuple(tree), z, n_rb)
            cases += 1

assert bad_core is None
assert false_strengthening == (
    3,
    (0, 1, 2),
    (0, 1, 1),
    ((0, 1), (0, 2)),
    2,
    1,
)
assert cases == sum(factorial(k - 1) * 2**k for k in range(2, 9))

print("ALL_EXACT_CHECKS_PASS")
print("epsilon_cert =", f"{eps.numerator}/{eps.denominator}")
print("epsilon_cert_decimal = 0.4723613755576")
print("rigorous_log_gap_positive =", gap > 0)
print("u_star_bracket = [2.8351352, 2.8351353]")
print("chosen_u =", f"{u.numerator}/{u.denominator}")
print("cycle_color_cases_checked =", cases)
print("max_singleton_cycle_k = 8")
print("no_counterexample_to_2N_ge_Z =", bad_core is None)
print("false_strengthening_N_ge_Z_counterexample =", false_strengthening)
