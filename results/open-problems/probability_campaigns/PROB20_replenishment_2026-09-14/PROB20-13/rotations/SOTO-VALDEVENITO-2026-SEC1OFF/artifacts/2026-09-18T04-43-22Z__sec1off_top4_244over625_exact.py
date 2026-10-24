from fractions import Fraction
from functools import lru_cache

# Exact hard distribution on top-four preliminary orders.  Each order is
# followed by the same decreasing tail x^5,x^6,...,x^n.
HARD = {
    (1, 2, 3, 4): Fraction(71, 320),
    (2, 1, 3, 4): Fraction(47, 400),
    (3, 2, 1, 4): Fraction(21, 1600),
    (4, 1, 2, 3): Fraction(227, 1600),
    (4, 2, 1, 3): Fraction(103, 1600),
    (4, 3, 1, 2): Fraction(291, 1600),
    (4, 3, 2, 1): Fraction(83, 320),
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
    """Exact optimal one-query success in the iid-top-four reduced game."""
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
                response = min(seen) - 1 if seen else M
                qgroups.setdefault(response, []).append(idx)
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

    Each hidden-state prior is replaced by its exact coordinatewise interval
    maximum.  The Bellman recursion is monotone in every nonnegative hidden
    weight, so this gives a valid interval-wide upper bound even though the
    coordinatewise maxima need not occur at the same p.
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
                response = min(seen) - 1 if seen else M
                qgroups.setdefault(response, []).append(idx)
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


# Exact point regressions.
assert point_value(Fraction(0)) == Fraction(39, 100)
assert point_value(Fraction(8, 25)) == Fraction(243995543, 625000000)
assert point_value(Fraction(321, 1000)) == Fraction(624629242636273, 1600000000000000)

# Adaptive exact interval cover of all p in [0,1].  Begin with 1000 rational
# cells and bisect only cells whose coarse monotone upper bound has not yet
# fallen below the target.  No cell may remain unresolved at MAX_DEPTH.
TARGET = Fraction(244, 625)
MAX_DEPTH = 15
stack = [(Fraction(i, 1000), Fraction(i + 1, 1000), 0) for i in range(1000)]
checked = 0
splits = 0
unresolved = []
leaf_max = Fraction(0)
leaf_interval = None

while stack:
    a, b, depth = stack.pop()
    upper = interval_upper(a, b)
    checked += 1
    if upper >= TARGET:
        if depth >= MAX_DEPTH:
            unresolved.append((a, b, upper, depth))
        else:
            splits += 1
            mid = (a + b) / 2
            stack.append((a, mid, depth + 1))
            stack.append((mid, b, depth + 1))
    else:
        if upper > leaf_max:
            leaf_max = upper
            leaf_interval = (a, b, depth)

assert not unresolved
assert checked == 2988
assert splits == 994
assert leaf_max == Fraction(511705087107315957, 1310720000000000000)
assert leaf_interval == (Fraction(313, 1000), Fraction(501, 1600), 3)
assert leaf_max < TARGET
assert TARGET - leaf_max == Fraction(892684043, 1310720000000000000)
assert TARGET < Fraction(2, 5)
assert TARGET < Fraction(33, 80)

print("hard_distribution =", [(pi, str(q)) for pi, q in HARD.items()])
print("point_V(0) =", point_value(Fraction(0)))
print("point_V(8/25) =", point_value(Fraction(8, 25)))
print("point_V(321/1000) =", point_value(Fraction(321, 1000)))
print("target_bound =", TARGET, float(TARGET))
print("initial_cells = 1000")
print("checked_intervals =", checked)
print("split_intervals =", splits)
print("unresolved_intervals =", len(unresolved))
print("largest_accepted_interval_upper =", leaf_max, float(leaf_max))
print("largest_accepted_interval =", leaf_interval)
print("strict_exact_margin =", TARGET - leaf_max, float(TARGET - leaf_max))
print("improves_33_over_80_by =", Fraction(33, 80) - TARGET, float(Fraction(33, 80) - TARGET))
print("ALL_EXACT_CHECKS_PASS")
