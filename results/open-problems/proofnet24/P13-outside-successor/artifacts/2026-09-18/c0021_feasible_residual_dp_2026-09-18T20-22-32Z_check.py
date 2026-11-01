from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb

# Exact self-check for P13 / C0021.
# Purpose: verify the finite inputs to the B4/B16 feasible-residual lower-bound route.
# All mathematical finite comparisons use fractions.Fraction.

def norm(ch):
    p = sum(c == '+' for c in ch)
    m = sum(c == '-' for c in ch)
    if p >= 2:
        return '+'
    if m >= 2:
        return '-'
    return tuple(sorted(ch, key=repr))

@lru_cache(None)
def queries(t):
    if t == 'u':
        return (('+', '-'),)
    if t in ('+', '-'):
        return ()
    out = set()
    for i, c in enumerate(t):
        if i and t[i] == t[i-1]:
            continue
        for cp, cm in queries(c):
            out.add((
                norm(t[:i] + (cp,) + t[i+1:]),
                norm(t[:i] + (cm,) + t[i+1:])
            ))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def V(t):
    if t in ('+', '-'):
        return Fraction(0)
    return min(Fraction(1) + (V(a) + V(b))/2 for a, b in queries(t))

@lru_cache(None)
def q(t):
    if t == '+':
        return Fraction(1)
    if t == '-':
        return Fraction(0)
    if t == 'u':
        return Fraction(1, 2)
    a, b, c = (q(x) for x in t)
    return a*b + a*c + b*c - 2*a*b*c

def full(h):
    return 'u' if h == 0 else norm((full(h-1),)*3)

def canonical_levels(max_h):
    levels = [{'+', '-', 'u'}]
    for _ in range(max_h):
        prev = sorted(levels[-1], key=repr)
        out = {'+', '-'}
        for a, b, c in combinations_with_replacement(prev, 3):
            out.add(norm((a, b, c)))
        levels.append(out)
    return levels

def min_regret(h):
    """A_h(s): minimum cumulative local Bellman regret from untouched state."""
    root = full(h)
    A = {root: Fraction(0)}
    front = {root}
    while front:
        candidates = {}
        for s in front:
            if s in ('+', '-'):
                continue
            vs = V(s)
            for a, b in queries(s):
                r = Fraction(1) + (V(a)+V(b))/2 - vs
                assert r >= 0
                cand = A[s] + r
                for z in (a, b):
                    if z not in candidates or cand < candidates[z]:
                        candidates[z] = cand
        new_front = set()
        for z, cand in candidates.items():
            if z not in A or cand < A[z]:
                A[z] = cand
                new_front.add(z)
        front = new_front
    return A

def canon3(t):
    return tuple(sorted(t, key=repr))

def terminal_residual(t):
    plus = [i for i,s in enumerate(t) if s == '+']
    minus = [i for i,s in enumerate(t) if s == '-']
    if len(plus) >= 2:
        pair = plus[:2]
        j = next(i for i in range(3) if i not in pair)
        return '+', t[j]
    if len(minus) >= 2:
        pair = minus[:2]
        j = next(i for i in range(3) if i not in pair)
        return '-', t[j]
    return None

def beta_exact(h):
    """Exact max expected W_h(residual) in the three-child outer-majority game."""
    A = min_regret(h)
    W = {s: V(s)-A[s] for s in A}

    @lru_cache(None)
    def B(t):
        term = terminal_residual(t)
        if term is not None:
            _, residual = term
            return W[residual]
        candidates = []
        for i, s in enumerate(t):
            if s in ('+', '-'):
                continue
            # Child-permutation quotient.
            if i and t[i] == t[i-1]:
                continue
            for a, b in queries(s):
                tp = canon3(t[:i] + (a,) + t[i+1:])
                tm = canon3(t[:i] + (b,) + t[i+1:])
                candidates.append((B(tp)+B(tm))/2)
        assert candidates
        return max(candidates)

    root = canon3((full(h),)*3)
    raw = B(root)
    return raw, raw / V(full(h)), B.cache_info().currsize, W

levels = canonical_levels(3)
assert [len(levels[h]) for h in range(4)] == [3, 6, 46, 17206]

D = [V(full(h)) for h in range(4)]
assert D == [
    Fraction(1),
    Fraction(5,2),
    Fraction(393,64),
    Fraction(15796051,1048576),
]

# Previous concave-envelope relaxations, for comparison.
rho = [
    Fraction(1,2),
    Fraction(3,5),
    Fraction(585,917),
    Fraction(165736792,236940765),
]

expected_beta = [
    Fraction(1,2),
    Fraction(87,160),
    Fraction(19180943,34340864),
]
expected_raw = [
    Fraction(1,2),
    Fraction(87,64),
    Fraction(57542829,16777216),
]
expected_outer_states = [8, 54, 17294]

beta_rows = []
for h in range(3):
    raw, beta, nstates, W = beta_exact(h)
    assert raw == expected_raw[h]
    assert beta == expected_beta[h]
    assert nstates == expected_outer_states[h]
    assert beta <= rho[h]
    lower = (3-beta)*D[h]
    beta_rows.append((h, raw, beta, rho[h]-beta, lower, nstates))

# At h=0 and h=1 this relaxation is exact; at h=2 it is a strict lower bound.
assert beta_rows[0][4] == D[1]
assert beta_rows[1][4] == D[2]
assert beta_rows[2][4] == Fraction(251524947,16777216)
assert beta_rows[2][4] < D[3]

# Exact net-regret coefficient gamma_h = 3 - D_{h+1}/D_h (identity, not a new bound).
gamma = [Fraction(3) - D[h+1]/D[h] for h in range(3)]
assert gamma == [
    Fraction(1,2),
    Fraction(87,160),
    Fraction(3520685,6438912),
]
for h in range(3):
    assert gamma[h] <= expected_beta[h]

# B4: a uniform terminal anti-alignment mass consequence of
# X = R*m_J in [-1,1], E X = -1/2.
# For a=1/4, P(X <= -a) >= (1/2-a)/(1-a) = 1/3.
a = Fraction(1,4)
forced_mass = (Fraction(1,2)-a)/(1-a)
assert forced_mass == Fraction(1,3)

# But exact state envelopes show this threshold alone is too weak:
# max W_h/D_h among states with |m| >= 1/4 is already large.
expected_hi = {
    1: Fraction(3,5),
    2: Fraction(329,393),
    3: Fraction(13611334,15796051),
}
hi_rows = []
for h in (1,2,3):
    A = min_regret(h)
    vals = []
    for s, av in A.items():
        m = abs(2*q(s)-1)
        if m >= a:
            vals.append((V(s)-av)/D[h])
    mx = max(vals)
    assert mx == expected_hi[h]
    hi_rows.append((h, mx))

# h=3 direct three-child feasible DP is combinatorially too large for this exact run.
# There are this many unordered triples even before pruning terminal states/actions.
h3_unordered_triples = comb(len(levels[3])+2, 3)
assert h3_unordered_triples == 849110525256

print("C0021 feasible-residual DP exact self-check")
for h,raw,beta,gap,lower,nstates in beta_rows:
    print("h", h,
          "D_h", D[h],
          "B_h_root", raw,
          "beta_h", beta,
          "rho_minus_beta", gap,
          "lower_D_(h+1)", lower,
          "outer_DP_states", nstates)
print("gamma_exact_from_known_D", *gamma)
print("B4_threshold_a", a)
print("B4_forced_anti_alignment_mass", forced_mass)
for h,mx in hi_rows:
    print("max_W_over_D_given_abs_m_ge_1_4_h", h, mx)
print("h3_child_states", len(levels[3]))
print("h3_unordered_three_child_states_before_pruning", h3_unordered_triples)
print("ALL_EXACT_FEASIBLE_RESIDUAL_DP_CHECKS_PASS")
