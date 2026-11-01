#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from math import factorial

# Exact-rational finite sanity/certificate for the P20 reference-profile
# subeigenvector mechanism.  Model: L=1, W=2 diagonal band with iid Exp(1)
# physical edges.  This is NOT a source-level curvature proof; it rigorously
# demonstrates that a nonflat reference profile improves the preceding flat
# ancestor fixed-point one-band constant.


def band(L, W):
    verts = []
    idx = {}
    for s in range(2 * L + 1):
        for d in range(-W, W + 1):
            if (s - d) % 2 == 0:
                idx[(s, d)] = len(verts)
                verts.append((s, d))
    edges = []
    for (s, d), i in idx.items():
        if s < 2 * L:
            for nd in (d - 1, d + 1):
                j = idx.get((s + 1, nd))
                if j is not None:
                    edges.append((i, j))
    left = [idx[(0, d)] for d in range(-W, W + 1) if (0, d) in idx]
    right = [idx[(2 * L, d)] for d in range(-W, W + 1) if (2 * L, d) in idx]
    return verts, edges, left, right


def transient_data(n, edges, target, start_mask):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    seen = {start_mask}
    stack = [start_mask]
    while stack:
        mask = stack.pop()
        counts = defaultdict(int)
        for u in range(n):
            if (mask >> u) & 1:
                for v in adj[u]:
                    if not ((mask >> v) & 1):
                        counts[v] += 1
        for v in counts:
            if v == target:
                continue
            nm = mask | (1 << v)
            if nm not in seen:
                seen.add(nm)
                stack.append(nm)

    states = sorted(seen, key=lambda m: (m.bit_count(), m))
    pos = {m: i for i, m in enumerate(states)}
    transitions = []
    for mask in states:
        counts = defaultdict(int)
        b = 0
        for u in range(n):
            if (mask >> u) & 1:
                for v in adj[u]:
                    if not ((mask >> v) & 1):
                        b += 1
                        counts[v] += 1
        children = []
        for v, mult in counts.items():
            if v != target:
                children.append((pos[mask | (1 << v)], mult))
        transitions.append((b, tuple(children)))
    return states, pos, transitions, adj


def exact_post_values(n, edges, target, states, activate_mask):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    @lru_cache(None)
    def V(mask):
        if (mask >> target) & 1:
            return Fraction(0)
        counts = defaultdict(int)
        b = 0
        for u in range(n):
            if (mask >> u) & 1:
                for v in adj[u]:
                    if not ((mask >> v) & 1):
                        b += 1
                        counts[v] += 1
        assert b > 0
        out = Fraction(1, b)
        for v, mult in counts.items():
            out += Fraction(mult, b) * V(mask | (1 << v))
        return out

    return [V(mask | activate_mask) for mask in states]


def delayed_interval(n, edges, target, start_mask, activate_mask, delay, N=80):
    # Before the deterministic activation time delay, only start_mask is active.
    # After it, activate_mask is added.  The backward equation is
    # U'(t)=Q U(t)+1, U(0)=V_post.  We enclose exp(delay*A)[V_post;1]
    # by an exact Taylor polynomial plus an exact infinity-norm remainder.
    states, pos, transitions, _ = transient_data(n, edges, target, start_mask)
    post = exact_post_values(n, edges, target, states, activate_mask)
    m = len(states)

    def Aact(w):
        out = [Fraction(0)] * (m + 1)
        reward = w[m]
        for i, (b, children) in enumerate(transitions):
            s = -b * w[i] + reward
            for j, mult in children:
                s += mult * w[j]
            out[i] = s
        out[m] = Fraction(0)
        return out

    w = post + [Fraction(1)]
    term = w[:]
    total = w[:]
    for k in range(1, N + 1):
        term = Aact(term)
        scale = delay / k
        term = [scale * x for x in term]
        total = [total[i] + term[i] for i in range(m + 1)]

    max_abs_row = 0
    for b, children in transitions:
        # Row of augmented A: diagonal -b, non-target child rates, reward +1.
        max_abs_row = max(max_abs_row, b + sum(mult for _, mult in children) + 1)
    r = delay * max_abs_row
    assert r < N + 2
    wnorm = max(abs(x) for x in w)
    first_omitted = wnorm * (r ** (N + 1)) / factorial(N + 1)
    tail = first_omitted / (1 - r / (N + 2))

    value = total[pos[start_mask]]
    return value - tail, value + tail, len(states), tail


verts, edges, left, right = band(1, 2)
n = len(verts)
assert len(left) == len(right) == 3
center = left[1]
start_mask = 1 << center
activate_mask = (1 << left[0]) | (1 << left[2])
a = Fraction(57, 100)

outer_lo, outer_hi, outer_states, outer_tail = delayed_interval(
    n, edges, right[0], start_mask, activate_mask, a
)
center_lo, center_hi, center_states, center_tail = delayed_interval(
    n, edges, right[1], start_mask, activate_mask, a
)

# Symmetry gives the same outer value at right[2].  The reference profile is
# z=(a,0,a), so Lambda(z)=max(T_outer-a, T_center).
lambda_upper = max(outer_hi - a, center_hi)
flat_ancestor_lambda = Fraction(43, 36)  # prior exact P20 artifact at z=0
simple_upper = Fraction(1113011, 1000000)

assert lambda_upper < simple_upper
assert simple_upper < flat_ancestor_lambda
assert flat_ancestor_lambda - simple_upper == Fraction(732901, 9000000)

print('MODEL = iid Exp(1), L=1, W=2 diagonal band')
print('reference_profile = (57/100, 0, 57/100)')
print('outer_transient_states =', outer_states)
print('center_transient_states =', center_states)
print('outer_interval_float = [%.15f, %.15f]' % (float(outer_lo), float(outer_hi)))
print('center_interval_float = [%.15f, %.15f]' % (float(center_lo), float(center_hi)))
print('outer_taylor_tail_lt = %.3e' % float(outer_tail))
print('center_taylor_tail_lt = %.3e' % float(center_tail))
print('Lambda_upper_float = %.15f' % float(lambda_upper))
print('CERTIFIED_LAMBDA_UPPER = 1113011/1000000')
print('PRIOR_FLAT_ANCESTOR_LAMBDA = 43/36')
print('CERTIFIED_IMPROVEMENT_AT_LEAST = 732901/9000000 = %.15f' % float(Fraction(732901, 9000000)))
print('SOURCE_THRESHOLD_PER_L = 3002823/5000000 = %.7f' % float(Fraction(3002823, 5000000)))
print('SOURCE_THRESHOLD_REACHED = False')
print('P20-REFERENCE-SUBEIGENVECTOR-EXACT-SANITY: ALL_EXACT_CHECKS_PASS')
