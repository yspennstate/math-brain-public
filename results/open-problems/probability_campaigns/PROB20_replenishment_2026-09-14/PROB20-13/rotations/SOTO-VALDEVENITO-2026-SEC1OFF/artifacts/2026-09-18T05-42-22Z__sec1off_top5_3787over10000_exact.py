from fractions import Fraction
from functools import lru_cache

# Exact hard distribution on a 13-element support of the 16 nested-end
# permutations of the top five ranks. Every top block is followed by the
# same decreasing tail x^6,x^7,... . Masses sum to 1 exactly.
HARD = {
    (1, 2, 3, 4, 5): Fraction(1165, 10000),
    (2, 1, 3, 4, 5): Fraction(886, 10000),
    (3, 2, 1, 4, 5): Fraction(312, 10000),
    (4, 2, 1, 3, 5): Fraction(89, 10000),
    (4, 3, 1, 2, 5): Fraction(190, 10000),
    (4, 3, 2, 1, 5): Fraction(296, 10000),
    (5, 1, 2, 3, 4): Fraction(1397, 10000),
    (5, 2, 1, 3, 4): Fraction(734, 10000),
    (5, 3, 2, 1, 4): Fraction(367, 10000),
    (5, 4, 1, 2, 3): Fraction(957, 10000),
    (5, 4, 2, 1, 3): Fraction(295, 10000),
    (5, 4, 3, 1, 2): Fraction(1325, 10000),
    (5, 4, 3, 2, 1): Fraction(1987, 10000),
}
M = 5
assert sum(HARD.values()) == 1

hidden = []
for pi, prob in HARD.items():
    for bits in range(1 << M):
        mask = frozenset(i + 1 for i in range(M) if (bits >> i) & 1)
        seq = tuple(r for r in pi if r not in mask)
        hidden.append((pi, mask, seq, len(mask), prob))
ALL = tuple(range(len(hidden)))
assert len(hidden) == 13 * 32


def mono(k, p):
    return p**k * (1 - p)**(M - k)


def point_value(p):
    """Exact optimal one-query success in the iid-top-five reduced game."""
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
    """Rigorous upper bound for all p in [a,b].

    Each nonnegative hidden-state prior is replaced by its exact coordinatewise
    interval maximum. The Bellman recursion uses only sums and maxima of such
    nonnegative masses, so it is coordinatewise monotone and the result is a
    valid interval-wide upper bound.
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


# Exact point regressions for independent implementations / future readback.
assert point_value(Fraction(0)) == Fraction(757, 2000)
assert point_value(Fraction(1, 3)) == Fraction(57499, 151875)
assert point_value(Fraction(67, 200)) == Fraction(242303406063873, 640000000000000)

# Adaptive exact cover of every p in [0,1].
TARGET = Fraction(3787, 10000)
MAX_DEPTH = 18
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
assert checked == 1766
assert splits == 383
assert leaf_max == Fraction(3877884501147374453961, 10240000000000000000000)
assert leaf_interval == (Fraction(1371, 4000), Fraction(343, 1000), 2)
assert leaf_max < TARGET
assert TARGET - leaf_max == Fraction(3498852625546039, 10240000000000000000000)

print("hard_distribution =", [(pi, str(q)) for pi, q in HARD.items()])
print("positive_hidden_states =", len(hidden))
print("point_V(0) =", point_value(Fraction(0)))
print("point_V(1/3) =", point_value(Fraction(1, 3)))
print("point_V(67/200) =", point_value(Fraction(67, 200)))
print("target_bound =", TARGET, float(TARGET))
print("checked_intervals =", checked)
print("split_intervals =", splits)
print("unresolved_intervals =", len(unresolved))
print("largest_accepted_interval_upper =", leaf_max, float(leaf_max))
print("largest_accepted_interval =", leaf_interval)
print("strict_exact_margin =", TARGET - leaf_max, float(TARGET - leaf_max))
print("ALL_EXACT_CHECKS_PASS")
