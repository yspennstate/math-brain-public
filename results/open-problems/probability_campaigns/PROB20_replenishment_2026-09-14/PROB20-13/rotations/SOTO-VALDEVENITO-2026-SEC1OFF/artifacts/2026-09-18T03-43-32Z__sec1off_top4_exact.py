from fractions import Fraction
from functools import lru_cache

HARD = {
    (1, 2, 3, 4): Fraction(9, 80),
    (4, 3, 2, 1): Fraction(3, 10),
    (4, 3, 1, 2): Fraction(3, 10),
    (4, 1, 2, 3): Fraction(3, 16),
    (2, 1, 3, 4): Fraction(1, 10),
}
M = 4
assert sum(HARD.values()) == 1

hidden = []
for pi, prob in HARD.items():
    for bits in range(1 << M):
        mask = frozenset(i + 1 for i in range(M) if (bits >> i) & 1)
        seq = tuple(r for r in pi if r not in mask)
        hidden.append((pi, mask, seq, len(mask), prob))
ALL = tuple(range(len(hidden)))


def mono(k, p):
    return p**k * (1 - p)**(M - k)


def point_value(p):
    """Exact optimal one-query success in the reduced iid-top-four game."""
    w = [prob * mono(k, p) for pi, mask, seq, k, prob in hidden]

    @lru_cache(None)
    def V(state, step, used):
        if not state or step >= M:
            return Fraction(0)

        qbest = None
        if not used:
            qgroups = {}
            for idx in state:
                pi, mask, seq, k, prob = hidden[idx]
                seen = set(mask) | set(seq[: min(step, len(seq))])
                q = min(seen) - 1 if seen else M
                qgroups.setdefault(q, []).append(idx)
            qbest = sum(V(tuple(group), step, True) for group in qgroups.values())

        groups = {}
        for idx in state:
            pi, mask, seq, k, prob = hidden[idx]
            if step >= len(seq):
                continue
            r = seq[step]
            seen = set(mask) | set(seq[: step + 1])
            obs = 1 + sum(rr < r for rr in seen)
            groups.setdefault(obs, []).append(idx)

        wait = Fraction(0)
        for group in groups.values():
            group = tuple(group)
            select = sum(w[idx] for idx in group if hidden[idx][2][step] == 1)
            reject = V(group, step + 1, used)
            wait += max(select, reject)

        return wait if qbest is None else max(wait, qbest)

    return V(ALL, 0, False)


def mono_max(k, a, b):
    vals = [mono(k, a), mono(k, b)]
    if 0 < k < M:
        critical = Fraction(k, M)
        if a <= critical <= b:
            vals.append(mono(k, critical))
    return max(vals)


def interval_upper(a, b):
    """Rigorous upper bound for every p in [a,b].

    Each hidden-state prior weight is replaced by its exact interval maximum.
    The Bellman recursion is positive-homogeneous in the unnormalized weights
    and uses only sums and maxima, so coordinatewise weight upper bounds give a
    valid success-probability upper bound throughout the interval.
    """
    w = [prob * mono_max(k, a, b) for pi, mask, seq, k, prob in hidden]

    @lru_cache(None)
    def U(state, step, used):
        if not state or step >= M:
            return Fraction(0)

        qbest = None
        if not used:
            qgroups = {}
            for idx in state:
                pi, mask, seq, k, prob = hidden[idx]
                seen = set(mask) | set(seq[: min(step, len(seq))])
                q = min(seen) - 1 if seen else M
                qgroups.setdefault(q, []).append(idx)
            qbest = sum(U(tuple(group), step, True) for group in qgroups.values())

        groups = {}
        for idx in state:
            pi, mask, seq, k, prob = hidden[idx]
            if step >= len(seq):
                continue
            r = seq[step]
            seen = set(mask) | set(seq[: step + 1])
            obs = 1 + sum(rr < r for rr in seen)
            groups.setdefault(obs, []).append(idx)

        wait = Fraction(0)
        for group in groups.values():
            group = tuple(group)
            select = sum(w[idx] for idx in group if hidden[idx][2][step] == 1)
            reject = U(group, step + 1, used)
            wait += max(select, reject)

        return wait if qbest is None else max(wait, qbest)

    return U(ALL, 0, False)


assert point_value(Fraction(0)) == Fraction(2, 5)
assert point_value(Fraction(1, 10)) == Fraction(325053, 800000)
assert point_value(Fraction(3, 10)) == Fraction(41139, 100000)

N = 1000
maximum = Fraction(0)
worst = None
for i in range(N):
    a = Fraction(i, N)
    b = Fraction(i + 1, N)
    upper = interval_upper(a, b)
    if upper > maximum:
        maximum = upper
        worst = (a, b)

TARGET = Fraction(33, 80)
assert maximum == Fraction(16094073149, 39062500000)
assert worst == (Fraction(37, 125), Fraction(297, 1000))
assert maximum < TARGET

# 33/80 < (20*sqrt(10)-29)/81 iff 4993 < 1600*sqrt(10).
assert 4993**2 < 1600**2 * 10

print("hard_distribution =", [(pi, str(q)) for pi, q in HARD.items()])
print("point_V(0) =", point_value(Fraction(0)))
print("point_V(1/10) =", point_value(Fraction(1, 10)))
print("point_V(3/10) =", point_value(Fraction(3, 10)))
print("partition_intervals =", N)
print("worst_interval =", worst)
print("certified_interval_upper =", maximum, float(maximum))
print("target_bound_33/80 =", TARGET, float(TARGET))
print("strict_margin =", TARGET - maximum, float(TARGET - maximum))
print("old_endpoint_comparison_square =", 4993**2, "<", 1600**2 * 10)
print("ALL_EXACT_CHECKS_PASS")
